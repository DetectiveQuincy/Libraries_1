#--------------------------------------------------
# Name:        Import Assignment
# Purpose:
#
# Author:      kenny.coons
# From : Other > more_stuff
# Created:     28/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------

#---------------------Imports--------------------
import time

#------------------Lists and Dictionaries--------
breakfast_dictionary = {}

#------------------Functions--------------------
def add_items_b():
    stop = False
    while stop == False:
        items = input("what do you want to add to your breakfast list").lower()
        if items == "stop":
            stop = True
        elif items != "stop":
            value = input("how much of that would you like to add")
            print ("adding", value, items)
            breakfast[items] = value

def remove_items_b():
    stop = False
    while stop == False:
        items = input("what would you like to remove from your list").lower()
    if items == "stop":
        stop = True
    elif items != "stop":
        if items in breakfast:
            print ("removing", items)
            del breakfast[items]

def view_items_b():
    stop = False
    for(items, value) in breakfast.items():
        print ("You have", value, items, "in your list")

def main_b():
    play = 1
    print("Time to go shopping")
    while play == 1:
        time.sleep(1)
        choice = input("Would you like to add or remove items, view the list or stop?").lower()
        if choice == "add":
            add_items_b()
        elif choice == "remove":
            remove_items_b()
        elif choice == "view":
            view_items_b()
        elif choice == "stop":
            stop_stuff()
            play = 0
            print("dinner time")
        else:
            print("i am sorry, i didn't understand that")


#Main Code
main_b()


