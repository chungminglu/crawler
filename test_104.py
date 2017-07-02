import requests
from bs4 import BeautifulSoup
import lxml
from collections import Counter
import time
cnt=Counter()#比較器
count=1      #偵錯用
try:
    p=1 #第一頁
    while True:
        set1=set()
        url="https://www.104.com.tw/jobbank/joblist/joblist.cfm?jobsource=n104bank1&ro=0&keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&order=1&asc=0&page="+str(p)+"&psl=N_A"
        re =requests.get(url)
        soup=BeautifulSoup(re.text,'lxml')
        #print(soup.select(".job_name > a"))
        next=soup.select(".mar_L10 ")[0]
        print(next.text)
        for murl in soup.select(".job_name > a"):
            nu=str(murl["href"]).split("jobno=")[1].split("&")[0]
            set1.add(nu)
        for surl in set1:
            url1="http://www.104.com.tw//job/?jobno="+str(surl)+"&amp;jobsource=n104bank1&amp;hotjob_chr="
            re1=requests.get(url1)
            soup=BeautifulSoup(re1.text,'lxml')
            print("第%d筆更新" %(count))
            for title in soup.select('title'):
                print(str(title).split('<title>')[1].split('-')[0])
                print("="*50)
                print("擅長工具:")
                count+=1
                tc=0
                for tool in soup.select(".tool > a"):
                    tc+=1
                    print(tool.text)
                    if tool.text in cnt:
                        cnt[tool.text]+=1
                    else:
                        cnt[tool.text]=1
                if tc < 1:
                    	print("不拘")
                    	cnt["不拘"]+=1
               	print("=" * 50)
        if(next.text==""):  ##because 149 also "" so 設150頁也是思考重點
            if(p==150):
                break
        p+=1
        time.sleep(3)
    print(cnt.most_common(20))
except requests.ConnectionError:
        print("Connection aborted")