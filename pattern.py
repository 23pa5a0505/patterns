import streamlit as st
import google.generativeai as genai

def generate_pattern_program(pattern, language, level):
    """Generates a pattern program based on the given pattern, language, and difficulty level.

    Args:
        pattern: The pattern description.
        language: The programming language for the pattern.
        level: The difficulty level of the pattern (basic, intermediate, advanced).

    Returns:
        The generated pattern program.
    """

    try:
        # Configure API key
        genai.configure(api_key="AIzaSyBZKWOxPAaF357psP9I2hYToZIW6kzqi_0")

        # Create the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are a programming expert. Create a pattern program in the given language for the given difficulty level.",
        )

        # Construct the prompt
        prompt = (f"Create a {level} pattern program in {language} for the following pattern: {pattern}. "
                  "The program should be clear, well-documented, and appropriate for the specified difficulty level.")

        # Generate the pattern program
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit application
st.set_page_config(page_title="Pattern Program Generator", page_icon=":sparkles:")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        color: #333;
        font-family: 'Arial', sans-serif;
        background-color: #f5f5f5;
        padding: 2rem;
    }
    .header {
        text-align: center;
        color: #4CAF50;
    }
    .code {
        background-color: #f4f4f4;
        border-radius: 5px;
        padding: 1rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .btn-primary {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 5px;
        cursor: pointer;
    }
    .btn-primary:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Pattern Program Generator :sparkles:", anchor="header")

st.write("""
    Welcome to the Pattern Program Generator! This tool helps you create pattern programs in any programming language 
    based on the pattern description you provide. Select the difficulty level and let our AI generate the code for you!
""")

pattern = st.text_area("Enter the pattern description:", placeholder="e.g., a pyramid pattern of stars")
language = st.selectbox("Select the programming language:", ["Python", "Java", "C++", "JavaScript", "C#", "Ruby", "PHP", "Go", "Swift"])
level = st.selectbox("Select the difficulty level:", ["basic", "intermediate", "advanced"])

if st.button("Generate Pattern Program", key="generate", help="Click to generate the pattern program", use_container_width=True):
    if pattern and language and level:
        with st.spinner("Generating your pattern program..."):
            program = generate_pattern_program(pattern, language, level)
        st.subheader("Generated Pattern Program:")
        st.markdown(f'<pre class="code">{program}</pre>', unsafe_allow_html=True)
    else:
        st.error("Please enter a pattern description, select a programming language, and choose a difficulty level.")

st.markdown("""
    ---
    *Need help?* Contact our support team or visit our [documentation](https://www.example.com/docs).
""")
