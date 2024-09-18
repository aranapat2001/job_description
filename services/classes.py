### DEFINE CLASSES FOR INPUT PARAMETERS ####

from pydantic import BaseModel

class GenerationDetails(BaseModel):
    business_unit: str | None = None
    template_structure: str | None = None
    template_name: str | None = None
    emojis: str | None = None
    tone: str | None = None
    language: str | None = None
    
class ClientParams(BaseModel):
    client_sector: str | None = None
    client_url: str | None = None
    
class JobParams(BaseModel):
    profession: str | None = None
    city: str | None = None
    province: str | None = None
    min_pay: str | None = None
    max_pay: str | None = None
    freq_pay: str | None = None
    bonus: str | None = None
    benefits: str | None = None
    contract_type: str | None = None
    work_rate: str | None = None
    num_employees: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    schedule: str | None = None
    
class ReqParams(BaseModel):
    skills: str | None = None
    driving_license: str | None = None
    vehicle: str | None = None
    work_type: str | None = None