import React from "react";
import Navbar from "../../components/Navbar";
import Page from "../../components/Page";
import Footer from "../../components/Footer";
import { Link } from "react-router-dom";
import PracticePage from "../PracticePage";
import StudyPage from "../StudyPage";

const Tag = "Main";

class MainPage extends React.Component {
  constructor() {
    super();
    this.state = {};
    console.log(Tag);
  }

  render() {
    return (
      <div className="MainPage">
        <Page header={<Navbar />} footer={<Footer />}>
          <div className="Main1">
            <img src="images/Main1.png" alt="Main1.png" />
          </div>
          <div className="Main2">
            <video src="videos/cat.mp4" autoPlay loop />
            <div className="card">오늘의 발표 수</div>
          </div>
          <div className="Main3">
            <h2>스피치 실력을 키워볼까요?</h2>
            <div className="card">
              <Link to="/practice" element={<PracticePage />}>
                혼자연습
              </Link>
            </div>
            <div className="card">
              <Link to="/study" element={<StudyPage />}>
                함께연습
              </Link>
            </div>
          </div>
          <div className="Main4">
            <img src="images/Main2.png" alt="" />
          </div>
        </Page>
      </div>
    );
  }
}

export default MainPage;
