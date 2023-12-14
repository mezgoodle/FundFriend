import React from "react";

const DocumentDynamicPage = ({ params }) => {
  return <div data-testid="root">{params.documentId}</div>;
};

export default DocumentDynamicPage;
