import random
from utils.reward import calculate_reward
from services.llm_factory import evaluate_code

class CodeReviewEnv:
    def __init__(self):
        self.state_size = 5 # arbitrary metrics: complexity, length, lines, etc.
        self.action_size = 5
        # Actions mapping
        # 0: Detect syntax errors
        # 1: Detect logical bugs
        # 2: Suggest optimization
        # 3: Suggest code improvements
        # 4: Approve/reject code
        
    def reset(self, code: str):
        # Convert code to dummy state vector
        # In a real system, this would be an embedding of the code
        return [random.random() for _ in range(self.state_size)]
        
    def step(self, action: int, code: str, language: str = "python"):
        # Real environment dynamics using LLM
        eval_result = evaluate_code(code, language)
        
        is_correct = eval_result.get("is_correct", False)
        is_useful = eval_result.get("is_useful", False)
        missed_critical = eval_result.get("missed_critical", False)
        detected_issue = eval_result.get("detected_issue", "None")
        
        reward = calculate_reward(is_correct, is_useful, missed_critical)
        
        # Next state could be updated metrics, but for now we keep it random for the agent to learn
        next_state = [random.random() for _ in range(self.state_size)]
        done = True # One-shot review
        
        return next_state, reward, done, detected_issue
