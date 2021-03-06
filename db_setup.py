import sqlite3
def get_connection(a):
    database=a
    con = sqlite3.connect(database)
    cur = con.cursor()
    return con,cur

def create_table():
    try:
        query1="create table credentials (username varchar,password varchar,designation varchar)"
        #print query1
	query2="create table employee_details (emp_id varchar primary key,emp_name varchar,designation varchar,experience int,email_id varchar,contact int,manager varchar)"
	#print query2
	query3="create table leave_balances (emp_id varchar,casual_leaves int,sick_leaves int)"
	query4="create table leave_details (emp_id varchar, date date,type_of_leave varchar)"
	query5="create table total_leaves (type_of_leave varchar,leave_id int,days int)" 
        con,cur=get_connection("leave_management.db")
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        cur.execute(query4)
        cur.execute(query5)
    except Exception as err:
        print err
    finally:
        cur.close()
        con.close()

if __name__=="__main__":
    create_table()
