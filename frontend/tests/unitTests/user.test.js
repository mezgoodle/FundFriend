import UserPage from "@/app/user/page";
import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";

describe("User page", () => {
  it("renders a user component", () => {
    render(<UserPage />);
    expect(screen.getByTestId("root")).toBeInTheDocument();
    expect(screen.getByTestId("root")).toHaveTextContent("Hello user");
  });
});
