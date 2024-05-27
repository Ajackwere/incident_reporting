import { QueryClient, QueryClientProvider } from "react-query";
import { ReactQueryDevtools } from "react-query/devtools";

import "./App.css";
import Main from "./Components/Main";
import { Context } from "./AppContext/Context";
function App() {
  const queryClient = new QueryClient();

  return (
    <Context>
      <QueryClientProvider client={queryClient}>
        <Main />
        <ReactQueryDevtools initialIsOpen={false} />
      </QueryClientProvider>
    </Context>
  );
}

export default App;
