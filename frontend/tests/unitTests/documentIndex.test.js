import DocumentPage from "@/app/user/documents/page";
import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";

describe("Document page", () => {
  it("renders a document component", () => {
    render(<DocumentPage />);
    expect(screen.getByTestId("root")).toBeInTheDocument();
    expect(screen.getByTestId("root")).toHaveTextContent("Your Documents");
  });
});
