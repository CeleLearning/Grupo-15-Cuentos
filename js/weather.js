
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
    const url = `http://api.openweathermap.org/data/2.5/weather?q=${city},${country}&appid=${apiId}`;

    fetch(url)
        .then(data => data.json())
        .then(dataJSON => {
            if (dataJSON.cod === '404') {
                showError('Ciudad no encontrada');
            } else {
                clearHTML(); // Limpiar el error
                showWeather(dataJSON);
            }
        })
        .catch(error => {
            console.log(error);
        });
}

function showWeather(data) {
    const { name, weather: { temp, temp_min, temp_max }, weather: [arr] } = data;

    const degrees = kelvinToCentigrade(temp); // Cambio de Kelvin a centígrados
    const min = kelvinToCentigrade(temp_min); // Cambio de Kelvin a centígrados
    const max = kelvinToCentigrade(temp_max); // Cambio de Kelvin a centígrados

    const content = document.createElement('div');
    content.innerHTML = `
        <h5>Clima en ${name}</h5>
        <img src="https://openweathermap.org/img/wn/${arr.icon}@2x.png" alt="icon">
        <h2>${degrees}°C</h2>
        <p>Max.: ${max}°</p>
        <p>Min.: ${min}°</p>
    `;

    result.appendChild(content);
    /* 
     console.log(name);
     console.log(temp);
     console.log(temp_max);
     console.log(temp_min);
     console.log(arr.ico);
 
 */
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

function kelvinToCentigrade(temp) {
    return parseInt(temp - 273.15);
}

function clearHTML() {
    result.innerHTML = '';
}