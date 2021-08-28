'''
@author: PANAGIOP
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from PageLocators import TestCaseLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Browser(object):
    
    def __init__(self):
        self.driver = ''

    def open_chrome_driver(self):
        
        self.driver = webdriver.Chrome(TestCaseLocators.CHROME_DRIVER_PATH)
        self.driver.maximize_window()
        
    def close_browser(self):
        self.driver.close()
        
    def open_URL(self,input_URL):
        self.driver.get(input_URL)
    
def waitForLoadById(self, inputValue): 
    try:
        testWait = WebDriverWait(self.browser.driver, TestCaseLocators.max_wait_time)
        element = testWait.until(EC.presence_of_element_located((By.ID, inputValue)))
        time.sleep(0.5)
        return(element)
    except TimeoutException: 
        self.browser.driver.find_element_by_id(inputValue)
        
        
def waitForLoadByClassName(self, inputValue): 
    try:
        testWait = WebDriverWait(self.browser.driver, TestCaseLocators.max_wait_time)
        element = testWait.until(EC.presence_of_element_located((By.CLASS_NAME, inputValue)))
        time.sleep(0.5)
        return(element)
    except TimeoutException: 
        self.browser.driver.find_element_by_class_name(inputValue)
        
        
def waitForLoadByIdContinue(self, inputValue): 
    try:
        testWait = WebDriverWait(self.browser.driver, TestCaseLocators.max_wait_time)
        element = testWait.until(EC.presence_of_element_located((By.ID, inputValue)))
        time.sleep(0.5)
        return(element)
    except TimeoutException:
        return(False)
    
def waitForLoadByClassNameContinue(self, inputValue): 
    try:
        testWait = WebDriverWait(self.browser.driver, TestCaseLocators.max_wait_time)
        element = testWait.until(EC.presence_of_element_located((By.CLASS_NAME, inputValue)))
        time.sleep(0.5)
        return(element)
    except TimeoutException:
        return(False)
    
def waitElementToLoadByClassName(self,inputValue):
    element =  waitForLoadByClassNameContinue(self,inputValue)
    i=0
    while( not (element) and i< TestCaseLocators.max_wait_time):                                                       
        element = waitForLoadByClassNameContinue(self,inputValue)
    i+=1
    return element

def waitElementToLoadByID(self,inputValue):
    element =  waitForLoadByIdContinue(self,inputValue)
    i=0
    while( not (element) and i< TestCaseLocators.max_wait_time):                                                       
        element = waitForLoadByIdContinue(self,inputValue)
    i+=1
    return element
      
def SelectValueFromListByName(self,object_menu,value):
    for tab in object_menu.find_elements_by_tag_name('li'):
        if value in str(tab.text).upper():
            tab.click()
            break
        
        
def SelectValueFromListByIndex(self,index_value,product_elemets):
    index=0
    for product in product_elemets:
        if index==index_value:
            product.click()
            break 
        index += 1
        
        
        
        
        