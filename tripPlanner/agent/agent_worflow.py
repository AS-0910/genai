from utils.model_loader import ModelLoader
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from prompt_library.prompt import SYSTEM_PROMPT
from tools.place_info_tool import PlaceSearchTool
from tools.arithmetic_tool import ArithmeticTool
from tools.currency_conversion_tool import CurrencyConversionTool
from tools.weather_info_tool import WeatherInfoTool


class GraphBuilder:
    def __init__(self):
        self.model_loader = ModelLoader()
        self.llm= self.model_loader.load_model()
        self.system_prompt = SYSTEM_PROMPT

        self.tools = []
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = ArithmeticTool()
        self.currency_converter_tools = CurrencyConversionTool()

        self.tools.extend([* self.weather_tools.weather_tool_list, 
                           * self.place_search_tools.tools_list,
                           * self.calculator_tools.tools_list,
                           * self.currency_converter_tools.tools_list])
        
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        self.graph = None

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