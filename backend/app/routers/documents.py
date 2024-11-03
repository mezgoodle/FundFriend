from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from ..crud.document import DocumentCRUD
from ..dependencies import (
    SessionDep,
    get_current_active_user,
    get_document_crud,
)
from ..schemas.document import DocumentCreate, DocumentOut, DocumentUpdate
from ..schemas.user import UserOut

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
    dependencies=[Depends(get_document_crud)],
)


@router.post(
    "/", response_model=DocumentOut, status_code=status.HTTP_201_CREATED
)
def create_document(
    document: DocumentCreate,
    session: SessionDep,
    current_user: Annotated[UserOut, Depends(get_current_active_user)],
    document_crud: DocumentCRUD = Depends(),
):
    return document_crud.create(session, document, current_user.id)


@router.get("/{document_id}", response_model=DocumentOut)
def read_document(
    document_id: int,
    session: SessionDep,
    document_crud: DocumentCRUD = Depends(),
):
    db_document = document_crud.get(session, document_id)
    if db_document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Document not found"
        )
    return db_document


@router.get(
    "/",
    response_model=list[DocumentOut],
    status_code=status.HTTP_200_OK,
)
async def read_documents(
    session: SessionDep,
    offset: int = 0,
    limit: int = 100,
    document_crud: DocumentCRUD = Depends(),
) -> list[DocumentOut]:
    documents = document_crud.get_all(session, offset, limit)
    return documents


@router.put("/{document_id}", response_model=DocumentOut)
def update_document(
    document_id: int,
    document: DocumentUpdate,
    session: SessionDep,
    document_crud: DocumentCRUD = Depends(),
):
    db_document = document_crud.update(session, document_id, document)
    if db_document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Document not found"
        )
    return db_document


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(
    document_id: int,
    session: SessionDep,
    document_crud: DocumentCRUD = Depends(),
):
    db_document = document_crud.delete(session, document_id)
    if db_document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Document not found"
        )
    return {"message": "Document deleted successfully"}


@router.get(
    "/user/{user_id}",
    response_model=list[DocumentOut],
    status_code=status.HTTP_200_OK,
)
async def read_documents_by_user(
    user_id: int,
    session: SessionDep,
    document_crud: DocumentCRUD = Depends(),
) -> list[DocumentOut]:
    documents = document_crud.get_documents_by_user(session, user_id)
    return documents
