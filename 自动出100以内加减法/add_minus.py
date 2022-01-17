'''

100以内加减法混合出题
'''

import random
exp1,exp2 = '',''
str1,str2 = '',''
j = 0

count = int(input('请输入出题数量：\n'))
while j < count:
    if j < count:
        flag = random.choice(['+','-','x','÷'])
        if flag == '+':
            a = random.randint(0,100)
            b = random.randint(0,100-a)
            result = a+b
        elif flag == '-':
            a = random.randint(0,99)
            b = random.randint(0,99)
            if a < b:
                a,b = b,a
            result = a - b
        elif flag == 'x':
            a = random.randint(1,99)
            b = random.randint(1,99)
            result = a * b
        else:
            a = random.randint(1,99)
            while True:
                b = random.randint(1,99)
                if(a % b == 0):
                    break
            result = int(a / b)
        a = str(a).ljust(2," ")
        b = str(b).ljust(2," ")
        exp1 = a + " " + flag + " " + b + ' ='
        exp2 = a + " " + flag + " " + b + ' =' + str(result)
        if j % 2 == 0:
            str1 = str1 + exp1 + '\t\t'
            str2 = str2 + exp2 + '\t\t'
        else:
            str1 = str1 + exp1 + '\n'
            str2 = str2 + exp2 + '\n'
        j = j + 1
        '''
with open('math.txt','w') as f:
    f.write(str1)
with open('key.txt','w') as f:
    f.write(str2)
    '''
print(count,'道混合加减法题：')
print(str1)
print(count,'道混合加减法题（带答案）：')
print(str2)