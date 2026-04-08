from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from env.code_review_env import CodeReviewEnv
from agent.dqn_agent import DQNAgent
from services.llm_factory import get_explanation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global RL instances for demonstration state persistence
env = CodeReviewEnv()
agent = DQNAgent(env.state_size, env.action_size)

ACTIONS = [
    "Detect syntax errors",
    "Detect logical bugs",
    "Suggest optimization",
    "Suggest code improvements",
    "Approve/reject code"
]

class ReviewRequest(BaseModel):
    code: str
    language: str

@app.post("/review")
async def review_code(req: ReviewRequest):
    # 1. State representing the code
    state = env.reset(req.code)
    
    # 2. Agent decides which action category applies to this code snippet
    action_idx = agent.act(state)
    
    # 3. Environment validates the code and steps forward
    next_state, reward, done, detected_issue_real = env.step(action_idx, req.code, req.language)
    
    detected_issue = detected_issue_real if detected_issue_real != "None" else ACTIONS[action_idx]
    
    # 4. Remember transition and train memory
    agent.remember(state, action_idx, reward, next_state, done)
    agent.replay(1)
    
    # 5. Generate explanation
    explanation_text = get_explanation(req.code, detected_issue, req.language)
    
    return {
        "detected_issue": detected_issue,
        "reward_score": reward,
        "explanation": explanation_text,
        "agent_epsilon": agent.epsilon
    }

# Serve Static Files (Frontend)
# This will serve the build output from the `dist` directory
dist_path = os.path.join(os.path.dirname(__file__), "..", "dist")
if os.path.exists(dist_path):
    app.mount("/assets", StaticFiles(directory=os.path.join(dist_path, "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        if full_path.startswith("review"): # Don't intercept API calls if they don't start with /api (but here they don't)
            return None 
        # For simplicity, serve index.html for everything else to support SPA routing
        index_path = os.path.join(dist_path, "index.html")
        return FileResponse(index_path)
