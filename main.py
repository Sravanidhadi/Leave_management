import calendar
from tabulate import tabulate
def main():
    print ("1.Holidays list \n2.Calendar \n3.Leave")
    select=raw_input("select anyone:")
    if int(select)==1:
        print tabulate([['14/01/2018','Pongal'],['26/01/2018','Republic day'],['13/02/2018','Sivarathri'],['18/03/2018','Ugadi'],['15/08/2018','Independence day'],['13/09/2018','Ganesh chathurthu'],['25/12/2018','Christmas']],headers=['Date','Holiday'],tablefmt='orgtbl')
        #print "Holidays list"
    elif select=="2":
        year=int(input("Enter year:"))
        month=int(input("Enter month:"))
        print(calendar.month(year,month))
    elif select=="3":
        print "Leave"
if __name__=="__main__":
    main()
