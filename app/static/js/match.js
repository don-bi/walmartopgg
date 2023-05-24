const baronIcon = document.querySelector('.baron-icon');
const dragonIcon = document.querySelector('.dragon-icon');
const topMinionIcon = document.querySelector('.top.minion-icon');
const midMinionIcon = document.querySelector('.mid.minion-icon');
const botMinionIcon = document.querySelector('.bot.minion-icon');
const icons = [baronIcon, dragonIcon, topMinionIcon, midMinionIcon, botMinionIcon];

const baronKills = document.querySelector('.baron-kills');
const dragonKills = document.querySelector('.dragon-kills');
const topMinionKills = document.querySelector('.top-minion-kills');
const midMinionKills = document.querySelector('.mid-minion-kills');
console.log(midMinionKills);
const botMinionKills = document.querySelector('.bot-minion-kills');
const kills = [baronKills, dragonKills, topMinionKills, midMinionKills, botMinionKills];
icons.forEach((icon,index) => {
    icon.addEventListener('mouseover', () => {
        kills[index].style.display = 'block';
    });
    icon.addEventListener('mouseout', () => {
        kills[index].style.display = 'none';
    });
});


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

function createBarGraph(playerStat, avgStat, element, stat, player, champion) {
    const data = {
        labels: [`${player}'s ${stat}` , `Average ${champion} ${stat}`],
        datasets: [{
            label: `${stat}`,
            data: [playerStat, avgStat],
            backgroundColor: [
            'rgba(153, 221, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            ],
            borderColor: [
            'rgb(153, 221, 255)',
            'rgb(255, 159, 64)',
            ],
            borderWidth: 1
        }]
    }
    const charterMaker = new Chart(element ,{
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            plugins: {
            legend: {
                labels: {
                    color: "white"
                }
            }
            },
            scales: {
            y: {
                ticks: {
                    color: "white",
                },
                grid: {
                    display: false
                },
                beginAtZero: true
            },
            x: {
                ticks: {
                    color: "white",
                },
                grid: {
                    display: false
                },
            }
            }
         }
    });
}

positions[0].concat(positions[1]).forEach(pos => {
    const playerStats = participant_data[pos];
    const championName = playerStats['championName'];
    const champStats = champ_data[championName];
    const champKills = champStats['kills'];
    const champDeaths = champStats['deaths'];
    const champAssists = champStats['assists'];
    const champCS = champStats['cs'];
    const champDamageDealt = champStats['dmgDealt'];
    const champDamageTaken = champStats['dmgTaken'];
    console.log(champDamageDealt, playerStats['totalDamageDealtToChampions']);
    createBarGraph(playerStats['kills'], champKills, document.querySelector(`.player-data.${pos} .kill.chart`), 'Kills', playerStats['summonerName'], championName);
    createBarGraph(playerStats['deaths'], champDeaths, document.querySelector(`.player-data.${pos} .death.chart`), 'Deaths', playerStats['summonerName'], championName);
    createBarGraph(playerStats['assists'], champAssists, document.querySelector(`.player-data.${pos} .assist.chart`), 'Assists', playerStats['summonerName'], championName);
    createBarGraph(playerStats['totalMinionsKilled'] + playerStats['neutralMinionsKilled'], champCS, document.querySelector(`.player-data.${pos} .cs.chart`), 'CS', playerStats['summonerName'], championName);
    createBarGraph(playerStats['totalDamageDealtToChampions'], champDamageDealt, document.querySelector(`.player-data.${pos} .damage-dealt.chart`), 'Damage Dealt', playerStats['summonerName'], championName);
    createBarGraph(playerStats['totalDamageTaken'], champDamageTaken, document.querySelector(`.player-data.${pos} .damage-taken.chart`), 'Damage Taken', playerStats['summonerName'], championName);
});