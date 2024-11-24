"use client";
import React from "react";

function DocumentPage({ params }) {
  const { id } = params;

  const document = {
    id: id,
    name: "Документ 1",
    author: "Іван Іваненко",
    size: "1.2 MB",
    createdAt: "2022-01-01 12:00:00",
    googleBucketUrl: "https://example.com/document1.pdf",
    preview: "https://example.com/document1-preview.jpg",
  };

  return (
    <div className="flex flex-col h-screen">
      <div className="flex-1 overflow-y-auto">
        <h2 className="text-lg font-bold mb-4">{document.name}</h2>
        <p className="text-sm text-gray-700 mb-4">Автор: {document.author}</p>
        <p className="text-sm text-gray-700 mb-4">Розмір: {document.size}</p>
        <p className="text-sm text-gray-700 mb-4">
          Дата створення: {document.createdAt}
        </p>
        <p className="text-sm text-gray-700 mb-4">
          Посилання на гугл бакет:{" "}
          <a href={document.googleBucketUrl} target="_blank">
            Переглянути
          </a>
        </p>
        {document.preview && (
          <img
            src={document.preview}
            alt="Прев'ю документа"
            className="w-full h-auto mb-4"
          />
        )}
      </div>
    </div>
  );
}

export default DocumentPage;
