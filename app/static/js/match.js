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


const labels = [player_data['summonerName'], 'Average ' + player_data['championName']];
console.log(labels);