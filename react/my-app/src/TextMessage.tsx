import { useContext } from "react";
import { HelloContext } from "./context/hello-conext";

const TextMessage = () => {
  const { darkTheme, toggleTheme } = useContext(HelloContext);
  return (
    <div>
      {darkTheme ? "This is dark mode" : "This is light mode"}
      <br />
      <button onClick={() => toggleTheme()}>Change</button>
    </div>
  );
};

export default TextMessage;
