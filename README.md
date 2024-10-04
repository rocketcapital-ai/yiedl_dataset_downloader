# Downloader for [YIEDL Datasets](https://yiedl.ai/competition/datasets)

## Dependencies
The [requests](https://pypi.org/project/requests/) library.
```
pip install requests
```

## Usage
Place the files in the `lib` folder in a directory of your choosing and import the functions 
- `download_latest_yiedl_dataset` and;
- `download_historical_yiedl_dataset` 

from the `yiedl_dataset_downloader` module.

For both functions, you may optionally specify a custom file path to save to under the input parameter `local_filename`.
