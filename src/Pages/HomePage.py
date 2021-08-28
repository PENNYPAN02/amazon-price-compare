import Common
from PageLocators import HomepageLocators

class HomePage(object):
    
    def __init__(self, browser):
        self.browser = browser
    
    def getAllMenu_Button(self):
        element= Common.waitElementToLoadByID(self,HomepageLocators.ALL_MENU_BUTTON)
        return element
    
    def clickAllMenu_Button(self):
        HomePage.getAllMenu_Button(self).click()
    
    def getCategoriesList(self):
        element= Common.waitElementToLoadByID(self,HomepageLocators.ALL_MENU_CONTENT)
        visible_element=element.find_element_by_class_name(HomepageLocators.ALL_MENU_CATEGORIES_LIST)
        return visible_element
    
    def SelectCategoryOptionFromMenu(self,list_elements,value):
        Common.SelectValueFromListByName(self,list_elements,value)