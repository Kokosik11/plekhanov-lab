const person = document.querySelector(".person-btn");
const confid = document.querySelector(".confid-btn");
const order = document.querySelector(".order-btn");

const personalInfo = document.querySelector(".personal-info");
const confidentiality = document.querySelector(".confidentiality");
const orderBlock = document.querySelector(".orders");

const day = document.querySelector(".day");
const month = document.querySelector(".month");
const year = document.querySelector(".year");

person.onclick = () => {
    const active = document.querySelector(".active");
    active.classList.remove("active");
    person.classList.add("active");

    personalInfo.style.display = "block";
    confidentiality.style.display = "none";
    orderBlock.style.display = "none";
}

confid.onclick = () => {
    const active = document.querySelector(".active");
    active.classList.remove("active");
    confid.classList.add("active");

    personalInfo.style.display = "none";
    confidentiality.style.display = "block";
    orderBlock.style.display = "none";
}

order.onclick = () => {
    const active = document.querySelector(".active");
    active.classList.remove("active");
    order.classList.add("active");

    personalInfo.style.display = "none";
    confidentiality.style.display = "none";
    orderBlock.style.display = "block";
}

const dayOptions = () => {
    for(let i = 0; i < 31; i++) {
        day.innerHTML += `<option value=${i+1}>${i+1}</option>`;
    }
}

const monthOptions = () => {
    const months = ["Янв", "Фев", "Март", "Апр", "Май", "Июнь", "Июль", "Авг", "Сен", "Окт", "Ноя", "Дек"];
    for(let i = 0; i < months.length; i++) {
        month.innerHTML += `<option value=${i}>${months[i]}</option>`;
    }
}

const yearOptions = () => {
    for(let i = 1920; i < 2021; i++) {
        year.innerHTML += `<option value=${i}>${i}</option>`;
    }
}

const options = () => {
    dayOptions();
    monthOptions();
    yearOptions();
} 

options();