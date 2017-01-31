# coding:utf-8
name = '冯卓雨'
print(name)

print(type(name))

a = 'a'.encode('utf-8')
print(a)

lang = 'python'
print(lang[0])
print(lang[0:2])

alist = [1, 2, 3, 4, 5, 6]
a = alist[::-1]
b = alist
c = list(reversed(alist))
d = len(alist)
print(a, b, c, d)

blist = [1, '小红', '小芳']

clist = ['小亮', '小明', '大王']

e = alist + blist

print(e, 1 in blist, min(alist), max(clist))

a = ['python', 'like', 'I']
a.append('good')

print(a)

b = a.index('like')
c = a[2]
d = a[:2]
print(b, c, d)
print(a[2] == a[-2])

print(dir(list))

clist = ['python', 'fengzy']

clist.extend(['1111', '444'])
clist.append([22, 33])

a = clist.index('1111')
clist.insert(0, ['插入', '列表'])

print(clist, a)

print('-' * 20)

a = ['python', 'c', 'php', 'python', 'java']
while 'python' in a:
    a.remove('python')
    print(a)
else:
    print('no python!')

a.pop(-1)

print(a)

b = 'hi you!'
for n in b.split():
    c = list(n)
    print(c)

print('-' * 20)
print(a + c, len(c), len(b))
print('-' * 20)
a[1] = 'c++'
c = b[0] + 'o' + b[2:]
print(a, b, c)

citys = ['suzhou', 'tangshan', 'beijing', 'shanghai']
city_codes = ['0512', '0315', '010', '012']
print('{}:{}'.format(citys[0], city_codes[0]))
person = {'name': 'fengzy', 'site': 'newpm.net', 'lang': 'python'}
p = person['name']
person['name2'] = 'joey'
person['name3'] = 'fengzy'
del person['name2']

print(person)
print(len(person))
print('name' in person)

print('-' * 20)
city_code = {
    'suzhou': '0512',
    'beijing': '010',
    'tangshan': '0315',
    'nanjng': '025'
}
l = 'suzhou is a beautiful city, its area code is %s!' % city_code['suzhou']
l2 = '\nsuzhou is a beautiful city, its area code is %(suzhou)s!' % city_code
print(l, l2)
print('-' * 20)
my = {'name': 'fengzy', 'lang': 'python'}
temp = '<html><head><title>%(lang)s</title></head><body><p>My name is %(name)s.</p></body></html>'
temp2 = '\n<html><head><title>{}</title></head><body><p>My name is {}.</p></body></html>'.format(my['lang'], my['name'])

print(temp % my, temp2)
print('-' * 20)
s1 = set('ffengzy')  # 实验创建集合
print(s1)

d = {'[1, 2]': '123', '(1, 2)': 'hwi'}  # 实验字典的key是否可以使用list（结果：可以）
print(type(d))  # 类形是dict

s2 = {'facebook', 'book', 123}  # 实验创建集合
ns2 = type(s2)  # 类型是set
s4 = set(['123', '222'])
print(s2, ns2, s4)
print('-' * 20)

s1 = set([1, 2, 3])
ts1 = type(s1)
l1 = list(s1)
tl1 = type(l1)
print(ts1, tl1, dir(s1))

a_set = set('fengzy')
a_set.add('[1, "2", "fengzy"]')  # 为集合添加一个元素
print(a_set)

f_set = frozenset('fengzy')  # 创建一个冻结集合，不可修改的
print(f_set)

for i in [1, 2, 3, 4]:
    print(i)

print(pow(3, 2))

print('-' * 20)

'''
print('请输入任意一个数字：')
number = int(input())

if number == 10:
    print('您输入的数字是： %d' % number)
    print('You are smart!')
elif number > 10:
    print('您输入的数字是： %d' % number)
    print('大了大了！')
elif number < 10:
    print('您输入的数字是： %d' % number)
    print('小了小了！')
else:
    print('Are you a human?')
'''

hello = 'world'
for i in range(len(hello)):
    print(hello[i])

# 创建一个0-100能够被3整除的列表
z_int = []  # 创建一个空列表
for n in range(0, 100):  # 将0-100每个数字代入n
    if n % 3 == 0:  # 如果n能够被3整除
        z_int.append(n)  # 向列表内放入一个n
print(z_int)  # 打印列表结果

# 学以致用，将上述代码简化
n = range(0, 100, 3)  # 设n为0-100，步长为3的数字
print(list(n))  # 将n转化为列表并打印

# 创建一个字典
a_dict = {'name': 'fengzy', 'lang': 'python', 'email': 'beyond0420@126.com', 'web': 'newpm.net'}
# 获取字典键值对方法一
for k in a_dict.keys():
    print(k, a_dict[k])
# 获取字典键值对方法二
for k, v in a_dict.items():
    print(k, v)
# 获取值
for v in a_dict.values():
    print(v)

a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]
c = []
for i in range(5):
    c.append(a[i] + b[i])
print(c)
# 使用zip函数解决上段代码问题
print(list(zip(a)))
d = []
for x, y in zip(a, b):
    d.append(x + y)
print(d)

'''
# 数字游戏
import random

number =  random.randint(1, 100)

guess = 0

while True:
    num_input = input('请输入1至100的数字！')
    guess += 1
    if not num_input.isdigit():
        print('请输入数字！')
    elif int(num_input) < 0 or int(num_input) >= 100:
        print('输入数字必须为1至100的整数！')
    else:
        if number == int(num_input):
            print('OK, you are good. It is only %d,then you successed.' % guess)
            break
        elif number > int(num_input):
            print('your number is more less.')
        elif number < int(num_input):
            print('your number is bigger.')
        else:
            print('There is something bad, I will not work.')
'''

print('-' * 20)

count = 0
while count < 5:
    print(count, 'is less than5')
    count += 1
else:
    print(count, 'is not less than 5')

from math import sqrt

for n in range(99, 1, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print('Nothing!')

f = open('README.MD')
for line in f:
    print(line)
f.close()

with open('README.MD', 'r') as f:
    print(f.read())

print('-' * 20)

a, b = open('README.MD')
print(a, b)

# 练习一：包含10个元素的列表，将列表每个元素依次向前移动一个位置，然后输出这个列表
raw = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # 假设列表raw包含10个数字
i = 0  # 默认起始次数
while i < 10:  # 设定条件，当i小于10时
    b = raw.pop(0)  # 将从列表起始位置删除的成员赋值给b
    raw.append(b)  # 在列表末尾追加被删除的成员
    i += 1  # 将循环次数加1
    print(raw)  # 打印列表

print('-' * 20)

import random  # 导入随机数模块

score = [random.randint(0, 100) for i in range(40)]  # 取得40个0-100的随机数以列表的形式赋值给score
print(score)  # 打印分数列表

num = len(score)  # 获取分数的个数
sum_score = sum(score)  # 求分数之和
ave_num = sum_score / num  # 求平均分
less_ave = len([i for i in score if i < ave_num])  # 过滤出小于平均分的分数，并取得个数
print('小于平均分的学生有 %d 个' % less_ave)  # 打印个数

sorted_score = sorted(score, reverse=True)  # 按照倒序排列分数
print(sorted_score)  # 打印排列后的分数

print('-' * 20)

string = 'I love  code.'  # 设定一个字符串
print(string)  # 打印字符串

str_lst = string.split(' ')  # 将字符串通过一个空格进行分割

print(str_lst)  # 打印分割后的字符串

words = [s for s in str_lst if s != '']  #将非空格的字符串代入s，目的是删除空格
print(words)  # 打印字符串

new_string = ' '.join(words)  # 以空格为连字符组装字符串
print(new_string)  # 打印组装后的字符串

print('-' * 20)

a, b = 0, 1
for i in range(4):
    a, b = b, a + b
print(a)

print('-' * 20)

class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def color(self, color):
        print('%s is %s' % (self.name, color))

me = Person('fengzy')
me.color('white')