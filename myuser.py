#!/usr/bin/python

import sys
import os
import sqlite3
import math
import usermenus

#User menu for python project

def main(conn):
    global c 
    c = conn.cursor() #Create cursor to database
    while True:
        usermenus.printmainmenu()
        selection = input()
        if selection == '4':
            print("Goodbye!")
            sys.exit(0)
        elif selection == '3':
            usermenus.reactionmenu(c)
        elif selection == '2':
            usermenus.compoundmenu(c)
        elif selection == '1':
            usermenus.labmenu(c)
        else:
            print("Unrecognized option!")

