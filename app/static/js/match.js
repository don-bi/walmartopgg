const playerDatas = document.querySelectorAll('.player-data');
playerDatas.forEach(data => {
    data.style.display = 'none';
});

const playerSection = document.querySelector('.player-section');
playerSection.style.display = 'none';

const playerBtns = document.querySelectorAll('.player');
playerBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        playerBtns.forEach(element => {element.classList.remove('active')});
        btn.classList.add('active');
        playerSection.style.display = 'block';
        playerDatas.forEach(data => {
            data.style.display = 'none';
        });
        const playerPos = btn.classList[1];
        const playerData = document.querySelector(`.player-data.${playerPos}`);
        playerData.style.display = 'block';

        window.scrollTo(0, window.innerHeight);
    })
});

const kdaBoxes = document.querySelectorAll('.kda-box');
console.log(kdaBoxes)
kdaBoxes.forEach(box => {
    box.childNodes.forEach(element => {
        if (element.innerHTML != undefined ) {
            element.style.color = 'white';
        }
    });
    const killNode = box.childNodes[1];
    const kills = parseInt(killNode.innerHTML);
    const deathNode = box.childNodes[3]
    const deaths = parseInt(deathNode.innerHTML);
    if (deaths == '0') {
        killNode.style.color = 'yellow';
        deathNode.style.color = 'yellow';
    } else if (deaths > kills) {
        deathNode.style.color = 'rgb(255, 77, 77)';
    } else if (deaths < kills) {
        killNode.style.color = 'rgb(92, 214, 92)';
    }
});

const items = document.querySelectorAll('.item');
items.forEach(item => {
    item.childNodes[1].addEventListener('mouseover', () => {
        item.childNodes[3].style.display = 'block';
    });
    item.childNodes[1].addEventListener('mouseout', () => {
        item.childNodes[3].style.display = 'none';
    });
});

// Data for the line graph
const dataset = [
    { duration: 0, kills: 0 },
    { duration: 10, kills: 3 },
    { duration: 20, kills: 5 },
    { duration: 30, kills: 9 },
    { duration: 40, kills: 6 },
    { duration: 50, kills: 8 },
    { duration: 60, kills: 12 },
    // Add more data points as needed
  ];
  
 
function makeGraph(data, element, xaxis, yaxis) {
    const margin = { top: 20, right: 20, bottom: 50, left: 50 };
    const width = 500 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;
    const xName = Object.keys(data[0])[0];
    const yName = Object.keys(data[0])[1];

    // Create SVG element
    const svg = d3.select(element)
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

    // Define x and y scales
    const x = d3.scaleLinear()
        .domain([0, d3.max(data, d => d[xName])])
        .range([0, width]);

    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d[yName])])
        .range([height, 0]);

    // Create area gradient
    const gradient = svg.append("defs").append("linearGradient")
        .attr("id", "area-gradient")
        .attr("x1", 0)
        .attr("y1", 0)
        .attr("x2", 0)
        .attr("y2", "100%");

    gradient.append("stop")
        .attr("offset", "0%")
        .style("stop-color", "lightsteelblue")
        .style("stop-opacity", 1);

    gradient.append("stop")
        .attr("offset", "100%")
        .style("stop-color", "lightsteelblue")
        .style("stop-opacity", 0.2);

    // Create area under the line
    const area = d3.area()
        .x(d => x(d[xName]))
        .y0(y(0))
        .y1(d => y(d[yName]));

    svg.append("path")
        .datum(data)
        .attr("fill", "url(#area-gradient)")
        .attr("d", area);

    // Create line
    const line = d3.line()
        .x(d => x(d[xName]))
        .y(d => y(d[yName]));

    svg.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 2)
        .attr("d", line);

    // Add x-axis
    svg.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(d3.axisBottom(x));

    // Add y-axis
    svg.append("g")
        .call(d3.axisLeft(y));

    // Add x-axis label
    svg.append("text")
        .attr("class", "x-axis-label")
        .attr("text-anchor", "end")
        .attr("x", width/2 + 50)
        .attr("y", height + margin.bottom/2 + 10) // Adjust the y position
        .text(xaxis);

    // Add y-axis label
    svg.append("text")
        .attr("class", "y-axis-label")
        .attr("text-anchor", "end")
        .attr("x", -margin.left - 40)
        .attr("y", -margin.top - 20)
        .attr("dy", "0.75em")
        .attr("transform", "rotate(-90)")
        .text(yaxis);

    // Add emphasized point
    const emphasizedPoint = { [xName]: 20, [yName]: 10 }; // Example emphasized data point

    svg.append("circle")
        .attr("class", "emphasized-point")
        .attr("cx", x(emphasizedPoint[xName]))
        .attr("cy", y(emphasizedPoint[yName]))
        .attr("r", 6)
        .attr("fill", "red");
}

makeGraph(dataset, "#chart", "Game Duration (min)", "Kills");