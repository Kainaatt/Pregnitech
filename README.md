PregniTech

PregniTech is an AI-based pregnancy guidance platform designed to assist expecting mothers from 1 to 9 months of pregnancy. The platform provides diet plans, mental health guidance, and partner tips through interactive AI chatbots embedded via iframes, hosted on Hugging Face Spaces using Gradio interfaces.

The platform implements a Retrieval-Augmented Generation (RAG) approach, allowing the chatbots to retrieve relevant pregnancy guidance from preloaded textual data to provide more accurate, context-aware, and personalized responses.

Features

Month-wise Pregnancy Chatbots: AI chatbots for each month of pregnancy (1–9 months).

Diet & Nutrition Guidance: Suggests suitable meal plans for the mother.

Mental Health Support: Provides tips for mental well-being during pregnancy.

Partner Guidance: Offers advice to partners to support the mother.

RAG-Powered Responses: Chatbots leverage RAG to give contextually relevant answers.

Customizable AI Response: Adjustable parameters such as max tokens, temperature, and top-p for fine-tuning chatbot outputs.

Tech Stack

The project leverages a modern full-stack and AI ecosystem:

Frontend:

React

TypeScript

Embedded Gradio chat interfaces via iframes

Backend / AI:

Python

Gradio – for building interactive chat interfaces

Hugging Face Inference API – for AI chat models (e.g., google/gemma-2-2b-it)

Sentence Transformers – for text embeddings (all-MiniLM-L6-v2)

FAISS – for similarity search and RAG retrieval

Python standard libraries – for file handling and preprocessing

RAG Implementation:

Load month-specific pregnancy guidance text.

Chunk text data for easier embedding.

Embed chunks using SentenceTransformer.

Store embeddings in FAISS index.

Retrieve relevant chunks based on user queries.

Augment system prompt with retrieved context for AI response.

Project Structure
PregniTech/
│
├─ frontend/               # React + TypeScript app
│
├─ backend/                # Python AI scripts (Gradio, RAG setup)
│   ├─ pregnancy_month1.txt
│   ├─ main.py
│
├─ README.md
└─ requirements.txt        # Python dependencies

Installation & Running

Clone the repository:

git clone https://github.com/Kainaatt/Pregnitech.git
cd PregniTech


Install Python dependencies:

pip install -r requirements.txt


Run the Gradio backend:

python backend/main.py


Start the frontend:

cd frontend
npm install
npm start


Access the app via your browser at http://localhost:3000.

Note: Ensure you have a Hugging Face token for AI inference API integration.

Team

Hashir Ehtisham – AI Chatbots Developer / Computer Engineer

Lameea Khan – Graphics Designer / Computer Engineer

Kainat Ali – MERN Stack Developer / Software Engineer

Learning & Implementation Highlights

Integration of RAG with AI chat models for context-aware pregnancy guidance.

Building interactive chat interfaces using Gradio in Python.

Month-specific content management and AI prompt augmentation.

Full-stack deployment using React + TypeScript and AI-powered backend.

Future Improvements

Expand chatbot knowledge base to include more detailed trimester-specific guidance.

Add voice-based interaction for better accessibility.

Integrate reminders and notifications for diet, medication, and appointments.

Improve frontend UI/UX for mobile-first accessibility.

License

This project is open-source. Feel free to fork, modify, and contribute.
