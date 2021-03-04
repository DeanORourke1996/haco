package com.example.haco.helpers

import android.content.ContentProvider
import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import com.example.haco.models.User

var DATABASE_VERSION = 1
const val DATABASE_NAME = "haco_wildfire_local"
const val TABLE_NAME = "Users"
const val COL_USERNAME = "username"
const val COL_DATE_JOINED = "date_joined"
const val COL_LAST_LOGIN = "last_login"
const val COL_IS_ADMIN = "is_admin"
const val COL_IS_ACTIVE = "is_active"
const val COL_IS_STAFF = "is_staff"
const val COL_IS_SUPERUSER = "is_superuser"
const val COL_EMAIL = "email"
const val COL_PASSWORD = "password"
const val COL_COUNTRY = "country"
const val COL_FIRST_NAME = "first_name"
const val COL_LAST_NAME = "last_name"

class DBHandler(context: Context) : SQLiteOpenHelper(context, DATABASE_NAME, null, DATABASE_VERSION) {
    override fun onCreate(db: SQLiteDatabase?) {
        val createTable = "CREATE TABLE " + TABLE_NAME + " (" +
                COL_USERNAME + " TEXT PRIMARY KEY, " +
                COL_DATE_JOINED + "TEXT, " +
                COL_LAST_LOGIN + "TEXT, " +
                COL_IS_ADMIN + "INTEGER, " +
                COL_IS_ACTIVE + "INTEGER, " +
                COL_IS_STAFF + "INTEGER, " +
                COL_IS_SUPERUSER + "INTEGER, " +
                COL_EMAIL + "TEXT, " +
                COL_PASSWORD + "TEXT, " +
                COL_COUNTRY + "TEXT, " +
                COL_FIRST_NAME + "TEXT, " +
                COL_LAST_NAME + "TEXT) "
        db?.execSQL(createTable)

    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {

    }

    fun insertUser(user: User){
        val db = this.writableDatabase
        var cv = ContentValues()

        cv.put(COL_USERNAME, user.username)
        cv.put(COL_DATE_JOINED, user.dateJoined)
        cv.put(COL_LAST_LOGIN, user.lastLogin)
        cv.put(COL_IS_ADMIN, user.isAdmin)
        cv.put(COL_IS_ACTIVE, user.isActive)
        cv.put(COL_IS_STAFF, user.isStaff)
        cv.put(COL_IS_SUPERUSER, user.isSuperuser)
        cv.put(COL_EMAIL, user.email)
        cv.put(COL_PASSWORD, user.password)
        cv.put(COL_COUNTRY, user.country)
        cv.put(COL_FIRST_NAME, user.firstName)
        cv.put(COL_LAST_NAME, user.lastName)

    }
    
}