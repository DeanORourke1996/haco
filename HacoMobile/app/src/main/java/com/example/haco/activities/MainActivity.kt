package com.example.haco.activities

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import com.example.haco.R
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Login Intent
        btn_nav_login.setOnClickListener {
            val intent = Intent(this, Login::class.java)
            startActivity(intent)
        }

        // Register Intent
        btn_nav_profile.setOnClickListener {
            val intent = Intent(this, Profile::class.java)
            startActivity(intent)
        }
    }



    /*private fun simulateHeavyLayout() {
        // simulate some heavy UI inflation
        for(i in 0..1000000){
            val d = tan(atan(tan(atan(tan(atan(tan(atan(tan(kotlin.math.atan(123456789.123456789))))))))))
            d.toString()
        }
    }*/
}