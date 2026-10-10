import streamlit as st
from PIL import Image
import openai
import base64
import io

# Set up page configuration
st.set_page_config(page_title="UI Locator Generator", layout="wide")
st.title("UI Locator Generator from Screenshot")
st.write("Upload a screenshot of your web page to generate a structured table of stable automation locators.")

# Sidebar for API Key configuration
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

# File uploader feature
uploaded_file = st.file_uploader("Choose a screenshot...", type=["png", "jpg", "jpeg"])

# Define the prompt we constructed earlier
PROMPT = """
You are an expert test automation architect. Your task is to analyze the provided screenshot of a user interface, identify all interactive elements (buttons, inputs, dropdowns, checkboxes, links, etc.), and generate a structured table containing highly stable, unique locators for each element.

For each identified element, provide the following details in a structured format:
1. Element Name: A logical, friendly name (e.g., "Submit Button", "Username Input").
2. Element Type: The type of control (e.g., Button, Text Field, Dropdown, Checkbox).
3. Primary Locator: The most stable locator based on the hierarchy below.
4. Strategy Used: The type of locator used (e.g., Test ID, Accessibility, Scoped CSS, Relative XPath).
5. Uniqueness Logic: A brief explanation of why this locator is unique and how duplicates were avoided.

Locator Priority Hierarchy:
1. Test IDs: If you infer the existence of test-specific attributes (e.g., data-testid="submit-btn").
2. Accessibility/Semantic Attributes: Playwright-style or Selenium-equivalent locators using roles, labels, or placeholders (e.g., role=button, name="Login").
3. Text Content: If the text is unique and static.
4. Scoped/Relative Locators: If identical elements exist (e.g., multiple dropdown items sharing the same class or ID), scope the locator to its unique parent container or use relative positioning. Do not use absolute XPaths (e.g., /html/body/div[1]/div[2]/...).

Handling Duplicates (e.g., Dropdowns/Lists):
- If multiple elements share identical attributes, do not use raw index numbers (like [2] or nth-child) unless absolutely necessary.
- Instead, construct a relative locator that anchors the target element to a unique parent container, header, or neighboring label.

Please output the result as a Markdown table that can be easily copied into a CSV file.
"""

def encode_image(uploaded_file):
    """Helper function to convert uploaded image to base64 for API transmission."""
    bytes_data = uploaded_file.getvalue()
    return base64.b64encode(bytes_data).decode("utf-8")

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Uploaded Screenshot")
        st.image(image, use_container_width=True)
        
    with col2:
        st.subheader("Locator Generation")
        if st.button("Generate Locators"):
            if not api_key:
                st.error("Please enter your OpenAI API Key in the sidebar.")
            else:
                try:
                    with st.spinner("Analyzing screenshot and generating locators..."):
                        # Initialize OpenAI client
                        client = openai.OpenAI(api_key=api_key)
                        
                        # Encode image to base64
                        base64_image = encode_image(uploaded_file)
                        
                        # Call GPT-4o (Vision) API
                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "text", "text": PROMPT},
                                        {
                                            "type": "image_url",
                                            "image_url": {
                                                "url": f"data:image/jpeg;base64,{base64_image}"
                                            }
                                        }
                                    ]
                                }
                            ],
                            max_tokens=1500
                        )
                        
                        # Display results
                        analysis_result = response.choices[0].message.content
                        st.markdown(analysis_result)
                        
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")