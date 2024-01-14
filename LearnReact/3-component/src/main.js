import React from "react"
import ReactDOM from "react-dom"
import { createRoot } from "react-dom/client"
import App from "./App.js"


// react 18 이후
const domNode = document.getElementById('root')
const root = createRoot(domNode);

root.render(<App />)

// react 18 이전
// ReactDOM.render(<App />, document.querySelector("#root"))