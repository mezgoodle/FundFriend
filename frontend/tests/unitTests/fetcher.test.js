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
      json: jest.fn().mockResolvedValue(mockData),
    });

    const data = await fetcher("/api/test");
    expect(data).toEqual(mockData);
    expect(fetch).toHaveBeenCalledWith("/api/test", expect.any(Object));
  });

  it("should throw an error when fetch fails", async () => {
    fetch.mockResolvedValueOnce({ ok: false });

    await expect(fetcher("/api/test")).rejects.toThrow("Failed to fetch");
  });

  it("should call fetch with provided options", async () => {
    const mockData = { name: "Test" };
    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      data: { key: "value" },
    };

    fetch.mockResolvedValueOnce({
      ok: true,
      json: jest.fn().mockResolvedValue(mockData),
    });

    const data = await fetcher("/api/test", options);

    expect(data).toEqual(mockData);
    expect(fetch).toHaveBeenCalledWith("/api/test", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(options.data),
    });
  });
});
