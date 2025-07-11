import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
model = genai.GenerativeModel('gemini-2.0-flash')
chat_model = genai.GenerativeModel('gemini-2.0-flash')

def get_gemini_response(input_prompt, image):
    if input_prompt != "":
        response = model.generate_content([input_prompt, image])
        return response.text
    
def get_chat_response(input_prompt):
    response = chat_model.generate_content(input_prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Herb Identification System", layout="wide")

st.title("🌿 Herb Identification System")
st.write("Upload an image of a herb to identify it and get detailed information!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert the image for Gemini
    if st.button("Identify Herb"):
        with st.spinner("Analyzing the image..."):
            # Initial prompt for herb identification
            identification_prompt = """
            You are a professional herbalist. Please analyze this image and:
            1. Identify the herb
            2. Provide its scientific name
            3. List its key medicinal properties
            4. Mention any safety precautions
            Please format the response in a clear, structured way.
            """
            
            response = get_gemini_response(identification_prompt, image)
            st.write("### Analysis Results")
            st.write(response)

    # ask quetion to model about herb         
    question = st.text_input("Ask a question about the herb in the image:")       
    # Handle specific questions about the herb
    if question:
        with st.spinner("Getting answer..."):
            # Combine the image and question for context
            response = get_gemini_response(question, image)
            st.write("### Answer")
            st.write(response)

# Sidebar with additional information
with st.sidebar:
    st.header("""About""")
    st.write("""
    This application uses AI to help identify herbs and provide detailed information about them. 
    Upload a clear image of a herb to get:
    - Herb identification
    - Scientific name
    - Medicinal properties
    - Safety information
    
    You can also ask specific questions about the herb in the image!
    """)
    
    st.warning("""
    WARNING!: Please ensure you have a enough information about the medicine.
    This application should not be used as the sole source for medical advice.
    Always consult with healthcare professionals before using any herbs medicinally.
    """) 