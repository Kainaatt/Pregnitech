import gradio as gr
import os
from huggingface_hub import InferenceClient
from sentence_transformers import SentenceTransformer
import faiss

# ------------ RAG SETUP ---------------- #

# Load text data
with open("pregnancy_month5.txt", "r", encoding="utf-8") as f:
    data = f.read()

# Simple chunking
chunks = data.split("\n\n")

# Load embeddings model
embedder = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = embedder.encode(chunks)

# Create Faiss index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def rag_retrieve(query, top_k=3):
    query_emb = embedder.encode([query])
    distances, indices = index.search(query_emb, top_k)
    retrieved_chunks = [chunks[i] for i in indices[0]]
    return "\n".join(retrieved_chunks)

# ------------ ORIGINAL FUNCTION (with RAG injected) ---------------- #

def respond(
    message,
    history: list[dict[str, str]],
    system_message,
    max_tokens,
    temperature,
    top_p,
    hf_token: gr.OAuthToken,
):

    # ✅ Retrieve context for current user query
    retrieved_context = rag_retrieve(message)

    # ✅ Modify system prompt to include relevant data
    rag_augmented_system = (
        f"{system_message}\n\n"
        "Relevant medical guidance below:\n"
        f"{retrieved_context}\n\n"
        "Use this information while responding clearly and politely."
    )

    client = InferenceClient(token=hf_token.token, model="google/gemma-2-2b-it")

    messages = [{"role": "system", "content": rag_augmented_system}]
    messages.extend(history)
    messages.append({"role": "user", "content": message})

    response = ""

    for message in client.chat_completion(
        messages,
        max_tokens=max_tokens,
        stream=True,
        temperature=temperature,
        top_p=top_p,
    ):
        choices = message.choices
        token = ""
        if len(choices) and choices[0].delta.content:
            token = choices[0].delta.content

        response += token
        yield response


# ------------ UI (unchanged) ---------------- #

chatbot = gr.ChatInterface(
    respond,
    type="messages",
    additional_inputs=[
        gr.Textbox(value="You are a friendly Pregnancy 5th month guidance chatbot named 'PREGNITECH' developed by team Helix AI which consists of 3 members: Hashir Ehtisham, Lameea Khan and Kainat Ali.", label="System message"),
        gr.Slider(minimum=1, maximum=4096, value=2048, step=1, label="Max new tokens"),
        gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(
            minimum=0.1,
            maximum=1.0,
            value=0.95,
            step=0.05,
            label="Top-p (nucleus sampling)",
        ),
    ],
)

with gr.Blocks() as demo:
    with gr.Sidebar():
        gr.LoginButton()
    chatbot.render()


if __name__ == "__main__":
    demo.launch()
