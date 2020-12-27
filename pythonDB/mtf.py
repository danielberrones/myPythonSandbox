crReq=float(input("CREDITS REQUIRED? "))
crEar=float(input("CREDITS EARNED? "))
crAtt=float(input("CREDITS ATTEMPTED? "))

mtf=crReq*1.5
float(mtf)
crRemaining=crReq-crEar

print("MTF: "+str(mtf)+"CREDITS")

if crRemaining+crAtt>=mtf:
    print("Stu has exceeded MTF")
else:
    print("Stu is OK!")






