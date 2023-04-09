import os

SMTP_HOST: str = "localhost"
SMTP_PORT: int = 8025
SMTP_TIMEOUT: int = 5

EMAIL_FROM: str = "admin@teste.com"
DATEFMT: str = "%d/%m/%Y %H:%M:%S"

ROOT_PATH: str = os.path.dirname(__file__)
DATABASE_PATH: str = os.path.join(ROOT_PATH, "..", "assets", "database.db")
SQL_CON_STRING: str = f"sqlite:///{DATABASE_PATH}"
