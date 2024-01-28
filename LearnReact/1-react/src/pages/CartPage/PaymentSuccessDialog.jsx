import * as MyRouter from "../../lib/MyRouter"
import * as MyLayout from "../../lib/MyLayout"
import Button from "../../components/Button";
import Dialog from "../../components/Dialog";

// 예 버튼을 클릭하면 주문상태 페이지로
// 아니오 버튼을 클릭하면 메뉴 목록 페이지로
const PaymentSuccessDialog = ({navigate, closeDialog}) => {
  const handleClickNo = () => {
    closeDialog()
    navigate('/')
  };
  const handleClickYes = () => {
    closeDialog()
    navigate('/order')
  };
  return (
    <Dialog
      header={<>결제 완료</>}
      footer={
        <>
          <Button style={{ marginRight: "8px" }} onClick={handleClickNo}>
            아니오
          </Button>
          <Button styleType={"brand"} onClick={handleClickYes}>
            예, 주문상태를 확인합니다.
          </Button>
        </>
      }
    >
      결제가 완료되었습니다. 주문 상태를 보러 가시겠습니까?
    </Dialog>
  );
};

// 주소 이동을 위해 navigate 써야함
export default MyLayout.withLayout(MyRouter.withRouter(PaymentSuccessDialog))