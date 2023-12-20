from fastapi import status, HTTPException


def find_error_message_exception(data_name: str, id: int):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"{data_name} with id: {id} was not found!")
