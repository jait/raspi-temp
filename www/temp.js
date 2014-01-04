(function() {
	var $ = jQuery;
	var pad = function pad(num, size) {
		var s = num + "";
		while (s.length < size)
			s = "0" + s;
		return s;
	};
	var fetch = function() {
		//console.log("fetching");
		$.getJSON("temp.json", function(result) {
			//console.log(result);
			$("#tempvalue").html(result["value"] + "&nbsp;&deg;C");
			// sec to ms
			var d = new Date(result["timestamp"] * 1000);
			//console.log(d);
			var html = d.getFullYear() + "-" + pad(d.getMonth() + 1, 2) + "-" + pad(d.getDate(), 2) + "&nbsp;" + pad(d.getHours(), 2) + ":" + pad(d.getMinutes(), 2);
			//$("#timestamp").html(d.toString());
			$("#timestamp").html(html);
		});
	};
	$(document).ready(function() {
		fetch();
		setInterval(fetch, 30000);
	});
}).call(this);
