# Document Q/A System using LlamaIndex & OpenAI API

## Overview
This project builds a **document-based Question-Answering (Q/A) system** using **LlamaIndex** and the **OpenAI API**. The system reads web pages, processes the content, and allows querying using a **vector-based retrieval** approach.

## Features
- Fetch and process web page content using `SimpleWebPageReader`
- Create a **VectorStoreIndex** for storing and retrieving document embeddings
- Use **query engine** to get insights from documents
- Integrate with **OpenAI API** (optional)

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/Abs-Futy7/Doc_QA_LlamaIndex.git
cd Doc_QA_LlamaIndex
```

### 2. Create a Virtual Environment & Install Dependencies
#### **For VS Code:**
1. Press `Ctrl + Shift + P`
2. Search for **Python: Select Interpreter**
3. Click **Create Virtual Environment (venv)**
4. Open a terminal and run:

```sh
pip install -r requirements.txt
```

### 3. Install Additional Dependencies
```sh
pip install llama-index-readers-web
pip uninstall llama-index
pip install llama-index
```

## Required Dependencies
Ensure the following libraries are installed:
```sh
pip install llama-index
pip install python-dotenv
pip install html2text
```

## Usage
### Run the Script
```sh
python webpagereader.py
```

## Environment Variables
Create a `.env` file to store API keys if required:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

---

Happy Coding! 🚀

