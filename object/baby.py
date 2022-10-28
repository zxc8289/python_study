class Baby:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print("응애")

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)


new_baby = Baby("김똘똘", 1)
new_baby.get_name()
new_baby.get_age()
