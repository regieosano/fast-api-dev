from db.database import create_database_table


def init_db():
 # Create the database and table
    try:
        create_database_table()
        print("Database and Tables Created!")
    except Exception as error:
        print("Error: Database NOT Created!", error)
