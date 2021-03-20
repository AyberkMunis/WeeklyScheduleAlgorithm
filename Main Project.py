from Classes import * #Importing our main class
a=class_name()
"""
The main purpose of this algorithm, placing names, which you typed, to a specific job on a randomly chosen day.  The algorithm assumes that a worker can only
do one duty on each day, so it restricts usage of the name more than one time for this day.

Problems are possible to face with
1.Infinite Loop
If the loop in classes is in an infinite loop, your condition must be impossible. You can check your condition and check again.
2.Don't Save the database
If you don't save the database, your algorithm should be crashed. Save your database and try again

---------The Main Process--------------
1. Selecting the job that you want to manage
2.If you have managed your database before, write the name you have typed before FOR THIS JOB(If you have typed any other names for other jobs, you will write them when you are editing these jobs)).
3.Writing new names 
4.Writing how many times a week will this person do this job 
5.Repeat this process until you have finished your list. 
6.If you have finished the list, press q and quit to the main menu
7.It is possible to choose another column and repeat this process
8.If you want to leave, type "bye" and press enter.

"""

while True:
    #Intro to user
    print(""" 
    Making Your Weekly Schedule
    1.Job1 (Type: 1 for this)
    2.Job2 (Type: 2 for this)
    3.Job3 (Type: 3 for this)
    4.Adding specific person to specific job at the day you want (Type: 4 for this)
    If you finish your list , please type q and press enter
    If you want to quit from the app, type bye and press enter (You must write this after 'Please write number of the job you want to manage')
    """)
    operation=input("Please write number of the job you want to edit:") #Selection of job that the user wants to manage

    if operation=="1" or operation=="Job1":

        jobs1 = []
        name = ""
        operation2 = input("Have you already added a name to jobs1(If you did write yes, else press enter):")
        if operation2.lower() == "yes":
            name = input("Please write his/her name:") #You type the name which you have already written manually, if you don't write something, you can press enter
        print("Now you write new people to job1")
        while True:
            people = input("Type name of the person:")
            if people.lower() == "q": #Breaks the selection loop when you write q
                break
            else:
                numberofjobs = int(input("Type how many days that you want to employ this person at job1:"))
                if numberofjobs == 1:
                    jobs1.append(people)
                else:
                    for i in range(numberofjobs): #This loop adds the name you have written to the list with the number of repetitions you wrote above.
                        jobs1.append(people)



        a.job1(jobs1,name)
    elif operation=="2" or operation=="Job2":

        jobs1 = []
        name=""
        operation2 = input("Have you already added a name to jobs2(If you did write yes, else press enter):")
        if operation2.lower()=="yes":
            name=input("Please write his/her name:")
        print("Now you write new people to job2")
        while True:
            people = input("Type name of the person:")
            if people.lower() == "q":
                break
            else:
                numberofjobs = int(input("Type how many days that you want to employ this person at job2:"))
                if numberofjobs==1:
                    jobs1.append(people)
                else:
                    for i in range(numberofjobs):
                        jobs1.append(people)



        a.job2(jobs1,name)
    elif operation=="3" or operation=="Jobs3":

        jobs1 = []
        name=""
        operation2 = input("Have you already added a name to jobs3(If you did write yes, else press enter):")
        if operation2.lower()=="yes":
            name=input("Please write his/her name:")
        print("Now you write new people to job3")
        while True:
            people = input("Type name of the person:")
            if people.lower() == "q":
                break
            else:
                numberofjobs = int(input("Type how many days that you want to employ this person at job3:"))
                if numberofjobs==1:
                    jobs1.append(people)
                else:
                    for i in range(numberofjobs):
                        jobs1.append(people)



        a.job3(jobs1,name)
    elif operation=="4":
        print("Which job do you want to manage 1,2,3?")
        job=input(":")
        name1=input("Please write his/her name?")
        day=input("Please write the day with number you want")
        a.specificday(name1,day,job)
    elif operation=="bye":
        break
