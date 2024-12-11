from db.models.models import Base
from db.session import engine

def init_db():
    '''
    Connection to the database.
    '''
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f'Error {e}')
