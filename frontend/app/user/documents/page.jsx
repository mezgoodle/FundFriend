// pages/documents.js
import React from "react";
import Link from "next/link";

function DocumentsPage() {
  const documents = [
    {
      id: 1,
      name: "Документ 1",
      type: "PDF",
      size: "1.2 MB",
    },
    {
      id: 2,
      name: "Документ 2",
      type: "DOCX",
      size: "2.5 MB",
    },
    {
      id: 3,
      name: "Документ 3",
      type: "XLSX",
      size: "1.8 MB",
    },
  ];

  return (
    <div className="flex flex-col h-screen">
      <div className="flex-1 overflow-y-auto">
        <table className="w-full table-auto border-collapse border border-gray-400">
          <thead>
            <tr>
              <th className="px-4 py-2 border border-gray-400">Назва</th>
              <th className="px-4 py-2 border border-gray-400">Тип</th>
              <th className="px-4 py-2 border border-gray-400">Розмір</th>
              <th className="px-4 py-2 border border-gray-400">Посилання</th>
            </tr>
          </thead>
          <tbody>
            {documents.map((document) => (
              <tr key={document.id} className="hover:bg-gray-100">
                <td className="px-4 py-2 border border-gray-400">
                  {document.name}
                </td>
                <td className="px-4 py-2 border border-gray-400">
                  {document.type}
                </td>
                <td className="px-4 py-2 border border-gray-400">
                  {document.size}
                </td>
                <td className="px-4 py-2 border border-gray-400">
                  <Link
                    href={{
                      pathname: `/user/documents/${document.id}`,
                    }}
                  >
                    Переглянути
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default DocumentsPage;
