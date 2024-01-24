import React from "react";
import Header from "./components/Header.jsx";
import SearchForm from "./components/SearchForm.jsx";
import SearchResult from "./components/SearchResult.jsx";
import store from "./Store.js";
import Tabs, { TabType } from "./components/Tabs.jsx";
import KeywordList from "./components/KeywordList.jsx";
import HistoryList from "./components/HistoryList.jsx";

export default class App extends React.Component {
  constructor() {
    super();

    this.state = {
      searchKeyword: "",
      searchResult: [],
      submitted: false,
      selectedTab: TabType.KEYWORD,
    };
  }

  handleChangeInput(searchKeyword) {
    if (searchKeyword.length <= 0) {
      this.handleReset();
    }
    this.setState({ searchKeyword });
  }

  search(searchKeyword) {
    // store 에서 가져와야함
    const searchResult = store.search(searchKeyword);

    this.setState({
      searchKeyword,
      searchResult,
      submitted: true,
    });
  }

  handleReset() {
    this.setState({ searchKeyword: "", submitted: false, searchResult: [] });
    console.log("TODO: handleReset");
  }

  render() {
    const { searchKeyword, searchResult, submitted, selectedTab } = this.state;

    return (
      <>
        <Header title="검색" />
        
        <div className="container">
          <SearchForm
            value={searchKeyword}
            onChange={(value) => this.handleChangeInput(value)}
            onSubmit={() => this.search(searchKeyword)}
            onReset={() => this.handleReset()}
          />
          <div className="content">
            {submitted ? (
              <SearchResult data={searchResult} />
            ) : (
              <>
                <Tabs
                  selectedTab={selectedTab}
                  onChange={(selectedTab) => this.setState({ selectedTab })}
                />
                {selectedTab === TabType.KEYWORD && <KeywordList onClick={keyword => this.search(keyword)} />}
                {selectedTab === TabType.HISTORY && <HistoryList onClick={keyword => this.search(keyword)}/>}
              </>
            )}
          </div>
        </div>
      </>
    );
  }
}
