# Swiggy Annual Report RAG QA System

This project implements a **Retrieval-Augmented Generation (RAG) system** that answers questions from the **Swiggy Annual Report** using document retrieval and a local language model.

The system loads the Swiggy annual report PDF, converts the text into embeddings, stores them in a FAISS vector database, retrieves relevant document chunks, and generates answers using a local LLM.

---

# Features

- PDF document ingestion
- Text chunking for better retrieval
- Sentence Transformer embeddings
- FAISS vector database for similarity search
- Retrieval-Augmented Generation (RAG)
- Local LLM inference using TinyLlama
- Displays final answer and supporting document context
- Supports both **Google Colab notebook** and **VS Code project**

---

# Project Structure

```
swiggy-rag-qa-system
│
├── README.md
├── requirements.txt
│
├── notebook
│   └── swiggy_rag_colab.ipynb
│
├── vscode_project
│   ├── ingest.py
│   ├── rag_pipeline.py
│   ├── app.py
│
├── data
│   └── Annual-Report-FY-2023-24.pdf
│
└── vector_db
```

---

# System Architecture

The system follows a standard **Retrieval-Augmented Generation pipeline**.

```
Swiggy Annual Report (PDF)
           │
           ▼
     Document Loader
           │
           ▼
       Text Chunking
           │
           ▼
 Sentence Transformer
       Embeddings
           │
           ▼
    FAISS Vector Store
           │
           ▼
        Retriever
           │
           ▼
     Local LLM (TinyLlama)
           │
           ▼
 Final Answer + Context
```

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/swiggy-rag-qa-system.git
```

Navigate to the project folder:

```
cd swiggy-rag-qa-system
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Running the Project

## Option 1: Google Colab

Open the notebook:

```
notebook/swiggy_rag_colab.ipynb
```

Run all cells to:

- upload the Swiggy PDF
- create embeddings
- build FAISS vector database
- query the RAG system

---

## Option 2: VS Code / Local Environment

Run the ingestion script:

```
python ingest.py
```

Run the application:

```
python app.py
```

or if using Streamlit:

```
streamlit run app.py
```

---

# Example Queries

### Question
Who is the CEO of Swiggy?

### Answer
Sriharsha Majety is the Managing Director and Group CEO of Swiggy.

### Supporting Context
Sriharsha Majety  
Managing Director & Group CEO  
Swiggy Limited

---

### Question
What services does Swiggy provide?

### Answer
Swiggy provides food delivery services, quick commerce, and grocery delivery through Instamart.

---

### Question
Where is Swiggy headquartered?

### Answer
Swiggy is headquartered in Bengaluru, India.

---

# Technologies Used

- Python
- LangChain
- FAISS Vector Database
- Sentence Transformers
- HuggingFace Transformers
- TinyLlama LLM
- Streamlit (for UI)
- Google Colab

---

# Key Concepts Implemented

This project demonstrates several important concepts in modern AI systems:

- Retrieval-Augmented Generation (RAG)
- Vector similarity search
- Document embeddings
- Context-based question answering
- Local LLM inference

---

# Future Improvements

Possible enhancements include:

- Adding a web UI with Streamlit
- Showing document page numbers for retrieved context
- Supporting multiple PDFs
- Adding conversational memory
- Improving answer summarization

---

# Author

Atharva Malvade

---

# License

This project is intended for educational purposes and internship assignments.