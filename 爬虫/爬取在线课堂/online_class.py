'''
爬网易在线课堂关于python的课程
运用xlsxwrite写到excel文档中
'''
import requests
import xlsxwriter

def get_json(index):
    '''
    爬取json信息
    :param index: 当前索引，从0开始
    :return: JSON数据
    '''

    url = "https://study.163.com/p/search/studycourse.json"
    #playload信息
    playload = {
       "activityId": 0,
        "keyword": "python",
        "orderType": 50,
        "pageIndex": index+ 1,
        "pageSize": 50,
        "priceType": -1,
        "qualityType": 0,
        "relativeOffset": 0,
        "searchTimeType": -1,
        "searchType": 30
    }

    #header 信息
    headers = {
        "accept": "application/json",
        "host" : "study.163.com",
        "content-type": "application/json",
        "origin": "https://study.163.com",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Connection":"keep-alive"
    }

    try:
        #发送post
        response = requests.post(url,json = playload,headers=headers)
        requests.adapters.DEFAULT_RETRIES=5
        s = requests.sessions
        s.keep_alive = False
        #获取json数据
        content_json = response.json()
        # 判断数据是否存在
        if content_json and content_json["code"] == 0:
            return content_json
        return None
    except Exception as e:
        print('出错了')
        print(e)
        return None

def get_content(content_json):
    '''
    获取课程列表
    :param content_json: 获取json格式数据
    :return: 课程数据
    '''

    if "result" in content_json:
        # 返回课程数据列表
        return content_json["result"]["list"]

def save_excel(content,index):
    '''
    储存到excel
    :param content: 课程内容
    :param index: 索引值，从0开始
    :return: None
    '''

    for num,item in enumerate(content):
        row = 50 *index+(num+1)
        worksheet.write(row, 0,item['productId'])
        worksheet.write(row, 1, item['courseId'])
        worksheet.write(row, 2, item['productName'])
        worksheet.write(row, 3, item['productType'])
        worksheet.write(row, 4, item['provider'])
        worksheet.write(row, 5, item['score'])
        worksheet.write(row, 6, item['scoreLevel'])
        worksheet.write(row, 7, item['learnerCount'])
        worksheet.write(row, 8, item['lessonCount'])
        worksheet.write(row, 9, item['lectorName'])
        worksheet.write(row, 10, item['originalPrice'])
        worksheet.write(row, 11, item['discountPrice'])
        worksheet.write(row, 12, item['discountRate'])
        worksheet.write(row, 13, item['imgUrl'])
        worksheet.write(row, 14, item['bigImgUrl'])
        worksheet.write(row, 15, item['description'])


def main(index):
    '''
    程序运行函数
    :param index:索引值 从0开始
    :return:
    '''
    content_json = get_json(index)
    content = get_content(content_json)
    save_excel(content,index)

if __name__ == '__main__':
    print('开始执行')
    workbook = xlsxwriter.Workbook("网易云课堂python课程数据.xlsx")
    worksheet = workbook.add_worksheet('first_sheet')

    #行首标题
    worksheet.write(0,0,'商品ID')
    worksheet.write(0,1,'课程ID')
    worksheet.write(0,2,'商品名称')
    worksheet.write(0,3,'商品类型')
    worksheet.write(0,4,'机构名称')
    worksheet.write(0,5,'评分')
    worksheet.write(0,6,'评分等级')
    worksheet.write(0,7,'学习人数')
    worksheet.write(0,8,'课程节数')
    worksheet.write(0,9,'讲师名称')
    worksheet.write(0,10,'原价')
    worksheet.write(0,11,'折扣价')
    worksheet.write(0,12,'折扣率')
    worksheet.write(0,13,'课程小图url')
    worksheet.write(0,14,'课程大图url')
    worksheet.write(0,15,'课程描述')

    totalPageCount = get_json(1)['result']['query']['totlePageCount'] #获取总页数


    #遍历每一页
    for index in range(totalPageCount):
        main(index)
    workbook.close()
    print('执行结束')
