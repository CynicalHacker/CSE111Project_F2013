#!/usr/bin/python

import sys
import os
import sqlite3
import math

#User menu for python project

global c

def main(conn):
    global c 
    c = conn.cursor() #Create cursor to database
    while True:
        printmainmenu()
        selection = int(input())
        if selection == 4:
            print("Goodbye!")
            sys.exit(0)
        elif selection == 3:
            reactionmenu()
        elif selection == 2:
            compoundmenu()
        elif selection == 1:
            labmenu()
        else:
            print("Unrecognized option!")
        

def printmainmenu():
    print("################################")
    print("# Welcome to the Lab Database! #")
    print("################################\n")
    print("\t 1. Look up Labs")
    print("\t 2. Look up Compounds")
    print("\t 3. Look up Reactions")
    print("\t 4. Exit")
    print("Please enter an option: ",end="")

def labmenu():
    print("Which lab would you like to look up? ",end="") #Assemble all info before printing
    labnum = input() #Get lab number
    if labnum == "":
        print("Got invalid input!")
        return
    print("Retrieving data for Lab %s..."%labnum) 
    
    c.execute("SELECT DISTINCT l_title FROM lab WHERE l_num=(?)", (labnum,))
    labname=c.fetchone() #Get lab name

    if labname == None: #If we do not find the lab name, abort
        print("Lab %s not found!\n\n" % labnum)
        return
    
    c.execute("SELECT DISTINCT l_rname FROM lab WHERE l_num=(?)", [labnum]) #Get rxns
    reactionlist = [x[0] for x in c.fetchall()] #List comprehension to get results
    compoundlist = []
    casnlist = []
    hazlist = []

    if reactionlist != []: #reaction list is not empty, get compounds
        for rxn in reactionlist:
            c.execute("SELECT DISTINCT c_cname,c_casn,c_hazard FROM compound, reaction WHERE c_casn = r_casn AND r_rname = ?",[rxn])
            results = c.fetchall()
            compoundlist += [x[0] for x in results]
            casnlist += [x[1] for x in results]
            hazlist += [x[2] for x in results]

    #Now print out all our info:
    print("\n") #Clear above
    print("-------Information for Lab %s--------"%labnum)
    print("Title: %s" % labname)
    print("Reactions used:")
    for rxn in reactionlist:
        print("\t %s" % rxn)
    print("Compounds used:")
    print("\t CAS #       | Haz | Compound \t")
    print("\t------------------------------")
    for j in range(len(compoundlist)):
        print("\t %s %s | %s | %s" % (casnlist[j], (10 - len(str(casnlist[j])))*' ',hazlist[j], compoundlist[j]))
    print("\n\n") #Pad below so that we don't run right onto the menu
    return
            

def compoundmenu():
    print("Work in progress!")

def reactionmenu():
    print("Which reaction would you like to look up? ",end="") #Assemble all info before printing
    rxnname = input() #Get lab number
    if rxnname == "":
        print("Got invalid input!")
        return
    print("Retrieving data for %s..."%rxnnum)    

    c.execute("SELECT r_casn FROM reaction WHERE r_rname=(?)", [rxnname]) #Get CAS for compounds
    caslist = [x[0] for x in c.fetchall()] #List comprehension to get results

    if caslist == []: #If we do not find the reaction, exit
        print("Reaction not found!")
        return

    lablist = []
    compoundlist = []
    hazlist = []

    for cas in compoundlist:
        c.execute("SELECT DISTINCT c_cname,c_hazard FROM compound WHERE AND c_casn = ?",[comp])
        results = c.fetchall()
        compoundlist += [x[0] for x in results]
        hazlist += [x[1] for x in results]

    c.execute("SELECT l_title, l_num FROM lab WHERE l_rname=?",[rxnname])
    
    
