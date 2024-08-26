#  Libraries
import cv2

# Camera class
class Camera:
    def __init__(self,device_index=0):
        self.device_index = device_index
        self.camera_object = None

        camera_control = self.create_camera()

        if camera_control:
            print("Camera object created successfully!")
        else:
            print("There is an error while creating camera!")

    def create_camera(self):
        self.camera_object = cv2.VideoCapture(self.device_index)

        if self.camera_object.isOpened():
            return True

        return False

    def read_frames(self):
        _, frame = self.camera_object.read()

        if not _:
            return None

        return frame

    def release(self):
        # Release camera object
        self.camera_object.release()

        print("Camera released successfully!")

