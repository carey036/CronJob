import requests
s = requests.session()
with open("urls.txt","r") as f:
    urls = f.readlines()
    f.close()
for url in urls:
    print(url+ " " +str(s.get(url).status)+"\n")
