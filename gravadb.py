import sqlite3


con = sqlite3.connect('agenda.db')
c = con.cursor()


dados = ('2w','Teste 1', '03:02', '2019-11-27', 'Local teste', '41999999999', 'tags tags2', '27/11/2019 15:12')

#c.execute("INSERT INTO agenda VALUES ('{}', '03:02', '2019-11-27', 'Local teste', '41999999999', 'tags tags2', '27/11/2019 15:12')",dados[1])

c.executemany("INSERT INTO agenda VALUES (?,?,?,?,?,?,?,?);", dados)


con.commit()
con.close()