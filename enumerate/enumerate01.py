temp = {"a", "b", "c"}
temp = enumerate(temp)

for num, value in temp:
    print(num, value)


a, b = {"name": "이름", "age": 12}.items()
print(a)
print(b)
print(a[1])
print(b[1])