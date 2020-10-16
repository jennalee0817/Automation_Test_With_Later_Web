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

    product_wheel = '//*[contains(text(), "Ken Block living life on the edge.")]'
    wheel_size = '(//input[@name="Size"])[1]'
    product_swimsuit = '/html/body/div/main/div/section/div[2]/a/figure/b'
    swimsuit_size = '(//input[@name="Size"])[1]'
    product_helmet = '/html/body/div/main/div/section/div[3]/a/figure/b'
    add_to_cart_button = '//html/body/div/div[2]/div/div[2]/div/div[2]/button'
    x_button = '//android.widget.Button'
    go_back_button = '/html/body/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div'
    remove_product = '/html/body/div/div[5]/ul/li[1]/div[2]/div[1]/button/div'

    def setUp(self):
        # #iOS settings
        # self.desired_caps = {}
        # self.desired_caps['platformName'] = 'iOS'
        # self.desired_caps['browserName'] = 'Safari'
        # self.desired_caps['deviceName'] = 'DEVICE_NAME'
        # self.desired_caps['platformVersion'] = '10.1'
        # self.desired_caps['automationName'] = 'XCUITest'  # Possible to run without.
        # self.desired_caps['udid'] = 'udid'
        # self.desired_caps['startIWDP'] = True

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
                    print("Test Case: " + elem + " : Pass")
                    result_value = True
                else:
                    print("Test Case: " + elem + " : Fail")
                    result_value = False
        except Exception as e:
            print("FAIL in test_automation, ", e)
            result_value = False

        finally:
            print("test_automation: " + str(result_value))
            return result_value

    def scroll_down(self):
        lcd_size = self.driver.get_window_size()
        self.driver.swipe(lcd_size['width'], lcd_size['height'], lcd_size['width'], lcd_size['height']*0)
        print('Test Case: scroll_down')

    def click_element(self, index, test_case):
        result_value = False
        elem = WebDriverWait(self.driver, self.time_out).until(EC.presence_of_element_located((By.XPATH, test_case)))
        time.sleep(self.time_out)
        if elem:
            elem.click()
            result_value = True
        if index == 0:
            time.sleep(self.time_out)
            self.scroll_down()
        elif index == 2:
            self.driver.press_keycode(self.HARD_WARE_BACK_BUTTON_KEY_CODE)
            self.driver.find_element_by_xpath(self.go_back_button).click()
        time.sleep(self.time_out)
        return result_value


if __name__ == "__main__":
    unittest.main()
