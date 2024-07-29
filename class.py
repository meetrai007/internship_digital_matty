"""create a dictonary to store detail of students"""

student_detail = {}


def store_detail(name, roll, course, age, gender, state, cast):
    """make a function to store all detail of students"""
    student_detail[name] = {
        "roll": roll,
        "course": course,
        "age": age,
        "gender": gender,
        "state": state,
        "cast": cast,
    }


"""make a dictnory to store name and rollno of students"""
student_rollno = {}


def store_roll(name, roll):
    """function to get data bfrom class and store in dictnory"""
    student_rollno[name] = roll


def roll(name):
    """create method to get roll no by name"""
    print(student_rollno[name])


class Students:
    """defining the class for students"""

    def __init__(self, name, rollno, age, cast, state="haryana", gender="male"):
        """initilaginng the perameters some defult or some input by user"""
        self.name = name
        self.rollno = rollno
        self.course = "python"
        self.age = age
        self.gender = gender
        self.state = state
        self.cast = cast
        store_roll(self.name, self.rollno)
        store_detail(
            name, self.rollno, self.course, self.age, self.gender, self.state, self.cast
        )

    # def roll(name):
    #     """create method to get roll no by name"""
    #     print(student_rollno[name])

    # def studentbygender(gen):
    #     for i in student_detail:
    #         if gen == student_detail[i]["gender"]:
    #             print(i)


s1 = Students("harmeet", 1, 21, "sc")
s2 = Students("akashdeep", 2, 18, "sc")
s3 = Students("amit", 3, 18, "sc")
s4 = Students("rani", 4, 19, "gernal", gender="female")

# """various way to find roll no  bu name"""
# print(student_rollno["harmeet"])
# print(student_detail)
# print(student_detail["harmeet"]["roll"])
# roll("harmeet")
# Students.roll("akashdeep")

# """way to find student by gender using studentbygender method in students class"""
# print(Students.studentbygender("male"))
# s = input()
# for i in list(student_detail.keys()):
#     if i == s:
#         print("user found")
#         break
#     print("user not found")

print(s1.rollno)