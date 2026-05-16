from utils.model_loader import ModelLoader
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from prompt_library.prompt import SYSTEM_PROMPT
from tools.place_info_tool import PlaceSearchTool
from tools.arithmetic_tool import ArithmeticTool
from tools.currency_conversion_tool import CurrencyConversionTool
from tools.weather_info_tool import WeatherInfoTool
import logging

logger = logging.getLogger(__name__)


class GraphBuilder:
    def __init__(self):
        logger.debug("Initializing GraphBuilder")
        self.model_loader = ModelLoader()
        self.llm= self.model_loader.load_model()
        logger.debug("LLM model loaded")
        self.system_prompt = SYSTEM_PROMPT

        self.tools = []
        logger.debug("Loading tools...")
        self.weather_tools = WeatherInfoTool()
        logger.debug(f"Weather tools loaded: {len(self.weather_tools.weather_tool_list)} tools")
        
        self.place_search_tools = PlaceSearchTool()
        logger.debug(f"Place search tools loaded: {len(self.place_search_tools.tools_list)} tools")
        
        self.calculator_tools = ArithmeticTool()
        logger.debug(f"Calculator tools loaded: {len(self.calculator_tools.tools_list)} tools")
        
        self.currency_converter_tools = CurrencyConversionTool()
        logger.debug(f"Currency converter tools loaded: {len(self.currency_converter_tools.tools_list)} tools")

        self.tools.extend([* self.weather_tools.weather_tool_list, 
                           * self.place_search_tools.tools_list,
                           * self.calculator_tools.tools_list,
                           * self.currency_converter_tools.tools_list])
        logger.info(f"Total tools loaded: {len(self.tools)}")
        
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        logger.debug("LLM bound with tools")
        self.graph = None

    def agentic_function(self, state : MessagesState):
        logger.debug(f"Agentic function called with state containing {len(state['messages'])} messages")
        user_input=state["messages"]
        context= [self.system_prompt] + user_input
        logger.debug(f"Context prepared with {len(context)} elements")
        response= self.llm_with_tools.invoke(context)
        logger.debug(f"LLM response received")
        return {"messages" : [response]}

    def build_graph(self):
        """
           start
            |
           Agent == tools
            |
            end  

        """
        logger.debug("Building graph...")
        graph_builder= StateGraph(MessagesState)

        graph_builder.add_node("agent", self.agentic_function)
        logger.debug("Added agent node to graph")
        
        graph_builder.add_node("tools",ToolNode(tools= self.tools))
        logger.debug("Added tools node to graph")

        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)
        logger.debug("Graph edges configured")

        self.graph=graph_builder.compile()
        logger.info("Graph compiled successfully")
        return self.graph
    
    def __call__(self):
        return self.build_graph()