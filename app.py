from dash import Dash, html, dcc, register_page, callback,Output,Input
import dash
from dashapp import create_dash_app
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn

app = FastAPI()

#myapp = dash_app

mydashapp = create_dash_app(requests_pathname_prefix="/")
app.mount("/", WSGIMiddleware(mydashapp.server))

from flask import send_from_directory

#@app.route('/static/<path:path>')
#def static_file(path):
#    static_folder = os.path.join(os.getcwd(), 'static')
#    return send_from_directory(static_folder, path)


if __name__ == '__main__':
	#app.run(debug=True)
	uvicorn.run(app, port=8000)