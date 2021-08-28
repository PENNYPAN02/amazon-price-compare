import Common
from PageLocators import CartPageLocators

class CartPage(object):
    
    def __init__(self, browser):
        self.browser = browser
    
    def getCartButton(self):
        element=Common.waitElementToLoadByID(self,CartPageLocators.VIEW_CART_BUTTON)
        return element
    
    def clickCartButton(self):
        CartPage.getCartButton(self).click()
        
    def getCartPrice(self):
        element=Common.waitElementToLoadByClassName(self,CartPageLocators.CART_CONTENT)
        cart_price= element.find_element_by_class_name(CartPageLocators.CART_PRICE)
        return cart_price.text