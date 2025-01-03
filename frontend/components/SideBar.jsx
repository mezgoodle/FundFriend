import React from "react";
import Link from "next/link";
import { redirect } from "next/navigation";

function Sidebar() {
  return (
    <div className="w-64 bg-gray-200 p-4 fixed top-0 left-0 h-screen z-10 shadow-2xl">
      <div className="flex items-center mb-4">
        <span className="text-lg font-bold">Maksym Zavalniuk</span>
      </div>
      <ul>
        <li>
          <Link href="/user/documents" className="block py-2 hover:bg-gray-300">
            Documents
          </Link>
        </li>
        <li>
          <Link href="/user/chats" className="block py-2 hover:bg-gray-300">
            Saved chats
          </Link>
        </li>
        <li>
          <Link href="messenger" className="block py-2 hover:bg-gray-300">
            New chat
          </Link>
        </li>
        <li>
          <Link href="/user" className="block py-2 hover:bg-gray-300">
            Profile
          </Link>
        </li>
        <li>
          <Link href="/logout" className="block py-2 hover:bg-gray-300">
            Logout
          </Link>
        </li>
      </ul>
    </div>
  );
}

export default Sidebar;
