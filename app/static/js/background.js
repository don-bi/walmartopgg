const backgroundList = [
    'https://wallpaperaccess.com/full/3823169.jpg',
    'https://wallpaperaccess.com/full/3823177.jpg',

]

const body = document.querySelector('body');
const randomBackground = backgroundList[Math.floor(Math.random() * backgroundList.length)];
body.style.background = `linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url(${randomBackground})`
