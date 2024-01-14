// 자바스크립트 코드의 시작점
import { formatRelativeDate } from "/js/helpers.js";
import store from "/js/Store.js"
// 이후 코드를 모듈별로 분류해서 파일을 추가예정

const TabType = {
  KEYWORD: "KEYWORD",
  HISTORY: "HISTORY",
};
  
const TabLabel = {
  [TabType.KEYWORD]: "추천 검색어",
  [TabType.HISTORY]: "최근 검색어",
};

class App extends React.Component {
  constructor() { // 생성자 함수
    super();  
    this.state = {
      searchKeyword: "",
      searchResult: [],
      submitted: false,
      selectedTab: TabType.KEYWORD,
      keywordList: [],
      historyList: [],
    }
  }  

  componentDidMount() {
    const keywordList = store.getKeywordList()
    const historyList = store.getHistoryList()
    this.setState({ keywordList, historyList })
  }

  // 리액트에서 이벤트를 처리하는 핸들러명은 handle 로 시작함
  handleChangeInput(event) {
    // this.state.searchKeyword = event.target.value
    // 강제로 render 함수가 실행되게 해야 함
    // this.forceUpdate()
    // 하지만 입력의 state의 변경사항이 있을때마다 render 되면 부자연스러움
    // React 컴포넌트 스스로 state의 변화를 인지하고 스스로 render를 호출하게끔 수정되게 해야 함
    const searchKeyword = event.target.value

    if (searchKeyword.length <= 0 && this.state.submitted) {
        return this.handleReset()
    }

    // 컴포넌트의 상태를 변경시키겠다 라는 함수
    this.setState({ searchKeyword })
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log('handleSubmit', this.state.searchKeyword)
    this.search(this.state.searchKeyword)
  }

  search(searchKeyword) {
    const searchResult = store.search(searchKeyword)
    const historyList = store.getHistoryList()
    this.setState({
      searchKeyword,
      searchResult,
      submitted: true,
      historyList,
    })
  }

  handleReset() {
    // this.setState({ searchKeyword: "" })
    this.setState({ 
      searchKeyword: "", 
      submitted: false, 
    })
  }

  handleClickRemoveHistory(event, keyword) {
    // x 버튼을 누르면 키워드 클릭 이벤트가 버블링되어 먼저 실행됨
    event.stopPropagation(); // 이벤트가 버블링되지않도록 차단
    store.removeHistory(keyword)
    const historyList = store.getHistoryList()
    this.setState({ historyList })
  }

  render() { // Component 의 render 를 오버라이딩
    // 요구사항 : 검색어를 입력하면 x 버튼이 보이고 없으면 x 버튼을 숨긴다
    // 1. 엘리먼트 변수 사용
    // let resetButton = null;

    // if (this.state.searchKeyword.length > 0) {
    //     resetButton = <button type="reset" className="btn-reset"></button>
    // }
    const searchForm = (
      <form 
        onSubmit={event => this.handleSubmit(event)}
        onReset={() => this.handleReset()}
        >
        <input 
          type="text" 
          placeholder="검색어를 입력하세요" 
          autoFocus 
          value={this.state.searchKeyword}
          onChange={evenet => this.handleChangeInput(event)}
        />
        {this.state.searchKeyword.length > 0 && <button type="reset" className="btn-reset"></button>}
      </form>)

    const searchResult = (
        this.state.searchResult.length > 0 ? 
        (
          <ul className="result">
            {this.state.searchResult.map(item => {
              return (
                <li key={item.id}>
                  <img src={item.imageUrl} alt={item.name} />
                  <p>{item.name}</p>  
                </li>
              )
            })}
          </ul>
        ) : 
        (
          <div className="empty-box">검색 결과가 없습니다.</div>
        ))
    
    const keywordList = (
      <ul className="list">
        {this.state.keywordList.map((item, index) => {
          return (
            <li 
              key={item.id}
              onClick={()=> {
                this.search(item.keyword)
              }} 
            >
              <span className="number">{index + 1}</span>
              <span>{item.keyword}</span>
            </li>
          )
        })}
      </ul>
    )

    const historyList = (
      <ul className="list">
        {this.state.historyList.map((item) => {
          return (
            <li 
              key={item.id}
              onClick={()=> {
                this.search(item.keyword)
              }} 
            >
              <span>{item.keyword}</span>
              <span className="date">{formatRelativeDate(item.date)}</span>
              <button 
                className="btn-remove"
                onClick={(event) => this.handleClickRemoveHistory(event, item.keyword)}
              ></button>
            </li>
          )
        })}
      </ul>
    )

    const tabs = (
      <>
      <ul className="tabs">
        {Object.values(TabType).map(tabType => (
          <li 
            className={this.state.selectedTab === tabType ? "active" : ""} 
            key={tabType}
            onClick={() => this.setState({selectedTab: tabType})}
            >
            {TabLabel[tabType]}
          </li>
        ))}
      </ul>
      {this.state.selectedTab === TabType.KEYWORD && keywordList}
      {this.state.selectedTab === TabType.HISTORY && historyList}
      </>
    )

      // 리액트 엘리먼트를 반환하는 함수
    return (
        <> 
          <header>
            <h2 className="container">검색</h2>
          </header>
          <div className="container">
            {searchForm}
            <div className="content">
              {this.state.submitted ? searchResult : tabs}
            </div>
          </div>
        </>
    )
  }
}
ReactDOM.render(<App />, document.querySelector("#app"));

// const element = (
//     // 루트 노드가 하나 있어야 함
//     // 비어있는 tag : fragment 라 하는데 실제로 DOM에 반영되지 않음
//   <> 
//     <header>
//       <h2 className="container">검색</h2>
//     </header>
//     <div className="container">
//       <form>
//         <input type="text" placeholder="검색어를 입력하세요" autoFocus />
//         <button type="reset" className="btn-reset"></button>
//       </form>
//     </div>
//   </>
// );
// ReactDOM.render(element, document.querySelector("#app"));
