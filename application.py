from flask import Flask, render_template , request
from forms import Register
from models import User
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = "secret"

app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://qtdkiadqujlwkt:32245eeb235f074e76f4f3e597b7686414ba09c9a8a1a4bbff95df560dc34544@ec2-174-129-32-240.compute-1.amazonaws.com:5432/d5f7lfpq6tn46o'
db = SQLAlchemy(app)


@app.route("/",methods=['GET','POST'])
def index():
	reg_form = Register()
	
	if reg_form.validate_on_submit():
		username = reg_form.username.data
		bio = reg_form.bio.data
		password = reg_form.password.data

		prev_user = User.query.filter_by(username=username).first()
		if prev_user:
			return "Username taken"

		user = User(username=username, bio=bio , password=password)
		db.session.add(user)
		db.session.commit()

		
		print("yesyesyes")
		return "Inserted in DB"

	return render_template("index.html",form=reg_form)


if __name__ == "__main__":
	app.run(debug=True)