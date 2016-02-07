from flask import Flask, render_template, redirect, request
from twilio.rest import TwilioRestClient
from twilio_creds import account_sid, auth_token, client

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('mainpage.html')

@app.route("/call-phone/", methods=['POST'])
def callPhone():
	phoneNumber = request.form['yourNumber']
	formattedNum = "+1"+phoneNumber
	call = client.calls.create(to=formattedNum, from_="+16505138187", url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)