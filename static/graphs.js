
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
                                                    title:{
                                                      display: true,
                                                      text: 'Number of beds average price' 
                                                    }
                                                  }

                                                }


                                              });
        $('#bedLegend').html(myBarChart.generateLegend());
      });
}


