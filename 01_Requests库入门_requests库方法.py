import requests

#head方法
head = requests.head("http://www.zeroxzhang.cc")
print(head.headers)
print(head.text)#这个时候是空

#post方法，新增数据
payload = {"key1":"value1","key2":"value2"}#字典默认存在form的字段下，字符串默认存在data的字段下
post = requests.post("http://httpbin.org/post",data=payload)
print(post.text)

#put方法与post方法类似，只不过会覆盖掉原有数据