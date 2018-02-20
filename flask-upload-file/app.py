# -*- encoding: utf-8 -*-
from flask import Flask, request, Response
from flask import render_template, redirect, url_for,jsonify
from flask_cors import *
import os
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/", methods=["GET", "POST"])
def temp():
    return render_template('index.html')


@app.route("/upload", methods=["POST"])
def upload():
    f = request.files['file']
    basepath = os.path.dirname(__file__)
    upload_path = os.path.join(basepath, "static", "uploads", f.filename)
    f.save(upload_path)
    return jsonify({"file": f.filename})


@app.route("/img/<imgid>")
def get_img(imgid):
    basepath = os.path.dirname(__file__)
    image = open(os.path.join(basepath, "static", "uploads", str(imgid)), "rb")
    resp = Response(image, mimetype="image/jpeg")
    return resp


@app.route("/video/<video_id>")
def get_video(video_id):
    basepath = os.path.dirname(__file__)
    image = open(os.path.join("L:\电影", str(video_id)), "rb")
    resp = Response(image, mimetype="video/x-msvideo")
    return resp


@app.route("/mp3/<mid>")
def get_mp3(mid):
    basepath = os.path.dirname(__file__)
    image = open(os.path.join(basepath, "static", "uploads", str(mid)), "rb")
    resp = Response(image, mimetype="audio/mpeg")
    return resp


if __name__ == '__main__':
    # 0.0.0.0 all ip can browse
    app.run(host="0.0.0.0", port=9999, debug=True)



