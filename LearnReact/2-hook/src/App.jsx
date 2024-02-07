import React, { setState } from "react";
import MyReact from "./lib/MyReact";
// const App = () => <>2-hook</>;

// export default App;

function NameField() {
  const [firstname, setFirstname] = MyReact.useState("사용자1")
  const [lastname, setLastname] = MyReact.useState("김")
  const [name, setName] = MyReact.useState("박")

  const handleChangeFirstname = (e) => {
    setFirstname(e.target.value)
  }
  const handleChangeLastname = (e) => {
    setLastname(e.target.value)
  }
  const handleChangeName = (e) => {
    setName(e.target.value)
  }
  return <>
  <input value={firstname} onChange={handleChangeFirstname}/>
  <input value={lastname} onChange={handleChangeLastname}/>
  <input value={name} onChange={handleChangeName}/>
  </>
}

export default () => <NameField />