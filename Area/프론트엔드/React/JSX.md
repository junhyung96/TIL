Javascript  syntax extension

React에서 사용되는 문법으로, JavaScript 코드 내에서 HTML과 유사한 형식의 markup 코드를 작성할 수 있게 해주는 문법

JSX Rules

1. 하나의 리액트 엘리먼트를 반환해야 함
	- 여러 태그가 있다면 하나의 큰 태그로 묶어서 반환
	- 굳이 ```<div></div>``` 가 아니어도 됨 ```<></>``` 빈 태그로 묶어서 반환가능 Fragement라고 함
2. 모든 태그는 닫혀 있어야 함
3. camelCase 를 사용
	1. [JSX attributes 공식문서](https://react.dev/reference/react-dom/components/common)

```JSX
export default function TodoList() {
      return (
      <>
        <h1>Hedy Lamarr's Todos</h1>
        <img 
          src="https://i.imgur.com/yXOvdOSs.jpg" 
          alt="Hedy Lamarr" 
	      class="photo"
        />
        <ul>
          <li>Invent new traffic lights</li>
          <li>Rehearse a movie scene</li>
          <li>Improve the spectrum technology</li>
        </ul>
      </>
	  );
	}
```

## HTML 과 JSX 의 차이

```JSX
const h1 = <h1>Hello world</h1>
ReactDOM.render(element, document.querySelector("#app"));
```

HTML - attribute name 소문자만 사용

```HTML
<h2 class="container">Hi</h2>
```

JSX - 기본적으로 javascript 이기 때문에 camelCase 사용

```JSX
<h2 className="container">Hi</h2>
// class 는 자바스크립트의 예약어이므로 사용불가 className으로 사용
```

## 기존의 HTML 문법대로 적고 변환사이트를 이용해서 JSX 문법으로 고칠 수 있다.

[HTML to JSX converter](https://transform.tools/html-to-jsx)

```json
{
  "name": "1-react",
  "version": "1.0.0",
  "description": "",
  "main": "src/main.js",
  "scripts": {
    "start": "webpack serve --config ../shared/webpack.config.js"
  },
  "author": "Jeonghwan Kim <ej88ej@gmail.com>",
  "license": "ISC",
  "dependencies": {
    "@babel/core": "^7.17.10",
    "@babel/preset-react": "^7.16.7",
    "babel-loader": "^8.2.5",
    "msw": "^1.2.1",
    "react": "^18.1.0",
    "react-dom": "^18.1.0",
    "webpack": "^5.72.1",
    "webpack-cli": "^4.9.2",
    "webpack-dev-server": "^4.9.0"
  },
  "babel": {
    "presets": [
      [
        "@babel/preset-react",
        {
          "runtime": "automatic"
        }
      ]
    ]
  }
}
```

JSX 문법을 사용하려면 코드 상단에 react 를 import 해와야 했는데 "babel" : 이후의 코드가 자동으로 해줌