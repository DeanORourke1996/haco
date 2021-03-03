package com.example.haco.helpers
import okhttp3.*
import java.io.IOException

class WeatherEvents : ApiProvider {
    override val apiToken = "518b54b7cfd7c1047999fb4815eab4a5"
    override val url = "https://api.openweathermap.org/data/2.5/weather?lat=50.5&lon=6.23&appid=$apiToken"
    override val client = OkHttpClient()

    // Create Weather Request
    override fun createRequest(): Request {
        val request = Request.Builder()
            .url(url)
            .get()
            .addHeader("Content-type", "application/json")
            .build();

        return request
    }

    // Call OpenWeatherAPI
    override fun callAPI(request: Request) {
        return client.newCall(request).enqueue(object : Callback {
            override fun onResponse(call: Call, response: Response) {
                val data = response.body?.string()
                println("Connection successful, parsing objects...\nData returned: $data")
            }

            override fun onFailure(call: Call, e: IOException) {
                val data = "{'error': 'data not retrieved for this event'}"
                println("Failed to complete request (e): $data")
            }
        })
    }
}