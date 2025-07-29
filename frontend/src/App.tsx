import "@/App.css";
import { createBrowserRouter, RouterProvider } from "react-router";
import ProtectedRoute from "@/components/protected-route";
import MainLayout from "@/components/main-layout";
import LoginPage from "@/pages";
import { Toaster } from "@/shadcn/ui/sonner";
import WorkflowPage from "./pages/workflow";

const router = createBrowserRouter([
  {
    path: "/",
    element: <ProtectedRoute />,
    children: [
      {
        element: <MainLayout />,
        children: [
          {
            index: true,
            Component: WorkflowPage,
          },
        ],
      },
    ],
  },
  {
    path: "/login",
    Component: LoginPage,
  },
]);

function App() {
  return (
    <>
      <RouterProvider router={router} />
      <Toaster richColors closeButton />
    </>
  );
}

export default App;
