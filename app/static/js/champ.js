const winrate = document.querySelector('.winrate');
const winrateNum = parseFloat(winrate.innerHTML);
if (winrateNum < 50) {
    winrate.style.color = 'rgb(255, 77, 77)';
} else if (winrateNum > 50) {
    winrate.style.color = 'rgb(92, 214, 92)';
};

function makeScatterPlot(x, y, championData, element, data, championName) {
new Chart(element, {
    type: 'scatter',
    data: {
    datasets: [
        {
        label: `${championName}'s KDA vs. Win Rate`,
        data: championData, // Array with only the emphasized point
        backgroundColor: 'rgba(255, 0, 0, 1)', // Red color for emphasis
        borderColor: 'rgba(255, 0, 0, 1)',
        pointRadius: 6,
        pointHoverRadius: 10,
        },{
        label: 'KDA vs. Win Rate',
        data: data,
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        pointRadius: 3,
    }],
    },
    options: {
    responsive: true,
    plugins: {
        legend: {
            labels: {
                color: "white",
            }
        }
    },
    scales: {
        x: {
        ticks: {
            color: "white",
        },
        grid: {
            color: "rgba(255,255,255,0.6)",
        },
        type: 'linear',
        position: 'bottom',
        scaleLabel: {
            display: true,
            labelString: x
        },
        min: 0,
        max: 5
        },
        y: {
        ticks: {
            color: "white",
        },
        grid: {
            color: "rgba(255,255,255,0.6)",
        },
        type: 'linear',
        scaleLabel: {
            display: true,
            labelString: y
        },
        min: 0,
        max: 100
        }
    },
    }
});
}

const winrateGraph = document.querySelector('.winrate-graph');
console.log(winrate_data)
const championWinrate = [{
    'x': (champ_data['kills'] + champ_data['assists'])/champ_data['deaths'],
    'y': champ_data['winRate']
}];
console.log(championWinrate)
makeScatterPlot('Game Duration', 'Win Rate', championWinrate, winrateGraph, winrate_data, champ_name);


const items = document.querySelectorAll('.item');
items.forEach(item => {
    item.childNodes[1].addEventListener('mouseover', () => {
        item.childNodes[3].style.display = 'block';
    });
    item.childNodes[1].addEventListener('mouseout', () => {
        item.childNodes[3].style.display = 'none';
    });
});

console.log(rune_data);

// const runeColumns = document.querySelectorAll('.column');
// runeColumns.forEach(column => {
//     const runePics = column.childNodes;
//     for (var i = 0; i < Math.floor(runePics.length/4); i++) {
//         console.log(i, runePics[i*4+1], runePics[(i+1)*4-1])
//         runePics[i*4+1].addEventListener('mouseover', () => {
//             (runePics[(i+1)*4-1]).style.display = 'block';
//         });
//         runePics[i*4+1].addEventListener('mouseout', () => {   
//             (runePics[(i+1)*4-1]).style.display = 'none';
//         });
//     }
// });