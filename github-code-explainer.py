import streamlit as st
import google.generativeai as genai
import requests
import re
import os
from datetime import datetime

# Configure the Gemini API
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# Set page config
st.set_page_config(
    page_title="GitHub Code Explainer",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
        background-color: #FF4B4B;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stMarkdown h1 {
        color: #1E1E1E;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .stMarkdown h3 {
        color: #1E1E1E;
        font-size: 1.5rem;
        margin-top: 1.5rem;
    }
    .stExpander {
        background-color: #F0F2F6;
        border-radius: 5px;
        margin-top: 1rem;
    }
    /* Dark mode improvements */
    [data-testid="stAppViewContainer"] {
        background-color: #0E1117;
    }
    /* Text colors */
    .stMarkdown h1, .stMarkdown h3 {
        color: #FFFFFF !important;
        font-weight: 600;
    }
    .stMarkdown p {
        color: #E0E0E0 !important;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    /* Expander styling */
    .stExpander {
        background-color: #1A1A1A !important;
        border: 1px solid #333333 !important;
        border-radius: 8px;
        margin-top: 1rem;
    }
    .stExpander .streamlit-expanderHeader {
        color: #FFFFFF !important;
        font-weight: 500;
        font-size: 1.1rem;
        padding: 1rem;
    }
    /* Info box styling */
    .stMarkdown div[style*="background-color: #F0F2F6"] {
        background-color: #1A1A1A !important;
        border: 1px solid #333333 !important;
        border-radius: 8px;
        padding: 1.2rem !important;
        margin: 1rem 0;
    }
    .stMarkdown div[style*="background-color: #F0F2F6"] p {
        color: #E0E0E0 !important;
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 0;
    }
    /* Footer styling */
    .stMarkdown div[style*="color: #666"] {
        color: #B0B0B0 !important;
        font-size: 0.9rem;
    }
    /* Horizontal rule */
    .stMarkdown hr {
        border-color: #333333;
        margin: 1.5rem 0;
    }
    /* Input field styling */
    .stTextInput>div>div>input {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: 1px solid #333333 !important;
    }
    .stTextInput>div>div>input::placeholder {
        color: #888888 !important;
    }
    /* Warning message styling */
    .stMarkdown div[data-testid="stMarkdownContainer"] {
        color: #FFB74D !important;
    }
    /* Spinner text */
    .stSpinner>div {
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

def get_file_language(file_path):
    """Detect the programming language based on file extension."""
    extension = os.path.splitext(file_path)[1].lower()
    language_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'jsx',
        '.ts': 'typescript',
        '.tsx': 'tsx',
        '.html': 'html',
        '.css': 'css',
        '.json': 'json',
        '.md': 'markdown',
        '.java': 'java',
        '.cpp': 'cpp',
        '.c': 'c',
        '.go': 'go',
        '.rb': 'ruby',
        '.php': 'php',
        '.swift': 'swift',
        '.kt': 'kotlin',
        '.rs': 'rust',
        '.scala': 'scala',
        '.r': 'r',
        '.sql': 'sql',
        '.sh': 'shell',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.toml': 'toml',
        '.ini': 'ini',
        '.xml': 'xml',
        '.vue': 'vue',
        '.svelte': 'svelte',
        '.astro': 'astro'
    }
    return language_map.get(extension, 'plaintext')

def convert_github_url_to_raw(url):
    """Convert GitHub URL to raw content URL."""
    # Handle raw.githubusercontent.com URLs
    if "raw.githubusercontent.com" in url:
        return url
        
    # Handle regular GitHub URLs
    pattern = r"https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)"
    match = re.match(pattern, url)
    if match:
        owner, repo, branch, path = match.groups()
        return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    return url

def fetch_code_from_url(url):
    """Fetch code content from URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        st.error(f"Error fetching code: {str(e)}")
        return None

def explain_code(code, language):
    """Generate code explanation using Gemini."""
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        prompt = f"""
        Please explain this code at a high level. Include:
        1. What the code does
        2. Key components and their purposes
        3. Any notable features or patterns
        4. Potential use cases
        
        Code:
        ```{language}
        {code}
        ```
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating explanation: {str(e)}")
        return None

# Streamlit UI
st.title("📚 GitHub Code Explainer")
st.markdown("""
    <div style='background-color: #2D3748; padding: 1.2rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid #4A5568;'>
        <p style='margin: 0; color: #FFFFFF; font-size: 1.1rem; font-weight: 500;'>Enter a GitHub URL to get an AI-powered explanation of the code.</p>
    </div>
""", unsafe_allow_html=True)

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    # Input field for GitHub URL
    github_url = st.text_input(
        "GitHub URL",
        placeholder="https://github.com/username/repo/blob/main/file.py",
        help="Enter a GitHub URL or raw.githubusercontent.com URL"
    )

    if st.button("🔍 Explain Code"):
        if github_url:
            with st.spinner("📥 Fetching code..."):
                # Convert URL to raw content URL
                raw_url = convert_github_url_to_raw(github_url)
                
                # Fetch code
                code = fetch_code_from_url(raw_url)
                
                if code:
                    # Detect language from URL
                    file_path = github_url.split('/')[-1]
                    language = get_file_language(file_path)
                    
                    with st.spinner("🤔 Generating explanation..."):
                        # Generate explanation
                        explanation = explain_code(code, language)
                        
                        if explanation:
                            # Display the explanation in a nice format
                            st.markdown("### 📝 Code Explanation")
                            st.markdown(explanation)
                            
                            # Display the code in an expander
                            with st.expander("👀 View Original Code"):
                                st.code(code, language=language)
        else:
            st.warning("⚠️ Please enter a GitHub URL first!")

with col2:
    # Add some helpful information in the sidebar
    st.markdown("### 🎯 How to Use")
    st.markdown("""
    1. Enter a GitHub URL (e.g., https://github.com/anand-ma/code-explorer/blob/main/github-code-explainer.py)
    2. Click 'Explain Code'
    3. Wait for the AI to analyze and explain the code
    """)
    
    st.markdown("### 🌐 Supported URLs")
    st.markdown("""
    - Regular GitHub URLs
    - Raw GitHub content URLs
    """)
    
    # Add footer with timestamp
    st.markdown("---")
    st.markdown(f"<div style='text-align: center; color: #666; font-size: 0.8rem;'>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>", unsafe_allow_html=True) 