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
print(a.__add__('y'))







