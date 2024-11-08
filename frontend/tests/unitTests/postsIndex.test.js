import Posts from "@/app/posts/page";
import "@testing-library/jest-dom";
import useSWR from "swr";
import { render, screen, waitFor } from "@testing-library/react";

jest.mock("swr");

describe("Posts page", () => {
  it("renders loading state initially", () => {
    useSWR.mockReturnValue({ data: null, error: null, isLoading: true });
    render(<Posts />);
    expect(screen.getByText("Loading...")).toBeInTheDocument();
  });

  it("renders data when request is successful", async () => {
    useSWR.mockReturnValue({ data: [{ name: "Test", id: 1 }], error: null });
    render(<Posts />);

    await waitFor(() => expect(screen.getByText("Test")).toBeInTheDocument());
  });

  it("renders error message on fetch failure", () => {
    useSWR.mockReturnValue({ data: null, error: new Error("Failed to fetch") });
    render(<Posts />);

    expect(screen.getByText("Failed to load")).toBeInTheDocument();
  });
});
