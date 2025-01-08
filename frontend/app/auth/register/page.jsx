"use client";

import React, { useState } from "react";
import RegisterForm from "@/components/RegisterForm";

function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (event) => {
    event.preventDefault();
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full p-8 bg-white rounded-lg shadow-md mx-auto">
        <h2 className="text-lg font-bold mb-4">Registration</h2>
        <RegisterForm
          name={name}
          setName={setName}
          email={email}
          setEmail={setEmail}
          password={password}
          setPassword={setPassword}
          handleRegister={handleRegister}
        />
      </div>
    </div>
  );
}

export default Register;
