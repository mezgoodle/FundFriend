import { Inter } from "next/font/google";
import "./globals.css";
import Sidebar from "@/components/SideBar";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "FundFriend",
  description: "Fund your knowledge with FundFriend",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <Sidebar />
      <body className={inter.className + " ml-72"}>{children}</body>
    </html>
  );
}
