#!/usr/bin/python

import sys
import os
import sqlite3
import math
import usermenus

#User menu for python project

def main(conn):
    global c 
    usermenus.clearscreen()
    c = conn.cursor() #Create cursor to database
    while True:
        usermenus.printmainmenu()
        selection = input()
        if selection == '4':
            print("Goodbye!")
            return
        elif selection == '3':
            usermenus.clearscreen()
            usermenus.reactionmenu(c)
        elif selection == '2':
            usermenus.clearscreen()
            usermenus.compoundmenu(c)
        elif selection == '1':
            usermenus.clearscreen()
            usermenus.labmenu(c)
      #  else:
      #  	clearscreen()
      #      print("Unrecognized option!")

