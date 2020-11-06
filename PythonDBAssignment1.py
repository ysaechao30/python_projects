
import sqlite3

conn = sqlite3.connect('DBAsst6.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('DBAsst6.db')

with conn:
    cur=conn.cursor()
    fileList = ('information.docx','hello.txt', 'myImage.png',\
    'mymovie.mpg', 'world.txt','data.pdf','myphoto.jpg')

    for document in fileList:
        if document.endswith('.txt'):
            cur.execute("INSERT INTO tbl_Files(col_file) VALUES(?)",[document])
    conn.commit()
conn.close()

 
