

const svg = d3.select('#chart1')
      .append('svg')
      .attr('width', '800px')
      .attr('height', '300px');


d3.csv('/my_data_handler').then(function(data){
 console.log(data);

let ymin = d3.min(data, function(d){
    return d.total_sqft;});

let ymax = d3.max(data, function(d){
    return d.total_sqft;});

let xmin = d3.min(data, function(d){
     return d.sale_price;});
let xmax = d3.max(data, function(d){
     return d.sale_price;
});
console.log(ymin);
console.log(ymax);

console.log(xmin);
console.log(xmax);
// make the scales
xScale = d3.scaleLinear()
        .domain([xmin,xmax])
        .range([10,790]);



yScale = d3.scaleLinear()
         .domain([ymin,ymax])
         .range([10,299]);

scatter = svg.selectAll('.house')
         .data(data)
         .enter()
         .append('circle')
         .attr('class', 'house') //set class
         .attr('cx', function(d){
          return xScale(d.sale_price);})
         .attr('cy', function(d){
          return yScale(d.total_sqft);})
         .attr('r','5')
         .attr('fill', 'blue');
//adding the x and y axis

xAxis = d3.axisBottom(xScale)
                    .tickValues([50000, xmax]);
yAxis = d3.axisLeft(yScale)
                    .tickValues([ymin,ymax]);

        // Add the x and y axis to the svg element and assign them a class
        xAxisG = svg.append('g')
                    .attr('id', 'xAxis')
                    .attr('class', 'axis');
        yAxisG = svg.append('g')
                    .attr('id', 'yAxis')
                    .attr('class', 'axis');
        // Put the x and y axis on the screen
        xAxisG.call(xAxis)
                .attr('transform', 'translate(0,' + (height-margin)+ ')') // First number is x axis move, second number is y axis move
                ;
        yAxisG.call(yAxis)
                .attr('transform', 'translate(30,0)') // First number is x axis move, second number is y axis move
                ;


});
  

