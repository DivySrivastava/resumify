from flask import Flask, request
import os
from lib import dotenv
from lib.github import parse

app = Flask(__name__)

app.apiKey = os.environ["API_KEY"]

@app.route('/<user>')
def getDetails(user):
  if (request.args.get("api_key") == app.apiKey):
    return str(parse(user))
  else:
    return "401"

if(__name__ == "__main__"):
  app.run()
