from PIL import Image
import pytesseract

def imgToWord(imgPath):
    if imgPath == '':
        imgPath = '/Users/apple/Desktop/orcTest.png';
        print ('imgPath='+imgPath);

    code=pytesseract.image_to_string(Image.open(imgPath),lang='chi_sim')
    print(code)
    return code