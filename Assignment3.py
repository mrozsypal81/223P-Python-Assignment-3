

import pandas as pd

class Course:
    def __init__(self, id, cname, desc):
        #Attributes
        self._id = id
        self._courseName = cname
        self._courseDesc = desc
        #Attributes

        #1-m relationship
        self._enrollment = list()
        #1-m relationship

    #Not sure if this is needed wording on assignment is vague
    def save(self):
        #Course.csv 
        try:
            df = pd.read_csv('Course.csv')
            #Apply the same 'update object' logic here 
            
            cnt = len(df.index)
            print('+++ Appending to the DataFrame +++', df.index, df)
            df.loc[cnt] = {'ID':self._id, 'Course_Name': self._courseName,'Description': self._courseDesc}
        except:
            print('+++ Creating a new DataFrame +++')
            df = pd.DataFrame([[self._id, self._courseName, self._courseDesc]], columns=['ID', 'Course_Name','Description'])
        df.to_csv('Course.csv', index=False)

    

class ClassEnrollment:
    def __init__(self, id, g):
        #Attributes
        self._id = id
        self._grade = g
        #Attributes

        #1-m relationship
        self._student = None
        self._course = None
        #1-m relationship

    def delete(self):
        # first find the row index of this object
        df = pd.read_csv('ClassEnrollment.csv')
        row = df[df.ID == self._id]
        print('+++ delete +++' , row.index[0])
        if (len(row.index) != 0):
            print('+++ Before ', df)
            df.drop(row.index[0], inplace=True)
            print('+++ After ', df)
            df.to_csv('ClassEnrollment.csv', index=False)

    def save(self):
        # ClassEnrollment.csv 
        try:
            df = pd.read_csv('ClassEnrollment.csv')
            #Apply the same 'update object' logic here 
            
            cnt = len(df.index)
            print('+++ Appending to the DataFrame +++', df.index, df)
            df.loc[cnt] = {'ID':self._id, 'Grade': self._grade}
        except:
            print('+++ Creating a new DataFrame +++')
            df = pd.DataFrame([[self._id, self._grade]], columns=['ID', 'Grade'])
        df.to_csv('ClassEnrollment.csv', index=False)

        if(self._course != None):
             self._course.save()
    
class Student:
    def __init__(self, c, f, l):
        #Attributes
        self._cwid = c
        self._firstname = f
        self._lastname = l
        #Attributes

        #1-m relationship
        self._enrollments = list()
        #1-m relationship

    def enroll2Class(self,Enclass):
        self._enrollments.append(Enclass)

    def delete(self):
        # first find the row index of this object
        df = pd.read_csv('Student.csv')

        #Convert int to string
        i = int(self._cwid)
        row = df[df.CWID == i]
        print(row)
        print('+++ delete +++' , row.index[0])
        if (len(row.index) != 0):
            print('+++ Before ', df)
            df.drop(row.index[0], inplace=True)
            print('+++ After ', df)
            df.to_csv('Student.csv', index=False)

    def save(self):
        # Student.csv 
        try:
            df = pd.read_csv('Student.csv')
            #Apply the same 'update object' logic here 
            
            cnt = len(df.index)
            print('+++ Appending to the DataFrame +++', df.index, df)
            df.loc[cnt] = {'CWID':self._cwid, 'FName': self._firstname,'LNAME': self._lastname}
        except:
            print('+++ Creating a new DataFrame +++')
            df = pd.DataFrame([[self._cwid, self._firstname, self._lastname]], columns=['CWID','FName','LName'])
        df.to_csv('Student.csv', index=False)
        for o in self._enrollments:
            o.save()

    #The specifications for the implementation of this method is quite vague
    #The current version returns the student object and all immediate associated data with that student
    #This includes the cwid, fname,lname,their classes, with class ids, with class grades
    def retrieveByCWID(self):
        print("Getting student Object")
        studentdata = list()
        studentdata.append(self)
        for i in self._enrollments:
            studentdata.append(i)
        return studentdata


############## TEST DATA ####################


#Creation of students
A = Student("1","Mike1","Rozy1")
B = Student("2","Mike2","Rozy2")
C = Student("3","Mike3","Rozy3")

#Creation of different Classes
C1 = Course("C1","Course1","Coursedesc1")
C2 = Course("C2","Course2","Coursedesc2")
C3 = Course("C3","Course3","Coursedesc3")

#Creation of different enrollments and grades
CE1 = ClassEnrollment("CE1","Grade1")
CE2 = ClassEnrollment("CE2","Grade2")
CE3 = ClassEnrollment("CE3","Grade3")

CE4 = ClassEnrollment("CE1","Grade4")
CE5 = ClassEnrollment("CE2","Grade5")
CE6 = ClassEnrollment("CE3","Grade6")

CE7 = ClassEnrollment("CE1","Grade7")
CE8 = ClassEnrollment("CE2","Grade8")
CE9 = ClassEnrollment("CE3","Grade9")

#These show saving of one student and ClassEnrollment as basic objects
#A.save()
#CE1.save()


#Assigning Students to each enrollment 
CE1._student = A
CE2._student = A
CE3._student = A

CE4._student = B
CE5._student = B
CE6._student = B

CE7._student = C
CE8._student = C
CE9._student = C


#Assigning Courses to each enrollment
CE1._course = C1
CE2._course = C2
CE3._course = C3

CE4._course = C1
CE5._course = C2
CE6._course = C3

CE7._course = C1
CE8._course = C2
CE9._course = C3


#Adding enrollment to the courses
C1._enrollment.append(CE1)
C1._enrollment.append(CE4)
C1._enrollment.append(CE7)

C2._enrollment.append(CE2)
C2._enrollment.append(CE5)
C2._enrollment.append(CE8)

C3._enrollment.append(CE3)
C3._enrollment.append(CE6)
C3._enrollment.append(CE9)

#Adding enrollment to the student objects
A.enroll2Class(CE1)
A.enroll2Class(CE2)
A.enroll2Class(CE3)

B.enroll2Class(CE1)
B.enroll2Class(CE2)
B.enroll2Class(CE3)

C.enroll2Class(CE1)
C.enroll2Class(CE2)
C.enroll2Class(CE3)


#Every save after the first one loses the last name for some reason
#This is copied almost directly from notes
A.save()
B.save()
C.save()


#Will delete the student will not delete their enrollment records or courses
#There is a delete method for Enrollment that must be used separately
A.delete()


#This is the method to get the student object and the objects that are related to it 
# They are then printed out to console
X = A.retrieveByCWID()

print(X[0]._cwid)
print(X[0]._firstname)
print(X[0]._lastname)
print(X[1]._id)
print(X[1]._grade)
print(X[2]._id)
print(X[2]._grade)
print(X[3]._id)
print(X[3]._grade)




