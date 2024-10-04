import json
import os
import requests


CONFIG_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json')
with open(CONFIG_FILE, 'r') as f:
    CONFIG = json.load(f)


def download_latest_yiedl_dataset(
        local_filepath=CONFIG['defaultLatestDatasetFilename'],
        show_progress=True) -> None:
    """
    Downloads the latest dataset from the Yiedl API.
    :param local_filepath: (optional) Path to save the latest dataset to.
    :param show_progress: (optional) If true, shows the percentage of the download progress.
    :return: None. Saves the dataset to the specified path.
    """
    url = f"{CONFIG['baseUrl']}?type={CONFIG['latestDatasetType']}"
    _download(url, local_filepath, show_progress)
    print(f"\nLatest dataset downloaded to {local_filepath}.")


def download_historical_yiedl_dataset(
        local_filename=CONFIG['defaultHistoricalDatasetFilename'],
        show_progress=True) -> None:
    """
    Downloads the historical dataset from the Yiedl API.
    :param local_filename: (optional) Path to save the historical dataset to.
    :param show_progress: (optional) If true, shows the percentage of the download progress.
    :return: None. Saves the dataset to the specified path.
    """
    url = f"{CONFIG['baseUrl']}?type={CONFIG['historicalDatasetType']}"
    _download(url, local_filename, show_progress)
    print(f"\nHistorical dataset downloaded to {local_filename}.")


def _download(url: str, local_filename: str, show_progress: bool) -> None:
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        chunk_size = CONFIG['chunkSize']
        downloaded_size = 0
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)
                if show_progress:
                    downloaded_size += len(chunk)
                    if total_size > 0:
                        progress = (downloaded_size / total_size) * 100
                        print(f"\rProgress: {progress:.2f}%", end="")

