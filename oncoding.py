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