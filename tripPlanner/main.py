import uvicorn
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting AI Travel Planner server...")
    uvicorn.run("app:app", host="localhost", port=9001)
 