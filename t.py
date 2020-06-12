class Student:
    def __init__(self,name,qPoints,qHours):
        self.name = name
        self.qPoints = qPoints
        self.qHours = qHours
    def getName(self):
        return self.name
    def getQualityPoints(self):
        return self.qPoints
    def getQualityHours(self):
        return self.qHours
    def gpa(self):
        return self.qPoints/self.qHours
    


