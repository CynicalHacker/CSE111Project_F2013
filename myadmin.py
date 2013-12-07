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
    c = conn.cursor() #Create cursor to database
    while True:
        conn.commit()
        adminmenus.clearscreen()
        adminmenus.printmainmenu()
        selection = input()
        if selection == '0':
            print("Goodbye!")
            sys.exit(0)
        elif selection == '5':
            adminmenus.suppliermenu(c)
            continue
        elif selection == '4':
            adminmenus.inventorymenu(c)
            continue
        elif selection == '3':
            usermenus.reactionmenu(c)
        elif selection == '2':
            usermenus.compoundmenu(c)
        elif selection == '1':
            usermenus.labmenu(c)
        elif selection == 'moo':
            print("This program has no super cow powers. Sorry")
        else:
            print("Unrecognized option!")

        print("Hit ENTER to return to menu: ", end = "")
        placeholder = input()
