from pydantic import BaseModel

class Invoice(BaseModel):
    id: int
    project_id: int
    total_claimed_amount: float
    balance_to_finish_including_retainage: float
    vendor_name: str
    contractor_name: str
