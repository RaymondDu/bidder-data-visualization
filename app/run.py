from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/<name>')
#when you hit '/' run this function
def index(name):	
	return render_template('index.html', name=name)

@app.route('/get/<member_id>')
#when you hit '/' run this function
def printStatusCode(member_id):
	url = "http://localhost:8610/1.0.0/members/"+member_id
	r = requests.get(url)	
	status_code = r.status_code
	content = r.content
	json_data = r.json()
	member = json_data["members"][0]
	billing_name = member.get("billing_name")
	short_name = member.get("short_name")
	api_last_modified = member["api_last_modified"]
	return render_template('index.html', name=status_code, billing_name=billing_name, short_name=short_name, api_last_modified=api_last_modified)


@app.route('/chart')
def chart(chartID = 'chart_ID', chart_type = 'column', chart_height = 350):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Total Inventory', "data": [50, 100, 200, 150]}, {"name": 'Bidding Imps', "data": [45,60,150,50]}, {"name":'Winning Imps', "data":[40, 30, 100, 35]}]
	title = {"text": 'bidding overtime'}
	xAxis = {"title": {"text": 'time'}, "categories": ['9:32 AM', '9:33 AM', '9:44 AM', '9:45 AM']}
	yAxis = {"title": {"text": 'Impressions'}, "plotLines": [{"value": 0,"width": 1,"color": '#808080'}]}
	legend = {"layout": 'vertical',"align": 'right',"verticalAlign": 'middle',"borderWidth": 0}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis, legend=legend)

if __name__ == '__main__':
	app.run(debug=True)

