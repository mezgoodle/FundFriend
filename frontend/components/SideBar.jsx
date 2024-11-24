import React from "react";
import Link from "next/link";
import { redirect } from "next/navigation";

function Sidebar() {
  return (
    <div className="w-64 bg-gray-200 p-4 fixed top-0 left-0 h-screen z-10 shadow-2xl">
      <div className="flex items-center mb-4">
        <span className="text-lg font-bold">Іван Іваненко</span>
      </div>
      <ul>
        <li>
          <Link href="/user/documents" className="block py-2 hover:bg-gray-300">
            Документи
          </Link>
        </li>
        <li>
          <Link href="/user/chats" className="block py-2 hover:bg-gray-300">
            Збережені чати
          </Link>
        </li>
        <li>
          <Link href="messenger" className="block py-2 hover:bg-gray-300">
            Новий чат
          </Link>
        </li>
        <li>
          <Link href="/user" className="block py-2 hover:bg-gray-300">
            Профіль
          </Link>
        </li>
        <li>
          <Link href="/logout" className="block py-2 hover:bg-gray-300">
            Вийти
          </Link>
        </li>
      </ul>
    </div>
  );
}

export default Sidebar;
