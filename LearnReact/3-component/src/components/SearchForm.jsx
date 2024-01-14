import React from "react";
// 입력 폼에는 사용자 입력이 있다
// input Element의 상태는 기본적으로 브라우저가 관리
// 우리의 역할은 입력한 값을 저장하고 있어야 함
// state가 필요하니 함수 컴포넌트보다는 클래스 컴포넌트가 적절하다

const SearchForm = ({value, onChange, onSubmit, onReset}) => {

    const handleSubmit = (event) => {
      event.preventDefault()
      onSubmit()
    }
    
    const handleReset = () => {
      onReset()
    }

    const handleChangeInput = (event) => {
        onChange(event.target.value)
      }

    return (
    <form
      onSubmit={handleSubmit}
      onReset={handleReset}
    >
      <input
        type="text"
        placeholder="검색어를 입력하세요"
        autoFocus
        value={value}
        onChange={handleChangeInput}
      />
      {value.length > 0 && (
        <button type="reset" className="btn-reset"></button>
      )}
    </form>
  );
};
export default SearchForm

// export default class SearchForm extends React.Component {
//   constructor() {
//     super();
//   }
//   render() {
//     return (
//   }
// }
