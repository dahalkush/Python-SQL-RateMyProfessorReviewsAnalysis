#importing libraries and packages
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.common.exceptions import TimeoutException
import time

#managing chrome driver and installingad extension
path="/home/sonata-lab-3/Downloads/chromedriver_linux64/chromedriver"
chop = webdriver.ChromeOptions()
#chop.add_extension("C:\Program Files (x86)/extension_4_35_0_0.crx")
driver=webdriver.Chrome(path,options=chop)

#providing the url to the chrome driver
driver.get("https://www.ratemyprofessors.com/ShowRatings.jsp?tid=806")

#closing the cookie which pops up in initial phase
close_button=driver.find_element_by_xpath('/html/body/div[5]/div/div/button')
close_button.click()

#clicking load more buttons using selenium
c=0
show_more_button=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/div[4]/div/div/button')
while(show_more_button.is_displayed()):
  show_more_button.click()
  time.sleep(1)
  c = c + 1
  if c == 2:
      break
  print(c)
print('Loop ended.')

#implementing bs4 for abstraction
data = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
Reviews=soup.find_all('div', attrs={'class': 'Rating__StyledRating-sc-1rhvpxz-1 jcIQzP'})
for review in Reviews:
   each_review = review.find('div', attrs={'class': 'Comments__StyledComments-dzzyvm-0 gRjWel'})
   each_review=each_review.text
   course_name = review.find('div', attrs={'class': 'RatingHeader__StyledClass-sc-1dlkqw1-2 gxDIt'})
   course_name=course_name.text
   rating = review.find('div', attrs={'class': 'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 kMhQxZ'})
   #take_again = take_again.text
   # printing the data
   print(each_review, ', ', course_name,',',rating)
   data.append({"Review": each_review, "course_name": course_name})

#storing the data in a csv file
#df = pd.DataFrame(data)
#df.to_csv('jerry_review.csv')