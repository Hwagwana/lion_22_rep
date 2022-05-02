install pip

pip install requests

import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
url = "https://search.zum.com/search.zum?method=uni&option=accu&rd=1&query=%EC%9D%B4%EC%8A%88%20%EA%B2%80%EC%83%89%EC%96%B4&qm=f_typing.top"
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
results_total = soup.findAll("span","txt")
results_now = results_total[0:10]

rank_file = open("rankresult.txt","w")

print(datetime.today().strftime("%Y년 %m월 %d일 %X의 실시간 검색어 순위입니다.\n"))

rank = 1
for x in results_now:
    rank_file.write(str(rank)+"위 : "+x.get_text()+"\n")
    print(str(rank)+"위 : "+x.get_text()+"\n")
    rank += 1