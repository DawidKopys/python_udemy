import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute('INSERT INTO book VALUES (NULL,?,?,?,?)', (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute('SELECT * FROM book')
        rows = self.cur.fetchall()
        return rows

    def search(self, title='', author='', year='', isbn=''):
        self.cur.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute('DELETE FROM book WHERE id=?', (id,))  # tak, ten przecinek w (item,) jest potrzebny xD
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

if __name__=='__main__':
    # insert('The Sun', 'John Wick', 1969, 123451234)
    print(view())
    # s = search(author='John Smith')
    # update(s[0][0], s[0][1], s[0][2], 1111, s[0][4])
    # print(view())
