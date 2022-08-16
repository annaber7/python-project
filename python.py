import pickle

lstPay=[]

class Employee (object):
    """This is a class used to create Employee Objects"""

    ####Constructor Method for class
    def __init__(self, Name="", Hours=0, Wage=0.0):  #keywords Name, Hours, Wage, and Full Name

        self.employeeName = Name.title( )  #set Name to what is passed in
        self.employeeHours = int(Hours)   #set Hours to what is passed in  
        self.employeeWage = float(Wage)  


        print( )
        print("Employee Object Created: ")
        print ("Employee Name:", self.employeeName)
        print ("Employee Hours:", self.employeeHours)
        print ("Employee Wage:", self.employeeWage)
        print ( )

    def __str__(self):
        strEmployee = self.employeeName + " " + str(self.employeeHours) + " " + str(self.employeeWage)
        return strEmployee


    #########Method for calculating pay
    def Emppay(self):
        if self.employeeHours<41:
            pay=self.employeeHours*self.employeeWage
        else:
            pay=(self.employeeHours-40)*(self.employeeWage*1.5)+(self.employeeWage*40)
        return pay


##############Mainline################

blnDone=False

while blnDone==False:
    strName = input("Enter employee's first and last name (or press ENTER when done): ")   ##SCD
    if len(strName)>0:
        intHours = 0
        while intHours < 1 or intHours > 60:
            intHours = int(input("Enter employee's hours this week: "))
            if intHours < 1  or intHours > 60:
                print("Hours invalid, please re-enter: ")


        intWage = 0
        while intWage <1 or intWage > 20:
            intWage = float(input("Enter employee's hourly wage: "))
            if intWage <1 or intWage > 20:
                print("Hours invalid, please re-enter: ")
    
        objEmployee = Employee(Name=strName, Hours=intHours, Wage=intWage)

        print(objEmployee)

        fltPay = objEmployee.Emppay()
        lstPay.append(fltPay)
    else:
        blnDone=True
        print("List of employees' pay: ", lstPay)
        

#############dumping list to file#########
try:
    filList=open("Payroll.dat", "wb")
    pickle.dump(lstPay, filList)
    filList.close()
except(IOError):
    print("Error writing lstPay to file")
    quit()

########load into lstWkPay##############
try:
    filList=open("Payroll.dat", "rb")
    lstWkPay=pickle.load(filList)
    filList.close()
except(IOError):
    print("Error loading list")
    quit()

#####Sorting lstWkPay####

def Low(pay = [ ]): #finding lowest pay
    pay.sort( )
    return pay[0]

def High(pay =[ ]): #finding highest pay
    pay.sort( )
    pay.reverse( )
    print("The highest pay is: ", pay[0])

def Avg(pay =[ ]): #finding average pay
    intTotal=0
    for num in pay:
        intTotal+=num
    fltAvg=intTotal/len(pay)
    print("Average score is", fltAvg)

######mainline########
fltPay = Low(pay=lstWkPay)
print("The lowest pay is: ", fltPay)
High(pay=lstWkPay)
Avg(pay=lstWkPay)
