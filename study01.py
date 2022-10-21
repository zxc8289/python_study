from decimal import Decimal
from distutils.util import change_root
import math
from unittest import result


# x = 2; y = 3
# num = x / y
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(-x)
# print(+x)
# print(abs(x))
# print(int(x))
# print(float(x))
# print(divmod(x,y))
# print(pow(x,y))
# print(x ** y)

# print(math.trunc(x))
# print(round(x/y, 3))
# print(math.floor(x))
# print(math.ceil(x))

# num = Decimal('1.1') + Decimal('0.1')
# print(num)

# name = 'jaybon'
# name1 = 'lookie'
# age = 10

# # 주석
# print("내 이름은 : " + name + "\n내 나이는 : " + str(age))
# print(f"{name=}\n{age=}")
# print("내 이름은 %s 내 나이는 %d"% (name, age))
# print("내 이름은 {0} 내 나이는 {1}".format(name, age))

# my_list = [1,2,3,4]
# print(len(my_list))
# for element in my_list:
#     print(element)

# string = "가나다라마바사"
# # split 문자열 잘라내기
# char_list = string.split('나')
# print(char_list)

# change_string = string.replace('나', '하')
# print(change_string)

# print(id(string))
# print(id(change_string))

## 문자와 숫자는 같은 데이터면 같은 주소가나온다. 
## 리스트나 집합은 다르게나옴
# d1 = "가나다"
# d2 = "가나다"
# print(id(d1))
# print(id(d2))

# input = 1
# while input < 4:
    
#     if input == 1:
#         print("input == 1 입니다.")
#         input = input + 1
        
#     elif input == 2:
#         print("input == 2 입니다.")  
#         input = input + 1
    
#     else :
#         print("1 or 2와 다른 값 입니다.")
#         input = input + 1
# i=0


# while i<10: 
#     data = int(input())
#     if data == 1:
#         print("input == 1 입니다.")
#         i = i + 1
#         print("count : "+str(i))
#     elif data == 2:
#         print("input == 2 입니다.")  
#         i = i + 1
#         print("count : "+str(i))
#     else :
#         print("1 or 2와 다른 값 입니다.")
#         i = i + 1
#         print("count : "+str(i))


# x=1
# while True:
#     data = int(input())
#     if x == 10:
#         break
#     else:
#         if data == 1:
#             print("input == 1 입니다.")
                  
#         elif data == 2:
#             print("input == 2 입니다.")  
             
#         else :
#             print("1 or 2와 다른 값 입니다.")
#         print("count : "+str(x))
#         x=x+1

## 함수사용
# def check_data():
#     x=1
#     while True:
#         data = int(input())
#         if x == 10:
#             break
#         else:
#             if data == 1:
#                 print("input == 1 입니다.")
                    
#             elif data == 2:
#                 print("input == 2 입니다.")  
                
#             else :
#                 print("1 or 2와 다른 값 입니다.")
#             print("count : "+str(x))
#             x=x+1
#     print("count : "+str(x))
# check_data()

# def sum_two_num(n1,n2):
#     return n1 + n2
    
# print(sum_two_num(1,2))

# result = not(1 == 2)

# print(result)

# my_set = {1,2,3,4,1,1,1,1}
# my_set = set([1,2,3,4,1,1,1,1])

# print(my_set)

# for item in my_set:
#     print(item)
    
## 값을 가져오기 위해서 items() 사용
# my_dict = {"score" : 15, "age" : 22}
# for key, value in my_dict.items():
#     print(f"{key} : {value}")

my_tuple = (1,1,2,3,4)


print(my_tuple)

for item in my_tuple:
    print(item)