
useEffect 는 외부시스템과 컴포넌트를 동기화하는 react hook 입니다
ajax 요청, 이벤트리스너 등록/해제, DOM 조작 등의 부수효과 처리에 사용됩니다.

useEffect 는 컴포넌트가 처음 마운트 될 때 실행됩니다.
이후에는 의존설 배열에 등록된 값이 변경될 때마다 실행됩니다.

### 추가 질문
#### useEffect 는 동기적으로 실행되나요?
비동기적으로 실행되며 렌더링이 완료된 후 실행됩니다
동기 실행이 필요하다면 useLayoutEffect 를 사용하면 됩니다.

#### useEffect 에서 비동기함수 async/await 를 사용할 수 있나요?
useEffect 의 콜백함수는 비동기함수로 직접 만들 수 없습니다
비동기 함수를 내부에서 호출하는 방식으로 처리합니다.
```js
useEffect(() => {
  async function fetchData() {
    const response = await fetch("https://api.example.com/data");
    const data = await response.json();
    console.log(data);
  }

  fetchData();
}, []);
```