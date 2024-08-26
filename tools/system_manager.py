# Libraries
from tools.sql_connector import SQL_Connector
from tools.camera_reader import Camera
from tools.timekeeper import Timekeeper
import time
import cv2

class Manager:
    def __init__(self, database_path : str):
        self.database = SQL_Connector(database_path)
        self.camera = Camera()


    def register(self):
        # Take name of user
        new_user_name = str(input("Please enter user's name: "))
        new_user_face = None

        # Create Timekeeper object
        timekeeper = Timekeeper(10)
        timekeeper.start()

        while True:
            # Read frames from camera
            frame = self.camera.read_frames()

            # Convert frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get user face vector


            # Show frames
            cv2.imshow("Camera", frame)

            if timekeeper.finished:
                cv2.destroyWindow("Camera")
                break

        self.database.add_data(new_user_name, new_user_face)


    def close(self):
        # Release Camera
        self.camera.release()

        # Close database connection
        self.database.close_sql_connection()



"""
# If user presses q close window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

"""