


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

