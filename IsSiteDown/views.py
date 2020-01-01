"""
Project: Is site down
Author: Rudra Sarkar 🦸‍♂️
Twitter: @rudr4_sarkar
"""

from datetime import datetime
from flask import *
from IsSiteDown import app
import requests as rs
from flask_toastr import Toastr

toastr = Toastr(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contact'
    )

@app.route('/status', methods=['GET', 'POST'])
def checkStatus():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    if request.method == "POST":
        site = request.form['domain']

        if 'http://' in site or 'https://' in site:
            try:
                req = rs.get(site, timeout=5, stream=True, headers=headers)
                return render_template(
                    'result.html',
                    title='Result',
                    year=datetime.now().year,
                    result_status = str(req.status_code)
                    )
            except:
                try:
                    req = rs.get('http://'+site, timeout=5, stream=True, headers=headers)
                    return render_template(
                        'result.html',
                        title='Result',
                        year=datetime.now().year,
                        result_status = str(req.status_code)
                        )
                except rs.exceptions.ConnectionError as e:
                    return render_template(
                        'result.html',
                        title='Result',
                        year=datetime.now().year,
                        result_status = 'Connection refused!'
                        )

        elif site == '':
            flash('Please fill domain Name', 'error')
            return redirect('/')
        else:
            try:
                req = rs.get('http://'+site, timeout=5, stream=True, headers=headers)
                return render_template(
                    'result.html',
                    title='Result',
                    year=datetime.now().year,
                    result_status = str(req.status_code)
                    )
            except:
                return 'Can not able to work on here :/'

    # Get Request
    elif request.method == 'GET':
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        '404.html',
        title='Page Not Found',
        year=datetime.now().year
        ), 404