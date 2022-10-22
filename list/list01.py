temp = [1, 2] + [3, 4]

# 값 붙이기
temp.append(5)

# 값 삭제
temp.remove(1)

temp = [1, 1, 1, 1]
temp.remove(1)
# 모든 같은 데이터를 지우지 않음
# 데이터 1이 4개가 있지만 하나만 삭제됨

temp = [1, 1, 1, 1]


def check(num):
    if num == 1:
        return False
    else:
        return True


print(check(12))


temp = [1, 2, 3, 1, 1]
temp = filter(check, temp)
temp = list(temp)
print(temp)
temp = [1, 2, 3, 4, 5]

# 2차원 배열
temp = [[1, 2], [3, 4]]
print(temp[0][0])
print(temp[0][1])
print(temp[1][0])
print(temp[1][1])

temp = [
    {"key": "value", "name" : "이름"},
    {"b" : "d", "aa" : "dd"}
]

print(temp[0]["name"])
