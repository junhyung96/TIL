import React, { useState } from "react";

const MyReact = (function MyReact() {
  let firstname;
  let isInitialized = false;

  function useName(initialValue = "") {
    const { forceUpdate } = useForceUpdate();

    if (!isInitialized) {
      firstname = initialValue;
      // 처음 훅이 호출되었을 때만 저장되야함
      isInitialized = true;
    }

    // firstname 을 변경할 setter
    const setFirstname = (value) => {
      if (firstname === value) return;
      firstname = value;
      // 상태를 변경했으면 리렌더링해줘야하는데 직접 구현하기 힘듬
      // forceUpdate라는 함수를 만들고 그안에서
      // React 의 useState 함수를 사용함 = 리렌더링됨
      // 이 때 setFirstname 도 같이 리렌더링되게 해줌
      // forceUpdate 가 실행되면 컴포넌트가 다시 리렌더됨
      forceUpdate();
    };

    function useForceUpdate() {
      const [value, setValue] = React.useState(1);
      const forceUpdate = () => setValue(value + 1);
      return { forceUpdate };
    }

    return [firstname, setFirstname];
    // useName 함수가 종료되더라도 firstname 과 setFirstname 을 사용하기 때문에
    // 클로저에 캡쳐되어 있을 것임
  }
  return { useName };
})();
// 끝에 () 붙이면 즉시실행함수

// export default MyReact;

// 함수가 종료되더라도 유지되는 값
