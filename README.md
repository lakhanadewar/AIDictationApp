# User Guide for AI Dictation App

## Overview

The AI Dictation App is a Flask-based application that allows users to:

1. Transcribe audio files into clean and refined text.
2. Restyle existing text based on specific instructions.
3. Translate text into different languages.
4. View the application's privacy policy.

This app leverages OpenAI's API for transcription and text processing, as well as Google Translate for multilingual support.

---

## Prerequisites

1. **Python Environment**: Ensure Python 3.7+ is installed on your system.
2. **Dependencies**: Install the required Python libraries by running:
   ```bash
   pl
   ```
3. **ease OpenAI API Key**: Set up your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```
4. **Run the Application**: Start the app by executing:
   ```bash
   python app.py
   ```
   The app will be accessible at `http://127.0.0.1:5000/`.

---

## API Endpoints

### 1. **Transcription Endpoint**

- **URL**: `/transcribe`
- **Method**: `POST`
- **Description**: Converts an audio file into refined text.
- **Request Parameters**:
  - `audio`: (File) The audio file to transcribe.
- **Response**:
  - Success: `{ "transcription": "Refined text" }`
  - Error: `{ "error": "Error message" }`

**Example Usage** (via `curl`):

```bash
curl -X POST -F "audio=@path/to/audio.wav" http://127.0.0.1:5000/transcribe
```

---

### 2. **Restyle Endpoint**

- **URL**: `/restyle`
- **Method**: `POST`
- **Description**: Restyles given text based on user instructions.
- **Request Body (JSON)**:
  - `text`: (String) The original text.
  - `instruction`: (String) The restyling instruction (e.g., "make it more formal").
- **Response**:
  - Success: `{ "restyled_text": "Restyled text" }`
  - Error: `{ "error": "Error message" }`

**Example Usage** (via `curl`):

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"text": "This is amazing!", "instruction": "make it formal"}' \
http://127.0.0.1:5000/restyle
```

---

### 3. **Translation Endpoint**

- **URL**: `/translate`
- **Method**: `POST`
- **Description**: Translates text into a specified language.
- **Request Body (JSON)**:
  - `text`: (String) The text to translate.
  - `language`: (String) The target language (e.g., "es" for Spanish).
- **Response**:
  - Success: `{ "translated_text": "Translated text" }`
  - Error: `{ "error": "Error message" }`

**Example Usage** (via `curl`):

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"text": "Hello, world!", "language": "es"}' \
http://127.0.0.1:5000/translate
```

---

### 4. **Privacy Policy Endpoint**

- **URL**: `/privacy`
- **Method**: `GET`
- **Description**: Displays the application's privacy policy.
- **Response**:
  - `{ "privacy": "We do not store your audio, use your data to train AI models, or sell your data to third parties." }`

**Example Usage** (via `curl`):

```bash
curl http://127.0.0.1:5000/privacy
```

---

## Features

### Transcription Cleanup

The app refines transcriptions by removing fillers (e.g., "uh", "um") and applying proper punctuation and capitalization for more readable text.

### Restyling

Users can rewrite text with different tones or styles, such as making it formal, friendly, or professional.

### Multilingual Support

Supports translations for over 30 languages.

### Privacy First

The app ensures user data is not stored, used for training, or shared with third parties.

---

## Troubleshooting

- **404 Errors**: Ensure you're using the correct endpoint URLs.
- **500 Errors**: Check if your OpenAI API key is correctly set and that the audio file or JSON payload is properly formatted.

---

## Contact

For issues or questions, please contact [support@example.com](mailto\:support@example.com).

