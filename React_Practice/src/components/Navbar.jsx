import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => (
  <div className="Navbar">
    <nav>
      <Link to="/">Home</Link>
      <Link to="/board">게시판</Link>
      <Link to="/study">스터디</Link>
      <Link to="/practice">연습</Link>
      <Link to="/login">로그인</Link>
      <Link to="/signup">회원가입</Link>
    </nav>
  </div>
);

export default Navbar;
