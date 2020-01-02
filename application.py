from flask import Flask, render_template


app = Flask(__name__)

app.secret_key = "secret"


if __name__ == "main":
	app.run(debug=True)