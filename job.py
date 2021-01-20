import requests
s = requests.session()
with open("urls.txt","r") as f:
    urls = f.readlines()
    f.close()
#print (urls)
for url in urls:
    print(url + str(int(s.get(url.strip()).status_code))+"\n")
    #print(url+ " " +str(s.get("http://www.baidu.com").status)+"\n")
