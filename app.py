import os
from flask import Flask
from flask import render_template
import requests
import datetime
from bs4 import BeautifulSoup as bs

url = 'http://fans.fcbarcelona.com/'
response = requests.get(url)
html = response.content
soup = bs(html)
ht = soup.find('div',{'class':'m-match-team-home'}).contents
at = soup.find('div',{'class':'m-match-team-away'}).contents
ven = soup.find('span',{'class':'m-match-location'}).contents
hometteam = ht[0]
awayteam = at[0]
venue = ven[2].strip('\n  ')
dt = soup.find('div',{'class':'m-match-countdown'})
dattime = dt['data-datetime']


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html',hometteam = hometteam, awayteam = awayteam, venue = venue,datetime = dattime);

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
