from flask import Flask, render_template, request, session, redirect, url_for, jsonify


app = Flask(__name__)

@app.route("/", methods=["GET"])
def show_upload():
    return render_template("upload.html")

@app.route("/upload-lineup", methods=["POST"])
def upload_lineup():
    # right now, just confirm Flask sees the upload
    file = request.files.get("file")
    if not file:
        return "No file received", 400
    return f"Got {file.filename}", 200