from fastapi import APIRouter

router = APIRouter(prefix="/students", tags=["students"])

#hard code list 
students = [
    {
        "id": 1,
        "name": "Yangzoom Lama",
    },
    {
        "id": 2,
        "name": "John Doe",
    },
    {
        "id": 3,
        "name": "lily Jones",
    },
]

#get 
@router.get("")
def get_students():
    print("Students:", students)
    return students
