import json
class Student(object):

    # Constructor
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

    # To get name
    def getName(self):
        return self.name
    # To get name
    def getSubject(self,name):
        return self.subjects

    # To check if this person is an employee
    def isSpecialized(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class PyhtonSpecialist(Student):
    # Here we return true
    def isSpecialized(self):
        return True

class DataSpecialist(Student):
    # Here we return true
    def isSpecialized(self):
        return True

class DataScienceSpecialist(Student):
    # Here we return true
    def isSpecialized(self):
        return True

# Driver code
student = Student("Neha",30,1010101)  # An Object of Student
subjects = {
  "Subject 1": "Math",
  "Subject 2": "Science",
  "Subject 2": "English",
}
student.subjects = subjects
print(student.getName(), student.isSpecialized(),json.dumps(student.subjects, indent=3))

pythonSpecialist = PyhtonSpecialist("Jack",40,1010102)  # An Object of PyhtonSpecialist
subjects = {
  "Subject 1": "Pyhton",
  "Subject 2": "Web Programming",
  "Subject 2": "Troubleshooting",
}
pythonSpecialist.subjects = subjects
print(pythonSpecialist.getName(), pythonSpecialist.isSpecialized(), json.dumps(pythonSpecialist.subjects, indent=3))

dataSpecialist = DataSpecialist("Alex",50,1010103)  # An Object of DataSpecialist
subjects = {
  "Subject 1": "SQL Progrmming",
  "Subject 2": "Sql dministrator",
  "Subject 2": "DB Management",
}
dataSpecialist.subjects = subjects
print(dataSpecialist.getName(), dataSpecialist.isSpecialized(), json.dumps(dataSpecialist.subjects, indent=3))

dataScienceSpecialist = DataScienceSpecialist("Luka", 60,1010104)  # An Object of DataScienceSpecialist
ubjects = {
  "Subject 1": "Supervise Learning",
  "Subject 2": "Unsupervise Lerning",
  "Subject 2": "Machine Learning",
}
dataScienceSpecialist.subjects = subjects
print(dataScienceSpecialist.getName(), dataScienceSpecialist.isSpecialized(), json.dumps(dataScienceSpecialist.subjects, indent=3))