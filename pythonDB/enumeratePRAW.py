import tkinter as tk
import praw


reddit = praw.Reddit(
    client_id='xZHnziUldeZEbg',
    client_secret="P52m77JjNefq4-XVyLEsrkaPGS8",
    user_agent='carldangerAPI33',
)

userInput = input("Enter a SubReddit: ")

sub = reddit.subreddit(userInput)

hotTitle, hotURL, hotID, hotScore = [i.title for i in sub.hot(limit=10)],[i.url for i in sub.hot(limit=10)],[i.id for i in sub.hot(limit=10)],[i.score for i in sub.hot(limit=10)]

newTitle, newURL, newID, newScore = [i.title for i in sub.new(limit=10)],[i.url for i in sub.new(limit=10)],[i.id for i in sub.new(limit=10)],[i.score for i in sub.new(limit=10)]

for i, y in enumerate(zip(hotTitle, hotURL, hotID, hotScore)):
    print("SORTED BY: HOT ".center(40, "*"))
    print("hotTitle", "hotURL", "hotID", "hotScore")
    print(i, y, '\n\n\n')

for i, y in enumerate(zip(newTitle, newURL, newID, newScore)):
    print("SORTED BY: NEW ".center(40, "*"))
    print("newTitle", "newURL", "newID", "newScore")
    print(i, y, '\n\n\n')


