import { createContext, useEffect, useState } from "react";

const CONT = createContext(null);
function Context({ children }) {
  const [userIsLoged, setUserIsLoged] = useState(false);
  const [path, setPath] = useState([
    { title: "Dashboard", path: "/admin/dashboard" },
  ]);
  const functions = {
    path,
    setPath,
    formatCurrencyKE,
    userIsLoged,
    setUserIsLoged,
  };

  function formatCurrencyKE(number) {
    if (isNaN(number)) {
      return "Invalid Input";
    }
    const amount = parseFloat(number);
    const formatter = new Intl.NumberFormat("en-KE", {
      style: "currency",
      currency: "KES",
    });

    return formatter.format(amount);
  }

  return <CONT.Provider value={functions}>{children}</CONT.Provider>;
}
export { Context, CONT };
