from selenium import webdriver
from PIL import Image
from pytesseract import image_to_string
import pytesseract
import time
#recaptcha libraries
import speech_recognition as sr
import ffmpy
import requests
import urllib
import pydub
pytesseract.pytesseract.tesseract_cmd = (r"E:\Program File\Tesseract-OCR\tesseract.exe")
browser = webdriver.Chrome('E:\\Python_Pratics\\Auto_website\\chromedriver')
# login into the Website
browser.get("https://services.gst.gov.in/services/login")
# browser.set_page_load_timeout(30)
time.sleep(10)
# Enter Login Details
browser.find_element_by_id('username').send_keys("HarshAutomobile")
browser.find_element_by_id('user_pass').send_keys("Vageta@0786")
# click on play button
browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/form/div[5]/div/div/div/table/tbody/tr[1]/th[2]/button').click()
# get the mp3 file
# time.sleep(5)
# src = browser.find_elements_by_xpath
# src = "https://services.gst.gov.in/services/audiocaptcha"
# print("[INFO] Audio src: %s"%src)
#download the mp3 audio file from the source
# urllib.request.urlretrieve('https://services.gst.gov.in/services/audiocaptcha', "E:\\Python_Pratics\\Auto_website\\sample.mp3")
# urllib.request.urlretrieve(src,"E:\\Python_Pratics\\Auto_website\\sample.mp3")
sound = pydub.AudioSegment.from_mp3("E:\\Python_Pratics\\Auto_website\\sample.mp3")
sound.export("E:\\Python_Pratics\\Auto_website\\sample.wav", format="wav")
sample_audio = sr.AudioFile("E:\\Python_Pratics\\Auto_website\\sample.mp3")
r= sr.Recognizer()
with sample_audio as source:
    audio = r.record(source)

# #translate audio to text with google voice recognition
key=r.recognize_google(audio)
print("[INFO] Recaptcha Passcode: %s"%key)



# working on Captcha
# location=captcha.location
# size=captcha.size
# browser.save_screenshot('E:\\Python_Pratics\\Auto_website\\screenshot.png')
# # browser.find_element_by_id('captcha').send_keys(captchatext)
# im = Image.open('E:\\Python_Pratics\\Auto_website\\screenshot.png') # uses PIL library to open image in memory
# left = location['x']
# top = location['y']
# right = location['x'] + size['width']
# bottom = location['y'] + size['height']
# im = im.crop((left, top, right, bottom)) # defines crop points
# im.save('E:\\Python_Pratics\\Auto_website\\screenshot1.png')
# captcha_text = image_to_string(Image.open('E:\\Python_Pratics\\Auto_website\\screenshot1.png'))
# print(captcha_text)