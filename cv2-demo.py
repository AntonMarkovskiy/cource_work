import cv2
import numpy as np

SOURCES = {'video1': "Hourglass.mp4", "web": 0}


class Cv2Demo:
    @staticmethod
    def capture_video(source):
        cap = cv2.VideoCapture(source)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Error reading frame!")
                break
            yield frame
            if cv2.waitKey(25) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    @staticmethod
    def process_frame(frame, process_func, *args, **kwargs):
        return process_func(frame, *args, **kwargs)

    @staticmethod
    def motion_blur(image, kernel_size=3):
        kernel_motion_blur = np.zeros((kernel_size, kernel_size))
        kernel_motion_blur[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
        kernel_motion_blur = kernel_motion_blur / kernel_size
        return cv2.filter2D(image, -1, kernel_motion_blur)

    @staticmethod
    def corner_detector(image, max_corners=5, quality_level=0.01, min_dist=20):
        new_image = image.copy()
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray_image, max_corners, quality_level, min_dist)
        corners = np.float32(corners)
        for item in corners:
            x, y = item[0]
            cv2.circle(new_image, (int(x), int(y)), 5, 255, -1)
        return new_image

    @staticmethod
    def colorspace_change(input_frame):
        return cv2.cvtColor(input_frame, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def rotate(video, angle):
        num_rows, num_cols = video.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), angle, 1)
        img_rotation = cv2.warpAffine(video, rotation_matrix, (num_cols, num_rows))
        return img_rotation

    @classmethod
    def menu(cls):
        print("\nChoose an option:")
        print("1. Capture Video")
        print("2. Capture Webcam")
        print("3. Apply Filter")
        print("4. Detect Corners")
        print("5. Convert to Grayscale")
        print("6. Rotate Video")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            for frame in cls.capture_video(SOURCES.get('video1')):
                cv2.imshow('frame', frame)
        elif choice == '2':
            for frame in cls.capture_video(SOURCES.get('web')):
                cv2.imshow('frame', frame)
        elif choice == '3':
            cls.process_video(SOURCES.get('video1'), cls.motion_blur, kernel_size=7)
        elif choice == '4':
            cls.process_video(SOURCES.get('video1'), cls.corner_detector, max_corners=20, quality_level=0.01,
                              min_dist=50)
        elif choice == '5':
            cls.process_video(SOURCES.get('video1'), cls.colorspace_change)
        elif choice == '6':
            cls.process_video(SOURCES.get('video1'), cls.rotate, angle=30)
        cv2.destroyAllWindows()

    @classmethod
    def process_video(cls, source, process_func, *args, **kwargs):
        cap = cv2.VideoCapture(source)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Error reading frame!")
                break
            processed_frame = cls.process_frame(frame, process_func, *args, **kwargs)
            cv2.imshow('frame', frame)
            cv2.imshow('processed_frame', processed_frame)
            if cv2.waitKey(25) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)


if __name__ == "__main__":
    Cv2Demo.menu()
