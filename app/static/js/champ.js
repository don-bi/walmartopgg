const winrate = document.querySelector('.winrate');
const winrateNum = parseFloat(winrate.innerHTML);
if (winrateNum < 50) {
    winrate.style.color = 'rgb(255, 77, 77)';
} else if (winrateNum > 50) {
    winrate.style.color = 'rgb(92, 214, 92)';
};

function makeScatterPlot(x, y, championData, element, data) {
new Chart(element, {
    type: 'scatter',
    data: {
    datasets: [
        {
        label: 'Emphasized Point',
        data: championData, // Array with only the emphasized point
        backgroundColor: 'rgba(255, 0, 0, 1)', // Red color for emphasis
        borderColor: 'rgba(255, 0, 0, 1)',
        pointRadius: 8,
        pointHoverRadius: 10,
        },{
        label: 'Game Duration vs. Win Rate',
        data: data,
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        pointRadius: 6,
    }],
    },
    options: {
    scales: {
        x: {
        type: 'linear',
        position: 'bottom',
        scaleLabel: {
            display: true,
            labelString: x
        }
        },
        y: {
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
    'x': champ_data['winRate'], 
    'y': champ_data['gameDuration']/60
}];
console.log(championWinrate)
makeScatterPlot('Game Duration', 'Win Rate', championWinrate, winrateGraph, winrate_data);
