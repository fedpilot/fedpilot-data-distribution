from src.downloaders.dataset_downloader import download_client_dataset
from src.validators.config_validator import ConfigValidator
from src.utils.log import Log


def get_client_dataset(url_or_path: str, config: ConfigValidator,  log: Log):

    if url_or_path.lower().startswith("http"):
        client_dataset = download_client_dataset()
    else:
        client_dataset = read_client_dataset(url_or_path)



def read_client_dataset(path: str):
    return NotImplemented