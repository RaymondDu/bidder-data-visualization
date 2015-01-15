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
def chart(chartID = 'chart_ID', chart_type = 'line', chart_height = 350):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'BidRate', "data": [10,15,17,18]}, {"name": 'InventoryRate', "data": [10, 8, 6, 2]}, {"name":'SpendRate', "data":[2, 6, 15, 30]}]
	title = {"text": 'Learn and Hack'}
	xAxis = {"categories": ['9:32 AM', '9:33 AM', '9:44 AM', '9:45 AM']}
	yAxis = {"title": {"text": 'Count'}, "plotLines": [{"value": 0,"width": 1,"color": '#808080'}]}
	legend = {"layout": 'vertical',"align": 'right',"verticalAlign": 'middle',"borderWidth": 0}
	return render_template('chart.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis, legend=legend)

if __name__ == '__main__':
	app.run(debug=True)

