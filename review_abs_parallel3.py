# importing libraries and packages
from pandas import read_csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.common.exceptions import TimeoutException
import time
import csv

with open('Inidiana University- Bloomington.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        urls = line[3]
        p_name = line[1]
        print(urls)

        counts=line[0]
        numbering=counts+p_name
        print(numbering)

        try:

            # managing chrome driver and installingad extension
            path = "/home/sonata-lab-3/Downloads/chromedriver_linux64/chromedriver"
            # chop = webdriver.ChromeOptions()
            # chop.add_extension("C:\Program Files (x86)/extension_4_35_0_0.crx")
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(path, options=options)
            driver.get(urls)

            # closing the cookie which pops up in initial phase
            close_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/button')
            close_button.click()

            # clicking load more buttons using selenium
            c = 0
            # professor_name=driver.find('href', attrs={'class': 'TeacherInfo__RateButton-ti1fio-0 fNonZd'})
            try:
                show_more_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/div[4]/div/div/button')
            except:
                print("absence of load more button")







            try:
                while (show_more_button.is_displayed()):
                        show_more_button.click()
                        time.sleep(15)
                        c = c + 1
                        print(c)
            except:
                    print("Loop to load show more has ended")

            print("Loop to load show more has ended")
            # implementing bs4 for abstraction
            data = []
            content = driver.page_source
            soup = BeautifulSoup(content, features="html.parser")
            Reviews = soup.find_all('div', attrs={'class': 'Rating__StyledRating-sc-1rhvpxz-1 jcIQzP'})

            for review in Reviews:
                each_review = review.find('div', attrs={'class': 'Comments__StyledComments-dzzyvm-0 gRjWel'})
                each_review = each_review.text
                course_name = review.find('div', attrs={'class': 'RatingHeader__StyledClass-sc-1dlkqw1-2 gxDIt'})
                course_name = course_name.text
                dates = review.find('div', attrs={
                    'class': 'TimeStamp__StyledTimeStamp-sc-9q2r30-0 bXQmMr RatingHeader__RatingTimeStamp-sc-1dlkqw1-3 BlaCV'})
                dates = dates.text
                difficulty = review.find('div',
                                         attrs={'class': 'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 cDKJcc'})
                difficulty = difficulty.text
                new = review.find('span', attrs={'class': 'Tag-bs9vf4-0 hHOVKF'})
                emotions = review.find('div', attrs={'class': 'EmotionLabel__StyledEmotionLabel-sc-1u525uj-0 cJfJJi'})
                quality = review.find('div', attrs={'class': 'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 kMhQxZ'})
                p_name = p_name
                # take_again = take_again.text
                # printing the data
                print(p_name, ',', urls, ',', each_review, ', ', course_name, ',', dates, ',', emotions, ',', quality)
                # rows=[urls, each_review, course_name,dates, difficulty, new,emotions, quality]
                # csv_writer.writerow(urls, each_review, course_name,dates, difficulty, new,emotions, quality)

                data.append({"Professor_name": p_name, "Professor_Link": urls, "Review": each_review,
                             "course_name": course_name, "Date": dates, "Difficulty": difficulty, "Extra": new,
                             "Emotion": emotions, "Quality": quality})

            # storing the data in a csv file
            df = pd.DataFrame(data)
            directory='/home/sonata-lab-3/PycharmProjects/RMP Abstraction/Indiana University- Bloomington/'
            filename = "%s.csv" % p_name
            df.to_csv(directory+filename)

        except:
            print("first row neglected")
