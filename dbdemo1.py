import MySQLdb
con=MySQLdb.connect(host='localhost',database='boss',user='shoaib',password='admin@123')
cur=con.cursor()
#query='insert into user values("xyz@gmail.com","laptop",5)'
#query='insert into user values("mmm@gmail.com","new",8)'
#query="insert into user values('%s','%s','%d')"
#dt=('mmm','good',45)
query='insert into user values("majnu@gmail.com","laila",786)'
#query='delete from user where(status=786)'
cur.execute(query)
con.commit()
cur.close()
con.close
