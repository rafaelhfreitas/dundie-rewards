"""Core modules of dundie """

from dundie.utils.log import get_logger

log = get_logger()



def load(filepath):
    """Loads data from filepath to the database
    
    python3 -m doctest -v dundie/core.py 

    >>> len(load('assets/people.csv'))
    2
    >>> load('assets/people.csv')[0][0]
    'R'

    """
    try:
        with open(filepath) as file_:
            return file_.readlines()
    except FileNotFoundError as e:
        print(f"File doesnt exists {e}")
        log.error(str(e))
        raise e