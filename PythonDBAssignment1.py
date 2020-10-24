
import sqlite3

conn = sqlite3.connect('DBAsst1.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT, \
        col_type TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('DBAsst1.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_Files(col_file, col_type) VALUES (?,?)", \
                ('information.docx','Word Document'))
    cur.execute("INSERT INTO tbl_Files(col_file, col_type) VALUES (?,?)", \
                ('Hello.txt','Text Document'))
    cur.execute("INSERT INTO tbl_Files(col_file, col_type) VALUES (?,?)", \
                ('myImage.png','Image Document'))
    cur.execute("INSERT INTO tbl_Files(col_file, col_type) VALUES (?,?)", \
                ('myMovie.mpg','Video Document'))
    cur.execute("INSERT INTO tbl_Files(col_file, col_type) VALUES (?,?)", \
                ('World.txt','Text Document'))
    cur.execute("INSERT INTO tbl_Files(col_file, col_type) VALUES (?,?)", \
                ('data.pdf','PDF Document'))
    cur.execute("INSERT INTO tbl_Files(col_file, col_type) VALUES (?,?)", \
                ('myPhoto.jpg','Image Document'))
    conn.commit()
conn.close()

conn = sqlite3.connect('DBAsst1.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file, col_type FROM tbl_Files WHERE col_type = 'Text Document'")
    varDocu = cur.fetchall()
    for document in varDocu:
        msg = "File Name: {}\nFile Type: {}".format(document[0], document[1],)
        print(msg)
    conn.commit()
conn.close()
