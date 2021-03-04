package com.example.haco.models

class User {

    var username: String = ""
    var dateJoined: String = ""
    var lastLogin: String = ""
    var isAdmin: String = ""
    var isSuperuser: Boolean? = null
    var isActive: Boolean? = null
    var isStaff: Boolean? = null
    var email: String = ""
    var password: String = ""
    var country: String = ""
    var firstName: String = ""
    var lastName: String = ""

    // Constructor
    constructor(_username:String, _dateJoined:String,
                _lastLogin:String, _isAdmin: String,
                _isSuperuser:Boolean, _isActive:Boolean,
                _isStaff:Boolean, _email:String,
                _country:String, _password:String,
                _firstName:String, _lastName:String
    ){
        this.username = _username
        this.dateJoined = _dateJoined
        this.lastLogin = _lastLogin
        this.isAdmin = _isAdmin
        this.isSuperuser = _isSuperuser
        this.isActive = _isActive
        this.isStaff = _isStaff
        this.email = _email
        this.password = _password
        this.country = _country
        this.firstName = _firstName
        this.lastName = _lastName
    }



}