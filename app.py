from flask import Flask, url_for, render_template


app = Flask('app')




@app.route('/agendar')
def agendamento():
	return render_template('agendamento.html')



app.run()