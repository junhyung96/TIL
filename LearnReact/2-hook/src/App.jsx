import React, { setState, useState } from "react";
import MyReact from "./lib/MyReact";


const Counter = () => {
  MyReact.resetCursor()

  const [count, setCount] = useState(0)
  const [name, setName] = useState(localStorage.getItem("name" || ""))

  const handleClick = () => setCount(count + 1)

  const handleChangeName = e => setName(e.target.value)

  // 지금 useEffect 는 name 이 변경되어도 호출됨
  // useEffect 에는 현재 count 만 사용되고 있고
  // count에 변경사항이 있을 때만 실행되도록 해야함
  // 이 때 등장하는게 의존성

  MyReact.useEffect(() => {
    document.title = `count: ${count}`
    console.log("effect1")
  }, count)

  MyReact.useEffect(() => {
    localStorage.setItem("name", name)
    console.log("effect2")
  }, name)

  console.log('Counter rendered')
  return <>
  <button onClick={handleClick}>더하기</button>
  <input value={name} onChange={handleChangeName} />
  </>
}

export default Counter


// const App = () => <>2-hook</>;

// export default App;
