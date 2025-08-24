# 🧠 NoteWeb

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/LLM-LLaMA_3_via_Ollama-brightgreen?logo=openai)](https://ollama.com/)
[![Semantic Search](https://img.shields.io/badge/Semantic_Search-Enabled-blueviolet)](#)
[![File Support](https://img.shields.io/badge/File_Support-PDF-yellow)](#file-support)
[![Status](https://img.shields.io/badge/Status-Active_Development-orange)](#roadmap)
[![First AI Project](https://img.shields.io/badge/My_First_AI_Project-%F0%9F%A4%96-lightgrey)](#)

>  A local-first AI-powered tool to **search, summarize, and understand your notes** — built for students, by a student.  
> Uses chunking, vector embeddings, and LLaMA 3 via Ollama for real semantic understanding.

---

##  Features

- Index PDFs, Word, Excel, and PowerPoint files into semantic chunks
- Embed and store those chunks using vector search
- Ask questions using LLaMA 3 via Ollama (offline + local)
- Get answers with real context grounding (like the ChatGPT Retrieval Plugin)
+ - Follow-up question support with persistent memory
+ - Ingest multiple files at once from a folder
+ - Test-ready with `test files/` folder


---

## Folder Structure

```
noteweb/
├── main.py                 # CLI entrypoint
├── search.py              # Embedding search logic
├── llm_answerer.py        # Sends chunks to LLaMA via Ollama
├── embedder.py            # Generates embeddings
├── chunker.py             # Breaks files into semantic chunks
├── files_loader.py        # PDF loader (more formats soon)
├── generate_index.py      # Index generator (embeds + saves)
├── embeddings_index.json  # Your saved vector index
├── test files/            # Sample PDFs to test with
├── requirements.txt
└── venv/                  # Your virtual environment
```

---

## Requirements

- Python **3.11+**
- [Ollama](https://ollama.com) installed and running
  ```bash
  brew install ollama
  ollama run llama3
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

---

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/marcanjoul/noteweb.git
cd noteweb
```
Or, if you downloaded the ZIP, unzip it and navigate into the folder via:
```bash
cd ~/Desktop/noteweb-main  # or wherever you saved it
```
### 2. Set Up a Virtual Environment
We recommend using a virtual environment to keep dependencies clean:
```bash
python3 -m venv venv
source venv/bin/activate  # (for mac) # On Windows, use venv\Scripts\activate
```
### 3. Install Dependencies
Run the following to install all required packages:
```bash
pip install -r requirements.txt
```
If needed, manually install these extras:
```bash
pip install python-docx python-pptx openpyxl sentence-transformers
```
### 4. Add Your Files
Create or drop any files you want to search into the test files/ directory. Supported formats:
.pdf
.docx
.pptx
.xlsx
### 5. Run this to generate semantic embeddings from files in your folder
```bash
python generate_index.py
```
This will:
- Load all .pdf, .docx, .xslx, and .pptx files from your test files/ folder
- Chunk the content into semantically meaningful parts
- Embed each chunk using sentence-transformers
- Save everything to embeddings_index.json

### 6. Search Your Files with the AI
```bash
python search.py
```
This will:
- Search your indexed chunks for relevant context
- Pass top matches to **LLaMA 3**
- Return an answer based on your notes
- You can also ask follow-up questions, as NoteWeb remembers the context!
  
💡 Example Usage
> What is the difference between supervised and unsupervised learning?

❗ Requirements
Make sure you have:
- Python 3.9+
- pip
- Optional: Ollama installed and running (for local LLaMA 3 support)

💡 Optional: Skip venv (Not Recommended)
You can also run NoteWeb without using a virtual environment:

```bash
pip install -r requirements.txt
pip install python-docx python-pptx openpyxl sentence-transformers
```
---

### 2. Ask a question

```bash
python main.py --search "What is instruction-level parallelism?"
```
---

## Why This Matters

NoteWeb simulates *real retrieval-augmented generation (RAG)* — the same strategy used in:
- ChatGPT w/ File Uploads
- Perplexity AI
- Open-source RAG pipelines (like LangChain, LlamaIndex)

But here, it’s all:
- **Local**
- **Educational**
- **Hackable**

Perfect for learning how vector search + LLMs work together.

---

## File Support

- ✅ PDF  
+ - ✅ DOCX (.docx)  
+ - ✅ PowerPoint (.pptx)
+ - ✅ Excel (.xlsx)    
+ - 🔜 TXT, Markdown, Web scraping

You can drop files into the `test files/` folder!

---

## Roadmap

- [x] Multi-file indexing (entire folders at once)
- [x] DOCX, PPTX, and XLSX support
- [x] Follow-up question support
- [x] Optional toggle in code for chunk visibility
- [ ] Index caching to skip re-embedding unchanged files
- [ ] Command-line UI / TUI
- [ ] Streamed LLaMA answers with citations
- [ ] Web UI or notebook wrapper?


---

## Project Status

NoteWeb is my **first AI-integrated project** — made while learning:
- How LLMs like LLaMA work
- What “semantic search” really means
- How chunking, embeddings, and vector stores come together

This is the foundation for bigger projects — search tools, academic companions, even personalized AI.

---

## Credits

- Built with 💻 and ☕ by [@marcanjoul](https://github.com/marcanjoul)
- PDF parsing via [`PyMuPDF`](https://pymupdf.readthedocs.io/)
- DOCX parsing via [`python-docx`](https://python-docx.readthedocs.io/)
- PowerPoint parsing via [`python-pptx`](https://python-pptx.readthedocs.io/)
- Excel parsing via [`openpyxl`](https://openpyxl.readthedocs.io/)
- Embeddings via [`sentence-transformers`](https://www.sbert.net/)
- LLM answers via [Ollama](https://ollama.com) and Meta’s [LLaMA 3](https://ai.meta.com/llama/)


---

### Want to improve or collaborate?
> Open an issue, drop a PR, or fork it and make it your own.I'd appreciate any feedback!
