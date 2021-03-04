package com.example.haco.helpers
import okhttp3.*
import java.io.IOException

class AmbeeAPIClient : ApiProvider {
    override val url = "https://api.ambeedata.com/latest/fire"
    override val apiToken = "WTAiAW33D04pu4l1v7T7r1okNOz5FSU7aPBZk49j"
    override val client = OkHttpClient()

    override fun createRequest(): Request {
        // Create a request
        val request = Request.Builder()
            .url(url)
            .get()
            .addHeader("x-api-key", apiToken)
            .addHeader("Content-type", "application/json")
            .build();

        return request
    }


    override fun callAPI(request: Request) {
        // Add request to client and execute
        return client.newCall(request).enqueue(object : Callback {
            override fun onResponse(call: Call, response: Response) {
                val body = response.body?.string()
                println("Connection successful, parsing objects...\nData returned: $body")
            }

            override fun onFailure(call: Call, e: IOException) {
                println("Failed to complete request")
            }
        })
    }
}