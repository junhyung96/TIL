import React from 'react'
import Page from "../../components/Page";
import Footer from "../../components/Footer";
import { Link } from "react-router-dom";
import MainPage from "../MainPage";
import SignUpPage from "../SingUpPage";
import Button from "../../components/Button"

class LoginPage extends React.Component {
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
        <div className="Login">
          <h2>Login</h2>
          <form action="">
            <input type="text" id="id" placeholder="id" />
            <input type="password" id="pw" placeholder="password" />
            <label>
              <input type="checkbox" />
              아이디 저장하기
            </label>
            {/* <input type="submit" value="Login" /> */}
            <Button>Login</Button>
          </form>
        </div>
        <Link to="/findpw" element={<SignUpPage />}>
          아이디/비밀번호 찾기
        </Link>
        <Link to="/signup" element={<SignUpPage />}>
          회원가입
        </Link>
        <div className="SocialLogin">
            <div className="KakaoLogin">카카오 로그인</div>
            <div className="GoogleLogin">구글 로그인</div>
        </div>
      </Page>
    );
  }
}

export default LoginPage;