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
    print("\t 5. Look up/edit suppliers")
    print("\t 0. Exit")
    print("Please enter an option: ",end="")
    
def suppliermenu(c):
    while True:
        print("Would you like to view or edit the supplier list?[v/e/c]")
        inp = input()
        if inp == "v":
            print_supplist(c)
        elif inp == "e":
            edit_supplist(c)
        elif inp == "c":
            return
        else:
            clearscreen()
            printmainmenu()
            print("Unknown option!")
            suppliermenu(c)
            return
        print("Hit ENTER to continue: ", end = "")
        placeholder = input()
        clearscreen()
        printmainmenu()
        print("")

def inventorymenu(c):
    while True:
        print("Would you like to view or edit the inventory?[v/e/c] ",end="")
        inp = input()
        if inp == "v":
            print_inventory(c)
        elif inp == "e":
            edit_inventory(c)
        elif inp == "c":
            return
        else:
            clearscreen()
            printmainmenu()
            print("Unknown option!")
            suppliermenu(c)
            return
        print("Hit ENTER to continue: ", end = "")
        placeholder = input()
        clearscreen()
        printmainmenu()
        print("")
        

def print_supplist(c):
    
    c.execute("SELECT * FROM supplier")
    results = c.fetchall()
    
    #Fetch results
    name = []
    phonen = []
    country = []

    name += [x[0] for x in results]
    phonen += [x[1] for x in results]
    country += [x[2] for x in results]
        
    #Print results
    print("\n Current suppliers:")
    print("%30s | %11s | %11s"%("Name","Phone","Country")) 
    print("----------------------------------------------------------")
    
    for j in range(len(name)):
        print("%30s | %11s | %11s"%(name[j],phonen[j],country[j]))
        
def edit_supplist(c):
    print("Please enter a supplier name to edit: ",end="")
    name = input()
    c.execute("SELECT * FROM supplier WHERE s_sname = ?",(name,))
    tuple = c.fetchall()

    if [x[0] for x in tuple] == []: #We did not find the supplier. Add a new one
        print("Supplier not found! Add to inventory?[y/n] ",end="")
        if input() == "n":
            return #Do not add supplier, return to suppliermenu
        print("Please enter the phone number: ",end="")
        phonen = input()
        print("Please enter the country: ",end="")
        country = input()
        try:
            c.execute("INSERT INTO supplier VALUES (?,?,?)",(name, phonen, country))
            print("\n Inventory edited!")
        except sqlite3.OperationalError:
            print("Something is wrong with the supplied values. Aborting.")
        finally:
            return
    
    #If the supplier was found in the database:
    #Print status of supplier for reference
    print("Current status:")
    print("Name: %s"%tuple[0][0])
    print("Phone Number: %s"%(tuple[0][1]))
    print("Country: %s"%(tuple[0][2]))

    print("\nPlease enter the new phone number (blank to leave unchanged): ", end="")
    phonen = input()
    print("Please enter the new country (blank to leave unchanged): ", end="")
    country=input()
    
    if country == "" and phonen == "":
        print("Database unchanged.")
        return
    elif country =="":
        c.execute("UPDATE supplier SET s_phonenum=? WHERE s_sname=?",(phonen,tuple[0][0]))
    elif phonen=="":
        c.execute("UPDATE supplier SET s_location=? WHERE s_sname=?",(country,tuple[0][0]))
    else:
        c.execute("UPDATE supplier SET s_phonenum=?,s_location=?, WHERE s_sname=?",(phonen,country,tuple[0][0]))
        
    print("\n Supplier list edited!")

    print_supplist(c)
    return    
    
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
    print("-----------------------------------------------")
    
    for j in range(len(amt)):
        print("%20s | %8s | %10s"%(name[j],casn[j],str(str(amt[j])+str(units[j]))))

def edit_inventory(c):
    print("Please enter a compound to edit: ",end="")
    compound = input()

    isCAS = True
    try:
        int(compound) #If we got a CAS#, this will work
    except ValueError:
        isCAS = False #If not, we got a name

    if isCAS:
        c.execute("SELECT * FROM inventory WHERE i_casn = ?",(compound,)) #Is it in the DB?
        tuple = c.fetchall()
        if [x[0] for x in tuple] == []: #Compound not found in database
            print("Compound not found! Add to inventory?[y/n] ",end="")
            if input() == "n":
                return #Do not want to add compound. Return to inventorymenu
            print("Please enter the name of the compound: ",end="")
            cname = input()
            print("Please enter the units of measure [g/L]: ",end="")
            units = input()
            print("Please enter the amount: ",end="")
            amount = input()
            try:
                int(amount)
                c.execute("INSERT INTO inventory VALUES (?,?,?,?)",(amount,units,cname,compound))
                print("\n Inventory edited!")
            except sqlite3.OperationalError:
                print("Something is wrong with the supplied values. Aborting.")
            except ValueError:
                print("Error: Need numeric values for amount.")
            finally:
                return

        #Here, we found the compound. Print its status for reference
        print("Current status:")
        print("Name: %s"%tuple[0][2])
        print("Amount: %s%s"%(tuple[0][0],tuple[0][1]))
        print("What is the new amount?", end="")
        amount = input()
        try:
            int(amount)
        except ValueError:
            print("Error: Amount is not valid!")
            return
        c.execute("UPDATE inventory SET i_amount=? WHERE i_casn=?",(amount,compound))
        
        print("\n Inventory edited!")
        
    #Evetything in this else clause is a mirror of the if above, using names instead of CAS#
    else: #IS NOT CAS
        c.execute("SELECT * FROM inventory WHERE i_cname = ?",(compound,))
        tuple = c.fetchall()
        if [x[0] for x in tuple] == []:
            print("Compound not found! Add to inventory?[y/n] ",end="")
            if input() == "n":
                return
            print("Please enter the CAS # of the compound: ",end="")
            casno = input()
            print("Please enter the units of measure [g/L]: ",end="")
            units = input()
            print("Please enter the amount: ",end="")
            amount = input()
            try:
                int(casno)
                int(amount)
                c.execute("INSERT INTO inventory VALUES (?,?,?,?)",(amount,units,compound,casno))
                print("\n Inventory edited!")
            except sqlite3.OperationalError:
                print("Something is wrong with the supplied values. Aborting.")
            except ValueError:
                print("Error: Need numeric values for CAS # and amount.")
            finally:
                return
        print("Current status:")
        print("Name: %s"%tuple[0][2])
        print("Amount: %s%s"%(tuple[0][0],tuple[0][1]))
        print("What is the new amount?", end="")
        amount = input()
        try:
            int(amount)
        except ValueError:
            print("Error: Amount is not valid!")
            return
        c.execute("UPDATE inventory SET i_amount=? WHERE i_cname=?",(amount,compound))
        
        print("\n Inventory edited!")

    print_inventory(c)
    
def clearscreen(): #CLEAR!!
	os.system('cls' if os.name=='nt' else 'clear')
    
