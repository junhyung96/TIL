function NameField() {
    const name = 'user1'
    const handleChange = e => {
      
    }
    return <input value={name} onChange={handleChange}/>
  }
  
export default () => <NameField />

// name 을 변경할 수 없다.
// name 은 함수가 종료되면 날라가기 때문
// 핸들 체인지 안에서는 클로저로 남아있다하더라도 변경할 수 있는 공간은 없음

// 입력값을 어딘가에 저장해야하고
// 사용자의 입력에 따라 변할 친구이기 때문에 "상태 state"라고 부를 개념이 등장

// 리액트의 useState를 사용하면 함수 컴포넌트가 상태변환에 따라 호출됨

// useEffect 훅을 직접 구현하면서 구조를 이해해보자
// ==> MyReact 로 이동
