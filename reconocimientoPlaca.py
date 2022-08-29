# Limrerias opencv y teseract
import cv2 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #path donde se encuentra tesseract

placa = [] #se almacenara imagen de placa detectada
image = cv2.imread('placa3.webp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 150, 200)
#canny = cv2.dilate(canny, None, iterations=1)
cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)#OpenCV 4
print(cnts)
print(cv2.RETR_LIST)
for c in cnts:
   area = cv2.contourArea(c)
   if area > 2000 and area < 7000:
        print(area)
        cv2.drawContours(image,[c],-1,(0,255,0),2)

cv2.imshow('Imagen de Vehiculo', image)
cv2.imshow('Bordes', canny)
cv2.waitKey(0)