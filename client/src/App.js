
import React from "react";
import TodoList from "./components/TodoList";
import './App.css';

function App() {
  return (

    <div className="App">
      <p
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          fontSize: "2rem",
          fontWeight: "bolder",
        }}
      ><strong>TO DO LIST</strong></p>
      <hr />

      <TodoList />

    </div>

  );

}

export default App;