
##conditional graph

from typing import TypedDict, Literal
from langgraph.graph import START, StateGraph , END
from IPython.display import Image , display

class Portfolio(TypedDict):
    amount_usd: float
    total_usd : float
    tar_curr : Literal["EUR", "INR"]
    total : float


def calc_total(state : Portfolio):
    state["total_usd"]= state["amount_usd"]*1.08
    return state

def convert_to_inr(state : Portfolio):
    state["total_inr"]= state["total_usd"]*95.0
    return state

def convert_to_eur(state : Portfolio):
    state["total_eur"]= state["total_usd"]*0.92
    return state

def choose_currency(state : Portfolio):
    if state["tar_curr"] == "INR":
        return "convert_to_inr"
    else:
        return "convert_to_eur"

if __name__ == "__main__":
    builder = StateGraph(Portfolio)
    builder.add_node("calc_total", calc_total)
    builder.add_node("convert_to_inr", convert_to_inr)
    builder.add_node("convert_to_eur", convert_to_eur)

    builder.add_edge(START, "calc_total")
    builder.add_conditional_edges("calc_total", choose_currency)
    builder.add_edge(["convert_to_inr", "convert_to_eur"], END)

    graph = builder.compile()

    print(graph.get_graph().draw_mermaid())

    print(graph.invoke({"amount_usd": 1000.0, "tar_curr": "INR"}))
