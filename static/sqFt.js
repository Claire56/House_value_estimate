


    // Make scatter plot showing relatioship between price and  sqFt
    let ctx = $("#scatter1").get(0).getContext("2d");

    $.get("/scatter.json", function (data) {
        // data is 
           // {'points': [{x:444, y:666}, ...]}

        let listOfPoints= data.points;
      

        var scatterChart = new Chart(ctx, {
            type: 'scatter',
            data: {
                datasets: [{
                    label: 'Scatter Plot showing the relationship between Price and total sqft Dataset',
                    data: listOfPoints
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'linear',
                        position: 'bottom'
                    }]
                }
            }



        })



    });


    let bedBar = $("#beds").get(0).getContext("2d");

      $.get("/mean_price_bed.json", function (data) {
        
        let myBedChart = new Chart(bedBar, {
                                                type: 'bar',
                                                data: data,
                                                options: {
                                                  scales:{
                                                    xAxes:[{
                                                      display: true,
                                                      labelString: 'Beds'
                                                    }]
                                                    // title:{
                                                    //   display: true,
                                                    //   text: 'Number of beds average price' 
                                                    // }
                                                  }

                                                }


                                              });
        $('#bedLegend').html(myBedChart.generateLegend());
      });


      let grgBar = $("#garage").get(0).getContext("2d");

      $.get("/grg.json", function (data) {
        
        let myGrgChart = new Chart(grgBar, {
                                                type: 'doughnut',
                                                data: data,
                                                options: {
                                                  scales:{
                                                    xAxes:[{
                                                      display: true,
                                                      labelString: 'Garage'
                                                    }]
                                                    // title:{
                                                    //   display: true,
                                                    //   text: 'Number of beds average price' 
                                                    // }
                                                  }

                                                }


                                              });
        $('#grgLegend').html(myGrgChart.generateLegend());
      });



    let poolBar = $("#pool").get(0).getContext("2d");

      $.get("/pool.json", function (data) {
        
        let myPoolChart = new Chart(poolBar, {
                                                type: 'pie',
                                                data: data,
                                                options: {
                                                  scales:{
                                                    xAxes:[{
                                                      display: true,
                                                      labelString: 'pools'
                                                    }]
                                                    // title:{
                                                    //   display: true,
                                                    //   text: 'Number of beds average price' 
                                                    // }
                                                  }

                                                }


                                              });
        $('#poolLegend').html(myPoolChart.generateLegend());
      });


let bathBar = $("#baths").get(0).getContext("2d");

      $.get("/baths.json", function (data) {
        
        let myBathChart = new Chart(bathBar, {
                                                type: 'bar',
                                                data: data,
                                                options: {
                                                  scales:{
                                                    xAxes:[{
                                                      display: true,
                                                      labelString: 'Bath rooms'
                                                    }]
                                                    // title:{
                                                    //   display: true,
                                                    //   text: 'Number of beds average price' 
                                                    // }
                                                  }

                                                }


                                              });
        $('#bathLegend').html(mybathChart.generateLegend());
      });
