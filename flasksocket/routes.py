from flask import render_template , request ,flash, redirect, url_for 
from flasksocket import app, db, bcrypt
from forms import Register, Login
from models import User
from flask_sqlalchemy import SQLAlchemy



@app.route("/",methods=['GET','POST'])
def index(): 
	reg_form = Register()
	
	if reg_form.validate_on_submit():
		username = reg_form.username.data
		bio = reg_form.bio.data
		password = reg_form.password.data
		s_pass = bcrypt.generate_password_hash(password).decode('utf-8')
		prev_user = User.query.filter_by(username=username).first()
		if prev_user:
			return "Username taken"

		user = User(username=username, bio=bio , password=s_pass)
		db.session.add(user)
		db.session.commit()

		
		print("yesyesyes")
		return redirect(url_for('login'))
	return render_template("index.html",form=reg_form)


@app.route('/login',methods=['GET','POST'])
def login():
	form = Login()

	if form.validate_on_submit():
		return "Logged in"

	return render_template("login.html", form=form)






if  __name__ == "__main__":
	app.run(debug=True)