class Student:
    def __init__(self,  name,  house):
        if not name :
            raise ValueError(" missing name")
        if house not in["azoz", "alamda", "altlatene", "alcom"]:
            raise ValueError ("invalid house")
        self.name = name
        self.house = house
        

def __str__(self):
    return f"{self.name} from {self.house}"


def main():
    student = get_student()          
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("name: ")
    student.house = input("house: ")
    return student

if __name__ == "__main__":
    main()