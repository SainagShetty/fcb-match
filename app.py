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
time1 = ti[0];
hours1 = int(time1[0:2]);
min1 = int(time1[3:5]);
date = dat[0];
month = int(date[0:2]);
day = int(date[3:5]);
year = int(date[7:10]);
year = year+2000
now  = datetime.datetime.now()
a = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,00)
b = datetime.datetime(year,month,day,hours1,min1,00)
d = b + datetime.timedelta(hours = 3, minutes = 30)
val = (d-a)
days, seconds = val.days, val.seconds
hours = (days-1) * 24 + seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print(days)
print(hours)
print(minutes)
print(val)
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html',opp = opp[0], ven = ven[0], days = days, hours = hours, minutes = minutes);

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
