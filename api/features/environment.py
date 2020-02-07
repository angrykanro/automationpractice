from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selene.support.shared import browser, config

# def after_scenario(context, scenario):
    # Attaching image
    # f = open('./files/fescobar.png', "rb")
    # image = f.read()
    # attach(image, name='image', attachment_type=AttachmentType.PNG)

    # Attaching video
    # f = open('./files/google.mp4', "rb")
    # video = f.read()
    # attach(video, name='video', attachment_type=AttachmentType.MP4)



def before_all(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # context.browser = webdriver.Chrome(options=chrome_options)
    browser.config.driver = webdriver.Chrome(options=chrome_options)
    context.browser = browser
    # context.browser.implicitly_wait(10)
    

def after_all(context):
    context.browser.quit()