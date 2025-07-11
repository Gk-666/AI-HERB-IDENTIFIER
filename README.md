# Herb Identification System

This is a Streamlit-based web application that uses Google's Gemini AI to identify herbs and provide detailed information about them. The application can analyze images of herbs and answer specific questions about them.

## Features

- Upload and analyze herb images
- Get detailed herb identification including scientific names
- Learn about medicinal properties and safety precautions
- Ask specific questions about identified herbs
- User-friendly interface with real-time responses

## Setup Instructions

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

4. Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```
5. Add your Gemini API key to the `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Running the Application

To run the application, use the following command:
```bash
streamlit run app.py
```

The application will open in your default web browser.

## Usage

1. Upload an image of a herb using the file uploader
2. Click "Identify Herb" to get detailed information about the herb
3. Ask specific questions about the herb using the text input field
4. View the results in real-time

## Important Notes

- Ensure you have a stable internet connection
- Use clear, well-lit images for better results
- The application should not be used as the sole source for medical advice
- Always consult healthcare professionals before using herbs medicinally

## Requirements

- Python 3.7+
- Streamlit
- Google Generative AI
- Pillow
- python-dotenv 