import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# Web driver configuring
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver.exe')

# Getting the url and oppening the browser
url = 'https://e2etec.com.br/'
driver.get(url)
time.sleep(5) # Time to wait ultil the page loads

## The page loads the elements we need, without having to scroll or click on 
## something, so we can get the HTML elements directly without interacting with the page
try:
    # Getting the number element and its html text
    numberElement = driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/article/div/div/div/div[9]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/p/span[1]')
    number = numberElement.get_attribute('innerHTML')

    # Getting the email element and its html text
    emailElement = driver.find_element_by_xpath('//*[@id="panel-w5f11b62f8fe0c-0-0-0"]/div/div/p/span[2]')
    email = emailElement.get_attribute('innerHTML')

    
except:
    print("Error in scraping data from the page!")
finally:
    # Whatever we got the data or not the browser should be closed.
    driver.quit()

# Creates a file(if it does't already exists) in '/temp' folder at the computer directory(C:)
try:
    arquivo = open('C:/temp/data_file.txt', 'w')
    arquivo.write(number + '\n') # Saves the data in this file
    arquivo.write(email)
    print('Data saved with success, acces the file in your C:/ directory.')
except: 
    print('Error in writing the data in the file!')
finally:
     arquivo.close() # Close the file
     


