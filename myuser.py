#!/usr/bin/python

import sys
import os
import sqlite3
import math
import usermenus
import moo

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
#            usermenus.clearscreen()
            print("Unrecognized option!")
        
        print("Hit ENTER to return to menu: ", end = "")
        placeholder = input()
