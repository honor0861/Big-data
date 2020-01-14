from bs4 import BeautifulSoup
import requests

url = "https://www.weather.go.kr/w/weather/now.do"
str = requests.get(url)
# print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_body_data = soup.find_all('div',{"class":"radio-wrap"})
print(all_body_data)

"""
for tmp in all_div_data:
    print(tmp.find("a").text)
"""