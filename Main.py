from selenium import webdriver
from config1 import keys
import time



def order(k):
    driver = webdriver.Chrome(executable_path=r'/Users/username/Desktop/path/to/the/chromedriver')
    driver.get(k['product_url'])
    driver.find_element_by_link_text(k["product_title"]).click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone_number"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["adress"])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
    driver.find_element_by_xpath('// *[ @ id = "order_billing_country"] / option[24]').click()
    driver.find_element_by_xpath('// *[ @ id = "credit_card_type"]').click()
    driver.find_element_by_xpath('//*[@id="cnb"]').send_keys(k['ccinfo'])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(k["ccmonth"])).click()
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(k["ccyear"])).click()
    driver.find_element_by_xpath('//*[@id="vval"]').send_keys(k["CVV"])
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()
    time.sleep(100)





if __name__ == '__main__':
    order(keys)
