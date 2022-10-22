import numbers


i = 0
y = 0
while i < 5:
    print("*****")
    i = i+1

# i = ["*", "*", "*", "*", "*"]
# for item in i:
#     print(item)
print("")


for i in range(5):
    print("*****")

print("")


# 빈 직사각형 그리기
for i in range(5):
    if i == 0 or i == 4:
        print("*****")
    elif i > 0 and i < 4:
        print("*   *")


# 배열의 평균 값
def solution(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum+numbers[i]
    return sum/len(numbers)


print(solution(numbers=[1, 2, 3, 4, 7, 5, 7, 8, 9, 10]))


# 머쓱이보다 키큰사람
array = [1, 0, 1, 1, 1, 3, 5]
# height = 167
# answer = 0
# for i in range(len(array)):
#     if array[i] > height:
#         answer = answer+1
# print(answer)


def solution(num_list):
    num_list.reverse()
    return num_list


# 리스트 자르기
print(solution([1, 0, 1, 1, 1, 3, 5]))
num1 = 1
num2 = 3
numbers = [1, 2, 3, 4, 5]
print(numbers[num1:num2])


# 특정 문자 개수 세기
str1 = "12345433444"
count = str1.count("3")+str1.count("1")
print(count)