import React from "react";
import { HelloProvider } from "./context/hello-conext";
import TextMessage from "./TextMessage";
interface Props {}

const App: React.FC<Props> = (props) => {
  return (
    <HelloProvider>
      <TextMessage />
    </HelloProvider>
  );
};

export default App;
