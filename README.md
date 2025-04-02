# GitHub Code Explainer

A powerful web application that provides AI-powered explanations of code from GitHub repositories. Built with Streamlit and powered by Google's Gemini AI, this tool helps developers understand code more effectively.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Code%20Explainer-blue?style=flat-square)](https://code-explorer.streamlit.app/)

## 📸 Screenshot

<img src="https://raw.githubusercontent.com/anand-ma/code-explorer/main/assets/code-explorer.png" alt="GitHub Code Explainer Interface" width="800">

## 🌟 Features

- **AI-Powered Code Analysis**: Get detailed explanations of code using Google's Gemini AI
- **Support for Multiple Languages**: Works with various programming languages including Python, JavaScript, TypeScript, Java, and many more
- **Easy to Use**: Simply paste a GitHub URL and get instant explanations
- **Dark Mode Support**: Comfortable viewing experience with dark mode
- **Responsive Design**: Works well on both desktop and mobile devices
- **Code Preview**: View the original code alongside the explanation

## 🎯 Use Cases

- **Learning New Codebases**: Helps developers quickly understand unfamiliar code
- **Code Review**: Can assist in understanding the purpose and functionality of code being reviewed
- **Documentation**: Can be used to automatically generate high-level documentation for code
- **Educational Tool**: Useful for students learning to code, allowing them to understand existing code examples
- **Reverse Engineering**: Can assist in understanding the functionality of closed-source code (though ethical considerations apply)
- **Code Exploration**: Quickly understand the function of snippets found online

## ��️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini AI
- **Styling**: Custom CSS with dark mode support
- **Language Detection**: Built-in file extension detection
- **URL Processing**: Python requests library

## 🚀 Live Demo

Visit the live application at: [https://code-explorer.streamlit.app/](https://code-explorer.streamlit.app/)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-code-explainer.git
cd github-code-explainer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Create a `.streamlit/secrets.toml` file
   - Add your Google API key:
```toml
GOOGLE_API_KEY = "your-api-key-here"
```

## 💻 Usage

1. Start the application:
```bash
streamlit run github-code-explainer.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter a GitHub URL in the input field (e.g., https://github.com/username/repo/blob/main/file.py)

4. Click "Explain Code" to get an AI-powered explanation

## 🔧 Supported File Types

The application supports a wide range of programming languages and file types, including:
- Python (.py)
- JavaScript (.js, .jsx)
- TypeScript (.ts, .tsx)
- HTML (.html)
- CSS (.css)
- Java (.java)
- C/C++ (.c, .cpp)
- And many more...

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for providing the powerful language model
- Streamlit for the amazing web framework
- All contributors and users of the application 