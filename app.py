from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import openai
import os
import docx

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# OpenAI API Key Setup
openai.api_key = os.getenv("OPENAI_API_KEY", "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")  # Replace with your actual API key
 
def read_text_file(file_path):
    """Reads a plain text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return str(e)

def read_docx_file(file_path):
    """Reads a DOCX file and extracts text."""
    try:
        doc = Document(file_path)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()])
    except Exception as e:
        return str(e)

@app.route('/process_file', methods=['POST'])
def process_file():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided."}), 400
        
        file = request.files['file']
        file_extension = file.filename.split('.')[-1].lower()
        
        if file_extension not in ['txt', 'docx']:
            return jsonify({"error": "Unsupported file format. Only TXT and DOCX are supported."}), 400
        
        # Save file temporarily
        temp_path = f"temp_file.{file_extension}"
        file.save(temp_path)
        
        # Read file content
        text_content = ""
        if file_extension == 'txt':
            text_content = read_text_file(temp_path)
        elif file_extension == 'docx':
            text_content = read_docx_file(temp_path)
        
        # Check if text was extracted successfully
        if not text_content.strip():
            return jsonify({"error": "No text found in the document."}), 400
        
        return jsonify({"processed_text": text_content})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/restyle', methods=['POST'])
def restyle():
    try:
        data = request.json
        text = data.get("text")
        instruction = data.get("instruction")

        if not text or not instruction:
            return jsonify({"error": "Missing text or instruction"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant that rewrites text in different styles."},
                {"role": "user", "content": f"Rewrite this text in a {instruction} style: {text}"}
            ]
        )

        restyled_text = response["choices"][0]["message"]["content"].strip()

        return jsonify({"restyled_text": restyled_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
