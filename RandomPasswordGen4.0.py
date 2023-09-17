from random import sample
import sys
import random as rd
clr = {"blue", "red", "yellow", "green", "purple", "violet", "black", "white", "brown", "orange", "pink", "gold",
       "silver", "bronze", "cyan", "grey", "tan", "copper", "olive", "indigo", "magenta", }
ani = {"cat", "dog", "cow", "sheep", "chicken", "pig", "snake", "horse", "bird", "octopus", "lion", "shark", "lizard",
       "frog", "bear", "fox", "goat", "donkey", "monkey", "fish", "tiger", "wolf", "dolphin", "whale", "deer",
       "mouse", "rabbit", "bull", "beetle", "spider", "penguin", "crocodile", "fox", "bat", "ant", "ram", "snail",
       "hawk", "scorpion", "liama", "butterfly", "fly", }

minlen = 16

clr1 = tuple(clr)
ani1 = tuple(ani)
clr2 = rd.sample(clr1, 1)
ani2 = rd.sample(ani1, 1)
pw = clr2+ani2
pw1 = str(pw)
len1 = len(pw1)
if len1 < minlen:
    clr2 = rd.sample(clr1, 1)
    ani2 = rd.sample(ani1, 1)
    pw = clr2+ani2
    pw1 = str(pw)
    len1 = len(pw1)
else:
    pw21 = pw1.replace('[', '')
    pw22 = pw21.replace(']', '')
    pw23 = pw22.replace(',', '')
    pw24 = pw23.replace(' ', '')
    pw25 = eval(pw24)

print(pw25)
