import React, {  useState } from "react";

export const HelloContext = React.createContext();

export const HelloProvider= ({ children }) => {
  const [darkTheme, setDarkTheme] = useState(true);

  const toggleTheme = () => {
    setDarkTheme((prevDarkTheme) => !prevDarkTheme);
  };
  return (
    <HelloContext.Provider value={{ darkTheme, toggleTheme }}>
      {children}
    </HelloContext.Provider>
  );
};
