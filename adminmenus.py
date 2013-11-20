#!/usr/bin/python

import math
import sys
import sqlite3
import os

def printmainmenu():
    print("##### ADMIN MODE ENABLED!! #####")
    print("################################")
    print("# Welcome to the Lab Database! #")
    print("################################\n")
    print("\t 1. Look up Labs")
    print("\t 2. Look up Compounds")
    print("\t 3. Look up Reactions")
    print("\t 4. Look up/edit inventory")
    print("\t 5. Look up Suppliers")
    print("\t 0. Exit")
    print("Please enter an option: ",end="")

def inventorymenu(c):
    while True:
        print("Would you like to view or edit the inventory?[v/e/c]")
        inp = input()
        if inp == "v":
            print_inventory(c)
        elif inp == "e":
            edit_inventory(c)
        elif inp == "c":
            return
        else:
            print("Unknown option!")


def print_inventory(c):
    c.execute("SELECT * FROM inventory")
    results = c.fetchall()
    
    #Fetch results
    amt = []
    units = []
    name = []
    casn = []

    amt += [x[0] for x in results]
    units += [x[1] for x in results]
    name += [x[2] for x in results]
    casn += [x[3] for x in results]
        
    #Print results
    print("\n Current inventory:")
    print("%20s | %8s | %10s"%("Name","CAS #","Amount")) 
    
    for j in range(len(amt)):
        print("%20s | %8s | %10s"%(name[j],casn[j],str(str(amt[j])+str(units[j]))))

def edit_inventory(c):
    print("Please enter a name or CAS# to edit:")
    compound = input()

    isCAS = True
    try:
        int(compound) #If we got a CAS#, this will work
    except ValueError:
        isCAS = False #If not, we got a name

    if isCAS:
        c.execute("SELECT * FROM inventory WHERE i_casn = ?",(compound,))
        tuple = c.fetchall()
        if [x[0] for x in tuple] == []:
            print("Compound not found!")
            return
        print("Current status:")
        print("Name: %s"%tuple[0][2])
        print("Amount: %s%s"%(tuple[0][0],tuple[0][1]))
        print("What is the new amount?")
        amount = input()
        try:
            int(amount)
        except ValueError:
            print("Error: Amount is not valid!")
            return
        c.execute("UPDATE inventory SET i_amount=? WHERE i_casn=?",(amount,compound))
        
        print("\n Inventory edited!")
    else:
        c.execute("SELECT * FROM inventory WHERE i_cname = ?",(compound,))
        tuple = c.fetchall()
        if [x[0] for x in tuple] == []:
            print("Compound not found!")
            return
        print("Current status:")
        print("Name: %s"%tuple[0][2])
        print("Amount: %s%s"%(tuple[0][0],tuple[0][1]))
        print("What is the new amount?")
        amount = input()
        try:
            int(amount)
        except ValueError:
            print("Error: Amount is not valid!")
            return
        c.execute("UPDATE inventory SET i_amount=? WHERE i_cname=?",(amount,compound))
        
        print("\n Inventory edited!")

    print("New inventory:")
    print_inventory(c)
    
