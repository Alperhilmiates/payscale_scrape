from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
chart_list = []

class Scepedata():
    def __init__(self,num):
        self.payscale = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{num}"
        self.responde = requests.get(self.payscale, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"})
        self.respo_txt = self.responde.text
        self.webscrape = BeautifulSoup(self.respo_txt, "html.parser")
        self.major_name = self.webscrape.find_all(class_="csr-col--school-name")
        self.total_page_num = self.webscrape.find_all(class_="pagination__btn--inner")
        self.data_name = self.webscrape.find_all(class_='data-table__title')
        self.data_value = self.webscrape.find_all(class_="data-table__value")

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
deneme = Scepedata(1)

print(deneme.total_page_num)
for n in deneme.total_page_num:
    if not n.text == '' or n.text == '…':
        chart_list.append(n.text)
max_page = (len(chart_list))
max_page_value = int(chart_list[max_page-1])+1

for pages in range (1,max_page_value):
    open_web_page = Scepedata(pages)
    print(open_web_page.data_value)
    for n in deneme.major_name:
        if not n.text == 'Major':
            metin = n.text.split(':')
            list1.append(metin[1])
    # for n in deneme.data_name:
    #     name = n.text
    #     print(name)
    counter = 1
    for n in deneme.data_value:
        value = n.text
        # if counter == 1:
        #     df['Rank']= value
        if counter == 2:
            list2.append(value)
        # if counter == 3:
        #     df['Type'] = value
        if counter == 4:
            list3.append(value)
        if counter == 5:
            list4.append(value)
        # if counter == 6:
        #     list5.append(value)
        counter +=1
        if counter == 7:
            counter = 1

df['Undergraduate Major'] = list2
df['Starting Median Salary'] = list3
df['Mid-Career Median Salary'] = list4
# df['Meaning Value'] = list5
print(df)
print(df.head())
# print(df)

# print(max(chart_list))
# print(deneme.total_page_num)
# print(deneme.data_name)
# print(deneme.data_value)
