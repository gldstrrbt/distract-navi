import sounddevice as sd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import _find_element
import selenium.webdriver.common.action_chains
from selenium.webdriver.common.action_chains import ActionChains

duration = (((10*6)*60)*24)*7

def distract_navi():
	driver = webdriver.Firefox(executable_path="./geckodriver")
	driver.get("https://youtu.be/0B7FMcuGFrU?t=5")
	time.sleep(7)
	driver.close()

def print_sound(indata, outdata, frames, time, status):
	volume_norm = np.linalg.norm(indata)*10
	print(int(volume_norm))
	if int(volume_norm) > 20:
		distract_navi()

def init():
	with sd.Stream(callback=print_sound):
		sd.sleep(duration * 1000)
		init()

init()
