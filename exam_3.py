def func1(list1):
    list1.insert(0, 'start')
    list1.insert(0, 'element')
    list1.append('finish')
    return list1
print(func1(['hello', 'John']))

def func2(*args):
    a = list(args)
    b = {}
    j = 1
    for i in range(len(a)):
        b[a[i]] = j
        j += 1
    return b
print(func2('x', 5, 'John'))

def func3(num):
    lst = list(num)
    a = (list(filter(lambda x: x % 2 == 0,lst)))
    b = (list(map(lambda x: x ** 2,lst)))
    return a,b

a, b = func3((1,2,3,4,5))
print(a)
print(b)