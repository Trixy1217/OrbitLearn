from src.agents.States.state import CoachState
from src.agents.diagnostic_agent.node import node_diagnostic
from src.agents.evaluator_agent.node import evaluator_node
from src.agents.gamification_agent.node import gamification_node
from src.agents.planner_agent.node import planner_node
from src.agents.rag_agent.node import rag_node
from src.agents.orchestador_agent.node import orchestor_node
from src.agents.graph.router  import router






import os



from langgraph.graph import StateGraph, START, END



builder = StateGraph(CoachState)
builder.add_node("orchestrator", orchestor_node)
builder.add_node("diagnostic", node_diagnostic)
builder.add_node("planner", planner_node)
builder.add_node("rag",rag_node)



builder.add_edge(START, "orchestrator")

builder.add_conditional_edges("orchestrator", router,
    {
        "diagnostic": "diagnostic",
        "planner": "planner",
        "rag": "rag"
    }
)


builder.add_edge("diagnostic","planner")

builder.add_edge("planner","rag")

builder.add_edge("rag",END)

graph = builder.compile()