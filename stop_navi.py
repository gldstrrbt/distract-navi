import sounddevice as sd
import numpy as np
import os, time
from pygame import mixer
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.expected_conditions import _find_element
# import selenium.webdriver.common.action_chains
# from selenium.webdriver.common.action_chains import ActionChains
##sd.default.samplerate = 44100
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

##sd.check_output_settings(device=None, channels=None, dtype=None, extra_settings=None, samplerate=None)

duration = (((10*6)*60)*24)*7

def distract_navi():
    mixer.init()
    mixer.music.load("./navi_call.mp3")
    mixer.music.play()
##    driver = webdriver.Chrome()
##    driver.get("https://youtu.be/0B7FMcuGFrU?t=5")
##    time.sleep(7)
##    driver.close()

def print_sound(indata, frames, time, status):
    print(status)
    print(indata)
    volume_norm = np.linalg.norm(indata)*10
    print(int(volume_norm))
    if int(volume_norm) > 30:
        distract_navi()

def init():
    with sd.InputStream(callback=print_sound):
        sd.sleep(duration * 1000)
        ## init()

init()
