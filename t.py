import re
import bs4
import requests
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import sys
import time


def n():
    'print 30 new lines'
    print("\n"*30)

n()

# re
# pattern = "...a$"
# testString = "casa"
# testString1 = "taza"

# outcome = re.match(pattern,testString)
# outcome1 = re.match(pattern,testString1)
# print(outcome)
# print(outcome1)

r = requests.get('https://api.github.com/events')


