const data = [ { title: "Одностраничное-приложение", data: "Ваша визитная карта" },
               { title: "Многостраничное-приложение", data: "Сложный многостраничный сайт" },
               { title: "Интернет магазин", data: "Сделаем продающий сайт, полный цикл разработки" },
               { title: "Верстка", data: "Воплотим ваш макет в жизнь. HTML + CSS + JS" },
               { title: "Фото-обработка", data: "Обработка фотографии, коррекция цвета и т.д." }, 
               { title: "Печатная продукция", data: "Дизайн печатной продукции" },
               { title: "Логотип", data: "Развивайте свой бренд. А мы поможем вам с этим" }, 
               { title: "Айдентика", data: "Ваш логотип на одежде, визитных картах, ручках и т.д" }, ];

const arrows = document.querySelectorAll(".dropdown-arrow");

arrows.forEach(arrow => {
    arrow.addEventListener("click", (e) => {
        const menu = document.querySelector(`.dropdown-menu[data-id="${arrow.dataset.id}"]`);
        menu.classList.add("dropdown-menu-active");

        menu.addEventListener("mouseleave", (e) => {
            menu.classList.remove("dropdown-menu-active");
        })

        const elements = menu.querySelectorAll(".dropdown-option");

        elements.forEach(elem => {
            elem.onclick = () => {
                const title = document.querySelector(`.menu-title[data-id="${arrow.dataset.id}"`);
                title.innerHTML = elem.innerText;
                menu.classList.remove("dropdown-menu-active");

                data.forEach(d => {
                    if(d.title == elem.innerHTML) {
                        const subtitle = document.querySelector(`.service-card-subtitle[data-id="${arrow.dataset.id}"`);
                        subtitle.innerText = d.data;
                        console.log(d.data);
                    }
                })
            }
        })
    })
})

