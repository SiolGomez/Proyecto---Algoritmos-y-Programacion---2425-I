class Nacionalidad:
    def __init__(self,nacionality):
        self.nacionality = nacionality

    def show(self):
        print(f"Nacionalidades: ")
        for nacionalidad in self.nacionality:
            print(f"{nacionalidad}")