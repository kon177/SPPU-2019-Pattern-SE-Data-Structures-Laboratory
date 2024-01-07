
"""In second year computer engineering class, group A student’s play cricket, 
    group B students play badminton and group C students play football.
    Write a Python program using functions to compute following: -
    a. List of students who play both cricket and badminton 
    b. List of students who play either cricket or badminton but not both
    c. Number of students who play neither cricket nor badminton 
    d. Number of students who play cricket and football but not badminton. (Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)"""

def crickandbad():
    l1=[]
    for i in crick:
        if i in bad:
            l1.append(i)
    print(l1)

def crickorbad():
    onlycrick=[]
    onlybad=[]
    for i in crick:
       if i not in bad:
        onlycrick.append(i)
    for j in bad:
        if j not in crick:
            onlybad.append(j)
    crickorbadList=onlycrick+onlybad
    print(crickorbadList)

def neicrickorbad():
    neicob=[]
    addcrickbad=crick+bad
    for i in clasS:
        if i not in addcrickbad:
            neicob.append(i)
    print(len(neicob)," Students Play Neither Cricket nor Badminton")
    print(neicob)

def crickandfootbnd():
    l2=[]
    for i in crick:
        if i in foot:
            l2.append(i)
    cafbnbad=[]
    for i in clasS:
        if i in l2 and i not in bad:
            cafbnbad.append(i)
    print(len(cafbnbad)," Students Play Cricket and FootBall But Not Badminton")
    print(cafbnbad)

def addname(n,name):
    for i in range(0,n):
        stuName=input("Enter Student Name(Press Enter After Entering Each Name): ")
        name.append(stuName)

def createList():
    global clasS,crick,foot,bad
    clasS=[]
    crick=[]
    foot=[]
    bad=[]
    n=int(input("Enter Total Student Count: "))
    addname(n,clasS)

    n=int(input("Count Of Students Who Play Football: "))
    addname(n,foot)

    n=int(input("Count Of Students Who Play Cricket: "))
    addname(n,crick)

    n=int(input("Count Of Students Who Play Badminton: "))
    addname(n,bad)

def opr():
    keys=[1,2,3,4,0]
    ch=1
    while True:
        print("OPERATIONS")
        print("1.List of Students Who Play Cricket And Badminton")
        print("2.List of Students Who Play Either Cricket Or Badminton But Not Both")
        print("3.Number of students who play neither cricket nor badminton")
        print("4.Number of students who play cricket and football but not badminton.")
        print("0.Quit")
        ch=int(input("Select An Operation: "))
        if ch==1:
            crickandbad()
        if ch==2:
            crickorbad()
        if ch==3:
            neicrickorbad()
        if ch==4:
            crickandfootbnd()
        if ch==0:
            print("Ended")
            break
        if ch not in keys:
            print("Invalid Key")
def menu():
    createList()
    opr()
menu()