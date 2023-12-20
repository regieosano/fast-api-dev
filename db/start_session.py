from db.database import engine
from sqlalchemy.orm import sessionmaker


def init_session(route_module: str):
    try:
        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session = Session()
        print(f"{route_module} Session Established!")
        return session
    except Exception as error:
        print(f"Error: {route_module} Session Connection Failed!", error)
