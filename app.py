#!/usr/bin/python3
from flask import Flask, Response, jsonify
from slack import WebClient

FLASK_APP = Flask(__name__)
SLACK_APP = None

# Flask Methods
@FLASK_APP.route("/md5/<string:data_to_hash>")
def calc_md5(data_to_hash):
   hash = ""
   return jsonify(input=data_to_hash, output=hash)

@FLASK_APP.route("/factorial/<int:number>")
def calc_factorial(number):
    factorial = 0
    return jsonify(input=number, output=factorial)

@FLASK_APP.route("/fibonacci/<int:number>")
def calc_fibonacci(number):
    fibonacci = 0
    return jsonify(input=number, output=fibonacci)

@FLASK_APP.route("/is-prime/<int:number>")
def calc_is_prime(number):
    is_prime = False
    return jsonify(input=number, output=is_prime)

@FLASK_APP.route("/slack-alert/<string:message>")
def post_slack_alert(message):
    response = SLACK_APP.chat_postMessage(channel='#group-4', text=message)
    return jsonify(input=message, output=response["ok"])

if __name__ == "__main__":
    print("Attempting to read Slack App Key from slack.key file...")
    SLACK_KEY = None
    for l in open("slack.key"):
        SLACK_KEY = l.replace(" ", "")
    if SLACK_KEY == None or len(SLACK_KEY) < 55:
        print("ERROR: Could not read Slack App Key from slack.key file!")
    else:
        print("Connecting to Slack App with Key ", SLACK_KEY)
        SLACK_APP = WebClient(SLACK_KEY)
    print("Launching Flask App.")
    FLASK_APP.run(host="0.0.0.0")
