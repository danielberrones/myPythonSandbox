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

    # student A
    print(f"Student's Name: {aStudent.getName()}")
    print(aStudent.getQualityHours())
    print(aStudent.getQualityPoints())
    print(aStudent.gpa())
    
    # student B
    print(f"Student's Name: {bStudent.getName()}")
    print(bStudent.getQualityHours())
    print(bStudent.getQualityPoints())
    print(bStudent.gpa())


main()
