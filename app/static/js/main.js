$(document).ready(function() {
/*	 $(chart_id).highcharts({
		chart: chart,
		title: title,
		xAxis: xAxis,
		yAxis: yAxis,
		series: series,
	});

*/

	var campaign_id_list = [1192, 1994, 1050];

	for ( i = 0; i < campaign_id_list.length; i++ ) {
		var link = "<a href='/campaigns/" + campaign_id_list[i] + "'><li>" + campaign_id_list[i] + "</li></a>";
		$('#side_nav ul').append(link);
		console.log(link);
	}

	$("li").each(function(){
		$(this).hover(function(){
			$(this).addClass('selected');	
		}, function (){
			$(this).removeClass('selected');
		});
	});


});