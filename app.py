#!/usr/bin/env python3
import os
import uuid
from flask import Flask, request, render_template, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from whisper_transcribe import transcribe_audio

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["OUTPUT_FOLDER"] = "transcriptions"
app.config["ALLOWED_EXTENSIONS"] = {"mp3", "wav", "ogg", "flac", "m4a"}
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB max upload

# Create necessary directories
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    # Check if file is provided
    if "file" not in request.files and not request.form.get("audio_path"):
        return jsonify({"error": "No file or path provided"}), 400
    
    model = request.form.get("model", "base")
    
    # Handle direct file upload
    if "file" in request.files and request.files["file"].filename:
        file = request.files["file"]
        if not allowed_file(file.filename):
            return jsonify({"error": "File type not allowed"}), 400
        
        # Generate unique filename
        original_filename = secure_filename(file.filename)
        filename = f"{uuid.uuid4()}_{original_filename}"
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
    
    # Handle file path input
    elif request.form.get("audio_path"):
        filepath = request.form.get("audio_path")
        if not os.path.exists(filepath):
            return jsonify({"error": "File not found"}), 404
        filename = os.path.basename(filepath)
    
    else:
        return jsonify({"error": "No valid file provided"}), 400
    
    try:
        # Perform transcription
        text = transcribe_audio(filepath, model, app.config["OUTPUT_FOLDER"])
        
        # Get the base filename for download links
        base_filename = os.path.splitext(filename)[0]
        if "file" in request.files:  # If uploaded, use the UUID version
            base_filename = os.path.splitext(filename)[0]
        else:  # If path provided, use original name
            base_filename = os.path.splitext(os.path.basename(filepath))[0]
        
        # Prepare download links
        download_links = {
            "txt": f"/download/{base_filename}.txt",
            "json": f"/download/{base_filename}.json",
            "srt": f"/download/{base_filename}.srt",
            "vtt": f"/download/{base_filename}.vtt",
            "tsv": f"/download/{base_filename}.tsv",
        }
        
        return jsonify({
            "text": text,
            "download_links": download_links
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True) 