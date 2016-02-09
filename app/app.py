import os
from flask import Flask, render_template, redirect, request
from twilio.rest import TwilioRestClient

app = Flask(__name__)

twilioPhoneNumber = ""
auth_token = ""
account_sid = ""
numberToCall = ""
entry.Url = "www.twilio.com"

@app.route('/')
def home():
    return render_template('mainpage.html')

@app.route('/login/', methods=['POST'])
def login():
    global account_sid
    account_sid = request.form['sid']
    global auth_token
    auth_token = request.form['auth_token']
    global twilioPhoneNumber
    twilioPhoneNumber = "+1" + request.form['number']
    return redirect('/')

@app.route("/call-phone/", methods=['POST'])
def callPhone():
    if twilioPhoneNumber == "" or auth_token == "" or account_sid == "":
        return redirect('/')
    client=TwilioRestClient(account_sid, auth_token)
    global numberToCall
    numberToCall = request.form['numberToCall']
    if numberToCall == "":
        return redirect('/')
    formattedNum = "+1" + numberToCall
    call = client.calls.create(to=formattedNum, from_=twilioPhoneNumber, url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    return redirect('/making-call/')

@app.route("/making-call/")
def calling():
    return render_template('makingCall.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port)



