# PregniTech

**PregniTech** is an AI-based pregnancy guidance platform designed to assist expecting mothers from **1 to 9 months** of pregnancy. The platform provides **diet plans, mental health guidance, and partner tips** through interactive AI chatbots embedded via **iframes**, hosted on **Hugging Face Spaces** using **Gradio interfaces**.  

The platform implements a **Retrieval-Augmented Generation (RAG)** approach, allowing the chatbots to retrieve relevant pregnancy guidance from preloaded textual data to provide more accurate, context-aware, and personalized responses.  

---

## Features

- **Month-wise Pregnancy Chatbots:** AI chatbots for each month of pregnancy (1–9 months).  
- **Diet & Nutrition Guidance:** Suggests suitable meal plans for the mother.  
- **Mental Health Support:** Provides tips for mental well-being during pregnancy.  
- **Partner Guidance:** Offers advice to partners to support the mother.  
- **RAG-Powered Responses:** Chatbots leverage RAG to give contextually relevant answers.  
- **Customizable AI Response:** Adjustable parameters such as **max tokens**, **temperature**, and **top-p** for fine-tuning chatbot outputs.  

---

## Tech Stack

- **Frontend:**  
  - React  
  - TypeScript  
  - Embedded **Gradio chat interfaces** via iframes  

- **Backend / AI:**  
  - Python  
  - **Gradio** – for building interactive chat interfaces  
  - **Hugging Face Inference API** – for AI chat models (e.g., `google/gemma-2-2b-it`)  
  - **Sentence Transformers** – for text embeddings (`all-MiniLM-L6-v2`)  
  - **FAISS** – for similarity search and RAG retrieval  
  - **Python standard libraries** – for file handling and preprocessing  

- **RAG Implementation:**  
  1. Load month-specific pregnancy guidance text.  
  2. Chunk text data for easier embedding.  
  3. Embed chunks using **SentenceTransformer**.  
  4. Store embeddings in **FAISS index**.  
  5. Retrieve relevant chunks based on user queries.  
  6. Augment system prompt with retrieved context for AI response.  

---

## Team Members

- **Hashir Ehtisham** – AI Chatbots Developer / Computer Engineer  
- **Lameea Khan** – Graphics Designer / Computer Engineer  
- **Kainat Ali** – MERN Stack Developer / Software Engineer  

---

## Installation & Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kainaatt/Pregnitech.git
   cd PregniTech
