import requests
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()#这个用来判断返回的response是不是200，
        r.encoding = r.apparent_encoding#保证解码正确
        return r.text
    except:
        return "产生异常"

if __name__ == '__main__':
    url = "http://1t.click/c7d"
    print(getHTMLText(url))
