from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

@app.route('/')
#when you hit '/' run this function
def index():	

	return render_template('index.html',)

@app.route('/campaigns/<campaign_id>')
def chartById(campaign_id):
	# curl get
	
	url = "http://777.bjohn.dev.nym2.adnexus.net:8880/campaignstats/"+campaign_id
	r = requests.get(url)	
	# process response
	status_code = r.status_code
	json_data = r.json()

	inventory_data = []
	bidding_data = []
	winning_data = []
	time_sequence = []
	sample_list = json_data["campaignstats"]
	# loop through this array can be 0 to max length of 10
	for i in range(len(sample_list)):
		sample = sample_list[i]
		t = sample.get("sample_time")
		# 2015-01-15T19:39:49Z
		u = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ")
		hh_mm_str = u.strftime("%H:%M")
		time_sequence.append(hh_mm_str)
		inventory_data.append(sample.get("elig_inv_rate"))
		bidding_data.append(sample.get("bid_rate"))
		winning_data.append(sample.get("spend_rate"))
	# the data is coming in desc order of sample_time
	inventory_data.reverse()
	bidding_data.reverse()
	winning_data.reverse()
	time_sequence.reverse()

	member_name = "AT&T"
	campaignid = campaign_id
	#inventory_data = [50, 100, 200, 150, 300, 500, 800, 400, 100, 20]
	#bidding_data   = [45, 60,  150, 50,  290, 250, 600, 100, 90,  15]
	#winning_data   = [40, 30,  100, 35,  280, 100, 500, 20,  80,  15]
	#time_sequence  = ["9:31", "9:32", "9:33", "9:34", "9:35", "9:36", "9:37", "9:38", "9:39", "9:40"]

	# calculate total number of imps
	sum_imps = 0
	for imp in inventory_data:
		sum_imps+=imp

	sum_bids = 0
	for bid in bidding_data:
		sum_bids+=bid

	sum_wins = 0
	for win in winning_data:
		sum_wins+=win

	pct_bid = int(100*sum_bids/(float(sum_imps)+1))
	pct_win = int(100*sum_wins/(float(sum_bids)+1))
	# chart settings
	chartID = 'chart_ID'
	chart_type = 'column'
	chart_height = 600
	chart_width = 845
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, "width": chart_width}
	series = [{"name": 'Total Biddable Imps', "data": inventory_data}, {"name": 'Bids', "data": bidding_data}, {"name":'Wins', "data": winning_data}]
	title = {"text": 'bidding overtime'}
	xAxis = {"title": {"text": 'time'}, "categories": time_sequence}
	yAxis = {"title": {"text": 'Impressions'}, "plotLines": [{"value": 0,"width": 1,"color": '#808080'}]}
	legend = {"layout": 'vertical',"align": 'right',"verticalAlign": 'middle',"borderWidth": 0}
	return render_template('index.html', 
		TotalImps=sum_imps,
		PctBid = pct_bid,
		PctWin = pct_win,
		StartTime=time_sequence[0],
		EndTime=time_sequence[9],
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
	inventory_data = []
	bidding_data = []
	winning_data = []
	time_sequence = []
	json_data = {"hostAddress":"10.6.253.135","count":2,"start":0,"end":1,"numberOfElements":2,"campaignstats":[{"id":1,"sample_time":"2015-01-15T19:39:49Z","bid_rate":200,"elig_inv_rate":200,"spend_rate":200},{"id":1,"sample_time":"2015-01-15T19:37:15Z","bid_rate":100,"elig_inv_rate":100,"spend_rate":100}]}
	sample_list = json_data["campaignstats"]
	# loop through this array can be 0 to max length of 10
	for i in range(len(sample_list)):
		sample = sample_list[i]
		t = sample.get("sample_time")
		# 2015-01-15T19:39:49Z
		u = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ")
		hh_mm_str = u.strftime("%H:%M")
		time_sequence.append(hh_mm_str)
		inventory_data.append(sample.get("elig_inv_rate"))
		bidding_data.append(sample.get("bid_rate"))
		winning_data.append(sample.get("spend_rate"))

	print time_sequence
	print inventory_data
	print bidding_data
	print winning_data
	return
		
if __name__ == '__main__':
	app.run(debug=True)

