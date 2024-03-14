from flask import Flask, g, render_template, request, redirect
import flask_login
import pymysql
import pymysql.cursors
from flask_httpauth import HTTPBasicAuth
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_file=['settings.toml']
)

def connect_db():
    return pymysql.connect(
        host="10.100.33.60",
        user=settings.user,
        password=settings.passw,
        database=settings.name,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )