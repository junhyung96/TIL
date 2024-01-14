import React from "react";
import List from "./List.jsx";
import store from "../Store.js";

export default class KeywordList extends React.Component {
  constructor() {
    super();

    this.state = {
      keywordList: [],
    };
  }

  componentDidMount() {
    const keywordList = store.getKeywordList();
    this.setState({ keywordList });
  }

  render() {
    const { onClick } = this.props;
    const { keywordList } = this.state

    return (
      <List
        data={keywordList}
        onClick={onClick}
        hasIndex // 불리언 값을 넘길때는 속성명만 적어도 된다 true로 반환
      />
    );
  }
}
