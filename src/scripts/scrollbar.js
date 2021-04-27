const scrollbar = document.querySelector('.scroll');
const progressbar = document.querySelector('.progress');

window.addEventListener('scroll', e => {
    let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrolled = (winScroll / height) * 100;
    progressbar.setAttribute("style", `height: ${scrolled}%`)

    if(scrolled >= 20) {
        const anchor = document.querySelector('.anchor[data-id="2"]');
        anchor.classList.add("active-anchor")
        setInterval(() => {
            anchor.classList.add("anchor-before")
        }, 1000)
    }

    if(scrolled >= 40) {
        const anchor = document.querySelector('.anchor[data-id="3"]');
        anchor.classList.add("active-anchor")
    }

    if(scrolled >= 72) {
        const anchor = document.querySelector('.anchor[data-id="4"]');
        anchor.classList.add("active-anchor")
    }

    if(scrolled >= 100) {
        const anchor = document.querySelector('.anchor[data-id="5"]');
        anchor.classList.add("active-anchor")
    }

    if(scrolled < 100) {
        const anchor = document.querySelector('.anchor[data-id="5"]');
        anchor.classList.remove("active-anchor")
    }

    if(scrolled < 72) {
        const anchor = document.querySelector('.anchor[data-id="4"]');
        anchor.classList.remove("active-anchor")
    }

    if(scrolled < 40) {
        const anchor = document.querySelector('.anchor[data-id="3"]');
        anchor.classList.remove("active-anchor")
    }

    if(scrolled < 20) {
        const anchor = document.querySelector('.anchor[data-id="2"]');
        anchor.classList.remove("active-anchor")
    }
})

const anchors = document.querySelectorAll(".anchor");

anchors[0].onclick = () => {
    window.scrollTo(0, 0);
}

anchors[1].onclick = () => {
    window.location.hash = "#first";
}

anchors[2].onclick = () => {
    window.location.hash = "#second";

}

anchors[3].onclick = () => {
    window.location.hash = "#third";
}

anchors[4].onclick = () => {
    window.location.hash = "#fourth";

}