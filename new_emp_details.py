import db_setup
def insert_data(query):
    try:
        con, cur=db_setup.get_connection("leave_management.db")
        #for i in range(300):
        #q="insert into credentials values('nex0288','sravani288')"
        cur.execute(query)        
    except Exception as err:
        print err
    else:
        print "commiting data"
        con.commit()
    finally:
        cur.close()
        con.close()

if __name__=="__main__":
    while True:
        username = raw_input("enter username: ")
        if username:
            password = raw_input("enter password: ")
            query = "insert into credentials values ('{0}', '{1}')".format(username,password)
            insert_data(query)
        else:
            break
