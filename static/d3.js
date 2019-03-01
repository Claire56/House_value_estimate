



// const sample = $get('/mean_price_bed.json');

// const svg = d3.select('svg');
//     const svgContainer = d3.select('#container');
    
//     const margin = 80;
//     const width = 1000 - 2 * margin;
//     const height = 600 - 2 * margin;

//     const chart = svg.append('g')
//       .attr('transform', `translate(${margin}, ${margin})`);

//     const xScale = d3.scaleBand()
//       .range([0, width])
//       .domain(sample.map((s) => s.Num_beds))
//       .padding(0.4)
    
//     const yScale = d3.scaleLinear()
//       .range([height, 0])
//       .domain([0, 100]);

//     // vertical grid lines
//     // const makeXLines = () => d3.axisBottom()
//     //   .scale(xScale)

    // const makeYLines = () => d3.axisLeft()
    //   .scale(yScale)

    // chart.append('g')
    //   .attr('transform', `translate(0, ${height})`)
    //   .call(d3.axisBottom(xScale));

    // chart.append('g')
    //   .call(d3.axisLeft(yScale));

    
    // chart.append('g')
    //   .attr('class', 'grid')
    //   .call(makeYLines()
    //     .tickSize(-width, 0, 0)
    //     .tickFormat('')
    //   )

    // const barGroups = chart.selectAll()
    //   .data(sample)
    //   .enter()
    //   .append('g')

    // barGroups
    //   .append('rect')
    //   .attr('class', 'bar')
    //   .attr('x', (g) => xScale(g.Num_beds))
    //   .attr('y', (g) => yScale(g.value))
    //   .attr('height', (g) => height - yScale(g.value))
    //   .attr('width', xScale.bandwidth())
    //   .on('mouseenter', function (actual, i) {
    //     d3.selectAll('.value')
    //       .attr('opacity', 0)

        // d3.select(this)
        //   .transition()
        //   .duration(300)
        //   .attr('opacity', 0.6)
        //   .attr('x', (a) => xScale(a.Num_beds) - 5)
        //   .attr('width', xScale.bandwidth() + 10)

        // const y = yScale(actual.value)

        // line = chart.append('line')
        //   .attr('id', 'limit')
        //   .attr('x1', 0)
        //   .attr('y1', y)
        //   .attr('x2', width)
        //   .attr('y2', y)

        // barGroups.append('text')
        //   .attr('class', 'divergence')
        //   .attr('x', (a) => xScale(a.Num_beds) + xScale.bandwidth() / 2)
        //   .attr('y', (a) => yScale(a.value) + 30)
        //   .attr('fill', 'white')
        //   .attr('text-anchor', 'middle')
        //   .text((a, idx) => {
        //     const divergence = (a.value - actual.value).toFixed(1)
            
        //     let text = ''
        //     if (divergence > 0) text += '+'
        //     text += `${divergence}%`

        //     return idx !== i ? text : '';
        //   })

    //   })
    //   .on('mouseleave', function () {
    //     d3.selectAll('.value')
    //       .attr('opacity', 1)

    //     d3.select(this)
    //       .transition()
    //       .duration(300)
    //       .attr('opacity', 1)
    //       .attr('x', (a) => xScale(a.Num_beds))
    //       .attr('width', xScale.bandwidth())

    //     chart.selectAll('#limit').remove()
    //     chart.selectAll('.divergence').remove()
    //   })

    // barGroups 
    //   .append('text')
    //   .attr('class', 'value')
    //   .attr('x', (a) => xScale(a.Num_beds) + xScale.bandwidth() / 2)
    //   .attr('y', (a) => yScale(a.value) + 30)
    //   .attr('text-anchor', 'middle')
    //   .text((a) => `${a.value}%`)
    
    // svg
    //   .append('text')
    //   .attr('class', 'label')
    //   .attr('x', -(height / 2) - margin)
    //   .attr('y', margin / 2.4)
    //   .attr('transform', 'rotate(-90)')
    //   .attr('text-anchor', 'middle')
    //   .text('Love meter (%)')

    // svg.append('text')
    //   .attr('class', 'label')
    //   .attr('x', width / 2 + margin)
    //   .attr('y', height + margin * 1.7)
    //   .attr('text-anchor', 'middle')
    //   .text('Languages')

    // svg.append('text')
    //   .attr('class', 'title')
    //   .attr('x', width / 2 + margin)
    //   .attr('y', 40)
    //   .attr('text-anchor', 'middle')
    //   .text('Most loved programming languages in 2018')

    // svg.append('text')
    //   .attr('class', 'source')
    //   .attr('x', width - margin / 2)
    //   .attr('y', height + margin * 1.7)
    //   .attr('text-anchor', 'start')
    //   .text('Source: Stack Overflow, 2018')





$(function () {
        var posts = [
            { category: "Finance", count: 3 },
            { category: "Law", count: 13 },
            { category: "Business", count: 17 },
            { category: "Health", count: 17 },
            { category: "Sport", count: 23 },
            { category: "Celebrity", count: 17 },
            { category: "IT", count: 7, color: "red" },
            { category: "Technology", count: 12 },
            { category: "Geek", count: 5 },
            { category: "Politics", count: 7 },
            { category: "Religion", count: 17 }
        ];
        $("#chart").shieldChart({
            theme: "light",
            axisX: {
                categoricalValues: $.map(posts, function (item) {
                    return item.category;
                })
            },
            axisY: {
                title: {
                    text: "Posts per day"
                }
            },
            seriesSettings: {
                bar: {
                    dataPointText: {
                        enabled: true
                    }
                }
            },
            primaryHeader: {
                text: "Article"
            },
            dataSeries: [{
                seriesType: "bar",
                collectionAlias: "Posts per Day",
                data: $.map(posts, function (item) {
                    return {
                        y: item.count,
                        color: item.color
                    }
                })
            }]
        });
    });