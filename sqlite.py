from bs4 import BeautifulSoup as bs # pip3 install beautifulsoup4
import sqlite3

posologies = []
with open('corpus-medical_snt/concord.html', 'r') as concord:
    text = concord.read()
    soup = bs(text, 'html.parser')
    for tr in soup.find_all('tr'):
        posologies.append(tr.find('a').get_text())

# Create Connection
con = sqlite3.connect('extraction.db')

# Create Cursor
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE EXTRACTION
               (id integer primary key, posologie text)''')

# Insert rows of data from concord.html
i = 1
for posologie in posologies:
    cur.execute("INSERT INTO EXTRACTION VALUES ('%d','%s')" %(i, posologie))
    print("%4d | %s" %(i, posologie))
    i += 1

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
