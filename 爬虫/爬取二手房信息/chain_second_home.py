'''
运用fake_useragent, asyncio, aiohttp,requests,lxml,pandas
爬取北上广二手房信息

Author: Nigel Chen
Date: 28/01/2022
'''
# 导入伪造头部信息模块
from fake_useragent import UserAgent
# 异步IO
import asyncio
# 异步网路请求
import aiohttp
# 网络请求
import requests
# 解析html模块
from lxml import etree
# pandas模块
import pandas
import time

class HomeSpider():
    def __init__(self):
        self.data = []
        self.headers = {"User-Agent": UserAgent().random} # 随机生成头部信息

    # 创建异步网路哦请求对象，通过异步方法get发送请求
    async def request(self, url):
        async with aiohttp.ClientSession() as session: #创建异步网络请求对象
            try:
                async with session.get(url, headers = self.headers,timeout=3) as response:
                    if response.status == 200 :  # 200说明请求成功
                        result = await response.text() # 获取请求结果中的文本代码
                        return result
            except Exception as e:
                print(e.args) #打印异常信息

    # 获取北上广对应代码
    def get_city_letter(self,city_name):
        city_dict = {"北京":"bj","上海":"sh","广州":"gz","杭州":'hz',"深圳":'sz'}
        return city_dict.get(city_name)

    # 发送一次网络请求，解析返回代码，获取总页数
    def get_page_all(self,city):
        city_letter = self.get_city_letter(city)
        url = 'https://{}.lianjia.com/ershoufang'.format(city_letter)
        response = requests.get(url,headers=self.headers) #发送网络请求
        if response.status_code == 200:
            html = etree.HTML(response.text)

            page_all = html.xpath('//*[@id="content"]/div[1]/div[7]/div[2]/div/@page-data')[0]
            page_all = str(page_all)[13:16]
            print(page_all)
            print("租房信息获取成功！")
            # 需要抓取每一页，所以结果+1
            return int(page_all) + 1
        else:
            print('获取所有页码请求未成功！')

    '''
    删除字符串中的空格与换行符
    '''
    def remove_spaces(self, info):
        info_list = []
        for i in info:
            x = i.replace(' ','').replace('\n','')
            if x == '':
                pass
            else:
                info_list.append(x)
        return info_list

    def divide(self,info):
        info_list = []
        room_list = []
        sqaure_list = []
        dir_list = []
        floor_list = []
        style_list = []
        for i in info:
            x = i.split('|')
            room_list.append(x[0])
            sqaure_list.append(x[1])
            dir_list.append(x[2])
            floor_list.append(x[4])
            style_list.append(x[5])
        info_list.append(room_list)
        info_list.append(sqaure_list)
        info_list.append(dir_list)
        info_list.append(floor_list)
        info_list.append(style_list)
        return info_list


    '''
    将大区域小区域信息合并
    '''
    def combined_regin(self, big_region, small_region):
        region_list = []

        for a,b in zip(big_region,small_region):
            region_list.append(a+'-'+b)
        return region_list

    '''
    异步方法，根据总页数循环解析页面抓取信息，包括标题、区域、面积、楼层、价格
    '''
    async def parse_data_all(self, page_all, city):
        for i in range(1,page_all): #根据租房信息总页码，分别对每一页发送网络请求
            city_letter = self.get_city_letter(city)
            if i == 1:
                url = 'https://{}.lianjia.com/ershoufang/ab200301001000rt200600000001'.format(city_letter, i)
            else:
                url = 'https://{}.lianjia.com/ershoufang/ab200301001000pg{}rt200600000001'.format(city_letter,i)
            html_text = await self.request(url) #发送请求，获取html代码
            html = etree.HTML(html_text)
            print('获取'+str(i)+'页信息！')

            #获取所有标题
            title_all = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[1]/a/text()')

            #获取大区域位置
            big_region_all = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[2]/text()')

            #获取小区位置
            small_region_all = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[1]/text()')

            # 房子信息
            info_all = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[3]/div/text()')

            # 房子价格
            price_all = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()')

            # 均价
            ave_price_all = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()')
            '''
            #获取房子面积
            square_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/text()[5]')

            #获取房子价格
            price_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/span/em/text()')

            #获取房子格局
            room_all = html.xpath('//*[@id="content"]/div[1]/div[1]/div/div/p[2]/text()[1]')
            '''

            # 去除信息中的空格以及换行符
            title_list = self.remove_spaces(title_all)
            big_region_list = self.remove_spaces(big_region_all)
            small_region_list = self.remove_spaces(small_region_all)
            info_list = self.remove_spaces(info_all)
            price_list = self.remove_spaces(price_all)
            ave_price_list = self.remove_spaces(ave_price_all)
            info_list_sub = self.divide(info_list)
         #   region_list = self.combined_regin(big_region_all,small_region_all)
         #   square_list = self.remove_spaces(square_all)
           # price_list = self.remove_spaces(price_all)
            data_page = {'标题':title_list,
                         '区名':big_region_list,
                         '小区/位置':small_region_list,
                         '几室几厅':info_list_sub[0],
                         '面积':info_list_sub[1],
                         '朝向':info_list_sub[2],
                         '楼层':info_list_sub[3],
                         '房子类型':info_list_sub[4],
                         '价格（万）':price_list,
                         '均价':ave_price_list}
            print('写入第'+str(i)+'页数据！')
            df = pandas.DataFrame(data_page)
            df.to_csv('{}二手房信息.csv'.format(city),mode = 'a',encoding='utf_8_sig',index=None)

    def start(self,page_all,city):
        loop = asyncio.get_event_loop() #创建loop对象
        loop.run_until_complete(self.parse_data_all(page_all,city))

if __name__ == '__main__':
    input_city = input('请输入需要下载二手房信息的城市名称!')
    home_spider = HomeSpider()
    page_all = home_spider.get_page_all(input_city)
    print(page_all)
    start = time.time()
    home_spider.start(page_all,input_city)
    end = time.time()
    print(f'程序执行时间是{end-start}秒.')


