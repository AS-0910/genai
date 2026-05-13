from utils.model_loader import ModelLoader
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from prompt_library.prompt import SYSTEM_PROMPT


class GraphBuilder:
    def __init__(self):
        self.tools= []
        self.llm= None
        self.llm_with_tools= None
        self.system_prompt= SYSTEM_PROMPT

    def agentic_function(self, state : MessagesState):
        user_input=state["messages"]
        context= [self.system_prompt] + user_input
        response= self.llm_with_tools.invoke(context)
        return {"messages" : [response]}

    def build_graph(self):
        """
           start
            |
           Agent == tools
            |
            end  

        """
        graph_builder= StateGraph(MessagesState)

        graph_builder.add_node("agent", self.agentic_function)
        graph_builder.add_node("tools",ToolNode(tools= self.tools))

        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edge("agent",tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)

        self.graph=graph_builder.compile()
        return self.graph
    
    def __call__(self):
        return self.build_graph()