from fastapi import APIRouter
from schemas.admin import Admin


admin_router = APIRouter()
@admin_router.post('/api/admin')
def create_admin(data_admin: Admin):
    print(data_admin)
