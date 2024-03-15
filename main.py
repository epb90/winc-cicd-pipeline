from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

@pp.route('/')
def index():
    return render_template('index.html', title="Index")