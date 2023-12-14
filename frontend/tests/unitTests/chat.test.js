import ChatPage from "@/app/user/chat/page";
import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";

describe("Chat page", () => {
  it("renders a chat component", () => {
    render(<ChatPage />);
    expect(screen.getByTestId("root")).toBeInTheDocument();
    expect(screen.getByTestId("root")).toHaveTextContent("Chat page");
  });
});
