from flask import Flask, render_template, request
import database
import router
app = Flask(__name__, static_folder='client', static_url_path='')

@app.route('/')
def index():
	return app.send_static_file('index.html')

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', port = 8000)
