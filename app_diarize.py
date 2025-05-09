#!/usr/bin/env python3
import os
import uuid
import json
import time
from flask import Flask, request, render_template, jsonify, send_from_directory, Response
from werkzeug.utils import secure_filename
from whisper_diarize import transcribe_and_diarize

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["OUTPUT_FOLDER"] = "transcriptions"
app.config["ALLOWED_EXTENSIONS"] = {"mp3", "wav", "ogg", "flac", "m4a"}
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50 MB max upload

# Create necessary directories
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)

# Store job status
jobs = {}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/")
def index():
    return render_template("diarize.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    # Check if file is provided
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files["file"]
    
    if not file or file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed. Please use: {', '.join(app.config['ALLOWED_EXTENSIONS'])}"}), 400
    
    # Get parameters
    model = request.form.get("model", "base")
    num_speakers = int(request.form.get("num_speakers", 2))
    
    # Generate unique filename and job ID
    job_id = str(uuid.uuid4())
    original_filename = secure_filename(file.filename)
    filename = f"{job_id}_{original_filename}"
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    
    # Save the file
    file.save(filepath)
    
    # Add job to queue
    file_basename = os.path.splitext(original_filename)[0]
    jobs[job_id] = {
        "id": job_id,
        "filename": original_filename,
        "status": "uploaded",
        "progress": 0,
        "filepath": filepath,
        "output_base": file_basename,
        "model": model,
        "num_speakers": num_speakers,
        "download_links": {}
    }
    
    # Start processing in a separate thread
    import threading
    thread = threading.Thread(target=process_transcription, args=(job_id,))
    thread.daemon = True
    thread.start()
    
    return jsonify({
        "job_id": job_id,
        "status": "processing",
        "message": "File uploaded and processing started"
    })

def process_transcription(job_id):
    """Process transcription in background"""
    job = jobs[job_id]
    
    try:
        # Update status
        job["status"] = "transcribing"
        job["progress"] = 10
        
        # Run transcription
        output_folder = app.config["OUTPUT_FOLDER"]
        text = transcribe_and_diarize(
            job["filepath"], 
            model_name=job["model"], 
            output_dir=output_folder,
            num_speakers=job["num_speakers"]
        )
        
        job["progress"] = 90
        
        # Update download links
        file_basename = job["output_base"]
        job["download_links"] = {
            "txt": f"/download/{file_basename}_diarized.txt",
            "json": f"/download/{file_basename}_diarized.json",
            "srt": f"/download/{file_basename}_diarized.srt",
            "vtt": f"/download/{file_basename}_diarized.vtt",
        }
        
        job["text"] = text
        job["status"] = "completed"
        job["progress"] = 100
        
    except Exception as e:
        job["status"] = "error"
        job["error_message"] = str(e)
        print(f"Error processing job {job_id}: {e}")

@app.route("/job/<job_id>", methods=["GET"])
def get_job_status(job_id):
    """Get job status"""
    if job_id not in jobs:
        return jsonify({"error": "Job not found"}), 404
    
    job = jobs[job_id]
    
    response = {
        "id": job["id"],
        "status": job["status"],
        "progress": job["progress"],
        "filename": job["filename"]
    }
    
    if job["status"] == "completed":
        response["download_links"] = job["download_links"]
        response["text"] = job["text"]
    elif job["status"] == "error":
        response["error_message"] = job.get("error_message", "Unknown error")
    
    return jsonify(response)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001) 