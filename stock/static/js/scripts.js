Highcharts.getJSON(
    "https://demo-live-data.highcharts.com/aapl-ohlc.json",
    function (data) {
      Highcharts.stockChart("container", {
        rangeSelector: {
          selected: 2
        },
        title: {
          text: "AAPL Stock Price"
        },
        plotOptions: {
          series: {
            showInLegend: true,
            marker: {
              enabled: false
            }
          }
        },
        legend: { enabled: true },
        series: [
          {
            type: "ohlc",
            data: data,
            name:'AAPL',
            id: "base"
          },
          {
            type: "linearRegression",
            linkedTo: "base",
            zIndex: -1,
            params: {
              period: 5
            }
          },
          {
            type: "linearRegression",
            linkedTo: "base",
            zIndex: -1,
            params: {
              period: 100
            }
          }
        ],
        tooltip: {
          shared: true,
          split: false
        }
      });
    }
  );