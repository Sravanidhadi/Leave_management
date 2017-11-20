import sqlite3
def get_connection(a):
    database=a
    con = sqlite3.connect(database)
    cur = con.cursor()
    return con,cur

def create_table():
    try:
        query="create table credentials (username varchar,password varchar)"
        print query
        con,cur=get_connection("leave_management.db")
        cur.execute(query)
    except Exception as err:
        print err
    finally:
        cur.close()
        con.close()

if __name__=="__main__":
    create_table()
