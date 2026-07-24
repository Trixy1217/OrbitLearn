from src.agents.States.state import CoachState

def router(state):
    return state["next_agent"]