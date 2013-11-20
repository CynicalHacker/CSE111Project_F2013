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
        adminmenus.printmainmenu()
        selection = input()
        if selection == '0':
            print("Goodbye!")
            sys.exit(0)
        elif selection == '5':
            adminmenus.suppliermenu(c)
        elif selection == '4':
            adminmenus.inventorymenu(c)
        elif selection == '3':
            usermenus.reactionmenu(c)
        elif selection == '2':
            usermenus.compoundmenu(c)
        elif selection == '1':
            usermenus.labmenu(c)
        else:
            print("Unrecognized option!")
