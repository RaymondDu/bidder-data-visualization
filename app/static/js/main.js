$(document).ready(function() {
/*	 $(chart_id).highcharts({
		chart: chart,
		title: title,
		xAxis: xAxis,
		yAxis: yAxis,
		series: series,
	});

*/

	console.log('ready');

	$("li").each(function(){
		$(this).hover(function(){
			$(this).addClass('selected');	
		}, function (){
			$(this).removeClass('selected');
		});
	});


});