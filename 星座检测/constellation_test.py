'''
输入出生年月日输出对应星座
可识别闰年闰月
可选择退出或者持续输入
可检测输入字符，非法字符会有提示用户重新输入
'''

import re

sdate = [20,19,21,20,21,22,23,23,23,24,23,22] # 星座判断列表
conts = ['摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座'] #星座,需要比日期多一个。

# 如果日期数据对应月列表对应日期则输出对应，不然输出下一个月对应星座
def sign(cmonth, cdate):
    if int(cdate) < sdate[int(cmonth) - 1]:
        print('您的星座是:',conts[int(cmonth) - 1])
    else:
        print('您的星座是:',conts[int(cmonth)])

#进行语句判断
while(True):
    # 用户输入
    birth = input('请输入你的出生年月，格式为2001-02-21,输入q退出:\n').strip(' ')
    if(birth == 'q'):
        break
    # 进行正则比较
    matchObj = re.match(r'[1-2][0,9][0-9]{2}-[0-1][0-9]-[0-3][0-9]',birth)
    if matchObj:
        cbir = birth.split('-')
        cyear = int(cbir[0])
        cmonth = str(cbir[1])
        cdate = str(cbir[2])

        #闰年闰月检测
        if (cyear % 4 == 0 and cyear % 100 != 0) or (cyear % 400 == 0):
            if(cmonth == '02' and int(cdate)>29):
                print('您输入的 %s 是闰年2月，日期超过了29，请确认出生日期'%(str(birth)))
            else:
                sign(cmonth, cdate)
        else:
            if (cmonth == '02' and int(cdate) > 28):
                print('您输入的 %s 是2月，日期超过了28，请确认出生日期' %(str(birth)))
            else:
                sign(cmonth, cdate)
                birth = input('若退出请输入q，若不退出任意输入: ').strip(' ')
                if(birth == 'q'):
                    break
    else:
        print('您输入的 %s 格式有误，正确格式为2001-02-21'%(str(birth)))