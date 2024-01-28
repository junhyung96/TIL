import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const { worker } = require("../../shared/mocks/browser");
worker.start({
  onUnhandledRequest: "bypass",
});

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<App />);
// 다이얼로그 문제?? 문제가 뭐였지 를 해결하려면
// 다이얼로그를 렌더링 해주는 부분을 포탈로 연결하면 된다.






// const root2 = ReactDOM.createRoot(document.getElementById("dialog"));


// import ReactDOM2 from 'react-dom'
// const Red = () =>
//   ReactDOM2.createPortal(
//     <div className="red">Red</div>,
//     document.getElementById("dialog")
//   )
// const Green = () => (
//   <div className="green" onClick={(event) => console.log('click', event)}>
//     <div>Green</div>
//     <Red />
//   </div>
// )
// root.render(<Green />)
// root2.render(<Red />)