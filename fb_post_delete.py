# Must have chromedriver installed in your system, Links:
               ### https://sites.google.com/a/chromium.org/chromedriver/downloads
               ### https://github.com/mozilla/geckodriver/releases
               ### https://webkit.org/blog/6900/webdriver-support-in-safari-10/
     ### for more info      https://selenium-python.readthedocs.io/installation.html
# Must know your fb username url
# You can use firefox instead of chrome at line 19


from selenium import webdriver
import time

emaill = input("Enter your email/phone : ")
pwdd = input("Enter your password : ")
username = input("Your username url : ")         # https://www.facebook.com/username/
n = int(input("How many posts? : "))
driver = input("Chromedriver Location : ")       #    C:\Zip files\chromedriver_win32\chromedriver.exe

test_driver = webdriver.Chrome(driver)
test_driver.get("https://www.facebook.com/")

email_input= test_driver.find_element_by_id("email")
pass_input= test_driver.find_element_by_id("pass")
login_button= test_driver.find_element_by_id("u_0_b")

email_input.send_keys(emaill)
pass_input.send_keys(pwdd)
login_button.click()

time.sleep(30)      # my facebook account does have TFA , i need this time to have the permission done!

for i in range(n):
    test_driver.get(username+"allactivity?category_key=STATUSCLUSTER&filter_hidden=ALL&filter_privacy=NONE")

    time.sleep(15)

    post = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[8]/div[2]/div[1]/a/div[1]")
    post.click()

    time.sleep(10)

    main_post = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div")
    main_post.click()

    time.sleep(10)

    try:
        delete = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[4]")
        delete.click()

        time.sleep(5)

        full_delete = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]")
        full_delete.click()

    except:

        cut_click = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div")
        cut_click.click()

        time.sleep(5)

        main_post = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div")
        main_post.click()

        time.sleep(10)

        delete = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[5]")
        delete.click()

        time.sleep(5)

        full_delete = test_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]")
        full_delete.click()

    time.sleep(15)

print("All done!")