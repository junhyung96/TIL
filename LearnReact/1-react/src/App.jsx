import Navbar from "./components/Navbar";
import ProductItem from "./components/ProductItem";
import Title from "./components/Title";

const fakeProduct = {
  id: "CACDA421",
  name: "해물 계란 라면",
  price: 6000,
  thumbnail: "./images/menu-해물계란라면.jpg",
};

// {id: 'CACDA422', name: '햄 야채 토스트', price: 8000, thumbnail: './images/menu-햄야채토스트.jpg'}

// {id: 'CACDA423', name: '프레시 케밥', price: 8000, thumbnail: './images/menu-프레시케밥.jpg'}

// {id: 'CACDA424', name: '부드러운 치즈 버거', price: 15000, thumbnail: './images/menu-부드러운치즈버거.jpg'}

// {id: 'CACDA425', name: '매운 푸팟퐁 커리', price: 20000, thumbnail: './images/menu-매운푸팟퐁커리.jpg'}

const App = () => (
  <div className="ProductPage">
    <div className="Page">
      <header>
        <Title>메뉴 목록</Title>
      </header>
      <main>
        <ul>
          <li>
            <ProductItem product={fakeProduct} />
          </li>
        </ul>
      </main>
      <footer>
        <Navbar />
      </footer>
    </div>
  </div>
);

export default App;
