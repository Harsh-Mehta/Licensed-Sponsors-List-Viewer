from pathlib import Path
from datetime import datetime

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH / "data"

today_date_str: str = datetime.today().strftime("%Y-%m-%d")
URL: str = f"https://assets.publishing.service.gov.uk/media/67e28763148bef6fa4cfda6d/[{today_date_str}_-_Worker_and_Temporary_Worker.csv"

DEFAULT_RECORDS_COUNT: int = 8