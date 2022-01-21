'''
测试爬虫是否成功
'''
import requests

resp = requests.get('https://www.baidu.com')
print(resp)
print(resp.content)