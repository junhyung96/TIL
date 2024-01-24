import React from "react";
import Page from "../../components/Page";
import Footer from "../../components/Footer";
import { Link } from "react-router-dom";
import MainPage from "../MainPage";
import Button from "../../components/Button";

class SignUpPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <Page footer={<Footer />}>
        <Link to="/" element={<MainPage />}>
          PLOUD
        </Link>
        <div className="box">
          <h2>Sign Up</h2>
          <form>
            <div className="signup-input">
              <input type="text" placeholder="id" />
              <Button>중복확인</Button>
            </div>
            <div className="signup-input">
              <input type="email" placeholder="email" />
              <Button>이메일 확인</Button>
            </div>
            <div className="signup-input">
              <input type="text" placeholder="nickname" />
              <Button>중복 확인</Button>
            </div>
            <div className="signup-input">
              <input type="password" placeholder="password" />
            </div>
            <div className="signup-input">
              <input type="password" placeholder="password check" />
            </div>
            <Button>Sign Up</Button>
          </form>
        </div>
      </Page>
    );
  }
}

export default SignUpPage;
