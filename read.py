import cv2 as cv 

#Lire les images
"""img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)"""

#Lire les vidéos

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()