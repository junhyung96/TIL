import React from "react";
import * as MyRouter from "./lib/MyRouter";
import * as MyLayout from "./lib/MyLayout";
import CartPage from "./pages/CartPage";
import OrderPage from "./pages/OrderPage";
import ProductPage from "./pages/ProductPage";
import { getComponentName } from "./lib/utils";
import Dialog from "./components/Dialog";
import Backdrop from "./components/Backdrop";

const App = () => (
  <MyLayout.Layout>
    <MyRouter.Router>
      <MyRouter.Routes>
        <MyRouter.Route path="/cart" element={<CartPage />} />
        <MyRouter.Route path="/order" element={<OrderPage />} />
        <MyRouter.Route path="/" element={<ProductPage />} />
      </MyRouter.Routes>
      <Backdrop>
        <Dialog />
      </Backdrop>
    </MyRouter.Router>
  </MyLayout.Layout>
);

export default App;

// class Header extends React.Component {
//   render() {
//     return <header>Header</header>;
//   }
// }

// class Button extends React.Component {
//   handleClick = () => {
//     this.props.log("클릭");
//   };
//   render() {
//     return <button onClick={this.handleClick}>버튼</button>;
//   }
// }

// // 고차 컴포넌트 관례 with 접두어 사용
// const withLogging = (WrappedComponent) => {
//   function log(message) {
//     console.log(`[${getComponentName(WrappedComponent)}] ${message}`);
//   }

//   class WithLogging extends React.Component {
//     render() {
//       const enhancedProps = {
//         log,
//       };
//       return <WrappedComponent {...this.props} {...enhancedProps} />;
//     }
//     componentDidMount() {
//       log("마운트");
//     }
//   }

//   return WithLogging;
// };

// const EnhancedHeader = withLogging(Header);
// const EnhancedButton = withLogging(Button);

// export default () => (
//   <>
//     <EnhancedHeader />
//     <EnhancedButton />
//   </>
// );
