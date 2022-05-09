Initially 72 universities are chosen and their 72 links of each university are collected manually. After getting the links for each university,
selenium, beautiful soup and google headless is implemented to get the link of all the professors for every university. After the creation of 72
csv files for each university with the prfessor name and their particular links, I wrote a script to abstract details including reviews, difficulty,
quality etc for each professor and stored it in the universities directory. I cleaned the reviews using selenium. After the completion of data cleaning,
I uploaded the data in mongodb and sql server. I used to write sql queries to abstract necesaary for our analysis. For the reviews we implemented sentiment 
analysis to get six emotions for each reviews. After having all the details of the reviews, we have also done the exploratory analysis of the data.
