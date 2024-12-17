from fastapi import APIRouter, Depends, HTTPException, Request
from app.db import get_invoices  # Ensure the function is imported here
from app.models import Invoice
from app.security import get_current_user
from fastapi.responses import JSONResponse
from app.security import authenticate_request
import logging
from typing import List, Dict

router = APIRouter()

# Initialize logger
logger = logging.getLogger("uvicorn.error")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Function to authenticate the API key
def authenticate_request(api_key: str):
    valid_api_key = "your_valid_api_key"  # Replace with your actual key
    if api_key != valid_api_key:
        return False
    return True
def authenticate_request(api_key: str) -> bool:
    # Replace this with actual authentication logic
    if api_key == "valid_api_key":
        return True
    return False


# Endpoint to get top 5 invoices based on amount for a specific project (e.g., Project X)
@router.get("/invoices/top/{project_id}", response_model=dict)
async def get_top_invoices_for_project(project_id: int, user: str = Depends(get_current_user)):
    try:
        invoices = get_invoices()  # Fetch invoices
        project_invoices = [inv for inv in invoices if inv.get("project_id") == project_id]
        
        if not project_invoices:
            raise HTTPException(status_code=404, detail=f"No invoices found for Project ID {project_id}")
        
        # Sort invoices by 'total_claimed_amount', with a fallback to 0 if the key is missing
        top_invoices = sorted(project_invoices, key=lambda x: x.get("total_claimed_amount", 0), reverse=True)[:5]
        
        # Format the response as a message and the top 5 invoices
        response_message = "Here are the Top 5 Invoices based on the amount:"
        formatted_invoices = [
            {
                "Invoice ID": inv.get("id", "Unknown ID"),
                "Contractor Name": inv.get("contractor_name", "Unknown Contractor"),
                "Vendor Name": inv.get("vendor_name", "Unknown Vendor"),
                "Invoice Amount": inv.get("total_claimed_amount", 0)
            }
            for inv in top_invoices
        ]
        
        return {
            "message": response_message,
            "top_invoices": formatted_invoices
        }
    
    except Exception as e:
        logger.error(f"Error while fetching top invoices for project {project_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint to get the invoice with the highest balance
@router.get("/invoices/highest_balance", response_model=dict)
async def get_highest_balance_invoice(user: str = Depends(get_current_user)):
    try:
        invoices = get_invoices()  # Fetch invoice data
        if not invoices:
            raise HTTPException(status_code=404, detail="No invoices found")
        
        # Find the invoice with the highest balance
        invoice_with_highest_balance = max(invoices, key=lambda x: x["summary"]["balance_to_finish_including_retainage"])
        highest_balance_invoice = invoice_with_highest_balance["summary"]
        invoice_id = invoice_with_highest_balance["id"]
        balance = highest_balance_invoice["balance_to_finish_including_retainage"]
        
        return {
            "message": f"Here you go, The invoice with Id {invoice_id} has the highest balance amount pending with an amount ${balance:,.2f}."
        }
    
    except Exception as e:
        logger.error(f"Error while fetching highest balance invoice: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint to handle unrelated or incorrect questions (converted from Flask to FastAPI)

@router.get("/chatbot/question")
async def handle_unrelated_question(question: str, request: Request):
    try:
        # Get the API key from headers
        api_key = request.headers.get('API-Key')

        # Check if the API key is valid
        if not authenticate_request(api_key):
            logger.error("Unauthorized access attempt.")
            raise HTTPException(status_code=403, detail="Unauthorized access")

        # Check if a question is provided
        if not question:
            logger.warning("No question provided.")
            raise HTTPException(status_code=400, detail="Please provide a question.")

        # Handle negative questions like sports scores
        if "current score" in question.lower():
            return JSONResponse(status_code=200, content={"error": "Sorry, I cannot provide sports scores."})

        # If the question is not relevant, return a generic error
        return JSONResponse(status_code=400, content={"error": "I'm not sure how to answer that. Could you rephrase the question?"})

    except Exception as e:
        logger.error(f"Error while handling unrelated question: {e}")
        raise HTTPException(status_code=500, detail="Internal server error while processing your query.")
