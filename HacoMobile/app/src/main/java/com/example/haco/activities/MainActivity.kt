package com.example.haco.activities

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Window
import com.example.haco.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        /******************************************
        **  EVENT LISTENERS FOR SWITICHING CONTEXTS
         ******************************************/
        /*// Login Intent
        binding.btnNavLogin.setOnClickListener() {
            val intent = Intent(this, Login::class.java)
            startActivity(intent)
        }

        // Register Intent
        binding.btnNavRegister.setOnClickListener() {
            val intent = Intent(this, Register::class.java)
            startActivity(intent)
        }

        // Profile Intent
        binding.btnNavProfile.setOnClickListener() {
            val intent = Intent(this, ReportTool::class.java)
            startActivity(intent)
        }*/

        // more intents to come...
    }
}