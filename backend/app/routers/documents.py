from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud
from ..dependencies import get_db
from ..schemas.document import DocumentCreate, DocumentOut, DocumentUpdate

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/", response_model=DocumentOut)
def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    return crud.create_document(db=db, document=document)


@router.get("/{document_id}", response_model=DocumentOut)
def read_document(document_id: int, db: Session = Depends(get_db)):
    db_document = crud.get_document(db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document


@router.put("/{document_id}", response_model=DocumentOut)
def update_document(
    document_id: int, document: DocumentUpdate, db: Session = Depends(get_db)
):
    db_document = crud.update_document(
        db=db, document_id=document_id, document=document
    )
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document


@router.delete("/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    db_document = crud.delete_document(db=db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"message": "Document deleted successfully"}
