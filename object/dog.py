from animal import Animal


class Dog(Animal):
    count = 0

    def __init__(self, name: str = "멍뭉이", age: int = 0):

        super().__init__(age)

        self.name = name

        Dog.count = Dog.count + 1

        return

    def eat(self):
        print(f"개 '{self.name}'이(가) 음식을 먹었습니다.")

    @classmethod
    def get_count(cls):
        print(f"개 {cls.count}마리 생성되었습니다.")
