

# 🧠 CodeReview AI

CodeReview AI is a professional, high-performance code auditing and optimization platform. It combines **Deep Reinforcement Learning (DQN)** with state-of-the-art **Large Language Models** to provide intelligent, contextual code analysis and real-time grading.

![CodeReview AI Dashboard](https://raw.githubusercontent.com/Gauravdeori/Code-Review/main/public/placeholder.svg)

## 🚀 Key Features

- **Intelligent Analysis**: Leverages a **PyTorch-based DQN (Deep Q-Network)** agent that classifies code issues into specific action categories (Optimization, Syntax, Logic, Security).
- **LLM-Powered Explanations**: Integrates with **Groq** and **OpenAI** via a dynamic `llm_factory` to generate deep, human-readable explanations and fix suggestions.
- **Real-time Feedback**: Get instant "Reward Scores" and diagnostic metrics from the RL agent as you type or review code.
- **Premium UI/UX**: A state-of-the-art 4-panel dashboard featuring:
  - **Monaco-style Code Editor** with syntax highlighting.
  - **Diagnostic Action Panels** with confidence scores.
  - **AI Explanation Terminal** with markdown support.
  - **Reward History** visualization.
- **Theme-Aware**: Fully integrated system-level **Light and Dark modes**.
- **Multi-Language Support**: Professional audits for 13+ languages including Python, JavaScript, C++, Java, and more.

## 🛠️ Technical Stack

- **Frontend**: [React.js](https://reactjs.org/), [Vite](https://vitejs.dev/), [Tailwind CSS](https://tailwindcss.com/), [Shadcn UI](https://ui.shadcn.com/), [Framer Motion](https://www.framer.com/motion/).
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/), [PyTorch](https://pytorch.org/) (Custom DQN Agent), [Pydantic](https://docs.pydantic.dev/).
- **AI Services**: [Groq Cloud](https://groq.com/), [OpenAI API](https://openai.com/).
- **Deployment**: [Docker](https://www.docker.com/), [Hugging Face Spaces](https://huggingface.co/spaces).

## 📦 Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Gauravdeori/Code-Review.git
   cd Code-Review
   ```

2. **Environment Configuration**:
   Create a `.env` file in the root with your API keys:
   ```env
   GROQ_API_KEY=your_groq_key
   OPENAI_API_KEY=your_openai_key
   ```

3. **Backend Setup**:
   ```bash
   pip install -r requirements.txt
   python -m uvicorn backend.main:app --port 8000
   ```

4. **Frontend Setup**:
   ```bash
   npm install
   npm run dev
   ```

## 🐳 Docker Deployment

To build and run the containerized version:
```bash
docker build -t codereview-ai .
docker run -p 7860:7860 --env-file .env codereview-ai
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---
Built  by [Gaurav Deori](https://github.com/Gauravdeori)
