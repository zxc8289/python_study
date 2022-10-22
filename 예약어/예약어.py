import math as mt
# True, is, if, False None등 예약어를 변수로 쓸 수 없다.

# __aaa = 123
# print(__aaa)

# temp = None
# print("temp에 None넣었음" + str(temp))
# temp = True and False

# print(temp)


# for item in range(10):
#     if item == 5:
#         # 건너뛰기
#         continue

#     elif item == 8:
#         # 멈춤
#         break

#     else:
#         print(item)


# try:
#     temp = "가나다"
#     temp[0] = "아"
# except Exception as e:
#     e.with_traceback()
#     # print("에러가 발생했습니다.")
# finally:
#     print("마지막으로 할 것은 하겠습니다.")

# print("넘어왔습니다.")

# temp = 1
# for i in range(10):
#     pass

# print(temp)

# temp = 1

# def my_func():
#     global temp
#     temp = 3
#     return temp

# print(my_func())
# print(temp)

# raise Exception("내가 만든 에러")

# def my_func(num):
#     print(num)

# my_func(12)

# 아규먼트, 인자, 인수

# my_func = lambda num : print(num)
# my_func(12)

# 람다식
# temp = list(filter(lambda num: num != 1, [1, 2, 3, 1]))
# print(temp)


def my_func():
    while True:
        yield 1
        yield 2
        yield 3


my_yield_data = my_func()

for item in my_yield_data:
    print(item)

# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))
