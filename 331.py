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
	<body class="jumbotron">
<script src="https://cdn.hcharts.cn/highstock/5.0.10/highstock.js"></script>
<script src="https://cdn.hcharts.cn/highstock/5.0.10/modules/exporting.js"></script>
<script>
  $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
</script>
<div id="container_cpu" style="height: 400px; width: 1000px"></div>
<div id="container_mem" style="height: 400px; width: 1000px"></div>

<script>
Highcharts.setOptions({
    global: {
        useUTC: false
    }
});
// Create the chart
Highcharts.stockChart('container_mem', {
    chart: {
        style: {
        fontFamily: "",
        fontSize: '12px',
        fontWeight: 'bold',
        color: '#006cee'
    },
        type: 'areaspline',
            animation: Highcharts.svg, // don't animate in old IE
            marginRight: 10,
        events: {
            load: function () {
                // set up the updating of the chart each second
                var series = this.series[0];
                setInterval(function () {
                    $.getJSON($SCRIPT_ROOT + "/dynamic", { }, function(json){
            //          alert("JSON Data: " + json.cpu);
                        var x = (new Date()).getTime(), // current time
                        y = json.mem/1000
                    series.addPoint([x, y], true, true);
                    });
                }, 1000);
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
        text: 'Memory Info'
    },
    tooltip: {
          //  valueDecimals: 2,
         //   valuePrefix: '$',
            valueSuffix: ' M'
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
        name: 'Memory Info',
        data: (function () {
            // generate an array of random data
            var data = [],
                time = (new Date()).getTime(),
                i;
            for (i = -999; i <= 0; i += 1) {
                data.push([
                    time + i * 1000,
                    0
                ]);
            }
            return data;
        }())
    }]
});

</script>

<script>
Highcharts.setOptions({
    global: {
        useUTC: false
    }
});
// Create the chart
Highcharts.stockChart('container_cpu', {
    chart: {
        type: 'areaspline',
            animation: Highcharts.svg, // don't animate in old IE
            marginRight: 10,
        events: {
            load: function () {
                // set up the updating of the chart each second
                var series = this.series;
                $.getJSON($SCRIPT_ROOT + "/dynamic", { }, function(json){
                setInterval(function () {
                    series[0].addPoint([(new Date()).getTime(), json.cpu[0]], true, true);
                    series[1].addPoint([(new Date()).getTime(), json.cpu[1]], true, true);
                    }, 1000);
                });
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
        text: 'CPU Info'
    },
    tooltip: {
        shared: true,
        valueSuffix: ' %'
        },
    exporting: {
        enabled: false
    },
       credits:{
        enabled:false
    },
    plotOptions: {
            area: {
                fillOpacity: 0.1, // 指定所有面积图的透明度
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
        name: 'CPU User',
        data: (function () {
            // generate an array of random data
            var data = [],
                time = (new Date()).getTime(),
                i;
            for (i = -999; i <= 0; i += 1) {
                data.push([
                    time + i * 1000,
                    0
                ]);
            }
            return data;
        }())
    },
        {
        name: 'CPU Kelnel',
        data: (function () {
            // generate an array of random data
            var data = [],
                time = (new Date()).getTime(),
                i;
            for (i = -999; i <= 0; i += 1) {
                data.push([
                    time + i * 1000,
                    0
                ]);
            }
            return data;
        }())
        }
    ]
});
		</script>
	</body>
{% endblock %}
