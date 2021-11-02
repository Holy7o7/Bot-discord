import pymysql
import datetime

def create_db():

    Host = "localhost" 	 
    User = "root"      
    Password = "sao2512" 		      
 
    conn  = pymysql.connect(host=Host, user=User, password=Password)

    cur  = conn.cursor()

    cur.execute("CREATE DATABASE sun")

    cur.execute("USE sun")

    values = [("Delitos"),("Politica"),("Naturaleza")]
    query = """INSERT INTO has_category (value) VALUES (%s)"""
    cur.executemany(query,values)
    values = [(1,"gran robo de autos", datetime.date(2021,1,1).strftime("%Y/%m/%d"), "www.lalegal.cl/robo", "La Legal"),
            (2,"Se descubre nuevo animal en Chile", datetime.date(2021,5,12).strftime("%Y/%m/%d"), "www.Nashionaljiografic/nuevo_animal", "Nashional Jiografic"),
            (3,"Elecciones presidenciales en Marzo", datetime.date(2020,5,16).strftime("%Y/%m/%d"), "www.CNNNN.com/elecciones", "CNNNN")
            ]
    query ="""INSERT INTO news (id_category,title,date,url,media_outlet) VALUES (%s,%s,%s,%s,%s)"""
    cur.executemany(query,values)
    for x in range(1,8):
        query = "UPDATE has_category SET id_news = "+str(x)+" WHERE id_category = "+str(x)

    cur.execute(query)
    conn.commit()      
    conn.close()

