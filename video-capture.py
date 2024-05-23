# підключення необхідних бібліотек
import cv2

sources = {'video1': "Hourglass.mp4", "web": 0}


def main():
    # зчитування даних з відеофайлу
    cap_video = cv2.VideoCapture(sources.get('video1'))
    while cap_video.isOpened():
        # Запис фреймів
        ret, frame = cap_video.read()
        # При виникненні помилці запису
        if not ret:
            print("Помилка запису фрейму!")
            break
        # Відображення результату
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break
    # Завершуємо запис у кінці роботи
    cap_video.release()
    
    # зчитування даних з відеокамери
    cap_web = cv2.VideoCapture(sources.get('web'))
    # Перевірка готовності веб-камери
    while cap_web.isOpened():
        # Запис фреймів
        ret, frame = cap_web.read()
        # При виникненні помилці запису
        if not ret:
            print("Помилка запису фрейму!")
            break
        # Відображення результату
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break
    cv2.destroyAllWindows()


# при запуску як головного файлу
if __name__ == '__main__':
    main()