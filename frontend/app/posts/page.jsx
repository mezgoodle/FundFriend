"use client";
import useSWR from "swr";
import React from "react";
import { fetcher } from "@/api/fetcher";

function Posts() {
  const { data, error, isLoading } = useSWR(
    "https://jsonplaceholder.typicode.com/users",
    fetcher
  );

  if (error) return <div>Failed to load</div>;
  if (isLoading) return <div>Loading...</div>;

  // render data
  return (
    <ul>
      {data.map((todo) => (
        <li key={todo.id}>{todo.name}</li>
      ))}
    </ul>
  );
}

export default Posts;
