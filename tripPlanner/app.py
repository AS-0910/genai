from fastapi import FastAPI
from agent.agent_worflow  import GraphBuilder
from starlette.responses import JSONResponse
from dto.request import RequestModel
from fastapi.middleware.cors import CORSMiddleware
import os
import datetime
import json

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
    graph = GraphBuilder()
    react_app = graph.build_graph()

    png_graph = react_app.get_graph().draw_mermaid_png()
    with open("my_graph.png", "wb") as f:
        f.write(png_graph)

    print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
    # Assuming request is a pydantic object like: {"question": "your text"}
    messages={"messages": [request.question]}
    
    try:
        output = react_app.invoke(messages)

        # If result is dict with messages:
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Last AI response
        else:
            final_output = str(output)
        
        response = json.dumps({"answer": final_output})

        return JSONResponse(content=response, status_code=200)
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})