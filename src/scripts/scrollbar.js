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
    }

    if(scrolled >= 40) {
        const anchor = document.querySelector('.anchor[data-id="3"]');
        anchor.classList.add("active-anchor")
    }

    if(scrolled >= 72) {
        const anchor = document.querySelector('.anchor[data-id="4"]');
        anchor.classList.add("active-anchor")
    }
    
    if(scrolled >= 87) {
        const anchor = document.querySelector('.anchor[data-id="5"]');
        anchor.classList.add("active-anchor")
    }

    if(scrolled >= 97) {
        const anchor = document.querySelector('.anchor[data-id="6"]');
        anchor.classList.add("active-anchor")
    }

    if(scrolled < 97) {
        const anchor = document.querySelector('.anchor[data-id="6"]');
        anchor.classList.remove("active-anchor")
    }

    if(scrolled < 87) {
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


    // Надписи
    if(scrolled < 2.5) {
        const anchor = document.querySelector('.anchor[data-id="1"] > .anchor-title');
        anchor.classList.add("active-title")
    } 

    if(scrolled >= 2.5) {
        const anchor = document.querySelector('.anchor[data-id="1"] > .anchor-title');
        anchor.classList.remove("active-title")
    }

    if(scrolled > 18.5 && scrolled < 25) {
        const anchor = document.querySelector('.anchor[data-id="2"] > .anchor-title');
        anchor.classList.add("active-title")
    }

    if(scrolled <= 18.5 || scrolled >= 25) {
        const anchor = document.querySelector('.anchor[data-id="2"] > .anchor-title');
        anchor.classList.remove("active-title")
    }

    if(scrolled > 39.4 && scrolled < 45) {
        const anchor = document.querySelector('.anchor[data-id="3"] > .anchor-title');
        anchor.classList.add("active-title")
    }

    if(scrolled <= 39.4 || scrolled >= 45) {
        const anchor = document.querySelector('.anchor[data-id="3"] > .anchor-title');
        anchor.classList.remove("active-title")
    }
    
    if(scrolled > 71.8 && scrolled < 76) {
        const anchor = document.querySelector('.anchor[data-id="4"] > .anchor-title');
        anchor.classList.add("active-title")
    }

    if(scrolled <= 71.8 || scrolled >= 76) {
        const anchor = document.querySelector('.anchor[data-id="4"] > .anchor-title');
        anchor.classList.remove("active-title")
    }

    if(scrolled > 87.7 && scrolled < 93) {
        const anchor = document.querySelector('.anchor[data-id="5"] > .anchor-title');
        anchor.classList.add("active-title")
    }

    if(scrolled <= 87.7 || scrolled >= 93) {
        const anchor = document.querySelector('.anchor[data-id="5"] > .anchor-title');
        anchor.classList.remove("active-title")
    }

    if(scrolled < 97) {
        const anchor = document.querySelector('.anchor[data-id="6"] > .anchor-title');
        anchor.classList.remove("active-title")
    } 

    if(scrolled >= 97) {
        const anchor = document.querySelector('.anchor[data-id="6"] > .anchor-title');
        anchor.classList.add("active-title")

    }
})

const anchors = document.querySelectorAll(".anchor");

anchors[0].onclick = () => {
    window.location.hash = "#top";
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

anchors[5].onclick = () => {
    window.location.hash = "#fifth";
}