from fastapi import APIRouter, Depends


from .paper.urls import paper_module_router
router = APIRouter()
router.include_router(paper_module_router)

