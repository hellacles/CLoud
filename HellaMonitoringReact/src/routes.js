import React from "react";
import { Redirect } from "react-router-dom";

// Layout Types
import { DefaultLayout } from "./layouts";

// Route Views
import DeliveryOverview from "./views/DeliveryOverview";
import UserProfileLite from "./views/UserProfileLite";
import Tables from "./views/Tables";

export default [
  {
    path: "/",
    exact: true,
    layout: DefaultLayout,
    component: () => <Redirect to="/delivery-overview" />
  },
  {
    path: "/delivery-overview",
    layout: DefaultLayout,
    component: DeliveryOverview
  },
  {
    path: "/user-profile-lite",
    layout: DefaultLayout,
    component: UserProfileLite
  },
  {
    path: "/tables",
    layout: DefaultLayout,
    component: Tables
  }
];
