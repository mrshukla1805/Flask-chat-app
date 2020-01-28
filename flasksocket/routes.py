from time import localtime , strftime
from flask import render_template , request ,flash, redirect, url_for 
from flasksocket import app, db, bcrypt , login_m , socketio
from flasksocket.forms import Register, Login
from flasksocket.models import User
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user , current_user,login_required,logout_user
from flask_socketio import SocketIO, send , emit , join_room, leave_room


ROOMS = ['lounge' ,'news', 'gaming' , 'coding', ]

@login_m.user_loader
def load_user(id):

	return User.query.get(int(id))

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

		flash('Registered successfully, kindly login. ','success')
		return redirect(url_for('login'))
	return render_template("index.html",form=reg_form)


@app.route('/login',methods=['GET','POST'])
def login():
	form = Login()

	if form.validate_on_submit():
		user_object= User.query.filter_by(username=form.username.data).first()
		print(user_object)
		login_user(user_object)
		return redirect(url_for('chat'))
		
	return render_template("login.html", form=form)



@app.route("/chat",methods=['GET','POST'])
def chat():
	return render_template('chat.html',username= current_user.username,
	rooms=ROOMS)
'''
	if not current_user.is_authenticated:
		flash('Please login', 'danger')
		return redirect(url_for('login')) 
	'''
	
	


@app.route("/logout",methods=['GET'])
def logout():
	
	logout_user()
	flash('You have logged out successfully.', 'success')
	return redirect(url_for('login'))

#Event handler
@socketio.on('message')
def message(data):
	print(f"\n\n{data}\n\n")
	send({'msg': data['msg'], 'username': data['username'],
	'time_stamp': strftime('%b-%d %I:%M%p', localtime())}, room=data['room'])
	

@socketio.on('join')
def join(data):

	join_room(data['room'])
	send({'msg':data['username'] + " has joined the " + data['room'] + 
	"room."} ,room=data['room'])

@socketio.on('leave')
def leave(data):

	leave_room(data['room'])
	send({'msg':data['username'] + " has left the " + data['room'] 
	+ "room."}, room=data['room'])







if  __name__ == "__main__":
	socketio.run(app, debug=True)