# importing packages and libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.common.exceptions import TimeoutException
import time

# managing chrome driver and installing ad extension
path = "/home/sonata-lab-3/Downloads/chromedriver_linux64/chromedriver"
chop = webdriver.ChromeOptions()

driver = webdriver.Chrome(path, options=chop)

# providing the url to the chrome driver
driver.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=1085")

# closing the cookie which pops up in initial phase
close_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/button')
close_button.click()

# clicking load more buttons using selenium
c = 0
show_more_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/div[1]/div[3]/button')
try:
    while (show_more_button.is_displayed()):
        show_more_button.click()
        time.sleep(1)
        c = c + 1
        print(c)
        print('Loop ended.')
except:
    print('loop finally ended')
# implementing bs4 for abstraction
data = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
professors = soup.find_all('a', attrs={'class': 'TeacherCard__StyledTeacherCard-syjs0d-0 dLJIlx'})
for professor in professors:
    name = professor.find('div', attrs={'class': 'CardName__StyledCardName-sc-1gyrgim-0 cJdVEK'})
    name = name.text
    department = professor.find('div', attrs={'class': 'CardSchool__Department-sc-19lmz2k-0 haUIRO'})
    department = department.text
    Take_again = professor.find('div', attrs={'class': 'CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf'})
    quality = professor.find('div', attrs={'class': 'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 fJKuZx'})
    number_of_ratings = professor.find('div', attrs={'class': 'CardNumRating__CardNumRatingCount-sc-17t4b9u-3 jMRwbg'}).text

    link = 'https://www.ratemyprofessors.com' + professor['href']
    # printing the data
    print(name, ' , ', department, ' , ', Take_again, ' ,', link, ' , ', quality, ' , ', number_of_ratings)
    data.append({"name": name, "faculty": department, "Links": link,"would_take_again":Take_again,"Quality":quality,"Total_Ratings":number_of_ratings})

df = pd.DataFrame(data)
df.to_csv('University of Chicago')