const person = document.querySelector(".person-btn");
const confid = document.querySelector(".confid-btn");
const order = document.querySelector(".order-btn");

const personalInfo = document.querySelector(".personal-info");
const confidentiality = document.querySelector(".confidentiality");
const orderBlock = document.querySelector(".orders");

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