from flask import *
import json
import requests

data = json.loads(requests.get('https://api.covid19india.org/data.json').content)

state = json.loads(requests.get('https://api.covid19india.org/state_district_wise.json').content)['Tamil Nadu']['districtData']

def fun(d):
	Table = []
	for key, value in d.items():
		if(key not in ['notes','delta','statenotes','deltaconfirmed','deltadeaths','deltarecovered','state','statecode']):
		    temp = []
		    temp.extend([key,value])
		    Table.append(temp)
	return Table

p = [[['district',i]]+fun(state[i]) for i in state.keys()]
print(p[0])

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def landing():
	return render_template('home.html')

@app.route('/state', methods=['GET','POST'])
def state():
	return render_template('state.html', l=data['statewise'], table=[fun(data['statewise'][i]) for i in range(len(data['statewise']))])

@app.route('/tn', methods=['GET','POST'])
def tn():
	return render_template('tn.html', l=state, table=p)


app.run(host = 'localhost', port = 5000, debug = True)