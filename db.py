import pymysql

def connect():
    try:
        conn=pymysql.connect(port=3306,host='localhost',user='shadow',passwd='notRealPassword,database='aaguirre')
        return conn;
    except IOError as e:
        print('Error: %s',e)
    return None

def get_Visits():
    c=connect()
    cur=c.cursor()
    cur.execute("select * from Visits;")
    visits=[]
    for row in cur:
        visits.append([str(row[0]), str(row[1]),str(row[2]) ,str(row[3]),str(row[4]),str(row[5])])
    return visits


def log_pro_visits(ID,project_id):
    if ID is None:
        return
    c=connect()
    cur=c.cursor()
    if project_id is '1':
        cur.execute("INSERT INTO Project_Views(Visitor_ID,Project_ID) VALUES(%s,1);",(ID))
    elif project_id is '2':
        cur.execute("INSERT INTO Project_Views(Visitor_ID,Project_ID) VALUES(%s,2);",(ID))
    elif project_id is '3':
        cur.execute("INSERT INTO Project_Views(Visitor_ID,Project_ID) VALUES(%s,3);",(ID))
    elif project_id is '4':
        cur.execute("INSERT INTO Project_Views(Visitor_ID,Project_ID) VALUES(%s,4);",(ID))
    c.commit()
    return

def log_visit(IP,Info):
    c=connect()
    cur=c.cursor()
    if IP is None:
        IP="Invalid ip";
    if Info is None:
        Info="Invalid info"
    cur.execute("INSERT INTO Visits (IP,TIME,Platform,Browser,Version,Language) VALUES(%s,NOW(),%s,%s,%s,%s);",(IP,str(Info.platform),str(Info.browser),str(Info.version),str(Info.language)))
    c.commit()
    cur.execute('SELECT LAST_INSERT_ID();')
    sid=""
    for row in cur:
        sid=str(row)
    sid=sid.split(',') 
    sid=sid[0]
    sid=sid[1:]
    print(sid)
    return [int(s) for s in sid.split() if s.isdigit()]
    
    
if __name__=="__main__":
    get_Visits()




