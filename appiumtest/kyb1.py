from  appiumtest.capability import driver
driver.implicitly_wait(3)

def click_skipbtn():
    print("点击跳过按钮")
    try:
        skipbtn=driver.find_element_by_id("com.tal.kaoyan:id/tv_skip")
    except Exception:
        print("没有跳过按钮")
    else:
        skipbtn.click()
def click_register():
    print("点击注册按钮")
    try:
        registerbtn=driver.find_element_by_id("com.tal.kaoyan:id/login_register_text")
    except Exception:
        print("没有注册按钮")
    else:
        registerbtn.click()
def register():
    driver.find_element_by_id("com.tal.kaoyan:id/activity_register_username_edittext").click()
    driver.find_element_by_id("com.tal.kaoyan:id/activity_register_username_edittext"). send_keys("sususu123")
    driver.find_element_by_id("com.tal.kaoyan:id/activity_register_password_edittext").send_keys("gao123456")
    driver.find_element_by_id("com.tal.kaoyan:id/activity_register_email_edittext").send_keys("315442614@qq.com")
    driver.find_element_by_id("com.tal.kaoyan:id/activity_register_userheader").click()
    driver.find_elements_by_id("com.tal.kaoyan:id/item_image")[1].click()
    driver.find_element_by_id("com.tal.kaoyan:id/save").click()
    driver.find_element_by_id("com.tal.kaoyan:id/activity_register_register_btn").click()
    print("选择院校")
    driver.find_element_by_id("com.tal.kaoyan:id/perfectinfomation_edit_school_name").click()
    driver.find_elements_by_id("com.tal.kaoyan:id/more_forum_title")[1].click()
    driver.find_element_by_id("com.tal.kaoyan:id/university_search_item_name")[0].click()
    print("选择专业")
    driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_major").click()
    driver.find_elements_by_id("com.tal.kaoyan:id/major_subject_title")[7].click()
    driver.find_elements_by_id("com.tal.kaoyan:id/major_group_title")[10].click()
    driver.find_elements_by_id("com.tal.kaoyan:id/major_search_item_name")[3].click()

    # 点击“进入考研帮”按钮
    driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()


if __name__ == '__main__':
    click_skipbtn()
    click_register()
    driver.implicitly_wait(3)
    register()
