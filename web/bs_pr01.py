from bs4 import BeautifulSoup
import requests

"""

"""
url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
str = requests.get(url)
# print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_body_data = soup.find_all('body','data')
print(all_body_data)

"""
for tmp in all_div_data:
    print(tmp.find("a").text)
"""