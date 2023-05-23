const input = document.querySelector('input');
input.addEventListener('click', showSearch);
window.addEventListener('keyup', showSearch);
window.addEventListener('click', cancelSearch, true);

function showSearch() {
    const current = input.value;
    const champBox = document.querySelector('.champ-names');
    var count = 0;
    champBox.style.display = 'none';
    champ_names.forEach(name => {
        if (name == "MonkeyKing") name = "Wukong"; 
        const champ = document.querySelector(`.${name}`);
        champ.style.display = 'none';
        if (current != ""){
            if (name.toLowerCase().includes(current.toLowerCase())) {
                champBox.style.display = 'block';
                champ.style.display = 'block';
                count ++;
            };
        };
    });
    if (count < 5) champBox.style.height = `${count * 6}vh`;
    else {champBox.style.height = '30vh';}
}

function cancelSearch() {
    const champBox = document.querySelector('.champ-names');
    champBox.style.display = 'none';
    champ_names.forEach(name => {
        const champ = document.querySelector(`.${name}`);
        champ.style.display = 'none';
    });
}