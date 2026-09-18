from fastapi import APIRouter

router = APIRouter()


@router.get("/interviews/{interview_id}")
async def get_interview(interview_id: int):
    return {
        "interview_id": interview_id
    }


@router.get("/interviews")
async def list_interviews(limit: int = 10):
    return {
        "limit": limit
    }