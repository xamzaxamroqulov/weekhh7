from webdriver_class.webdriver_functions import *

# # ************* Scenario with correct steps.
# launch_website("https://letskodeit.teachable.com/p/practice")
# find_elements_tag('button')
# web_driver_properties_switch_to_tab()
# close_browser()

# # *********** Scenario for go back, forward, refresh.
# launch_website("http://automationpractice.com/index.php")
# women_tab = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
# click_element_by_xpath(women_tab)
# go_back_to_previous_page()
# refresh_browser()
# go_next_page()
# close_browser()

# # ************ Scenario: Login to automationpractice.com
# Prerequisite: create an account:
# username: hello0@email.com, have strong password "fakepassword"
# Identify all locators by inspecting on browser (xpath), optional: id, css selector
sign_in_link = "//a[@class='login']"
email_input = "//input[@id='email']"
password_input = "//input[@id='passwd']"
sign_in_button = "//button[@id='SubmitLogin']"
sign_out_link = "//a[@class='logout']"

# Steps:
launch_website("http://automationpractice.com/index.php")
click_element_by_xpath(sign_in_link)
time.sleep(2)
enter_text_by_xpath(email_input, "hello0@email.com")
enter_text_by_xpath(password_input, "fakepassword")
click_element_by_xpath(sign_in_button)
time.sleep(10)
print("Successfully signed in ")
print("signing out now... ")
click_element_by_xpath(sign_out_link)
close_browser()
