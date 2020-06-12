questions=["Who is Epictetus? ","Why are you studying philosophy? ","What are you doing now? ","Tell me what you hear: ","Tell me what you see: ","How are you a better man today? ",
           "What do you want to get out of your life?"]

import time,random

while True:
    for x in questions:
        print(random.choice(questions))
        input()
    
