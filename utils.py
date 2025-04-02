from constants import URL, DATA_PATH, DEFAULT_RECORDS_COUNT
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def download_latest_data() -> None:
    try:
        logger.info("Downloading today's data ...")
        dest_file = DATA_PATH / "sponsors.csv"

        df = pd.read_csv(URL)
        df.to_csv(dest_file, index=False)
        logger.info("Latest data has been downloaded")

    except Exception as exception:
        logger.warning("Unable to download latest data. Relying on the latest stored data")
        logger.exception(exception)


def read_data(name: str = None) -> dict:
    src_file = DATA_PATH / "sponsors.csv"

    df = pd.read_csv(src_file)
    df = df.fillna("")

    if name not in ("", None):
        result = df[df["Organisation Name"].str.contains(name.strip())]
        count = len(df)
    else:
        count = DEFAULT_RECORDS_COUNT
        result = df.head(count)

    json_result = result.to_dict("tight")

    return count, json_result.get("columns"), json_result.get("data")