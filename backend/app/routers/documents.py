from fastapi import APIRouter, Depends, HTTPException, status

from ..crud.document import DocumentCRUD
from ..dependencies import SessionDep, get_document_crud
from ..schemas.document import DocumentCreate, DocumentOut, DocumentUpdate

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
    dependencies=[Depends(get_document_crud)],
)


@router.post("/", response_model=DocumentOut)
def create_document(
    document: DocumentCreate,
    session: SessionDep,
    document_crud: DocumentCRUD = Depends(),
):
    return document_crud.create(session, document)


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


@router.delete("/{document_id}")
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
