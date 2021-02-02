package com.example.haco.helpers

import okhttp3.*
import java.io.IOException

object AmbeeAPIClient {
    private const val BASE_URL = "https://api.ambeedata.com/latest/fire"
    private const val API_TOKEN = "WTAiAW33D04pu4l1v7T7r1okNOz5FSU7aPBZk49j"

    private val client = OkHttpClient()

    fun callAmbee() {

        // Create a request
        val request = Request.Builder()
            .url(BASE_URL)
            .get()
            .addHeader("x-api-key", API_TOKEN)
            .addHeader("Content-type", "application/json")
            .build();


        // Add request to client and execute
        val response = client.newCall(request).enqueue(object : Callback {
            override fun onResponse(call: Call, response: Response) {
                val body = response.body?.string()
                println("Connection was a success!")
            }

            override fun onFailure(call: Call, e: IOException) {
                println("Failed to complete request")
            }

        })
    }
}