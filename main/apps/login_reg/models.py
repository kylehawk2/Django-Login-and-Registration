# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validation(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "User name must be more than two characters!"
        # if '@' not in len(postData["email"]):
        #     errors["email"] = "User email must have an @ symbol!"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address!"
        if len(postData['password']) < 4:
            errors["password"] = "Password must be at least 4 characters long!"
        if postData['password'] != postData['cpassword']:
            errors['password'] = "Passwords do not match!"
        return errors 
    
    def login(self, postData):
        print ("validating")
        errors = {}
        if len(postData["email"]) < 1:
            errors["email"] = "Must enter in a email address"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Email address is not valid"
        if len(postData['password']) < 5:
            errors["password"] = "Password must contain at least 6 characters"


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __repr__(self):
    #     return "<User object: {} {}>".format(self.name, self.email)

    objects = UserManager()