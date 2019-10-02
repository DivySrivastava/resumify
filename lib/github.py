import requests
import datetime

def parse(user):
    data = github_user(user)
    sinceDate = datetime.datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    sinceDate = sinceDate.strftime("%d-%m-%Y").split("-")
    sinceMonth =int(sinceDate[1]);
    since = int(sinceDate[2]);
    currentYear = int(datetime.datetime.today().strftime("%Y"))
    if(since == currentYear-1):
      since = 'last year';
    elif(since == currentYear):
      since = 'this year';
    return data

def github_user(user):
    return requests.get('https://api.github.com/users/'+user).json()