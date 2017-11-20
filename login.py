import db_setup
import getpass

def browse_credentials(table_name):
    try:
        data=[]
        con, cur = db_setup.get_connection("leave_management.db")
        query = "select * from {0}".format(table_name)
        cur.execute(query)
        data=cur.fetchall()
    except Exception as err:
        print err
    finally:
        cur.close()
        con.close()
    return data

def login():
    table_name="credentials"
    username = raw_input("username :")
    password = getpass.getpass("password :")
    data = browse_credentials(table_name)
    #print data
    for i in data:
        if username==i[0]:
            if password ==i[1]:
                print"Login successful"
                return 1
                break
            else:
                print"Incorrect password"
                return 0
                break
    else:
        print"Invalid Username"
        return 0

    
if __name__=="__main__":
    login_status = login()
    print login_status
