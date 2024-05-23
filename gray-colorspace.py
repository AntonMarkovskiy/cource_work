# підключення необхідних бібліотек
import cv2

sources = {'video1': "Hourglass.mp4", "web": 0}
colorspaces = {'Gray': cv2.COLOR_BGR2GRAY, 'XYZ': cv2.COLOR_BGR2XYZ, 'LAB': cv2.COLOR_BGR2LAB,
               'YUV': cv2.COLOR_BGR2YUV, 'HSV': cv2.COLOR_BGR2HSV}


def colorspace_change(input_frame):
    return cv2.cvtColor(input_frame, cv2.COLOR_BGR2GRAY)

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

        # Зміна колірного простору зображення (фрейму)
        frame_gray = colorspace_change(frame)

        # Відображення результату
        cv2.imshow('frame Grayscale', frame_gray)
        if cv2.waitKey(25) == ord('q'):
            break
    # Завершуємо запис у кінці роботи
    cap.release()
    cv2.destroyAllWindows()


# при запуску як головного файлу
if __name__ == '__main__':
    main()
