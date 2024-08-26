# Libraries
from tools.camera_reader import Camera
from tools.system_manager import Manager
import cv2

# Main Method
if __name__ == "__main__":
    # Create manager object
    manager = Manager('sources/example.db')

    # For operation selection
    while True:
        try:
            operation = int(input("1-Register\n2-Login\nSelect: "))
            if operation == 1:
                manager.register()
                break
            elif operation == 2:

                break
            else:
                print("Invalid selection. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    manager.close()



