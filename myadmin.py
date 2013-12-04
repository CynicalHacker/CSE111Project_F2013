#!/usr/bin/python

import sys
import os
import sqlite3
import math
import usermenus
import adminmenus

#User menu for python project

global c

def main(conn):
    global c 
    usermenus.clearscreen()
    c = conn.cursor() #Create cursor to database
    while True:
        conn.commit()
        adminmenus.printmainmenu()
        selection = input()
        if selection == '0':
            print("Goodbye!")
            sys.exit(0)
        elif selection == '5':
            adminmenus.clearscreen()
            adminmenus.suppliermenu(c)
        elif selection == '4':
            adminmenus.clearscreen()
            adminmenus.inventorymenu(c)
        elif selection == '3':
            adminmenus.clearscreen()
            usermenus.reactionmenu(c)
        elif selection == '2':
            adminmenus.clearscreen()        
            usermenus.compoundmenu(c)
        elif selection == '1':
            adminmenus.clearscreen()        
            usermenus.labmenu(c)
        elif selection == 'moo':
            print("This program has no super cow powers. Sorry")
        else:
            clearscreen()
            print("Unrecognized option!")
