# s=1
# print(type(s))
# list=[10]
# print(list)
# s=True
# print(s)
# list=(10,"10",True,'admin')
# print(list)
# print(type(list))
# s=[10,'10',True,'admin']
# print(type(s))
# tuplevar=['admin',10,1.2,True,False,('lest',)]
# print(tuplevar[2:6:1])
# print(len(tuplevar))
# print(tuplevar[1])
# s=[12.12,12,28,3,7,999,5774,5,]
# s.sort
# s='1,2,3,2,3,2'
# w=s.split(',')
# print(w)
# s = '1 : 2 :3 :4'
# print(s.split(':'))
# print(s)
# i={'1':1,2:3,'admin':1}
# # i.pop('1')
# # print(i)
# data = [10, {'name': {'job': (10, 20, 30, [100, 200, {'sex': 'male'}])}}]
# i=data[1]
# a=i['name']
# b=a['job']
# c=b[3]
# f=c[2]
# g=f['sex']
# print(g)

# import random
# num = random.randint(1,10)
# i=5
# while i > 0:
#     data = int(input('请输入一个数字'))
#     if data == num:
#         print('你猜对了')
#         break
#     else:
#         print('你猜错了')
#         i-=1

# listvar = [10, 20, 30]
# tupvar = ('a', 'b', 'c')
# dicvar = {'name': 'tom', 'job': 'it'}
# data = '{0[1]}{1[1]}{2[name]}'.format(listvar, tupvar, dicvar)
# print(data)
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}*{}={}'.format(j, i, i * j),end='  ')
#     print(' ')
# try:
#     print(0/0)
# except BaseException as msg:
#     print(msg)
# try:
#     print(())
# except BaseException as msg:
#     print(msg)
# try:
# #     print(1/2)
# # except BaseException as msg:
# #     print(msg)
# # else:print(1/1)
# # finally:
# #     print(1/2)
# i = []
# s = []
# strvar = 'a2b3b5c6d8j9z7'
# for n in strvar:
#     if n.isalpha():
#         i.append(n)
#     else:
#         s.append(n)
# print(i)
# print(s)
# i = []
# s = []
# strvar = '1a2b3b5c56d8j9z7'
# for n in strvar:
#     try:
#         a=int(n)
#         i.append(a)
#     except:
#         s.append(n)
#
# print(i)
# print(s)
# unicod 字符集（字典）
# 基于这个字典的对二进制数据的翻译
# utf-8 utf-16 utf-32
# ascii编码 它既是字典也是一种翻译方式

# def test_apple():
#     print('这是一个函数')
#     print(1)
#     print(1)
# test_apple()
# a=1
# b=2
# c=['a']
# def test(a,b,c):
#     print(a,b,c)
# test(a,b,c)


# def funcA():
#     print('这是一个函数a')
# def funcB():
#     a()
# def funcC(a):
#     print('这是一个函数c')
# funcC(a)
# def funcF (a,d,b,e='hello',c='python'):
#     print(a,b,e,c,d)
# funcF(10,20,30)

# def funcA(x, y, z):
#     if x == '+':
#         print(int(y) + int(z))
#     elif x == '-':
#         print(int(y) - int(z))
#     elif x == '*':
#         print(int(y) * int(z))
#     elif x == '/':
#         print(int(y) / int(z))
#     else:
#         print('输出系统错误')


# funcA('+', 1, 2)

# def funcA(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
#
#
# funcA(1, 2, 3, 4, x=1, y=2)

# dictvar = {'name':'job','age':28}
# def funcA(name,age):
#     print(name,age)
# funcA(**dictvar)

# dictvar = 'hello'
# def funcA(var1,var2,var3, var4, var5):
#     print(var1, var2,var3, var4, var5)
# funcA(*dictvar)
# strvar = [10,20,30]
# def funcA():
#     strvar.append('hello')
#     print(strvar)
# funcA()
# intvar=10
# def funcA():
#     global intvar
#     intvar+=10
#     print(intvar)
# funcA()
# dictvar = {'apple':'苹果'}
# def getDict(var):
#     print('{}英文翻译是：',format(var),dictvar.get(var))
#
# def setDict(var1,var2):
#     if dictvar.get(var1,'找不到这个字典') == '找不到这个字典':
#         dictvar[var1] = var2
#         print('添加的字典信息成功')
#     else:
#         print('你已经添加过这个字典了')
# setDict('apple','苹果')
# setDict('techer','老师')
# def funcA():
#     strvar='admin'
#     return strvar
# data=funcA()
# print(data)
# def funcA():
#     strvar1='admin'
#     strvar2='haha'
#     strvar3=10
#     return strvar1,strvar2,strvar3
# print(funcA())
# dictvar={'hello':'你好'}
# def setDict(var1,var2):
#     data=dictvar.get(var1,' 找不到这个翻译')
#     if data == '找不到这个翻译':
#         dictvar[var1] = var2
#         return ' 添加成功'
#     else:
#         return '已经添加过了'turtle.cirecle(10)turtle.cirecle(10)
#     print(setDict('hello'))


#
# listvar = [10,20,30,50,60]
# for i in listvar:
#     if i ==30:
#         continue
#     print(i)

# for i in range(1,10):
#     for l in range(1,i+1):
#         print('{} * {} = {}'.format(i,l,i*l),end='  ')
#     print( )

# print(open('./test.txt','r',encoding='utf-8').readlines())
# print(open('D:/pyhon/test.txt','r',).readlines())
# open('./test.txt','r').close()
# f=open('./test.txt','r')
# f1 =f.readlines()
# print(f1)
# f.close()
# i='hello'
# j=(open('./test.txt','w+',).writelines(i) )
# print(open('./test.txt','r',).readlines())

# listvar = ['10', '20', '30', '40', '50']
# import json
#
# data = json.dumps(listvar)
# print(len(data))
# f = open('./test.txt', 'w+')
# i=f.write(data)
# print(type(i),i)
# f.close()
# strvar='ilovepython'
# f=open('./test.txt','w+')
# f.write(strvar)
# f=open('./test.txt','r')
# data=f.readlines()
#
# print(data)
#
# with open('./test.txt','r')as f1:
#     data=f1.read()
#     print(data)
# data2=data.replace('python','hello')
# f=open('./test.txt','w+')
# f.write(data2)

import day_tc
# from day import (strvar,funcA)
# print(strvar)
# print(funcA())
#
# from day import (strvar2,funcB)
# print(funcB())

import day_tc


# from day import funcB
# print(funcB())

# import sys
# print(sys.path)

# import day
# print(day.funcA())
# day.funcA()

# import os
# os.mkdir('./hello')
# os.rmdir('./hello')


# class Yifu(object):
#     yanse='red'
#     daxiao='170'
#     def i(self):
#        print ('这是一件衣服')
# if __name__ == '__main__':
#     var=Yifu()
#     print(var.daxiao)
#     print(var.yanse)
#     var.i()
# var='python'
# class Aclass(object):
#     var2='java'
#     def methodA(self):
#         print('输出的是一个全局变量',var)
#         print(self.var2)
#     def methodB(self):
#         var3='php'
#         print(var3)
#     def methodC(self):
#         self.var4='javascript'
#     def methodD(self):
#         print('类本身调用实例变量',self.var4)
# if __name__ == '__main__':
#     run=Aclass()
#     run.methodC()
#     run.methodD()
#     print('实例化之后调用的实例变量',run.var4)
# class Bclass(object):
#     var2='java'
#     def __init__(self,a,b):
#         print('魔法方法先输出')
#         self.a=a
#         self.b=b
#         print('self a is',a)
#         print('self b is',b)
#     def methodA(self,var):
#         print('这是一个人实例的方法',var)
#     def methodB(self):
#         print('这是一个实例方法B')
#     def methodC(self):
#         self.var2='php'
#     def __del__(self):
#         print('魔法方法最后输出')
# if __name__ == '__main__':
#     run = Bclass(10,20)
#     run2=Bclass('python','java')
#     print(run.var2)

# listvar = []
#
#
# class List(object):
#     def i(self, var):
#         listvar.append(var)
#
#     def o(self):
#         listvar.pop()
#
#     def p(self, a, b):
#         listvar.insert(a, b)
#
#
# if __name__ == '__main__':
#     run = List()
#     run.i('haha')
#     run.p(0,'xixi')
#     print(listvar)

# class Aclass(object):
#     def methodA(self):
#         return '这是一个实例方法'
#     @classmethod
#     def methodB(cls):
#         return '这是一个类方法'
#     @staticmethod
#     def methodC():
#         return '这是一个静态方法'
# if __name__ == '__main__':
#     # run=Aclass()
#     # print(run.methodA())
#     print(Aclass.methodB())
#     print(Aclass.methodC())
# class DictClass(object):
#     def __init__(self):
#         self.dectvar = {}
#
#     def getDict(self, key):
#         data = self.dectvar.get(key, '找不到这个数据')
#         if data == '找不到这个数据':
#             return self.dectvar
#         else:
#             return data
#
#     def addDict(self, key, value):
#         data = self.dectvar.get(key, '找不到这个数据')
#         if data == '找不到这个数据':
#             self.dectvar[key] = value
#             return '添加成功'
#         else:
#             return '已经添加过不可修改'
#     def removeDict(self,key):
#         data = self.dectvar.get(key, '找不到这个数据')
#         if data=='找不到这个数据'
#             return '这个值不存在不可删除'
#         else:
#             self.dectvar.pop(key)
#             return '删除成功'
# if __name__ == '__main__':
#     run=DictClass()
#
# class FatherClass(object):
#     fathervar='爸爸的变量'
#     def __init__(self):
#         self.fathervar='爸爸的实例变量'
#     def test(self):
#         print('这是爸爸类的测试方法')
# class CalcClass(object):
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         return self.num1+self.num2
#     def sub(self):
#         return self.num1-self.num2
#     def mul(self):
#         return self.num1*self.num2
#     def div(self):
#         return self.num1/self.num2
# import unittest
# class TestCalcClass(unittest.TestCase):
#     def testCalc4(self):
#         print('这是一个方法')
#     def testCalc3(self):
#         print('这是一条这是用例')
#     def testCalc1(self):
#         run=CalcClass(10,20)
#         data=run.add()
#         self.assertEqual(data,40)
#     def testCalc2(self):
#         run=CalcClass(10,20)
#         data=run.add(10,20)
#         self.assertEqual(data,30)
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
# import unittest
# class  TestCalcClass(unittest.TestCase):
#     def setUp(self):
#         print('测试用例开始执行了')
#     def test_print_data(self):
#         print('这是第一条测试用例')
#     @unittest.skip('这条测试用例不执行')
#     def test_print_data2(self):
#         print('这是第二条测试用例')
#     def test_print_data3(self):
#         print('这是第三条测试用例')
#     def test_print_data4(self):
#         print('这是第四条测试用例')
#     def tearDown(self):
#         print('这是结束了')
# if __name__ == '__main__':
#     unittest.main(verbosity=1)

import time
import unittest
from HTMLTestReportCN import HTMLTestRunner
dirpath='./Scripts'
discover=unittest.defaultTestLoader.discover(dirpath,pattern='*_tc.py')
currenttime=time.strftime('%y%m%d%H%M%S')
filedir='./Reports/'+'report'+currenttime+'.html'
fp=open(filedir,'wb')
runner=HTMLTestRunner(stream=fp,
                      title='计算器自动化测试报告',
                      description='计算器自动化测试项目详细描述',
                      tester='我是谁')
runner.run(discover)
fp.close()





