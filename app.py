from flask import Flask, request, jsonify
import whisper
import tempfile
import os

app = Flask(__name__)

# Load the Whisper model once at startup. Change "base" to another model size if needed.
model = whisper.load_model("base")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    # Check if a file part is present in the request
    if "file" not in request.files:
        return jsonify({"error": "No file provided in the request"}), 400

    audio_file = request.files["file"]

    # Ensure a file was selected
    if audio_file.filename == "":
        return jsonify({"error": "Empty file name provided"}), 400

    try:
        # Save the uploaded audio file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
            audio_file.save(temp)
            temp_filename = temp.name
        
        # Perform transcription using Whisper; the function expects a file path.
        result = model.transcribe(temp_filename)
        
        # Clean up the temporary file
        os.remove(temp_filename)
        
        return jsonify(result), 200

    except Exception as e:
        # Return an error message if transcription fails
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 so it listens on all network interfaces, on port 8080.
    app.run(host="0.0.0.0", port=8080)
