$(document).ready(function() {

    for (x = 0; x < campaignList.length; x++) {
        campaign_id = campaignList[x]["id"];
        campaign_name = campaignList[x]["name"];
        $("nav ul").append("<a href='/campaigns/" + campaign_id + "'><li data-id='" + campaign_id + "'>" + campaign_id + " - " + campaign_name + "</li></a>");
    }

	for (x = 0; x < campaignList.length; x++) {
	    campaign_id = campaignList[x]["id"];
	    campaign_name = campaignList[x]["name"];
	    $('#homepage').append("<div class='container'><a href='/campaigns/" + campaign_id + "' class='campaign' id='total_biddable_imps'><h2>" + campaign_id + " - " + campaign_name + "</h2></a></div>");
	    console.log("<div class='container'><a href='/campaigns/" + campaign_id + "' class='campaign' id='total_biddable_imps'><h2>" + campaign_id + " - " + campaign_name + "</h2></a></div>");
	}

	$("li").each(function(){
		if ($(this).data("id") == $('body').data("title")) {
			$(this).addClass('selected');	
		}
		else {
			$(this).removeClass('selected');
		};
	});

	if (typeof chart == 'object') {	
		$('.chart').highcharts({
			chart: chart,
			title: title,
			xAxis: xAxis,
			yAxis: yAxis,
			series: series,
		});
	};
	
/*	var campaign_id_list =  [6596095, 6513780, 6766936, 6513786];

	for ( i = 0; i < campaign_id_list.length; i++ ) {
		var link = "<a href='/campaigns/" + campaign_id_list[i] + "'><li>" + campaign_id_list[i] + "</li></a>";
		$('#side_nav ul').append(link);
		
	}
*/


});

function test()
{
	if (campaign_id != "" && campaign_name != "") {
		$.postJSON($SCRIPT_ROOT + '/admin/add', {
			id: $('input#campaign_id').val(),
			name: $('input#campaign_name').val()
		}, function(data) {
			$('#result').text(data.result);
		});
		return false
	} else {
		$('form').append("<div class='msg'>Please fill in the campaign ID and name</div>");
	}
}