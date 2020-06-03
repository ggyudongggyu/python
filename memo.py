# A = [[0 for col in range(10)] for row in range(10)]
#
# for i in range(10):
#     for j in range(10):
#         A[i][j] = i * j
#
# for j in range(len(A)):
#     print(A[j], end="\n")

##################################

# if 0:
#     print("True")
# else: print("False")

###########
# import random
# print(random.randrange(1,7))
##########

# try :
#     a = 10 / 0
# except ZeroDivisionError as ex:
#     print(ex)
#     print(type(ex))
#     print(ex.args)
# else:
#     print('completed')

#####################################

# A=[]
# for i in range(1, 101):
#     A.append(i)
# # A.reverse()
# # print(A)

###################

# import random
# random.seed(1)
# A=[]
# for i in range(1, 30) :
#     B = random.randrange(1,20)
#     A.append(B)
# print(A)

###################

# location = {
# 'Prefectur': 'hokkaido',
# 'city': 'wakananai',
# 'latitude': '45.404',
# 'longitute': '141.68'
# }
# location['city'] = 'wakkanai'
# location['population']= 40151
# if 'Sity'in location:
#     print(location['city'])

##############

# wday = ['Sun', 'Man','Tue','Wed','Thu','Fri']
# wday[1] = 'Mon'
# wday.append('Sat')
# idx = len(wday) - 2
# print(wday[idx])

####

# def spam(num):
#     return 'Spam'*num
# order1 = spam(3)
# order2 = spam(1)
# print(order1 + order2)

# class Spam:
#     def manufacture(self):
#         print('Homel Foods Cooporation')
# lunch = Spam()
# Company = lunch.manufacture()
# print(Company)

###############

# try:
#     c = 1//9
#     a = 10/0
# except TypeError:
#     print('Type ERROR')
# except ZeroDivisionError:
#     print('ZeroDiv ERORR')
# except:
#     print('ERROR')

##########
# class Spam:
#     def __init__(self, amount, salt):
#         self.salt = salt
#         self.amount = amount
#     def __str__(self):
#         msg1 = str(self.amount) + ' gram'
#         msg2 = str(self.salt) + ' milligrams'
#         return msg1 + ', ' + msg2

# lunch = Spam(280,560)
# print(lunch)

####

# print("{0:f}".format(12.34))
##

# f1 = 'cat'
# f0= 'rabbit'
# print('The quick brown {1} jumps over the lazy{0}'.format('fow', 'dog'))

# sentence = 'The quick brown fox, jumps over the lazy dog'
# sentences = sentence.split(',')
# words = sentences[1].split(' ')
# print(words[-1].title())

# import datetime
# from datetime import date
# # print(datetime.date.today())
# print(date.today())

# rabbits = ['Flopsy','Mopsy','Peter','Lily','Cotton-tail']
# trap = ",".join(rabbits)
# print(trap.split(',')[2])

# with open('sample.txt') as fin:
#     contents = fin.readline()
# if fin.closed:
#     print('something else')
# else:
#     print('none')

# import re
# m = re.search(r'You', 'Young Sharlock')
# if m :
#     print('hit')
# else:
#     print('miss')

# peter_rabbit = ['Flopsy','Mopsy','Peter','Lily','Cotton-tail']
# watership_down = ['Bigwig','Fiver','Hazle','Clover','Hyzenthlay']

# for i in range(len(watership_down)):
#     if i == 3 :
#         print(peter_rabbit[i], 'and', watership_down[i])



#######################


# class japanese:
#     def __init__(self, ninzu, namae):
#         self.name = namae
#         print("こんにちは",self.name,"です。")
#         self.pop = ninzu
#         print("日本の人数は",self.pop,"です。")

# class korean:
#     def __init__(self, ingu, irum):
#         self.name = irum
#         print("안녕하세요", self.name,"입니다.")
#         self.pop = ingu
#         print("한국의 인구는",self.pop,"입니다")


# soneshin = japanese(127185000, 'sonehara')
# shimizu  = japanese(1221, 'masaki')
# park = korean(60000000, 'donggyu')

# print(soneshin,'\n',park)

# a = [1,10,2,3,4,5,6]
# print(max(a))
# print(max )

# sentence = "Hello, my name is minori"
# print(sentence.split(',',3 #list[3]まで作る予定です))

# n=int(input())
# for i in range(1, n+1):
#     print("*"*i)
# for j in range(n-1, 0, -1):
#     print("*"*j)


A = [2]
A += [3]
print(A)    
