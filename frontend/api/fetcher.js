export const fetcher = (url, options = {}) => {
  const { method = "GET", headers = {}, data, ...rest } = options;

  const fetchOptions = {
    method,
    headers,
    ...(data ? { body: JSON.stringify(data) } : {}),
    ...rest,
  };

  return fetch(url, fetchOptions).then((res) => {
    if (!res.ok) throw new Error("Failed to fetch");
    return res.json();
  });
};
