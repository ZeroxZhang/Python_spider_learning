import requests

#requests方法。requests.request(method,url,**kwargs)
r = requests.request("GET","http://www.baidu.com")
print(r)
#上面这个方法等同于下面这个
r = requests.get("http://www.baidu.com")

#Requests方法一共包含13个访问控制参数如下，可灵活使用
#**kwargs是访问控制参数，可选，举例如下
kv = {"key1":"value1","key2":"value2"}
p = requests.request("GET","http://www.zeroxzhang.cc",params=kv)#params作为参数添加到url中
print(p.url)

#data是字典、字节序列或者文件对象，作为Request的内容。下面这个操作是把kv这组数据存到了服务器的data字段下
d = requests.request("POST","http://python123.io/ws",data=kv)

#json，可作为内容向http提交，作为request的内容向网站提交
j = requests.request("POST","http://python123.io/ws",json=kv)

#headers，字典，http定制头
hd = {"user-agent":"Chrome/10"}
h = requests.request("POST","http://python123.io/ws",headers=hd)

#cookies字段，字典或CookieJar，Requests中的cookie
#auth字段，元祖类型，支持http认证功能
#files字段，字典类型，传输文件
fs = {"file":open("null.py","rb")}
f = requests.request("POST","http://python123.io/ws",file=fs)

#timeout,设定超时时间，秒为单位。如果在设定的时间内没有返回，则会产生一个timeout异常
t = requests.request("GET","http://python123.io/ws",timeout=30)

#proxies:字典类型，设定访问代理服务器，可以增加登录认证。用来反爬虫逆向追踪
pxs = {"http":"http://10.10.10.1:1234"}
p = requests.request("GET","http://www.baidu.com",proxies=pxs)

#allow_redirects:True/False，默认True,重定向开关
#stream:True/False，默认为True，即获取内容立即下载
#verfy:True/False，默认为True,认证SSL证书开关
#cert:本地ssl证书路径