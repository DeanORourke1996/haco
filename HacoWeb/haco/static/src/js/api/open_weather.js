// Recursive function to return live data to the async callback
function liveWeatherFeed(_lat, _lon) {
    let url = `https://api.openweathermap.org/data/2.5/weather?lat=${_lat}&lon=${_lon}&appid=518b54b7cfd7c1047999fb4815eab4a5`;
    let weather_data = [];

    // Promise
    fetch(url)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(e => console.log(e.message))

    return weather_data;
}