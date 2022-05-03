import pymysql as MYSQL
def ConnectionPooling():
    db=MYSQL.connect(host="localhost",port=3306,user="root",passwd="Nivesh@1234",db="videostream")
    cmd=db.cursor()
    return db,cmd