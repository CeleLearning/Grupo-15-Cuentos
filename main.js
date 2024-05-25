// Mostrar buscador
const searchButton = document.getElementById('search-button');
const buscadorClose = document.getElementById('buscador-close');
const buscadorCont = document.getElementById('buscador-container');

// Buscador mostrar
if (searchButton) {
    searchButton.addEventListener('click', () => {
        buscadorCont.classList.add('show-search');
    });
}

// Salida del buscador
if (buscadorClose) {
    buscadorClose.addEventListener('click', () => {
        buscadorCont.classList.remove('show-search');
    });
}

// Mostrar formulario de inicio de sesión
const loginButton = document.getElementById('login-button');
const registroClose = document.getElementById('registro-close');
const registroCont = document.getElementById('registro-container');

// Mostrar formulario de inicio de sesión
if (loginButton) {
    loginButton.addEventListener('click', () => {
        registroCont.classList.add('show-login');
    });
}

// Salida del formulario de inicio de sesión
if (registroClose) {
    registroClose.addEventListener('click', () => {
        registroCont.classList.remove('show-login');
    });
}


var swiper = new Swiper('.swiper-container', {
    slidesPerView: 'auto', 
    spaceBetween: 10, 
    centeredSlides: true, 
    loop: true, 
    navigation: {a
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});



// header
const shadowHeader = () => {
    const header = document.getElementById('header');

    window.scrollY >= 50 ? header.classList.add('shadow-header') : header.classList.remove('shadow-header');
};
window.addEventListener('scroll', shadowHeader);
