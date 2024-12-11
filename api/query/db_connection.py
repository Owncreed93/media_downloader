from db.session import SessionLocal

def get_db():
    '''
    Get's a local connection through a session to the database.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()