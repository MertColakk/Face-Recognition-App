# Library
import sqlite3

# Database Class
class SQL_Connector:
    def __init__(self, db_file_name: str):
        try:
            self.db_name = db_file_name
            self.db_result = None

            # Connect Database
            self.db_connection = sqlite3.connect(self.db_name)

            # Create Cursor
            self.db_cursor = self.db_connection.cursor()

            if self.db_connection and self.db_cursor:
                print("Database initialization successful!")
        except sqlite3.Error as error:
            print(f"There is an error: {error}")

    def add_data(self,name : str,face_vector : str):
        self.db_cursor.execute("""
            INSERT INTO HUMAN (name, face)
            VALUES (?, ?)
        """,(name,face_vector))

        self.db_connection.commit()

        print("Human added successfully!")

    def close_sql_connection(self):
        self.db_cursor.close()
        self.db_connection.close()

        print("Database connection closed successfully!")


