import sqlite3


con = sqlite3.connect('agenda.db')
c = con.cursor()


dados = ('Teste 1', '03:02', '2019-11-27', 'Local teste', '41999999999', 'tags tags2', '27/11/2019 15:12')

c.execute("INSERT INTO agenda(nome, hora,data, local, telefone, tags, logData) VALUES ('Teste 1', '03:02', '2019-11-27', 'Local teste', '41999999999', 'tags tags2', '27/11/2019 15:12');")


	
con.commit()
con.close()