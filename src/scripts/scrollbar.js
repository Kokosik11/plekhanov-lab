const scrollbar = document.querySelector('.scroll');
const progressbar = document.querySelector('.progress');

window.addEventListener('scroll', e => {
    let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrolled = (winScroll / height) * 100;
    progressbar.setAttribute("style", `height: ${scrolled}%`)
    
})