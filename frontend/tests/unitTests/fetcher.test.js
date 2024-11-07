// fetcher.test.js
import { fetcher } from "@/api/fetcher";

global.fetch = jest.fn();

describe("fetcher", () => {
  afterEach(() => {
    fetch.mockClear();
  });

  it("should return JSON data when fetch is successful", async () => {
    const mockData = { name: "Test" };
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockData,
    });

    const data = await fetcher("/api/test");
    expect(data).toEqual(mockData);
    expect(fetch).toHaveBeenCalledWith("/api/test");
  });

  it("should throw an error when fetch fails", async () => {
    fetch.mockResolvedValueOnce({ ok: false });

    await expect(fetcher("/api/test")).rejects.toThrow("Failed to fetch");
  });
});
