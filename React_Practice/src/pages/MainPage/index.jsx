import React from "react";
import Navbar from "../../components/Navbar";
import Page from "../../components/Page";
import Footer from "../../components/Footer";
import { Link } from "react-router-dom";
import PracticePage from "../PracticePage";
import StudyPage from "../StudyPage";
import API from '../../services/Api';
import axios from 'axios'

export const login = async (code) => {
    const { data } = await API.post('url',
          JSON.stringify(code)
    );
    return data;
}

// export const getDeposit = function () {
//   axios({
//     method: "get",
//     url: "http://127.0.0.1:8000/finance/deposits",
//   })
//     .then((response) => {
//       this.setState({
//         depositProducts: response.data
//       })
//     })
//     .catch((error) => {
//       console.log(error);
//     });
// };

class MainPage extends React.Component {
  constructor() {
    super();
    this.state = {
      depositProducts: '',
    };
  }

  // componentDidMount() {
  //   getDeposit();
  // }


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
          <div className="Main5">
            {this.state.depositProducts}
          </div>
        </Page>
      </div>
    );
  }
}



export default MainPage;
