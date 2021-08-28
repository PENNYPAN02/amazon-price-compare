import Common
from PageLocators import ProductsPageLocators

class ProductsSearchPage(object):
    
    def __init__(self, browser):
        self.browser = browser
    
    def SelectProductFromResults(self,index,element_results):
        Common.SelectValueFromListByIndex(self,index,element_results)

    def getProductsList(self):
        element=Common.waitElementToLoadByClassName(self,ProductsPageLocators.PRODUCT_LIST_CONTENT)
        items=element.find_elements_by_class_name(ProductsPageLocators.PRODUCT_ITEMS)
        return items

    def getProductItemPrice(self):
        element= Common.waitElementToLoadByID(self,ProductsPageLocators.PRICE_LAYOUT)
        price_element=element.find_element_by_id(ProductsPageLocators.ITEM_PRICE)
        return price_element.text
    
    def getAddToCarButton(self):
        element= Common.waitElementToLoadByID(self,ProductsPageLocators.ADD_TO_CART_BUTTON)
        return element
    
    def clickAddToCartButton(self):
        ProductsSearchPage.getAddToCarButton(self).click()