# import necessary libraries
from pandas import read_csv
from bs4 import BeautifulSoup

import pandas as pd
from selenium.common.exceptions import TimeoutException
import time
import xlrd, webbrowser
import csv
import re
import glob
from bs4 import BeautifulSoup
def remove_tags(html):
    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

# use glob to get all the csv files
# in the folder
datas = []
path = 'Universities Data/University of Arizona'
csv_files = glob.glob(path + "/*.csv")
# print("files:",csv_files)
li = []

# loop over the list of csv files

for f in csv_files:
    # read the csv file
    print("file name: ", f)
    f = str(f)
    df = pd.read_csv(f)

        strings = df.Review
        for string in strings:
            print(string)
            #start
            abc = remove_tags(string)
            # print(abc)

            # difficulty calculation 1
            try:
                difficulty = re.search(r'\b(Difficulty)\b', abc)
                difficulty_end = difficulty.end()
                # print(difficulty_end)
                difficulty_end = int(difficulty_end)
                difficulty_end = difficulty_end + 1
                endl = abc.find(' ', difficulty_end)
                # print(endl)
                professor_difficulty = abc[difficulty_end:endl]
                print("Difficulty: ", professor_difficulty)
            except:
                print("Difficulty not available")

            # Quality calculate
            try:
                quality = re.search(r'\b(Quality)\b', abc)
                quality_end = quality.end()
                # print(quality_end)
                quality_end = int(quality_end)
                quality_end = quality_end + 1
                qendl = abc.find(' ', quality_end)
                # print(qendl)
                professor_quality = abc[quality_end:qendl]
                print("Quality: ", professor_quality)
            except:
                print("Quality not available")

            # Course Number calculate
            csnumber = re.search(r'\b(1dlkqw1-2 gxDIt"> <!-- -->)\b', string)
            csnumber_end = csnumber.end()
            csnumber_end = int(csnumber_end)
            csnumber_endl = csnumber_end
            csnumber_endll = string.find('<', csnumber_endl)
            professor_csnumber = string[csnumber_endl:csnumber_endll]
            print("Course_Number: ", professor_csnumber)

            # datetime calculate
            exword = re.search(r'\b(RatingHeader__RatingTimeStamp)\b', string)
            exword_end = exword.end()
            exword_end = int(exword_end)
            exword_endl = exword_end + 21
            exword_endla = exword_endl + 5
            exword_endll = string.find('<', exword_endl)
            # exword_endll=exword_endl+14
            professor_date = string[exword_endl:exword_endll]
            print("Date: ", professor_date)
            # for credit calculate
            try:
                credit = re.search(r'\b(For Credit)\b', abc)
                credit_end = credit.end()
                credit_end = int(credit_end)
                credit_end = credit_end + 3
                crendl = abc.find(' ', credit_end)
                professor_credit = abc[credit_end:crendl]
                print("For Credit: ", professor_credit)
            except:
                print("For Credit not available")

            # Attendance calculate
            try:
                credit = re.search(r'\b(Attendance)\b', abc)
                credit_end = credit.end()
                credit_end = int(credit_end)
                credit_end = credit_end + 3
                crendl = abc.find(' ', credit_end)
                professor_att = abc[credit_end:crendl]
                if (professor_att=='Mandatory'):
                    print(professor_att)
                else:
                    professor_att='Not'


                print("Attendance: ", professor_att)
            except:
                print("Attendance not available")

            # Textbook calculate
            try:
                credit = re.search(r'\b(Textbook)\b', abc)
                credit_end = credit.end()
                credit_end = int(credit_end)
                credit_end = credit_end + 3
                crendl = abc.find(' ', credit_end)
                professor_text = abc[credit_end:crendl]
                print("Textbook: ", professor_text)
            except:
                print("Textbook not available")

            # Would Take Again calculate
            try:
                credit = re.search(r'\b(Would Take Again)\b', abc)
                credit_end = credit.end()
                credit_end = int(credit_end)
                credit_end = credit_end + 3
                crendl = abc.find(' ', credit_end)
                professor_wta = abc[credit_end:crendl]
                print("Would Take Again: ", professor_wta)
            except:
                print("Would Take Again not available")

            # Review calculate
            start = re.search(r'\b(Comments__StyledComments)\b', string)
            start = start.end()
            start = int(start)
            start = start + 18
            end = string.find('<', start)
            professor_rev = string[start:end]
            print("Review: ", professor_rev)

            # emotion calculate
            if (re.search(r'\b(EmotionLabel__StyledEmotionLabel)\b', string)):
                exword = re.search(r'\b(EmotionLabel__StyledEmotionLabel)\b', string)
                exword_end = exword.end()
                exword_end = int(exword_end)
                exword_endl = exword_end + 69
                exword_endl = string.find('>', exword_endl)
                exword_endl=exword_endl+1
                exword_endll = string.find('<', exword_endl)
                professor_emotion = string[exword_endl:exword_endll]
                print("Emotion: ", professor_emotion)
            else:
                print("Emotion: Emotion doesnot exist")

            # Grade Calculate
            if (re.search(r'\b(Grade)\b', string)):
                exword = re.search(r'\b(Grade)\b', string)
                exword_end = exword.end()
                exword_end = int(exword_end)
                exword_endl = exword_end + 16
                exword_endll = string.find('<', exword_endl)
                professor_grade = string[exword_endl:exword_endll]
                print("Grade: ", professor_grade)
            else:
                print("Grade: Grade doesnot Exist in this review")

            # Review extra word calculate
            try:
                c=1
                pr_m = ''
                for m in re.finditer('Tag-bs9vf4-0 hHOVKF', string):
                    m_end = m.end()
                    m_end = int(m_end)
                    m_endl = m_end + 2
                    m_endll = string.find('<', m_endl)
                    professor_m = string[m_endl:m_endll]
                    print("Extra Word: ", professor_m)
                    pr_m += professor_m + ', '
                    print("Extra Word: ", pr_m)
            except:
                print("No extra words")

            print("111")
            print(professor_rev)
            fword = re.search(r'\b(Universities Data/University of Arizona)\b', f)
            fwordl = re.search(r'\b(.csv)\b', f)
            fword=fword.end()
            fwordl=fwordl.start()
            fword = fword + 1
            fword = f[fword:fwordl]
            print(professor_rev)
            datas.append(
                {"Professor": fword,"Difficulty": professor_difficulty, "Quality": professor_quality, "Course_Number": professor_csnumber,
                 "Date": professor_date, "For Credit": professor_credit, "Attendance": professor_att,
                 "Textbook": professor_text, "Would Take Again": professor_wta, "Review": professor_rev,
                 "Emotion": professor_emotion, "Extra Word": pr_m})
                 #end
    except:
        print("This professor does not have reviews")
 # storing the data in a csv file

daf = pd.DataFrame(datas)
filenames = "University of Arizona.csv"
daf.to_csv(filenames)
# for df1 in df:
#    review=df1.Review
#    print(review)



