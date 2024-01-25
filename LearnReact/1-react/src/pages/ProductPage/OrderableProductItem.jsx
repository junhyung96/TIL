import ProductItem from "../../components/ProductItem";
import * as MyRouter from "../../lib/MyRouter";

const OrderableProductItem = ({ product, navigate }) => (
  <MyRouter.routerContext.Consumer>
    {({ changePath }) => {
      const handleClick = () => {
        changePath(`/cart?productId=${product.id}`);
      };
      return <ProductItem product={product} onClick={handleClick} />;
    }}
  </MyRouter.routerContext.Consumer>
);

export default MyRouter.withRouter(OrderableProductItem);
