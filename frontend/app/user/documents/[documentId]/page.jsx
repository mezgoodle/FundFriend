"use client";
import React from "react";
import Document from "@/components/Document";

function DocumentPage({ params }) {
  const { id } = params;

  const document = {
    id: id,
    name: "Document 1",
    author: "John Doe",
    size: "1.2 MB",
    createdAt: "2022-01-01 12:00:00",
    googleBucketUrl: "https://example.com/document1.pdf",
    preview: "https://example.com/document1-preview.jpg",
  };

  return (
    <div className="flex flex-col h-screen" data-testid="root">
      <div className="flex-1 overflow-y-auto">
        <Document document={document} />
      </div>
    </div>
  );
}

export default DocumentPage;
