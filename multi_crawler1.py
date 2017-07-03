import time
import threading
class myThread (threading.Thread):
   def __init__(self, threadID, name,initurl,delay,proxy,dest):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.initurl=initurl
      self.delay=delay
      self.proxy=proxy
      self.dest=dest


   def run (self):
       crawyler(self.initurl,self.delay,self.proxy,self.dest)


def crawyler (initurl,delay,proxy,dest):
    import requests
    from bs4 import BeautifulSoup
    import lxml
    from collections import Counter
    import time
    cnt=Counter()#比較器
    count=1      #偵錯用
    try:
        #p=1 #第一頁
        for i in range(1,151):
            set1=set()
            url=initurl+str(i)+"&psl=N_A"
            re =requests.get(url,proxy)
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
                    	    #cnt["不拘"]+=1
               	    print("=" * 50)
            # if(next.text==""):  ##because 149 also "" so 設150頁也是思考重點
            #     if(p==150):
            #         break
            #p+=1
            time.sleep(delay)
        print(type(cnt.most_common(20)))
        for key in cnt:
            print("{}   有{}個工作要求".format(key,cnt.get(key)))
        print(cnt)
        # with open("dest.txt", "a", encoding="utf-8") as f:
        #     f.write("{} \n".format(myThread.name))
        for key in cnt:
            print("{}   有{}個工作要求".format(key,cnt.get(key)))
            with open(dest,"a",encoding="utf-8") as f:
                f.write("{}   有{}個工作要求\n".format(key,cnt.get(key)))
        with open(dest, "a", encoding="utf-8") as f:
            f.write("前20名的被工作要求的語言:")
        with open(dest,"a",encoding="utf-8") as f:
            f.write("{}".format(cnt.most_common(20)))


    except requests.ConnectionError:
            print("Connection aborted")
if __name__ == '__main__':
    url = "https://www.104.com.tw/jobbank/joblist/joblist.cfm?jobsource=n104bank1&ro=0&keyword=資訊&order=1&asc=0&page="
    url1 = "https://www.104.com.tw/jobbank/joblist/joblist.cfm?jobsource=n104bank1&ro=0&keyword=資料分析&order=1&asc=0&page="
    dest="crawler_1.txt"
    dest1="crawler_2.txt"
    thread1=myThread(1,"資訊",url,3,"https://125.224.233.167:3128",dest)
    thread2=myThread(2,"資料分析",url1,2,"https://211.72.239.245:3128",dest1)
    threads=[]

    try:
        thread1.start()
        thread2.start()
        threads.append(thread1)
        threads.append(thread2)
        for t in threads:
            t.join()
            print(" {} Exiting Main Thread".format(t))
    except:
        pass

