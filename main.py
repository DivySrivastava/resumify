from flask import Flask, render_template, redirect, url_for, request
import os
from lib import  dotenv

app = Flask(__name__)

app.apiKey = os.environ["API_KEY"]

@app.route('/<user>')
def getDetails(user):
  if (request.args.get("api_key") == app.apiKey):
    return user

if(__name__ == "__main__"):
  app.run()
