import random
import re
import urllib.request
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from structlog._config import BoundLoggerLazyProxy

import xmltodict

from pyrxiv.datamodel import ArxivPaper, Author
from pyrxiv.logger import logger


def get_batch_response(
    category: str = "cond-mat.str-el",
    start_index: int = 0,
    max_results: int = 100,
    iteration: int = 0,
    max_iteration: int = 10,
    logger: "BoundLoggerLazyProxy" = logger,
) -> list | dict:
    """
    Fetch a batch of papers from arXiv API based on the specified category, start index, and maximum results.

    NOTE: This function is happening because of a weird behavior of the arXiv API when `max_results` is hitting no response
    at random `max_results`. If the response does not have entries, we re-try again recursively with a different number
    for `max_results` until a maximum number of iterations is reached (defined by `max_iteration`).

    Args:
        category (str, optional): The arXiv category to fetch papers from. Defaults to "cond-mat.str-el".
        start_index (int, optional): The starting index for fetching papers. Defaults to 0.
        max_results (int, optional): The maximum number of results to fetch. Defaults to 100.
        iteration (int, optional): The current iteration count for recursive attempts. Defaults to 0.
        max_iteration (int, optional): The maximum number of recursive attempts to fetch papers if no results are found. Defaults to 10.
        logger (BoundLoggerLazyProxy, optional): The logger to log messages.

    Returns:
        list | dict: A list of papers metadata fetched from arXiv. If `max_results` is 1, the batch will be a single dictionary.
    """
    # Recursion safeguard
    if iteration >= max_iteration:
        logger.warning("Maximum recursion depth reached. Returning empty batch.")
        return []

    # Request from arXiv API
    url = (
        f"http://export.arxiv.org/api/query?"
        f"search_query=cat:{category}&start={start_index}&max_results={max_results}&"
        f"sortBy=submittedDate&sortOrder=descending"
    )
    try:
        request = urllib.request.urlopen(url)
    except Exception as e:
        logger.error(f"Error fetching data from arXiv API: {e}")
        return []
    data = request.read().decode("utf-8")
    data_dict = xmltodict.parse(data)

    # Extracting papers from the XML response
    batch = data_dict.get("feed", {}).get("entry", [])

    # Recursively trying to resolve batches
    if not batch and max_results > 1:
        # try again with a different `max_results`
        new_max_results = random.randint(1, max_results - 1)  # 1 <= value < max_results
        iteration += 1
        batch = get_batch_response(
            category=category,
            start_index=start_index,
            max_results=new_max_results,
            iteration=iteration,
            max_iteration=max_iteration,
        )
        if not batch:
            logger.info("No papers found in the response")
    return batch


class ArxivFetcher:
    """Fetch papers from arXiv and extract metadata from the queried papers."""

    def __init__(
        self,
        max_results: int = 200,
        category: str = "cond-mat.str-el",
        download_path: Path = Path("data"),
        start_id: str | None = None,
        start_from_filepath: bool = False,
        fetched_ids_file: str = "fetched_arxiv_ids.txt",
        **kwargs,
    ):
        """
        Initialize the ArxivFetcher class.
        This class fetches papers from arXiv and extracts metadata from the queried papers.
        It uses the `requests` library to fetch the papers and the `xmltodict` library to parse the XML response.
        It also uses the `ArxivPaper` and `Author` datamodels to store the metadata of the papers.


        Args:
            max_results (int, optional): The maximum number of results to fetch from arXiv. Defaults to 100.
            category (str, optional): The arXiv category to fetch papers from. Defaults to "cond-mat.str-el".
            download_path (Path, optional): The path where to store the fetched papers. Defaults to "data".
            start_id (str | None, optional): The starting arXiv ID to fetch papers from. If specified, the search will start from this ID.
                If not specified, the search will start from the newest papers in the `category`. Defaults to None.
            start_from_filepath (bool, optional): If True, the search will start from the last fetched arXiv ID in the specified file.
                This is useful for resuming the search from a specific point. If False, the search will start from the newest papers in the `category`.
                Defaults to False.
            fetched_ids_file (str, optional): The file where to store the fetched arXiv IDs. Defaults to "fetched_arxiv_ids.txt".
        """
        self.max_results = max_results
        self.category = category

        # Start index for fetching papers
        self.start_index = 0

        # check if `download_path` exists, and if not, create it
        download_path.mkdir(parents=True, exist_ok=True)
        if not fetched_ids_file:
            fetched_ids_file = "fetched_arxiv_ids.txt"
        self.fetched_ids_file = download_path / fetched_ids_file

        # The starting arXiv ID to fetch papers from.
        self.start_id = None
        self.skip_newer_ids = False
        # User specifies to start from a given ID, ignoring newer ones
        if start_id:
            self.skip_newer_ids = True
            self.start_id = start_id
        # Load last fetched id from file
        elif start_from_filepath and self.fetched_ids_file.exists():
            self.skip_newer_ids = True
            self.start_id = self._last_fetched_id(self.fetched_ids_file)

        self.logger = kwargs.get("logger", logger)

    def _last_fetched_id(self, fetched_ids_file: str | Path) -> str:
        """
        Gets the last fetched arXiv ID from the specified file.

        Args:
            fetched_ids_file (str | Path): The path to the file containing the fetched arXiv IDs.

        Returns:
            str: The last fetched arXiv ID from the file. If the file is empty or does not exist, returns an empty string.
        """
        if not fetched_ids_file:
            return ""
        if isinstance(fetched_ids_file, str):
            fetched_ids_file = Path(fetched_ids_file)

        last_id = ""
        with fetched_ids_file.open("r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            last_id = lines[-1] if lines else ""
        return last_id

    def _get_pages_and_figures(self, comment: str) -> tuple[int | None, int | None]:
        """
        Gets the number of pages and figures from the comment of the arXiv paper.

        Args:
            comment (str): A string containing the comment of the arXiv paper.

        Returns:
            tuple[int | None, int | None]: A tuple containing the number of pages and figures.
                If not found, returns (None, None).
        """
        pattern = r" *(\d+) *pages *, *(\d+) *figures *"
        match = re.search(pattern, comment)
        if match:
            n_pages, n_figures = match.groups()
            return int(n_pages), int(n_figures)
        return None, None

    def is_newer_than(self, paper_id: str, reference_id: str) -> bool:
        """
        Checks if the given `paper_id` is newer than the `reference_id`.

        Supports arXiv IDs of the form 'yymm.number[vN]' (e.g., '2507.02753v1').

        Returns:
            True if `paper_id` is newer than `reference_id`, False otherwise.
        """

        def normalize(arxiv_id: str) -> tuple[int | None, int | None]:
            match = re.match(r"^(\d{4})\.(\d{5})", arxiv_id)
            if not match:
                return None, None
            return int(match.group(1)), int(match.group(2))

        if not paper_id or not reference_id:
            self.logger.error("Both paper_id and reference_id must be provided.")
            return False

        paper_id_norm = normalize(paper_id)
        reference_id_norm = normalize(reference_id)
        if all(t_paper is None for t_paper in paper_id_norm) or all(
            t_ref is None for t_ref in reference_id_norm
        ):
            self.logger.error(
                f"Invalid arXiv ID format: paper_id={paper_id}, reference_id={reference_id}"
            )
            return False

        # If the year is the same, compare the number
        if paper_id_norm[0] == reference_id_norm[0]:
            return paper_id_norm[1] > reference_id_norm[1]
        # If the year is different, compare the years
        else:
            return paper_id_norm[0] > reference_id_norm[0]

    def fetch(
        self,
        n_papers: int,
        n_pattern_papers: int = 0,
        write: bool = True,
    ) -> list[ArxivPaper]:
        """
        Fetch new papers from arXiv, skipping already fetched ones, and stores their metadata in an `ArxivPaper`
        pydantic models. The newest fetched arXiv ID will be stored in `fetched_arxiv_ids.txt`.

        Args:
            n_papers (int): The number of papers to fetch from arXiv.
            n_pattern_papers (int, optional): The number of papers to fetch that match a specific regex pattern.
                This is useful for fetching papers that match a specific pattern, e.g., "cond-mat.str-el". Defaults to 0.
            write (bool, optional): If True, the fetched papers will be written to the `fetched_arxiv_ids.txt` file.
                Defaults to True.

        Returns:
            list[ArxivPaper]: A list of `ArxivPaper` objects with the metadata of the papers fetched from arXiv.
        """
        papers: list[ArxivPaper] = []
        while (
            len(papers) < self.max_results
            and (len(papers) + n_pattern_papers) < n_papers
        ):
            # ! commented out due to a bug in the arXiv API
            # remaining = self.max_results - len(papers)  # remaining papers to fetch
            # current_batch_size = min(self.max_results, remaining)

            # Fetch a batch of papers from arXiv
            batch = get_batch_response(
                category=self.category,
                start_index=self.start_index,
                max_results=self.max_results,
                logger=self.logger,
            )
            if not batch:
                self.logger.info("No papers found in the response")
                return []
            # In case `max_results` is 1, the response is not a list
            if not isinstance(batch, list):
                batch = [batch]

            # Store papers object ArxivPaper in a list
            initial_len = len(papers)
            for new_paper in batch:
                # If there is an error in the fetching, skip the paper
                if "Error" in new_paper.get("title", ""):
                    self.logger.error("Error fetching the paper")
                    # new_papers = papers
                    continue

                # If there is no `id`, skip the paper
                url_id = new_paper.get("id")
                if not url_id or "arxiv.org" not in url_id:
                    self.logger.error(f"Paper without a valid URL id: {url_id}")
                    # new_papers = papers
                    continue

                # Getting arXiv `id`, and skipping if newer than the `start_id`
                arxiv_id = url_id.split("/")[-1].replace(".pdf", "")
                if self.skip_newer_ids and self.is_newer_than(arxiv_id, self.start_id):
                    continue

                # If there is no `summary`, skip the paper
                summary = new_paper.get("summary")
                if not summary:
                    self.logger.error(f"Paper {url_id} without summary/abstract")
                    # new_papers = papers
                    continue

                # Extracting `authors` from the XML response
                paper_authors = new_paper.get("author", [])
                if not isinstance(paper_authors, list):
                    paper_authors = [paper_authors]
                authors = [
                    Author(
                        name=author.get("name"), affiliation=author.get("affiliation")
                    )
                    for author in paper_authors
                ]
                if not authors:
                    self.logger.info("\tPaper without authors.")

                # Extracting `categories` from the XML response
                arxiv_categories = new_paper.get("category", [])
                if not isinstance(arxiv_categories, list):
                    categories = [arxiv_categories.get("@term")]
                else:
                    categories = [
                        category.get("@term") for category in arxiv_categories
                    ]

                # Extracting pages and figures from the comment
                comment = new_paper.get("arxiv:comment", {}).get("#text", "")
                n_pages, n_figures = self._get_pages_and_figures(comment=comment)

                # Storing the ArxivPaper object in the list
                papers.append(
                    ArxivPaper(
                        id=arxiv_id,
                        url=url_id,
                        pdf_url=url_id.replace("abs", "pdf"),
                        updated=new_paper.get("updated"),
                        published=new_paper.get("published"),
                        title=new_paper.get("title"),
                        summary=summary,
                        authors=authors,
                        comment=comment,
                        n_pages=n_pages,
                        n_figures=n_figures,
                        categories=categories,
                    )
                )

                # ! too many messages, so I commented this out
                # self.logger.info(f"Paper {arxiv_id} fetched from arXiv.")

                # Making sure we do not exceed the number of papers to fetch
                if len(papers) >= self.max_results:
                    break

            # safeguard: break if no valid papers were added in this batch
            if len(papers) == initial_len:
                self.logger.warning(
                    f"No valid papers added in batch starting at index {self.start_index}. "
                    "This might indicate that all were skipped (e.g. newer than start_id, invalid, etc.). Exiting loop."
                )
                break

            # Incrementing the start index for the next batch
            self.start_index += self.max_results

        # If the fetched results are less than the starting point, increment the start index
        if not papers:
            self.start_index += self.max_results

        # Storing last fetched ID to the file if `start_from_filepath` is specified
        if write and papers:
            with open(self.fetched_ids_file, "w") as f:
                f.write(papers[-1].id)
        return papers
