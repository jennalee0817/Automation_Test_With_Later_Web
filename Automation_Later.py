import unittest
import time

from appium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import By

# from multi_automation_testing import multi_automation_settings


class TestAndroidCreateWebSession(unittest.TestCase):
    time_out = 1
    HARD_WARE_BACK_BUTTON_KEY_CODE = 4

    product_wheel = {'product_wheel': '//*[contains(text(), "Ken Block living life on the edge.")]'}
    wheel_size = {'wheel_size': '(//input[@name="Size"])[1]'}
    product_swimsuit = {'product_swimsuit': '/html/body/div/main/div/section/div[2]/a/figure/b'}
    swimsuit_size = {'swimsuit_size': '(//input[@name="Size"])[1]'}
    product_helmet = {'product_helmet': '/html/body/div/main/div/section/div[3]/a/figure/b'}
    add_to_cart_button = {'add_to_cart_button': '//html/body/div/div[2]/div/div[2]/div/div[2]/button'}
    x_button = {'x_button': '//android.widget.Button'}
    go_back_button = {'go_back_button': '/html/body/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div'}
    remove_product = {'remove_product': '/html/body/div/div[5]/ul/li[1]/div[2]/div[1]/button/div'}

    product_swimsuit_detail_info = ["Ladies Black and Green wet suit", '$90.00', 'Size', 'S', 'M', 'L',
                                    'Show More', 'Add To Cart']
    product_swimsuit_detail_check_cart = ["Ladies Black and Green wet suit", '$90.00', 'S', '1']
    product_helmet_detail_info = ["Fox Racing black Helmet", '$250.00', 'Product Description',
                                  'Full face black Helmet width visor.', 'Add To Cart']
    product_helmet_detail_check_cart = ["Fox Racing black Helmet", '$250.00', '1']

    def setUp(self):
        #Android settings
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['browserName'] = 'Chrome'
        desired_caps['deviceName'] = 'LGMV300S475b31f0'
        desired_caps['platformVersion'] = '9'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_automation(self):
        result_value = False
        try:
            url = 'https://staging.linkin.bio/latergear'
            self.driver.get(url)
            current_url = self.driver.current_url
            if url == current_url:
                print("Test Case: url is " + current_url + " : Pass")
                result_value = True
            else:
                print("Test Case: url is " + current_url + " : Fail")
                return result_value

            for index, elem in enumerate([self.product_swimsuit, self.swimsuit_size, self.add_to_cart_button,
                                          self.product_helmet, self.add_to_cart_button, self.remove_product]):
                if self.click_element(index, elem):
                    result_value = True
                else:
                    return result_value
        except Exception as e:
            print("FAIL in test_automation, "+self.test_case_name, e)
            result_value = False

        finally:
            print("test_automation: " + str(result_value))
            return result_value

    def scroll_down(self):
        lcd_size = self.driver.get_window_size()
        self.driver.swipe(lcd_size['width'], lcd_size['height'], lcd_size['width'], lcd_size['height']*0)
        print('Test Case: scroll_down')

    def click_element(self, index, test_case):
        for test_case_name, test_case_xpath in test_case.items():
            self.test_case_name = test_case_name
            result_value = False
            elem = WebDriverWait(self.driver, self.time_out).until(EC.presence_of_element_located((By.XPATH, test_case_xpath)))
            time.sleep(self.time_out)
            if elem:
                elem.click()
                result_value = True
            if index == 0:
                time.sleep(self.time_out)
                self.scroll_down()
            elif index == 1:
                result_value = self.get_test_detail_information(self.product_swimsuit_detail_info)
            elif index == 2:
                result_value = self.get_test_detail_information(self.product_swimsuit_detail_check_cart)
                self.driver.press_keycode(self.HARD_WARE_BACK_BUTTON_KEY_CODE)
                self.driver.press_keycode(self.HARD_WARE_BACK_BUTTON_KEY_CODE)
                # self.driver.find_element_by_xpath(self.go_back_button).click()
            elif index == 3:
                result_value = self.get_test_detail_information(self.product_helmet_detail_info)
            elif index == 4:
                result_value = self.get_test_detail_information(self.product_swimsuit_detail_check_cart
                                                                + self.product_helmet_detail_check_cart)
            time.sleep(self.time_out)
            return result_value

    def get_test_detail_information(self, product_detail_info):
        result_vale = False
        for detail_info in product_detail_info:
            if detail_info in self.driver.page_source:
                print("Test Case: Product information, " + detail_info + " is in the page - Pass")
                result_vale = True
            else:
                print("Test Case: Product information, " + detail_info + " is NOT in the page" + " - Fail")
        return result_vale


if __name__ == "__main__":
    unittest.main()
