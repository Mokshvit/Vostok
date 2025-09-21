import cv2 as cv
import mediapipe as mp
img  = cv.imread('vostok.jpg')

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

capture = cv.videocapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow("Hand", frame)
    if cv.wait(key) & 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()