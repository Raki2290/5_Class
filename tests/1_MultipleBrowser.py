from selenium import webdriver

browser='ie'
if browser=='chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/Indium Software/PycharmProjects/5_Class/driver/chromedriver.exe")
elif browser=='firefox':
    driver= webdriver.Firefox(executable_path="C:/Users/Indium Software/PycharmProjects/5_Class/driver/geckodriver.exe")
elif browser=='ie':
    driver= webdriver.Ie(executable_path="C:/Users/Indium Software/PycharmProjects/5_Class/driver/IEDriverServer.exe")
else:
    print("provide appropriate browser name")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_id("email").send_keys("Test")
driver.find_element_by_id("pass").send_keys("pass")
driver.find_element_by_id("u_0_2").click()
