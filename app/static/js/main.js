$(document).ready(function() {

    for (x = 0; x < campaignList.length; x++) {
        campaign_id = campaignList[x]["id"];
        campaign_name = campaignList[x]["name"];
        $("nav ul").append("<a href='/campaigns/" + campaign_id + "'><li data-id='" + campaign_id + "'>" + campaign_id + " - " + campaign_name + "</li></a>");
        console.log("<a href='/campaigns/" + campaign_id + "'><li data-id='" + campaign_id + "'>" + campaign_id + " - " + campaign_name + "</li></a>");
    }

	$("li").each(function(){
		if ($(this).data("id") == $('body').data("title")) {
			$(this).addClass('selected');	
		}
		else {
			$(this).removeClass('selected');
		};
	});

	$('.chart').highcharts({
		chart: chart,
		title: title,
		xAxis: xAxis,
		yAxis: yAxis,
		series: series,
	});
	
/*	var campaign_id_list =  [6596095, 6513780, 6766936, 6513786];

	for ( i = 0; i < campaign_id_list.length; i++ ) {
		var link = "<a href='/campaigns/" + campaign_id_list[i] + "'><li>" + campaign_id_list[i] + "</li></a>";
		$('#side_nav ul').append(link);
		
	}
*/


});