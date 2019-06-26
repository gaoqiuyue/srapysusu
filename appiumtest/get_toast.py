from selenium.webdriver.support.wait import WebDriverWait

from appiumtest.capability import driver
driver.implicitly_wait(5)
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys("huahua")
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("gao123456")
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
#保存截图
driver.save_screenshot("login.png")
driver.get_screenshot_as_file(r"C:\Users\top\PycharmProjects\srapysusu\appiumtest\image\login.png")
error_message="用户名或密码错误，你还可以尝试4次"

message='//*[@text=\'{}\']'.format(error_message)

toast_element=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)