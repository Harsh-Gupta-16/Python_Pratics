from pytesseract import image_to_string
import pytesseract
pytesseract.pytesseract.tesseract_cmd = (r"E:\Program File\Tesseract-OCR\tesseract.exe")
location=captcha.location
size=captcha.size
browser.save_screenshot('E:\\Python_Pratics\\Auto_website\\screenshot.png')
# browser.find_element_by_id('captcha').send_keys(captchatext)
im = Image.open('E:\\Python_Pratics\\Auto_website\\screenshot.png') # uses PIL library to open image in memory
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
im = im.crop((left, top, right, bottom)) # defines crop points
im.save('E:\\Python_Pratics\\Auto_website\\screenshot1.png')
captcha_text = image_to_string(Image.open('E:\\Python_Pratics\\Auto_website\\screenshot1.png'))
print(captcha_text)