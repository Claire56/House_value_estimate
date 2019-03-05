
window.onload = function(){
  let bedBar = $("#bedBarChart").get(0).getContext("2d");

      $.get("/mean_price_bed.json", function (data) {
        
        let myBarChart = new Chart(bedBar, {
                                                type: 'bar',
                                                data: data,
                                                options: {
                                                  scales:{
                                                    xAxes:[{
                                                      display: true,
                                                      labelString: 'Beds'
                                                    }]
                                                  }

                                                }


                                              });
        $('#bedLegend').html(myBarChart.generateLegend());
      });
}


options = {
  scales: {
    yAxes: [{
      scaleLabel: {
        display: true,
        labelString: 'probability'
      }
    }]
  }     
}