#!/usr/local/bin/python3.7

import datetime
from bottle import run, get, post, request, template
        
@get("/")
def get():
    return template('page')

@post("/")
def post():
    now = datetime.datetime.now() 
    with open(now.strftime("dat/post_%y%m%d_%H%M%S.txt"), 'w') as f:
        f.write(now.strftime("%Y-%m-%d %H:%M:%S")+"\n")
        f.write(request.environ.get('REMOTE_ADDR')+"\n")
        f.write(request.environ.get('HTTP_USER_AGENT')+"\n\n")
        f.write(request.forms.story)
    return template('page')
    
# run(host='localhost', port=8080, debug=True, reloader=True)
run(server='cgi')
