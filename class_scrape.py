# Created By: Richard Morales
# 
# This script logs into dropbox with a verified account and scrapes the account's classes with assignment descriptions using selenium.
# The username and password would need to be changed in order for script to work.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dropbox-spring2017.cse.sc.edu/login/index.php")
text_file = open("Assignments.txt", "w")


def Main():
    Login()
    Assignments()
    text_file.close()
    driver.close()

# Login to a Dropbox with username and pw
def Login():
    username = driver.find_element_by_xpath('//*[@id="username"]')
    username.send_keys("username")

    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys("password")


    login = driver.find_element_by_xpath('//*[@id="loginbtn"]')
    login.click()

    link = driver.find_element_by_link_text('Topics in Information Technology (590-002-S2017)')
    link.click()

# Prints the current url to a text file
def CurrentUrl():
    text_file.write('Current URL: \n' + driver.current_url + '\n')

# Grabs all the assignments completed and prints the description of each.
def Assignments():
    assignment1 = driver.find_element_by_xpath('//*[@id="module-5563"]/div/div/div[2]/div/a/span')
    assignment1.click()
    a1_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a1_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a1_title.text
    print ('######################################################################')
    print (a1_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a1_title.text + '\n')
    text_file.write(a1_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a1b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a1b_button.click()
    assignment2 = driver.find_element_by_xpath('//*[@id="module-5713"]/div/div/div[2]/div/a/span')
    assignment2.click()
    a2_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a2_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a2_title.text
    print ('######################################################################')
    print (a2_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a2_title.text + '\n')
    text_file.write(a2_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a2b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a2b_button.click()
    assignment3 = driver.find_element_by_xpath('//*[@id="module-5714"]/div/div/div[2]/div/a/span')
    assignment3.click()
    a3_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a3_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a3_title.text
    print ('######################################################################')
    print (a3_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a3_title.text + '\n')
    text_file.write(a3_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a3b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a3b_button.click()
    assignment4 = driver.find_element_by_xpath('//*[@id="module-5951"]/div/div/div[2]/div/a/span')
    assignment4.click()
    a4_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a4_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a4_title.text
    print ('######################################################################')
    print (a4_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a4_title.text + '\n')
    text_file.write(a4_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a4b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a4b_button.click()
    assignment5 = driver.find_element_by_xpath('//*[@id="module-5952"]/div/div/div[2]/div/a/span')
    assignment5.click()
    a5_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a5_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a5_title.text
    print ('######################################################################')
    print (a5_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a5_title.text + '\n')
    text_file.write(a5_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a5b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a5b_button.click()
    assignment6 = driver.find_element_by_xpath('//*[@id="module-5953"]/div/div/div[2]/div/a/span')
    assignment6.click()
    a6_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a6_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a6_title.text
    print ('######################################################################')
    print (a6_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a6_title.text + '\n')
    text_file.write(a6_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a6b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a6b_button.click()
    assignment7 = driver.find_element_by_xpath('//*[@id="module-5985"]/div/div/div[2]/div/a/span')
    assignment7.click()
    a7_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a7_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a7_title.text
    print ('######################################################################')
    print (a7_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a7_title.text + '\n')
    text_file.write(a7_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a7b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a7b_button.click()
    assignment8 = driver.find_element_by_xpath('//*[@id="module-5986"]/div/div/div[2]/div/a/span')
    assignment8.click()
    a8_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a8_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a8_title.text
    print ('######################################################################')
    print (a8_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a8_title.text + '\n')
    text_file.write(a8_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a8b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a8b_button.click()
    assignment9 = driver.find_element_by_xpath('//*[@id="module-5987"]/div/div/div[2]/div/a/span')
    assignment9.click()
    a9_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a9_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a9_title.text
    print ('######################################################################')
    print (a9_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a9_title.text + '\n')
    text_file.write(a9_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a9b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a9b_button.click()
    assignment10 = driver.find_element_by_xpath('//*[@id="module-6153"]/div/div/div[2]/div/a/span')
    assignment10.click()
    a10_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a10_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a10_title.text
    print ('######################################################################')
    print (a10_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a10_title.text + '\n')
    text_file.write(a10_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a10b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a10b_button.click()
    assignment11 = driver.find_element_by_xpath('//*[@id="module-6154"]/div/div/div[2]/div/a/span')
    assignment11.click()
    a11_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a11_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a11_title.text
    print ('######################################################################')
    print (a11_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a11_title.text + '\n')
    text_file.write(a11_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a11b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a11b_button.click()
    assignment12 = driver.find_element_by_xpath('//*[@id="module-6155"]/div/div/div[2]/div/a/span')
    assignment12.click()
    a12_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a12_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a12_title.text
    print ('######################################################################')
    print (a12_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a12_title.text + '\n')
    text_file.write(a12_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a12b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a12b_button.click()
    assignment13 = driver.find_element_by_xpath('//*[@id="module-6194"]/div/div/div[2]/div/a/span')
    assignment13.click()
    a13_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a13_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a13_title.text
    print ('######################################################################')
    print (a13_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a13_title.text + '\n')
    text_file.write(a13_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a13b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a13b_button.click()
    assignment14 = driver.find_element_by_xpath('//*[@id="module-6195"]/div/div/div[2]/div/a/span')
    assignment14.click()
    a14_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a14_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a14_title.text
    print ('######################################################################')
    print (a14_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a14_title.text + '\n')
    text_file.write(a14_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a14b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a14b_button.click()
    assignment15 = driver.find_element_by_xpath('//*[@id="module-6196"]/div/div/div[2]/div/a/span')
    assignment15.click()
    a15_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a15_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a15_title.text
    print ('######################################################################')
    print (a15_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a15_title.text + '\n')
    text_file.write(a15_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a15b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a15b_button.click()
    assignment16 = driver.find_element_by_xpath('//*[@id="module-6197"]/div/div/div[2]/div/a/span')
    assignment16.click()
    a16_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a16_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a16_title.text
    print ('######################################################################')
    print (a16_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a16_title.text + '\n')
    text_file.write(a16_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a16b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a16b_button.click()
    assignment17 = driver.find_element_by_xpath('//*[@id="module-6198"]/div/div/div[2]/div/a/span')
    assignment17.click()
    a17_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a17_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a17_title.text
    print ('######################################################################')
    print (a17_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a17_title.text + '\n')
    text_file.write(a17_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a17b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a17b_button.click()
    assignment18 = driver.find_element_by_xpath('//*[@id="module-6199"]/div/div/div[2]/div/a/span')
    assignment18.click()
    a18_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a18_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a18_title.text
    print ('######################################################################')
    print (a18_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a18_title.text + '\n')
    text_file.write(a18_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a18b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a18b_button.click()
    assignment19 = driver.find_element_by_xpath('//*[@id="module-6200"]/div/div/div[2]/div/a/span')
    assignment19.click()
    a19_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a19_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a19_title.text
    print ('######################################################################')
    print (a19_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a19_title.text + '\n')
    text_file.write(a19_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a19b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a19b_button.click()
    assignment20 = driver.find_element_by_xpath('//*[@id="module-6786"]/div/div/div[2]/div/a/span')
    assignment20.click()
    a20_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a20_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a20_title.text
    print ('######################################################################')
    print (a20_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a20_title.text + '\n')
    text_file.write(a20_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a20b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a20b_button.click()
    assignment21 = driver.find_element_by_xpath('//*[@id="module-6787"]/div/div/div[2]/div/a/span')
    assignment21.click()
    a21_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a21_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a21_title.text
    print ('######################################################################')
    print (a21_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a21_title.text + '\n')
    text_file.write(a21_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a21b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a21b_button.click()
    assignment22 = driver.find_element_by_xpath('//*[@id="module-6788"]/div/div/div[2]/div/a/span')
    assignment22.click()
    a22_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a22_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a22_title.text
    print ('######################################################################')
    print (a22_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a22_title.text + '\n')
    text_file.write(a22_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a22b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a22b_button.click()
    assignment23 = driver.find_element_by_xpath('//*[@id="module-7098"]/div/div/div[2]/div/a/span')
    assignment23.click()
    a23_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a23_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a23_title.text
    print ('######################################################################')
    print (a23_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a23_title.text + '\n')
    text_file.write(a23_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a23b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a23b_button.click()
    assignment24 = driver.find_element_by_xpath('//*[@id="module-7154"]/div/div/div[2]/div/a/span')
    assignment24.click()
    a24_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a24_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a24_title.text
    print ('######################################################################')
    print (a24_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a24_title.text + '\n')
    text_file.write(a24_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a23b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a23b_button.click()
    assignment24 = driver.find_element_by_xpath('//*[@id="module-7155"]/div/div/div[2]/div/a/span')
    assignment24.click()
    a24_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a24_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a24_title.text
    print ('######################################################################')
    print (a24_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a24_title.text + '\n')
    text_file.write(a24_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a24b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a24b_button.click()
    assignment25 = driver.find_element_by_xpath('//*[@id="module-7157"]/div/div/div[2]/div/a/span')
    assignment25.click()
    a25_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a25_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a25_title.text
    print ('######################################################################')
    print (a25_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a25_title.text + '\n')
    text_file.write(a25_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

    a25b_button = driver.find_element_by_xpath('//*[@id="page-navbar"]/nav/ul/li[4]/span/a')
    a25b_button.click()
    assignment26 = driver.find_element_by_xpath('//*[@id="module-7151"]/div/div/div[2]/div/a/span')
    assignment26.click()
    a26_title = driver.find_element_by_xpath('//*[@id="region-main"]/div[3]/h2')
    a26_descrip = driver.find_element_by_xpath('//*[@id="intro"]/div')
    print ('######################################################################')
    print a26_title.text
    print ('######################################################################')
    print (a26_descrip.text + '\n')

    text_file.write('############################################################# \n')
    text_file.write(a26_title.text + '\n')
    text_file.write(a26_descrip.text + '\n')
    CurrentUrl()
    text_file.write('############################################################# \n\n')

Main()
