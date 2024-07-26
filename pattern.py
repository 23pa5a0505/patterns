import streamlit as st
import google.generativeai as genai

def generate_pattern_program(pattern, language):
    """Generates a pattern program based on the given pattern and language.

    Args:
        pattern: The pattern description.
        language: The programming language for the pattern.

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
            system_instruction="You are a programming expert. Create a pattern program in the given language.",
        )

        # Construct the prompt
        prompt = f"Create a pattern program in {language} for the following pattern: {pattern}. The program should be clear and well-documented."

        # Generate the pattern program
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit application
st.set_page_config(page_title="Pattern Program Generator", page_icon=":sparkles:")

st.title("Pattern Program Generator :sparkles:")

st.write("""
    Welcome to the Pattern Program Generator! This tool helps you create pattern programs in any programming language 
    based on the pattern description you provide. Simply enter the pattern description and choose the programming language, 
    and let our AI generate the code for you!
""")

pattern = st.text_area("Enter the pattern description:", placeholder="e.g., a pyramid pattern of stars")
language = st.selectbox("Select the programming language:", ["Python", "Java", "C++", "JavaScript", "C#", "Ruby", "PHP", "Go", "Swift"])

if st.button("Generate Pattern Program"):
    if pattern and language:
        with st.spinner("Generating your pattern program..."):
            program = generate_pattern_program(pattern, language)
        st.subheader("Generated Pattern Program:")
        st.code(program, language=language.lower())
    else:
        st.error("Please enter a pattern description and select a programming language.")

st.markdown("""
    ---
    *Need help?* Contact our support team or visit our [documentation](https://www.example.com/docs).
""")
