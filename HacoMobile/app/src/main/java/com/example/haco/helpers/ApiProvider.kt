package com.example.haco.helpers
import okhttp3.*

interface ApiProvider {
    // Properties
    val url: String
    val apiToken: String
    val client: OkHttpClient

    // Methods
    fun createRequest(): Request
    fun callAPI(request: Request)
}