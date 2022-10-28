import imp
from animal import Animal
from cat import Cat
from dog import Dog
Animal.hello()

print()

a = Animal(12)
b = Cat("나옹", 5)
c = Dog("멍뭉이", 7)

a.eat()
b.eat()
c.eat()

print()

a.get_age()
b.get_age()
c.get_age()

print()

Animal.get_count()
Cat.get_count()
Dog.get_count()

# 동물 농장에 오신 것을 환영합니다.

# 동물 0번이 음식을 먹었습니다.
# 고양이 '나옹'이 음식을 먹었습니다.

# 동물 '0번'의 나이는 12살 입니다.
# 동물 '나옹'의 나이는 5살 입니다.

# 동물이 2마리 생성되었습니다.
# 고양이가 1마리 생성되었습니다.
