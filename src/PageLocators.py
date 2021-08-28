'''
@author: PANAGIOP
'''

class TestCaseLocators(object):
    CHROME_DRIVER_PATH=r'../chromedriver.exe'
    AMAZON_URL='http://www.amazon.com/'
    ELECTRONICS_TAB='ELECTRONICS'
    COMPUTER_ACCESSORIES_CATEGORY='COMPUTERS & ACCESSORIES'
    FIFTH_PRODUCT_ITEM=4
    POP_UP_TITLE= 'END OF FLOW'
    POP_UP_MESSAGE_POSITIVE='Cart price and Item price are the same!'
    POP_UP_MESSAGE_NEGATIVE='Cart price and Item price are NOT the same'
    max_wait_time = 15


class HomepageLocators(object):

    ALL_MENU_BUTTON = 'nav-hamburger-menu'
    ALL_MENU_CONTENT='hmenu-content'
    ALL_MENU_CATEGORIES_LIST='hmenu-visible'
    
    
class ProductsPageLocators(object):

    PRODUCT_LIST_CONTENT= 's-main-slot'
    PRODUCT_ITEMS='s-result-item'
    PRICE_LAYOUT='price'
    ITEM_PRICE='priceblock_ourprice'
    ADD_TO_CART_BUTTON='submit.add-to-cart'
    
    
class CartPageLocators(object):
    VIEW_CART_BUTTON='nav-cart'
    CART_CONTENT='sc-list-item-content'
    CART_PRICE='sc-product-price'

