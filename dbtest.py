import sqlite3

# try:
#     with sqlite3.connect(r'E:\Tutorial\Python\test2.db') as conn:
#         cursor = conn.cursor()
#         conn.execute('insert into test values (?,?)', ('name1', 100))
#         conn.execute('insert into test2 values (?,?)', ('name2', 200))
# except sqlite3.Error as e:
#     print(e)
#
#
# try:
#     with sqlite3.connect(r'E:\Tutorial\Python\test2.db') as conn:
#         cursor = conn.cursor()
#         conn.execute('insert into test values (?,?)', ('name1', 300))
# except sqlite3.Error as e:
#     print(e)


try:
    conn = sqlite3.connect(r'E:\Tutorial\Python\test2.db')
    cursor = conn.cursor()
    conn.execute('insert into test values (?,?)', ('name1', 100))
    conn.execute('insert into test2 values (?,?)', ('name2', 200))
    conn.commit()
except sqlite3.Error as e:
    conn.rollback()
    print(e)
finally:
    conn.close()

try:
    conn = sqlite3.connect(r'E:\Tutorial\Python\test2.db')
    cursor = conn.cursor()
    conn.execute('insert into test values (?,?)', ('name1', 300))
    conn.commit()
except sqlite3.Error as e:
    conn.rollback()
    print(e)
finally:
    conn.close()

# with sqlite3.connect(r'E:\Tutorial\Python\test2.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('insert into test values (?,?)', ('name1', 100))
#     cursor.execute('insert into test2 values (?,?)', ('name2', 200))
