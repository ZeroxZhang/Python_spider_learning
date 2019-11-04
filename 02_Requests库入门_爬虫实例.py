import requests

#爬取京东商品页面全代码
urljd = "https://item.jd.com/4406782.html"
try:
    r = requests.get(urljd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")

#爬去亚马逊商品页面代码，亚马逊禁止
urlam = "https://www.amazon.cn/dp/B07RHH7LFR/"
r= requests.get(urlam)
print(r.status_code)
print(r.encoding)
r.encoding = r.apparent_encoding
print(r.text)
print(r.request.headers)#查看请求的时候请求的信息是什么
kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
r = requests.get(urlam,headers=kv)
print(r.status_code)
print(r.text)
print(r.request.headers)

#基于以上分析，给到
urlam = "https://www.amazon.cn/dp/B07RHH7LFR/"
kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
try:
    r = requests.get(urlam,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬虫错误")