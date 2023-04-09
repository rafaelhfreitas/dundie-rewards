from sqlmodel import Session, create_engine

from dundie import models
from dundie.settings import SQL_CON_STRING

import warnings
from sqlalchemy.exc import SAWarning

from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

warnings.filterwarnings(
    'ignore', category=SAWarning
)

engine = create_engine(SQL_CON_STRING, echo=False)

models.SQLModel.metadata.create_all(bind=engine)


def get_session() -> Session:
    return Session(engine)
