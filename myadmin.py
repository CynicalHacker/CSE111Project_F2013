#!/usr/bin/python

import sys
import os
import sqlite3
import math
import usermenus
import adminmenus
import moo

#User menu for python project

global c
global mooct #counter for mooct

def main(conn):
    global c
    global mooct
    mooct = 0
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
            if mooct==0:
                print("This program has no super cow powers. Sorry")
                mooct += 1
            elif mooct==1:
                print("There are no super cow powers in this program!")
                mooct += 1
            elif mooct==2:
                print("I swear, there are no cow powers here")
                mooct += 1
            elif mooct==3:
                print("Additional moos may cause the program to terminate unexpectedly. Please, think of the children!")
                mooct += 1
            else:
                moo.moo()
                sys.exit(0)
        else:
            print("Unrecognized option!")

        print("Hit ENTER to return to menu: ", end = "")
        placeholder = input()
