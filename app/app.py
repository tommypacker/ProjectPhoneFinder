from flask import Flask, render_template, redirect, request
from twilio.rest import TwilioRestClient

app = Flask(__name__)

phoneNumber = ""
auth_token = ""
account_sid = ""

@app.route('/')
def home():
	return render_template('mainpage.html')

@app.route('/login/', methods=['POST'])
def login():
	global account_sid
	account_sid = request.form['sid']
	global auth_token
	auth_token = request.form['auth_token']
	global phoneNumber
	phoneNumber = request.form['number']
	return redirect('/')

@app.route("/call-phone/", methods=['POST'])
def callPhone():
	client=TwilioRestClient(account_sid, auth_token)
	formattedNum = "+1"+phoneNumber
	call = client.calls.create(to=formattedNum, from_="+16505138187", url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
	return redirect('/making-call/')

@app.route("/making-call/")
def calling():
	return render_template('makingCall.html')

if __name__ == '__main__':
	app.run(debug=True)