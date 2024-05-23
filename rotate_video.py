import cv2

sources = {'video1': "Hourglass.mp4", "web": 0}

# Функція поворту відео
def rotate(video, angle):
    num_rows, num_cols = video.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), angle, 1)
    img_rotation = cv2.warpAffine(video, rotation_matrix, (num_cols, num_rows))
    return img_rotation

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

        frame_rotate = rotate(frame, 30)

        # Відображення результату
        cv2.imshow('frame', frame_rotate)
        if cv2.waitKey(25) == ord('q'):
            break
    # Завершуємо запис у кінці роботи
    cap.release()
    cv2.destroyAllWindows()


# при запуску як головного файлу
if __name__ == '__main__':
    main()