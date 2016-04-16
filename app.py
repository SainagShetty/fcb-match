import os
from flask import Flask
from flask import render_template
import requests
import datetime
from bs4 import BeautifulSoup as bs

url = 'http://www.fcbarcelona.com/football'
response = requests.get(url)
html = response.content
soup = bs(html)
opp = soup.find('span', {'class': 'away'}).contents
ven = soup.find('span', {'class': 'venue'}).contents
dat = soup.find('span', {'class': 'date-time'}).contents
ti = soup.find('span', {'class': 'date-time local'}).contents
print("F C Barcelona is playing "+opp[0]+" at "+ven[0])

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html',opp = opp[0], ven = ven[0], days = days, hours = hours, minutes = minutes);

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
