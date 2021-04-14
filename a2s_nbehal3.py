#!/usr/bin/env python3
from fabric.api import *

env.user = 'student'

def addUser(Username):
    '''This function takes in one argument and stores the run implementation of fabric into a variable - it will utilize the sudo function to add a user'''
    
    aU = run("sudo useradd " + username)
    
def FindUser(Username):
    
    '''This function takes in one argument and stores the run implementation of fabric into a variable 
    - it then uses an if loop to check/confirm if the output 
    of the command run in the first place exactly matches the username or not and if it does it prints the success statement'''
    
    cmd = run("cat /etc/passwd | grep" + Username + '| cut -d: -f1')
    if cmd == Username:
        return("Found User "+ Username +" On the system")
    else:
        return("User " + Username + "is not on the system")
        
def listSysUser():
    '''This function takes in no argument and stores the run implementation of fabric of /etc/passwd file : 
    which stores the names of all the users into a variable - it then implements a splitline 
    function seperated by a \n i.e newline character'''
    listS = []
    SU = run("cat /etc/passwd " + "| " + "awk -F: '{print $1}'")
    SUV = SU.splitline("\n")
    print (SUV)
    
def listUser():
    '''This function takes in no argument and stores the run implementation of fabric of /etc/passwd file : 
    which stores the names of all the users into a variable - it then greps the output to find users that have a 
    home directory meaning those users which have a home directory i.e System Users'''
    
    LU = run("cat /etc/passwd " + "| " + " grep '/home' " + "| " + "cut -d: -f1")
    LUV = LU.splitline("\n") 
    print (LUV)      
        
        
