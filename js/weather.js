
// Api de clima
const result = document.querySelector('.result');
const form = document.querySelector('.get-weather');
const nameCity = document.querySelector('#city');
const nameCountry = document.querySelector('#country');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    if (nameCity.value === '' || nameCountry.value === '') {
        showError('Obligatorio...');
        return;
    }

    callAPI(nameCity.value, nameCountry.value);
});

function callAPI(city, country) {
    const apiId = 'f62bff16b1533c8b7d9c1001e211dc56';
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city},${country}&appid=${apiId}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.cod === '404') {
                showError('Ciudad no encontrada');
            } else {
                clearHTML(); // Limpiar el error
                showWeather(data);
            }
        })
        .catch(error => {
            console.log(error);
            showError('Hubo un problema al obtener los datos');
        });
}

function showWeather(data) {
    const { name, main: { temp, temp_min, temp_max }, weather } = data;
    const { icon } = weather[0];

    const degrees = kelvinToCelsius(temp); // Cambio de Kelvin a centígrados
    const min = kelvinToCelsius(temp_min); // Cambio de Kelvin a centígrados
    const max = kelvinToCelsius(temp_max); // Cambio de Kelvin a centígrados

    const content = document.createElement('div');
    content.innerHTML = `
        <h5>Clima en ${name}</h5>
        <img src="https://openweathermap.org/img/wn/${icon}@2x.png" alt="icon">
        <h2>${degrees}°C</h2>
        <p>Max.: ${max}°</p>
        <p>Min.: ${min}°</p>
    `;

    result.appendChild(content);
}

function showError(message) {
    console.log(message);
    const alert = document.createElement('p');
    alert.classList.add('alert-message');
    alert.innerHTML = message;

    form.appendChild(alert);
    setTimeout(() => {
        alert.remove();
    }, 3000);
}

function kelvinToCelsius(temp) {
    return parseInt(temp - 273.15);
}

function clearHTML() {
    result.innerHTML = '';
}
