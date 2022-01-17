'''
核心实现为用户持续输入数字，打印出数字累加的结果
Author：Nigel Chen
Date: 10/01/2022
'''

all = 0.0
alladd = 0.0
indig = ''
lst = []

# 做加法
def add(addin,data):
    addone = addin + data
    return addone

# 做减法
def minus(addin,data):
    minusone = addin - data
    return minusone

# 检测是否是数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata

        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass

    return False

# 检测是否是加减号
def is_add_minus(s):
    try:
        if(s == '+' or s =='-'):
            return True
    except ValueError:
        pass
    return False

print('''
-------------------
-                 -
-  简单加减法累加器  -
-  输入数字以及加减  -
-                 -
-------------------
''')

while True:
    indig = input('输入(退出输入q)：').strip('')
    if indig == 'q':
        break

    # 判断数字
    elif is_number(indig) == True:
        function_addminus = input('输入加号（+）做加法，输入减号做减法（-): ')

        # 判断是否是加减号输入正确
        if is_add_minus(function_addminus) == True:
            if function_addminus == '+':
                alladd = add(float(all),float(indig))
                all = format(alladd,'.2f')
            else:
                alladd = minus(float(all),float(indig))
                all = format(alladd,'.2f')

            # 记录输入的内容
            lst.append(indig)
            print(all)
            # 打印流程
            print('已输入：',end='')
            print(*lst,sep=',')
            print('-------------------------------')
        else:
            print('请输入正确加减号，清重新输入')
            print('-------------------------------')
    else:
        print('输入了非数字输入错误，请重新输入！')
        print('-------------------------------')