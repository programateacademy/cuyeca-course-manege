import datetime as _dt
import pydantic as _pydantic

class _SuperadminBase(_pydantic.BaseModel):
    email:str
    
 