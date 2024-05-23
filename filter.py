# підключення необхідних бібліотек
import cv2
import numpy as np


sources = {'video1': "Hourglass.mp4", "web": 0}

# Фільтрація з ефектом зсуву
def motion_blur(image, kernel_size=3):
    kernel_motion_blur = np.zeros((kernel_size, kernel_size))
    kernel_motion_blur[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
    kernel_motion_blur = kernel_motion_blur / kernel_size
    return cv2.filter2D(image, -1, kernel_motion_blur)

def main():
    cap = cv2.VideoCapture(sources.get('video1'))
    # Перевірка готовності веб-камери
    while cap.isOpened():
        # Запис фреймів
        ret, frame = cap.read()
        # При виникненні помилці запису
        if not ret:
            print("Помилка запису фрейму!")
            break

        frame_changed = motion_blur(frame, kernel_size=7)

        # Відображення результату
        cv2.imshow('frame', frame)
        cv2.imshow('frame_changed', frame_changed)
        if cv2.waitKey(25) == ord('q'):
            break
    # Завершуємо запис у кінці роботи
    cap.release()
    cv2.destroyAllWindows()


# при запуску як головного файлу
if __name__ == '__main__':
    main()