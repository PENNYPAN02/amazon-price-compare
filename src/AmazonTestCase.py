'''
@author: PANAGIOP
'''

from Common import Browser
from Pages import HomePage,ProductsPage,CartsPage
from PageLocators import TestCaseLocators
import unittest
import tkinter.messagebox as tkMessageBox

B = Browser()
homepage = HomePage.HomePage(B)
productpage=ProductsPage.ProductsSearchPage(B)
cartpage=CartsPage.CartPage(B)

class AmazonTC():
    
    B.open_chrome_driver()
    B.open_URL(TestCaseLocators.AMAZON_URL)
    homepage.clickAllMenu_Button()
    all_tabs= homepage.getCategoriesList()
    homepage.SelectCategoryOptionFromMenu(all_tabs,TestCaseLocators.ELECTRONICS_TAB)
    categories_list= homepage.getCategoriesList()
    homepage.SelectCategoryOptionFromMenu(categories_list,TestCaseLocators.COMPUTER_ACCESSORIES_CATEGORY)
    products_list= productpage.getProductsList()
    productpage.SelectProductFromResults(TestCaseLocators.FIFTH_PRODUCT_ITEM, products_list)
    item_price=productpage.getProductItemPrice()
    productpage.clickAddToCartButton()
    cartpage.clickCartButton()
    cart_price= cartpage.getCartPrice()
    
    if str(cart_price)==str(item_price):
        tkMessageBox.showinfo(title=TestCaseLocators.POP_UP_TITLE, message=TestCaseLocators.POP_UP_MESSAGE_POSITIVE)
    else:
        tkMessageBox.showinfo(title=TestCaseLocators.POP_UP_TITLE, message=TestCaseLocators.POP_UP_MESSAGE_NEGATIVE)
    B.close_browser()

if __name__ == '__main__':
    unittest.main()




