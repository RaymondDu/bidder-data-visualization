from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
#when you hit '/' run this function
def index():	
	return render_template('index.html')

@app.route('/campaigns/<campaign_id>')
def chartById(campaign_id):
	# curl get
	'''
	url = "http://localhost:8610/1.0.0/members/"+member_id
	r = requests.get(url)	
	# process response
	status_code = r.status_code
	content = r.content
	json_data = r.json()
	member = json_data["members"][0]
	billing_name = member.get("billing_name")
	short_name = member.get("short_name")
	api_last_modified = member["api_last_modified"]
	'''
	
	status_code = 200
	member_name = "AT&T"
	campaignid = campaign_id
	inventory_data = [50, 100, 200, 150, 300, 500, 800, 400, 100, 20]
	bidding_data   = [45, 60,  150, 50,  290, 250, 600, 100, 90,  15]
	winning_data   = [40, 30,  100, 35,  280, 100, 500, 20,  80,  15]
	time_sequence  = ["9:31", "9:32", "9:33", "9:34", "9:35", "9:36", "9:37", "9:38", "9:39", "9:40"]
	# chart settings
	chartID = 'chart_ID'
	chart_type = 'column'
	chart_height = 600
	chart_width = 1000
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, "width": chart_width}
	series = [{"name": 'Total Biddable Imps', "data": inventory_data}, {"name": 'Bids', "data": bidding_data}, {"name":'Wins', "data": winning_data}]
	title = {"text": 'bidding overtime'}
	xAxis = {"title": {"text": 'time'}, "categories": time_sequence}
	yAxis = {"title": {"text": 'Impressions'}, "plotLines": [{"value": 0,"width": 1,"color": '#808080'}]}
	legend = {"layout": 'vertical',"align": 'right',"verticalAlign": 'middle',"borderWidth": 0}
	return render_template('index.html', 
		StartTime=time_sequence[0]
		EndTime=time_sequence[9]
		StatusCode=status_code, 
		MemberName=member_name, 
		CampaignID=campaignid, 
		chartID=chartID, 
		chart=chart, 
		series=series, 
		title=title, 
		xAxis=xAxis, 
		yAxis=yAxis, 
		legend=legend)

@app.route('/test')
def test():
	json_data = {"hostAddress":"10.6.253.135","count":2,"start":0,"end":1,"numberOfElements":2,"campaignstats":[{"id":1,"sample_time":null,"bid_rate":0.0,"elig_inv_rate":0.0,"spend_rate":0.0},{"id":1,"sample_time":null,"bid_rate":0.0,"elig_inv_rate":0.0,"spend_rate":0.0}]}

if __name__ == '__main__':
	app.run(debug=True)

