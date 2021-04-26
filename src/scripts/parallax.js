let bg = document.querySelector('.mainpage-img');
    window.addEventListener('mousemove', function(e) {
        let x = e.clientX / window.innerWidth;
        let y = e.clientY / window.innerHeight;  
        bg.style.transform = 'translate(-' + x * 35 + 'px, -' + y * 35 + 'px)';
    });