import CartPage from "./pages/CartPage";
import OrderPage from "./pages/OrderPage";
import ProductPage from "./pages/ProductPage";

const App = () => (
  <>
    {/* <ProductPage /> */}
    {/* <OrderPage /> */}
    <CartPage />
  </>
);

// export default App;

import MyReact from "shared/lib/MyReact";
import React from "react";

const countContext = MyReact.createContext({
  count: 0,
  setCount: () => {},
});

class CountProvider extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
    };
  }
  render() {
    const value = {
      count: this.state.count,
      setCount: (nextValue) => this.setState({ count: nextValue }),
    };
    return (
      <countContext.Provider value={value}>
        {this.props.children}
      </countContext.Provider>
    );
  }
}

const Count = () => {
  return (
    <countContext.Consumer>
      {(value) => <div>{value.count}</div>}
    </countContext.Consumer>
  );
};

const PlusButton = () => {
  return (
    <countContext.Consumer>
      {(value) => (
        <button onClick={() => value.setCount(value.count + 1)}>
          + 카운트 올리기
        </button>
      )}
    </countContext.Consumer>
  );
};

export default () => (
  <CountProvider>
    <Count />
    <PlusButton />
  </CountProvider>
);

// const eventEmitter = createEventEmitter(0)
// const logger = value => console.log(value)

// eventEmitter.on(logger)
// console.log(eventEmitter.get())
// eventEmitter.set(1)
// eventEmitter.set(2)

// setTimeout(() => eventEmitter.set(10), 3000)
