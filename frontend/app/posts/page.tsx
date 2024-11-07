"use client";
import useSWR from "swr";
import React from "react";

function fetcher(url: string, ...args: any[]) {
  return fetch(url).then((res) => res.json());
}

function Profile() {
  const { data, error, isLoading } = useSWR(
    "https://jsonplaceholder.typicode.com/users",
    fetcher
  );

  if (error) return <div>failed to load</div>;
  if (isLoading) return <div>loading...</div>;

  // render data
  return (
    <ul>
      {data.map((todo) => (
        <li key={todo.id}>{todo.name}</li>
      ))}
    </ul>
  );
}

export default Profile;
