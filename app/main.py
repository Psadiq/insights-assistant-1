from fastapi import FastAPI
from app.routers import invoices
import logging

# Create the FastAPI instance first
app = FastAPI()

# Set up logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Create a logger instance
logger = logging.getLogger(__name__)

# Include the router for invoices
app.include_router(invoices.router)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Insight Assistant API is up and running!"}
