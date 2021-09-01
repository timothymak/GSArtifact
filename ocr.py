import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('./test/test_images/kokomi.png')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)
cv2.imshow('Test Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

custom_config = r'-l jpn --oem 3 --psm 6'
out = pytesseract.image_to_string(gray, config=custom_config)
print(out)