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
path = 'Universities Data/Alverno College'
csv_files = glob.glob(path + "/*.csv")
# print("files:",csv_files)
li = []

# loop over the list of csv files

for f in csv_files:
    # read the csv file
    print("file name: ", f)
    f = str(f)
    df = pd.read_csv(f)
    try:

        for rows in df:
            print(df.Professor_name)
            #start

            datas.append(
                {"Professor": df.Professor_name})
                 #end
    except:
        print("This professor does not have reviews")
 # storing the data in a csv file

daf = pd.DataFrame(datas)
filenames = "testing unity.csv"
daf.to_csv(filenames)
# for df1 in df:
#    review=df1.Review
#    print(review)



