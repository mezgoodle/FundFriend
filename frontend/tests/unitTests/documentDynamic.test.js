import DocumentDynamicPage from "@/app/user/documents/[documentId]/page";
import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";

describe("Document dynamic page", () => {
  it("renders a document dynamic component", () => {
    render(<DocumentDynamicPage params={{ documentId: "123" }} />);
    expect(screen.getByTestId("root")).toBeInTheDocument();
    expect(screen.getByTestId("root")).toHaveTextContent("123");
  });
});
