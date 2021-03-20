import _sqlite3
from random import *

def tuppletolist(tupple): #This custom function converts a tupple to a list
    liste2=[]
    for t in tupple:
        for item in t:
            liste2.append(item)
    return liste2

days=['1','2','3','4','5'] #A single number represents a day of a week. Ex:1 is Monday


class class_name(): #Our main class
    def __init__(self):
        self.connection()
    def connection(self):#Supplies the connection between the database and our code
        self.con2=_sqlite3.connect("table.db")
        self.crs=self.con2.cursor()
        self.con2.commit()
    def breakconnection(self): #Destroy the connection
        self.con2.close()
    def job1(self,listjob1,name): #This is our main function because the other functions are a copy of this
        query1 = "Update Jobs set Job1=? where Days=? "
        query2 = "Select Days From Jobs where Job1=? "#Taking the day of the name which is written before by the user
        self.crs.execute(query2, (name,))
        tuppleofname = self.crs.fetchall()
        listofname = tuppletolist(tuppleofname)#Converting tupple ,which contains the days of given name, to a list
        for i in listofname:
            i2 = str(i)
            days.remove(i2) #Removing these days from our main "days" list because if we didn't make this,
            # our function could change the value of this day with a different name we wrote during Main Project section
        while True:
            query3 = "Select Job1 From Jobs"
            self.crs.execute(query3)
            listofjob1 = self.crs.fetchall()
            listofjob1list = tuppletolist(listofjob1)
            res = list(filter(None, listofjob1list))
            shuffle(days) #Shuffling days list because if it is not shuffled, function would always give the same result.

            if len(res) == 5: #The function ends when length of the list of column job1 equals to 5. Because it means all days are filled
                break

            else:
                for i, j in zip(listjob1, days):#Matching remaining days with a person in the given list
                    query4 = "Select Job1 from Jobs" #Taking all data in the database
                    self.crs.execute(query4)
                    liste3 = self.crs.fetchall()
                    liste4 = tuppletolist(liste3)

                    query5 = "Select *  from Jobs where Days=?" #Taking data of the row which contains selected day
                    self.crs.execute(query5, (j,))
                    liste5 = self.crs.fetchall()
                    liste6 = tuppletolist(liste5)
                    if liste6.count(i) < 1 and liste4.count(i) != listjob1.count(i):
            #Writing a name from the list to matched day, if this name has not been written on selected day to an another job
                        self.crs.execute(query1, (i, j))
                        self.con2.commit()
                    else:
                        #If this condition didn't supply, the loop would continue until finding an appropriate situation.
                        #The algorithm tries different names with different days until finding a suitable situation
                        # Moreover, if nothing is written on the screen, the loop could be in a infinite loop, you should check the condition and try again.
                        continue
    def job2(self,listjob2,name):
        query1 = "Update Jobs set Job2=? where Days=? "
        query2 = "Select Days From Jobs where Job2=? "
        self.crs.execute(query2, (name,))
        tuppleofname = self.crs.fetchall()
        listofname = tuppletolist(tuppleofname)
        for i in listofname:
            i2 = str(i)
            days.remove(i2)
        print(days)
        while True:
            query3 = "Select Job2 From Jobs"
            self.crs.execute(query3)
            listofjob1 = self.crs.fetchall()
            listofjob1list = tuppletolist(listofjob1)
            res = list(filter(None, listofjob1list))
            shuffle(days)

            if len(res)==5:
                break

            else:
                for i,j in zip(listjob2,days):
                    query4 = "Select Job2 from Jobs"
                    self.crs.execute(query4)
                    liste3 = self.crs.fetchall()
                    liste4 = tuppletolist(liste3)

                    query5 = "Select *  from Jobs where Days=?"
                    self.crs.execute(query5, (j,))
                    liste5 = self.crs.fetchall()
                    liste6 = tuppletolist(liste5)
                    if liste6.count(i)<1 and liste4.count(i)!=listjob2.count(i):
                        self.crs.execute(query1, (i,j))
                        self.con2.commit()
                    else:
                        continue
    def job3(self,listjob3,name):
        query1 = "Update Jobs set Job3=? where Days=? "
        query2 = "Select Days From Jobs where Job3=? "
        self.crs.execute(query2, (name,))
        tuppleofname = self.crs.fetchall()
        listofname = tuppletolist(tuppleofname)
        for i in listofname:
            i2 = str(i)
            days.remove(i2)
        print(days)
        while True:
            query3 = "Select Job3 From Jobs"
            self.crs.execute(query3)
            listofjob1 = self.crs.fetchall()
            listofjob1list = tuppletolist(listofjob1)
            res = list(filter(None, listofjob1list))
            shuffle(days)

            if len(res) == 5:
                break

            else:
                for i, j in zip(listjob3, days):
                    query4 = "Select Job3 from Jobs"
                    self.crs.execute(query4)
                    liste3 = self.crs.fetchall()
                    liste4 = tuppletolist(liste3)

                    query5 = "Select *  from Jobs where Days=?"
                    self.crs.execute(query5, (j,))
                    liste5 = self.crs.fetchall()
                    liste6 = tuppletolist(liste5)
                    if liste6.count(i) < 1 and liste4.count(i) != listjob3.count(i):
                        self.crs.execute(query1, (i, j))
                        self.con2.commit()
                    else:
                        continue
    def specificday(self,name,day,job):
        #This function places specific name which the user typed to a specific location(day,job)
        if job=="1":
            query1 = "Update Jobs set Job1=? where Days=? "
            self.crs.execute(query1,(name,day))
            self.con2.commit()
        elif job=="2":
            query1 = "Update Jobs set Job2=? where Days=? "
            self.crs.execute(query1,(name,day))
            self.con2.commit()
        elif job=="3":
            query1 = "Update Jobs set Job1=? where Days=? "
            self.crs.execute(query1,(name,day))
            self.con2.commit()
