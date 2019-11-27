from flask import Flask, url_for, render_template, redirect, request
from datetime import datetime
import sqlite3




app = Flask('app')


@app.route('/gravar', methods=['POST'])
def gravar():
	nome = request.form['nome']
	horaAgenda = request.form['horaAgenda']
	dataAgenda = request.form['dataAgenda']
	local = request.form['local']
	telefone = request.form['telefone']
	tags = request.form['tags']

	datahora = datetime.now()
	dataLog = datahora.strftime('%d/%m/%Y %H:%M')

	tupla = (nome, horaAgenda, dataAgenda, local, telefone, tags, dataLog)
	dados = [tupla]
	print(tupla)
	print(dados)
	return redirect('/agendar')






@app.route('/agendar')
def agendar():
	return render_template('agendar.html')






app.run()