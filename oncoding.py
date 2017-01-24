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
s1 = set('ffengzy') #实验创建集合
print(s1)

d = {'[1, 2]': '123', '(1, 2)': 'hwi'} #实验字典的key是否可以使用list（结果：可以）
print(type(d)) #类形是dict


s2 = {'facebook', 'book', 123} #实验创建集合
ns2 = type(s2) #类型是set
s4 = set(['123', '222'])
print(s2, ns2, s4)
print('-' * 20)

s1 = set([1, 2, 3])
ts1 = type(s1)
l1 = list(s1)
tl1 = type(l1)
print(ts1, tl1, dir(s1))

a_set = set('fengzy')
a_set.add('[1, "2", "fengzy"]')
print(a_set)

f_set = frozenset('fengzy')
print(f_set)

