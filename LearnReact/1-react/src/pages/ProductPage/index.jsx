import Navbar from "../../components/Navbar";
import Page from "../../components/Page";
import ProductItem from "../../components/ProductItem";
import Title from "../../components/Title";
import React from "react";
import ProductApi from "shared/api/ProductApi";

class ProductPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      productList: [],
    };
  }

  async fetch() {
    try {
      const productList = await ProductApi.fetchProductList();
      this.setState({ productList });
    } catch (error) {
      console.error(error);
    }
  }

  componentDidMount() {
    this.fetch();
  }

  render() {
    return (
      <div className="ProductPage">
        <Page header={<Title>메뉴 목록</Title>} footer={<Navbar />}>
          <ul>
            {this.state.productList.map((product) => (
              <li key={product.id}>
                <ProductItem product={product} />
              </li>
            ))}
          </ul>
        </Page>
      </div>
    );
  }
}

export default ProductPage;
