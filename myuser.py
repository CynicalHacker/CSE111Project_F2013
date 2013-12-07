#!/usr/bin/python

import sys
import os
import sqlite3
import math
import usermenus

#User menu for python project
#Calls 

def main(conn):
    global c 
    c = conn.cursor() #Create cursor to database
    while True:
        usermenus.clearscreen()
        usermenus.printmainmenu()
        selection = input()
        if selection == '0':
            print("Goodbye!")
            return
        elif selection == '3':
            #usermenus.clearscreen()
            usermenus.reactionmenu(c)
        elif selection == '2':
            #usermenus.clearscreen()
            usermenus.compoundmenu(c)
        elif selection == '1':
            #usermenus.clearscreen()
            usermenus.labmenu(c)
        else:
#            usermenus.clearscreen()
            print("Unrecognized option!")
        
        print("Hit ENTER to return to menu: ", end = "")
        placeholder = input()
