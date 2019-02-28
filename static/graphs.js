

let bedBar = document.querySelector("#bedBarChart").get(0).getContext("2d");

    $.get("/mean_price_bed.json", function (data) {
      let myBarChart = new Chart(ctx_donut, {
                                              type: 'bar',
                                              data: data,
                                              options: options
                                            });
      $('#bedLegend').html(myBarChart.generateLegend());
    });



