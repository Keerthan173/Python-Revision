from fastapi import APIRouter
router=APIRouter()

@router.get("/items/{id}")
async def read_id(id:int):
    return {"Hello":"SCEM"}