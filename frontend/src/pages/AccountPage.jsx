import React, { useState } from 'react';
import RegForm from "../components/RegistrationForm.jsx";
import SuccessRegSignForm from "../components/SuccessRegSignForm.jsx";

function AccountPage() {
  const [isRegistrationComplete, setRegistrationComplete] = useState(false);

  const handleRegistrationSuccess = () => {
    setRegistrationComplete(true);
  };

  return (
    <div className="pt-40 px-20"> 
      <div className="justify-end">
        <div className="w-2/3 max-w-sm ml-auto">
          {isRegistrationComplete ? (
            <SuccessRegSignForm />
          ) : (
            <RegForm onSuccess={handleRegistrationSuccess} />
          )}
        </div>
      </div>
    </div>
  );
}

export default AccountPage;