# range(시작숫자, 끝 숫자, 배수)
# 3부터 30까지 3배수
# [3, 6, 9, 12, 15, 18, 21, 24, 27]
temp = list(range(3, 30, 3))
print(temp)

# temp = list(range(0, 10))
# for item in temp:
#     print(item)

# for문으로 레인지로 만들어진 값들을 돌림
temp = [item for item in range(0, 10)]

print(temp)
