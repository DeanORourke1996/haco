package com.example.haco.activities

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.haco.databinding.ActivityMainBinding
import com.example.haco.helpers.AmbeeAPIClient

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        initMapData()


        /******************************************
        **  EVENT LISTENERS FOR SWITICHING CONTEXTS
         ******************************************/
        // Login Intent
        binding.btnNavLogin.setOnClickListener() {
            val intent = Intent(this, Login::class.java)
            startActivity(intent)
        }

        // Register Intent
        binding.btnNavProfile.setOnClickListener() {
            val intent = Intent(this, Profile::class.java)
            startActivity(intent)
        }

        // Profile Intent
        binding.btnNavProfile.setOnClickListener() {
            val intent = Intent(this, ReportTool::class.java)
            startActivity(intent)
        }

        // more intents to come...
    }


    private fun initMapData() {
        val api = AmbeeAPIClient
        api.callAmbee()
    }
}