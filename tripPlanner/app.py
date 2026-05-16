from fastapi import FastAPI
from agent.agent_worflow  import GraphBuilder
from starlette.responses import JSONResponse
from dto.request import RequestModel
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import HumanMessage
import os
import datetime
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set specific origins in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/query")
def query(request: RequestModel):
    logger.info(f"Received query request: {request.question}")
    try:
        graph = GraphBuilder()
        logger.debug("GraphBuilder initialized")
        
        react_app = graph.build_graph()
        logger.debug("Graph built successfully")

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)
        logger.debug(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
        
        # Assuming request is a pydantic object like: {"question": "your text"}
        messages={"messages": [HumanMessage(content=request.question)]}
        logger.debug(f"Messages prepared: {len(messages['messages'])} message(s)")
        
        output = react_app.invoke(messages)
        logger.debug(f"Graph invoked, output type: {type(output)}")

        # If result is dict with messages:
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Last AI response
            logger.debug(f"Extracted final output from messages")
        else:
            final_output = str(output)
            logger.debug(f"Output converted to string")
        
        logger.info(f"Query processed successfully")

        return JSONResponse(content={"answer": final_output}, status_code=200)
    
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}", exc_info=True)
        return JSONResponse(status_code=500, content={"error": str(e)})