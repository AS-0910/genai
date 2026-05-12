from typing import TypedDict
from langgraph.graph import START, StateGraph , END
from IPython.display import Image , display

class Portfolio(TypedDict):
    amount_usd: float
    total_usd : float
    total_inr : float


def calc_total(state : Portfolio):
    state["total_usd"]= state["amount_usd"]*1.08
    return state

def convert_to_inr(state : Portfolio):
    state["total_inr"]= state["total_usd"]*95.0
    return state

if __name__ == "__main__":
    # portfolio: Portfolio = {
    #     "amount_usd": 1000.0,
    #     "total_usd": 5000.0,
    #     "total_inr": 370000.0
    # }

    # print(portfolio)

    builder = StateGraph(Portfolio)
    builder.add_node("calc_total", calc_total)
    builder.add_node("convert_to_inr", convert_to_inr)

    builder.add_edge(START, "calc_total")
    builder.add_edge("calc_total", "convert_to_inr")
    builder.add_edge("convert_to_inr", END)

    graph = builder.compile()

    display(Image(graph.get_graph().draw_mermaid_png()))

    print(graph.invoke({"amount_usd": 1000.0}))
