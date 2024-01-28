import * as MyLayout from "../lib/MyLayout"
import Backdrop from "./Backdrop";
import Dialog from "./Dialog";

const Page = ({ header, children, footer }) => (
  <div className="Page">
    <header>{header}</header>
    <main>{children}</main>
    <footer>{footer}</footer>
    <MyLayout.DialogContainer />
    {/* <MyLayout.layoutContext.Consumer>
      {({ setDialog }) =>
        <button
          onClick={() => {
            setDialog(<Dialog />)

            setTimeout(() => setDialog(null), 5000)
          }}>다이얼로그 열기</button>}
    </MyLayout.layoutContext.Consumer> */}
  </div>
);

export default Page;
