from flask import Flask, url_for, render_template


app = Flask('__init__')


@app.route('/')
def home():
	return "OK"