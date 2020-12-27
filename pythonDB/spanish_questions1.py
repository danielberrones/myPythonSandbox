##### 3 spanish questions with while loops ######
########## created by daniel berrones 5/22/2019 ###########

import random, time
prompt = "\n>> "


def questions():
	i=0
	print("3 questions to the end.")
	time.sleep(2)
	print("Are you ready?")
	input(prompt)
	
	
	print("What's the future tense of the verb hacer in the 2nd person singular?")
	guess1=input(prompt)
	while guess1 != "harás":
		print("What's the future tense of the verb hacer in the 2nd person singular?")
		guess1=input(prompt)
		i += 1
	print("Good.  You earned 5 points")
	points=[]
	g1=5
	points.append(g1)
	
	
	print("What's the imperfect tense of the verb tocar in the 3nd person plural?")
	guess2=input(prompt)
	while guess2 != "tocaban":
		print("What's the imperfect tense of the verb tocar in the 3nd person plural?")
		guess2=input(prompt)
		i += 1
	print("Great.  You earned 10 points.  That's 15 total")
	g2=10
	points.append(g2)
	
	
	print("What's the subjunctive mood of the verb decir in the 1st person plural?")
	guess3=input(prompt)
	while guess3 != "digamos":
		print("What's the subjunctive mood of the verb decir in the 1st person plural?")
		guess3=input(prompt)
		i += 1
	print("Great.  You earned 15 points.  That's 30 total")
	g3=15
	points.append(g3)	
	
	print("\nHeres the list of points:")
	print(points)
	print("It took you {} total guesses to correctly answer 3 questions.".format(i))
	
	if i > 6:
		print("You are really slow, aren't you?")
	elif i == 5 or i == 4:
		print("Well, you could have been dumber, but you're okay... I guess")
	elif i == 3:
		print("You got a perfect score, hot shot!")
	
	
questions()