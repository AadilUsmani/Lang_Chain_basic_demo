# 🦜⛓️ LangChain Models 001

A comprehensive repository demonstrating the integration and usage of various embedding and language models with [LangChain](https://github.com/langchain-ai/langchain). This project showcases implementations across multiple providers including Azure OpenAI, Hugging Face, and Google APIs, with examples for both local and cloud-based inference.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://github.com/langchain-ai/langchain)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

- **🔤 Embedding Models**: Implementation of both Azure OpenAI and open-source embedding models
- **🤖 Language Models**: Support for various LLM providers (OpenAI, Google, Hugging Face)
- **💬 Chat Models**: Interactive chat implementations with different AI providers
- **🏠 Local & Cloud**: Examples for both local inference and API-based solutions
- **🔧 Easy Configuration**: Environment-based configuration management
- **📊 Similarity Computing**: Built-in cosine similarity calculations for embeddings

---

## 📁 Project Structure

```
Lang_Chain_models_001/
│
├── 📄 .env.example              # Environment variables template
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                 # Project documentation
├── 📄 Project_001_langchain.py  # Main demonstration script
│
├── 📂 EmbeddedModels/
│   ├── 🔤 embed_open_ai.py      # Azure OpenAI embeddings
│   └── 🔤 embed_open_source.py  # Hugging Face embeddings
│
├── 📂 LLMS/
│   └── 🤖 llm_demo.py           # Language model demonstrations
│
└── 📂 ChatModels/
    ├── 💻 chatmodel_local_demo.py  # Local chat model
    ├── 🔷 chatmodels_openai.py     # OpenAI chat models
    ├── 🔍 google_api_demo.py       # Google Gemini/PaLM
    └── 🤗 hugging_face_demo.py     # Hugging Face chat models
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Lang_Chain_models_001
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your API keys and endpoints
nano .env  # or use your preferred editor
```

### 5. Run Your First Example
```bash
python Project_001_langchain.py
```

---

## 🔑 Environment Configuration

Create a `.env` file in the root directory with the following variables:

```bash
# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-12-01-preview
AZURE_DEPLOYMENT_NAME=your-deployment-name

# Google AI Configuration
GOOGLE_API_KEY=your_google_api_key

# Hugging Face Configuration
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token

# OpenAI Configuration (if using direct OpenAI)
OPENAI_API_KEY=your_openai_api_key
```

> ⚠️ **Important**: Never commit your `.env` file to version control. Add it to your `.gitignore`.

---

## 📚 Module Documentation

### 🔤 Embedding Models

#### `EmbeddedModels/embed_open_ai.py`
- **Purpose**: Demonstrates Azure OpenAI embedding generation
- **Model**: `text-embedding-3-small`
- **Use Case**: High-quality text embeddings for semantic search and similarity tasks
- **Requirements**: Azure OpenAI subscription and deployment

```python
# Example usage
from EmbeddedModels.embed_open_ai import generate_embeddings
embeddings = generate_embeddings(["Hello world", "Goodbye world"])
```

#### `EmbeddedModels/embed_open_source.py`
- **Purpose**: Local embedding generation using Hugging Face models
- **Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Use Case**: Privacy-focused, offline embedding generation
- **Requirements**: Sufficient local compute resources

### 🤖 Language Models

#### `LLMS/llm_demo.py`
- **Purpose**: Basic LLM interaction examples
- **Features**: Text generation, completion, and prompt engineering
- **Customizable**: Easy to switch between different LLM providers

### 💬 Chat Models

#### `ChatModels/chatmodel_local_demo.py`
- **Purpose**: Local conversational AI using Hugging Face transformers
- **Model**: GPT-2 or other local models
- **Benefits**: No API costs, full privacy control

#### `ChatModels/chatmodels_openai.py`
- **Purpose**: OpenAI GPT models for conversational AI
- **Features**: Advanced chat capabilities with context management
- **Models**: GPT-3.5-turbo, GPT-4, etc.

#### `ChatModels/google_api_demo.py`
- **Purpose**: Google's Gemini and PaLM models integration
- **Features**: Multimodal capabilities (text, images)
- **Benefits**: Competitive pricing and performance

#### `ChatModels/hugging_face_demo.py`
- **Purpose**: Hugging Face Hub models for chat and text generation
- **Flexibility**: Access to thousands of community models
- **Options**: Both API and local inference

---

## 🎯 Usage Examples

### Basic Embedding Generation
```bash
python EmbeddedModels/embed_open_ai.py
```

### Local Chat Model
```bash
python ChatModels/chatmodel_local_demo.py
```

### Similarity Search Demo
```bash
python Project_001_langchain.py
```

---

## 🛠️ Customization Guide

### Adding New Models
1. Create a new Python file in the appropriate directory
2. Import necessary LangChain components
3. Configure your model with environment variables
4. Follow the existing code patterns for consistency

### Switching Embedding Models
```python
# In embed_open_ai.py, change:
embeddings = AzureOpenAIEmbeddings(
    model="text-embedding-3-large"  # Upgrade to larger model
)
```

### Adding New Providers
1. Install provider-specific packages
2. Add API keys to `.env`
3. Create demonstration script following existing patterns

---

## 📊 Performance Considerations

| Model Type | Provider | Speed | Cost | Quality | Privacy |
|------------|----------|-------|------|---------|---------|
| Embeddings | Azure OpenAI | ⚡⚡⚡ | 💰💰 | 🌟🌟🌟🌟🌟 | 🔒🔒 |
| Embeddings | Hugging Face (Local) | ⚡⚡ | 💰 | 🌟🌟🌟🌟 | 🔒🔒🔒🔒🔒 |
| Chat | GPT-4 | ⚡⚡ | 💰💰💰 | 🌟🌟🌟🌟🌟 | 🔒🔒 |
| Chat | Local Models | ⚡ | 💰 | 🌟🌟🌟 | 🔒🔒🔒🔒🔒 |

---

## 🚨 Troubleshooting

### Common Issues

**1. API Key Errors**
```bash
Error: Invalid API key
```
- Verify your API keys in `.env`
- Check key permissions and quotas
- Ensure correct endpoint URLs

**2. Model Loading Issues**
```bash
Error: Model not found
```
- Check internet connection for downloads
- Verify sufficient disk space for local models
- Update model names to current versions

**3. Memory Issues**
```bash
CUDA out of memory
```
- Use smaller models for local inference
- Reduce batch sizes
- Consider using CPU instead of GPU

### Getting Help
- Check the [LangChain Documentation](https://python.langchain.com/docs/)
- Review provider-specific documentation
- Open an issue in this repository

---

## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- 4GB+ RAM (8GB+ recommended for local models)
- Internet connection for API-based models

### API Access Requirements
- Azure OpenAI: Active subscription and deployed models
- Google AI: Valid API key with enabled services
- Hugging Face: API token for Hub access (optional for public models)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow existing code style and patterns
- Add documentation for new features
- Include example usage for new models
- Test your changes across different environments

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) - The amazing framework that makes this all possible
- [Hugging Face](https://huggingface.co/) - For democratizing AI and providing excellent models
- [OpenAI](https://openai.com/) - For advancing the field of AI
- [Google AI](https://ai.google.dev/) - For innovative AI research and development

---

## 📞 Contact & Support

**Author**: Adil Usmani

- 📧 Email: [muhammadaadilusmani@gmail.com]
- 🐙 GitHub: [AadilUsmani]
- 💼 LinkedIn: [Adil Usmani]

---

## 🔄 Version History

- **v1.0.0** - Initial release with basic model implementations
- **v1.1.0** - Added Google AI integration
- **v1.2.0** - Enhanced documentation and examples

---

*Made with ❤️ and LangChain*