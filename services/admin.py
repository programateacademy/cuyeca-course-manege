import config.database as _database

def create_database():
    return _database.Base.create_all(bind=_database.engine)