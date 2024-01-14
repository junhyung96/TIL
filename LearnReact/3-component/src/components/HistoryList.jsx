import React from "react";
import List from "./List.jsx";
import store from "../Store.js";
import { formatRelativeDate } from "../helpers.js";

export default class HistoryList extends React.Component {
  constructor() {
    super();

    this.state = {
      historyList: [],
    };
  }

  componentDidMount() {
    this.fetch();
  }

  fetch() {
    const historyList = store.getHistoryList();
    this.setState({ historyList });
  }

  handleClickRemove(keyword) {
    store.removeHistory(keyword);
    this.fetch();
  }

  render() {
    const { onClick } = this.props
    const { historyList } = this.state
    return (
      <List
        data={historyList}
        onClick={onClick}
        hasDate
        onRemove={(keyword) => this.handleClickRemove(keyword)}
      />
    );
  }
}

// export default class HistoryList extends List {
//   componentDidMount() {
//     this.fetch()
//   }

//   fetch() {
//     const data = store.getHistoryList();
//     this.setState({ data });
//   }

//   handleClickRemoveHistory(event, keyword) {
//     event.stopPropagation()
//     store.removeHistory(keyword)
//     this.fetch()
//   }

//   renderItem(item, index) {
//     return (
//       <>
//         <span>{item.keyword}</span>
//         <span className="date">{formatRelativeDate(item.date)}</span>
//         <button
//           className="btn-remove"
//           onClick={(event) =>
//             this.handleClickRemoveHistory(event, item.keyword)
//           }
//         ></button>
//       </>
//     );
//   }
// }
