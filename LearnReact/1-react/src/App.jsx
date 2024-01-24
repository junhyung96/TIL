import * as MyRouter from "./lib/MyRouter";
import CartPage from "./pages/CartPage";
import ProductPage from "./pages/ProductPage";
import OrderPage from "./pages/OrderPage";

// 컨택스트를 쓰려면 Provider로 감싸야 한다 Why?????
// Router 는 routerContext.Provider 를 반환한다
const App = () => (
  <MyRouter.Router>
    <MyRouter.Routes>
      <MyRouter.Route path="/cart" element={<CartPage />} />
      <MyRouter.Route path="/order" element={<OrderPage />} />
      <MyRouter.Route path="/" element={<ProductPage />} />
    </MyRouter.Routes>
  </MyRouter.Router>
);

export default App;

// import MyReact from "./lib/MyReact";

// const countContext = MyReact.createContext({
//   count: 0,
//   setCount: () => {},
// });

// class CountProvider extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       count: 0,
//     };
//   }
//   render() {
//     const value = {
//       count: this.state.count,
//       setCount: (nextValue) => this.setState({ count: nextValue }),
//     };
//     return (
//       <countContext.Provider value={value}>
//         {this.props.children}
//       </countContext.Provider>
//     );
//   }
// }

// const Count = () => {
//   return (
//     <countContext.Consumer>
//       {(value) => <div>{value.count}</div>}
//     </countContext.Consumer>
//   );
// };

// const PlusButton = () => {
//   return (
//     <countContext.Consumer>
//       {(value) => (
//         <button onClick={() => value.setCount(value.count + 1)}>
//           + 카운트 올리기
//         </button>
//       )}
//     </countContext.Consumer>
//   );
// };

// export default () => (
//   <CountProvider>
//     <Count />
//     <PlusButton />
//   </CountProvider>
// );

// const eventEmitter = createEventEmitter(0)
// const logger = value => console.log(value)

// eventEmitter.on(logger)
// console.log(eventEmitter.get())
// eventEmitter.set(1)
// eventEmitter.set(2)

// setTimeout(() => eventEmitter.set(10), 3000)
