const scrollbar = document.querySelector('.scroll');
const progressbar = document.querySelector('.progress');

window.addEventListener('scroll', e => {
    console.log(window.scrollY);
    progressbar.style.height = (document.body.offsetHeight / window.scrollY) * scrollbar.style.height + " px";
    
})