
d3.tsv("results.tsv", function(data) {
	build_table(data);
});


function build_table(data) {
	var table = $("<table>",{id:'property_table', class:'bland'});
	$('#table').append(table)
	headers = Object.keys(data[0]);
	ordered = ['link','address','cashflow','beds','bath'];
	// Add elements not in ordered to ordered
	$(headers).each(function(i){
		var oi = ordered.indexOf(this+"");
		if (oi == -1) {
			ordered.push(this+"");
		}
	});
	headers = ordered;
	var header_row = $("<tr></tr>");
	table.append(header_row);
	$(headers).each(function(i){
		header_row.append("<th>"+this+"</th>");
	});

	$(data).each(function(i){
		var row = $("<tr></tr>");
		table.append(row);
		var data_row = this;
		$(headers).each(function(i){
			var e;
			if (this+'' === "link") {
				e = "<a href='" + data_row[this] + "'>-></a>";
			} else {
		   		e = data_row[this];
			}
			if ($.isNumeric(e)) { e = parseInt(e); };
			row.append("<td>"+e+"</td>")
		});
	});

}
