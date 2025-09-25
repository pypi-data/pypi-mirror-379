from __future__ import annotations

import shutil
import sys
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Dict, List, Tuple

import requests
from loguru import logger
from rich.progress import Progress, SpinnerColumn, TextColumn

from brats.constants import ADDITIONAL_FILES_FOLDER, ZENODO_RECORD_BASE_URL
from brats.utils.exceptions import ZenodoException


def get_dummy_path() -> Path:
    dummy = ADDITIONAL_FILES_FOLDER / "dummy"
    dummy.mkdir(exist_ok=True, parents=True)
    return dummy


def check_additional_files_path(record_id: str) -> Path:
    """Check if latest additional files are present and download them otherwise.

    Args:
        record_id (str): Zenodo record ID.

    Raises:
        ZenodoException: If the additional files are not found locally and Zenodo is unreachable.

    Returns:
        Path: Path to the additional files folder.
    """

    zenodo_response = _get_zenodo_metadata_and_archive_url(record_id=record_id)

    record_additional_files_pattern = f"{record_id}_v*.*.*"
    matching_folders = list(
        ADDITIONAL_FILES_FOLDER.glob(record_additional_files_pattern)
    )
    # Get the latest downloaded additional_files
    latest_downloaded_additional_files = _get_latest_version_folder_name(
        matching_folders
    )

    if not latest_downloaded_additional_files:
        if not zenodo_response:
            msg = "Additional files not found locally and Zenodo could not be reached. Exiting..."
            logger.error(msg)
            raise ZenodoException(msg)
        logger.info(f"Additional files not found locally")

        zenodo_metadata, archive_url = zenodo_response
        return _download_additional_files(
            zenodo_metadata=zenodo_metadata,
            record_id=record_id,
            archive_url=archive_url,
        )

    logger.info(
        f"Found downloaded local additional_files: {latest_downloaded_additional_files}"
    )

    if not zenodo_response:
        logger.warning(
            "Zenodo server could not be reached. Using the latest downloaded additional files."
        )
        return ADDITIONAL_FILES_FOLDER / latest_downloaded_additional_files

    zenodo_metadata, archive_url = zenodo_response
    # Compare the latest downloaded additional files with the latest Zenodo version
    if zenodo_metadata["version"] == latest_downloaded_additional_files.split("_v")[1]:
        logger.info(
            f"Latest additional files ({latest_downloaded_additional_files}) are already present."
        )
        return ADDITIONAL_FILES_FOLDER / latest_downloaded_additional_files

    logger.info(
        f"New additional files available on Zenodo ({zenodo_metadata['version']}). Deleting old and fetching new additional files..."
    )
    # delete old additional files
    shutil.rmtree(
        ADDITIONAL_FILES_FOLDER / latest_downloaded_additional_files,
        onerror=lambda func, path, excinfo: logger.warning(
            f"Failed to delete {path}: {excinfo}"
        ),
    )
    return _download_additional_files(
        zenodo_metadata=zenodo_metadata, record_id=record_id, archive_url=archive_url
    )


def _get_latest_version_folder_name(folders: List[Path]) -> str | None:
    """Get the latest (non empty) version folder name from the list of folders.

    Args:
        folders (List[Path]): List of folders matching the pattern.

    Returns:
        str | None: Latest version folder name if one exists, else None.
    """
    if not folders:
        return None
    latest_downloaded_folder = sorted(
        folders,
        reverse=True,
        key=lambda x: tuple(map(int, str(x).split("_v")[1].split("."))),
    )[0]
    # check folder is not empty
    if not list(latest_downloaded_folder.glob("*")):
        return None
    return latest_downloaded_folder.name


def _get_zenodo_metadata_and_archive_url(record_id: str) -> Tuple[Dict, str] | None:
    """Get the metadata for the Zenodo record and the files archive url.

    Args:
        record_id (str): Zenodo record ID.

    Returns:
        Union[Tuple[Dict,str], None]: Tuple with Metadata dict and archive URL if the record exists, else None.
    """
    try:
        response = requests.get(f"{ZENODO_RECORD_BASE_URL}/{record_id}")
        if response.status_code != 200:
            error_msg = f"Can not find additional files for record_id '{record_id}' on Zenodo ({response.status_code=}). Exiting..."
            logger.error(error_msg)
            raise ZenodoException(error_msg)

        data = response.json()
        return data["metadata"], data["links"]["archive"]

    except requests.exceptions.RequestException as e:
        logger.warning(f"Failed to fetch Zenodo metadata: {e}")
        return None


def _download_additional_files(
    zenodo_metadata: Dict, record_id: str, archive_url: str
) -> Path:
    """Download the latest additional files from Zenodo for the requested record and extract them to the target folder.

    Args:
        zenodo_metadata (Dict): Metadata for the Zenodo record.
        record_id (str): Zenodo record ID.
        archive_url (str): URL to the archive file.

    Raises:
        ZenodoException: If the download fails or the response is not successful.

    Returns:
       Path: Path to the folder where the additional files were extracted.
    """
    record_folder = (
        ADDITIONAL_FILES_FOLDER / f"{record_id}_v{zenodo_metadata['version']}"
    )
    # ensure folder exists
    record_folder.mkdir(parents=True, exist_ok=True)

    logger.info(f"Downloading additional files from Zenodo. This might take a while...")
    # Make a GET request to the URL
    response = requests.get(archive_url, stream=True)
    # Ensure the request was successful
    if response.status_code != 200:
        error_msg = (
            f"Failed to download additional files. Status code: {response.status_code}"
        )
        logger.error(error_msg)
        raise ZenodoException(error_msg)

    _extract_archive(response=response, record_folder=record_folder)

    logger.info(f"Zip file extracted successfully to {record_folder}")
    return record_folder


def _extract_archive(response: requests.Response, record_folder: Path):
    # Download with progress bar
    chunk_size = 1024  # 1KB
    bytes_io = BytesIO()

    with Progress(
        SpinnerColumn(),
        TextColumn("[cyan]Downloading additional files..."),
        TextColumn("[cyan]{task.completed:.2f} MB"),
        transient=True,
    ) as progress:
        task = progress.add_task("", total=None)  # Indeterminate progress

        for data in response.iter_content(chunk_size=chunk_size):
            bytes_io.write(data)
            progress.update(
                task, advance=len(data) / (chunk_size**2)
            )  # Convert bytes to MB

    # Extract the downloaded zip file to the target folder
    with zipfile.ZipFile(bytes_io) as zip_ref:
        zip_ref.extractall(record_folder)

    # check if the extracted file is still a zip
    for f in record_folder.iterdir():
        if f.is_file() and f.suffix == ".zip":
            with zipfile.ZipFile(f) as zip_ref:
                files = zip_ref.namelist()
                with Progress(transient=True) as progress:
                    task = progress.add_task(
                        "[cyan]Extracting files...", total=len(files)
                    )
                    # Iterate over the files and extract them
                    for i, file in enumerate(files):
                        zip_ref.extract(file, record_folder)
                        # Update the progress bar
                        progress.update(task, completed=i + 1)
            f.unlink()  # remove zip after extraction
