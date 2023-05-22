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

// Sample data
const gameDuration = Array.from({length: 60}, (x, i) => i);;
var kills = [];
for (var i = 0; i < 60; i++) {
    kills.push(Math.floor(Math.random() * 15));
}
gameDuration.push(40);
kills.push(12);

// Define the data points
const data = {
  labels: ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100','0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
  datasets: [{
    label: 'Kills',
    data: [0, 2, 5, 8, 12, 15, 18, 20, 23, 25, 28, 4, 7, 12, 5, 3, 18, 14, 13, 19, 21, 34],
    backgroundColor: 'rgba(255, 99, 132, 0.5)',
    borderColor: 'rgb(255, 99, 132)',
    borderWidth: 1
  }]
};

// Define the chart options
const options = {
  scales: {
    xAxes: [{
      scaleLabel: {
        display: true,
        labelString: 'Game Duration'
      }
    }],
    yAxes: [{
      scaleLabel: {
        display: true,
        labelString: 'Kills'
      }
    }]
  },
  plugins: {
    regression: {
      type: 'loess'
    }
  }
};

// Create the chart object
const ctx = document.querySelector('.kill.chart').getContext('2d');
const myChart = new Chart(ctx, {
  type: 'scatter',
  data: data,
  options: options
});