import datetime

def leave():
    print("1.Apply leave \n2. Leave balances \n3.Pending requests")
    leave = raw_input("Select any:")
    if leave=="1":
        print("1.sick leave \n2.Casual leave \n3.Maternity leave \n4.Paternity leave")
        typeofleave = raw_input("Select type of leave:")
        from_date=raw_input("select from date(yyyy-mm-dd):")
        to_date=raw_input("Enter to date(yyyy-mm-dd):")
        l1=from_date.split('-')
        d1=datetime.date(int(l1[0]),int(l1[1]),int(l1[2]))
        l2=to_date.split('-')
        d2=datetime.date(int(l2[0]),int(l2[1]),int(l2[2]))
        no_of_days = str(d2-d1).split()[0]
        print no_of_days


if __name__ == "__main__":
    leave()                                                  
