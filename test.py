import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


print(pytesseract.image_to_string('C:\\Users\\MIFIKUS\\Downloads\\avail1 (1).png', config='--psm 12--oem 3 -c tessedit_char_whitelist=0123456789'))