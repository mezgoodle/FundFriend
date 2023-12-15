import Home from "@/app/page";
import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";

describe("Home page", () => {
  it("renders a home component", () => {
    render(<Home />);
    expect(screen.getByTestId("root")).toBeInTheDocument();
    expect(screen.getByTestId("root")).toHaveTextContent("Index page");
  });
});
