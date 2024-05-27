import React from "react";
import { Route, RouterProvider, createRoutesFromElements } from "react-router";

import { createBrowserRouter } from "react-router-dom";
import Login from "./Login/Login";
import StateChecker from "./StateChecker";
import Account from "./Account/Account";

function Main() {
  const routes = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<StateChecker />}>
        <Route path="" element={<Account />} />
        <Route path="/login" element={<Login />} />
      </Route>
    )
  );

  return <RouterProvider router={routes} />;
}

export default Main;
