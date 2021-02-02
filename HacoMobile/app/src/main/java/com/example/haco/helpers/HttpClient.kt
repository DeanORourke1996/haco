package com.example.haco.helpers

import com.loopj.android.http.AsyncHttpClient
import com.loopj.android.http.AsyncHttpResponseHandler
import com.loopj.android.http.RequestParams

object HttpClient {
    private const val BASE_URL = "http://api.twitter.com/1/"
    private val client = AsyncHttpClient()
    operator fun get(
        url: String,
        params: RequestParams?,
        responseHandler: AsyncHttpResponseHandler?
    ) {
        client[getAbsoluteUrl(url), params, responseHandler]
    }

    fun post(
        url: String,
        params: RequestParams?,
        responseHandler: AsyncHttpResponseHandler?
    ) {
        client.post(
            getAbsoluteUrl(url),
            params,
            responseHandler
        )
    }

    fun getByUrl(
        url: String?,
        params: RequestParams?,
        responseHandler: AsyncHttpResponseHandler?
    ) {
        client[url, params, responseHandler]
    }

    fun postByUrl(
        url: String?,
        params: RequestParams?,
        responseHandler: AsyncHttpResponseHandler?
    ) {
        client.post(url, params, responseHandler)
    }

    private fun getAbsoluteUrl(relativeUrl: String): String {
        return BASE_URL + relativeUrl
    }
}