{% extends "base.html" %}

{% block page_content %}

	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>Highstock Example</title>

		<script src="https://cdn.hcharts.cn/jquery/jquery-1.8.3.min.js"></script>
		<style>
${demo.css}
		</style>
	</head>
	<body>
<script src="https://cdn.hcharts.cn/highstock/5.0.10/highstock.js"></script>
<script src="https://cdn.hcharts.cn/highstock/5.0.10/modules/exporting.js"></script>

<div id="container" style="height: 400px; width: 900px"></div>

<script>
Highcharts.setOptions({
    global: {
        useUTC: false
    }
});

// Create the chart
Highcharts.stockChart('container', {
    chart: {
        type: 'areaspline',
            animation: Highcharts.svg, // don't animate in old IE
            marginRight: 10,
        events: {
            load: function () {

                // set up the updating of the chart each second
                var series = this.series[0];
                setInterval(function () {
                    $.getJSON("http://127.0.0.1:9527/dynamic", { }, function(json){
                        var x = (new Date()).getTime(), // current time
                        y = json.cpu/1000
                    series.addPoint([x, y], true, true);
                    });
                }, 600);
            }
        }
    },

    rangeSelector: {
        buttons: [{
            count: 1,
            type: 'minute',
            text: '1M'
        }, {
            count: 5,
            type: 'minute',
            text: '5M'
        }, {
            type: 'all',
            text: 'All'
        }],
        inputEnabled: false,
        selected: 0
    },

    title: {
        text: 'CPU Data'
    },
    exporting: {
        enabled: false
    },
       credits:{
        enabled:false
    },
    plotOptions: {
            area: {
                fillOpacity: 0.2, // 指定所有面积图的透明度
                pointStart: 1940,
                marker: {
                    enabled: false,
                    symbol: 'circle',
                    radius: 2,
                    states: {
                        hover: {
                            enabled: true
                        }
                    }
                }
            }
        },
    series: [{
        name: 'CPU Data',
        data: (function () {
            // generate an array of random data
            var data = [],
                time = (new Date()).getTime(),
                i;

            for (i = -999; i <= 0; i += 1) {
                data.push([
                    time + i * 600,
                    0
                ]);
            }
            return data;
        }())
    }]
});


		</script>
	</body>
{% endblock %}
