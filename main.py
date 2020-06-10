class Student:
    def __init__(self,name,qhours,qpoints):
        self.name=name
        self.qhours=qhours
        self.qpoints=qpoints
    def getName(self):
        return self.name
    def getQualityHours(self):
        return self.qhours
    def getQualityPoints(self):
        return self.qpoints
    def gpa(self):
        return self.qpoints/self.qhours


def main():
    aStudent = Student("Mark Williams",33,89)
    bStudent = Student("Jeb Doe",66,150)

    print(aStudent.getName())
    print(bStudent.getName())

    print(aStudent.getQualityHours())
    print(bStudent.getQualityHours())

    print(aStudent.getQualityPoints())
    print(bStudent.getQualityPoints())

    print(aStudent.gpa())
    print(bStudent.gpa())


main()
