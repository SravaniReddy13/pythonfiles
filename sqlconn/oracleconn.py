import cx_Oracle
import csv
conn=cx_Oracle.Connection('system/manager@mother')
cur=conn.cursor()
 
def createtable():
    query='''create table mcasravani(
    id number(2) primary key,
    name varchar(20)
    )
    '''
    cur.execute(query)
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    cur.execute("insert into mcasravani(id,name)values(:id,:name)",record)
    conn.commit()
#insertrecord(2,'pooja')
#insertrecord(3,'maya')
#insertrecord(4,'nandhana')

def read_records():
    query='select * from mcasravani'
    cur.execute(query)
    records=cur.fetchall()
    for row in records:
        print(row)
    # with open('records.csv','w',newline='') as csvfile:
    #     data=csv.writer(csvfile)
    #     data.writerow(['id','name'])
    #     for row in records:
    #       data.writerow(row)
read_records()
def update_record():
    query='''update mcasravani
    set name='sravani reddy'
    where id=1'''
    cur.execute(query)
    conn.commit()
#update_record()
def delete_record():
    query='''delete from mcasravani where id=2'''
    cur.execute(query)
    conn.commit()
#delete_record()
def fetch_record():
    query='select * from mcasravani where id=1'
    cur.execute(query)
    records=cur.fetchall()
    for row in records:
        print(row)
#fetch_record()
def truncate():
    query='truncate table mcasravani'
    cur.execute(query)
#truncate()  
def insert_from_csv():
    with open('records.csv','r') as csvfile:
        data=csv.reader(csvfile)
        data=list(data)
        for rows in range(1,len(data)):
            insertrecord(*data[rows])

