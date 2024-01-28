const App = () => <>2-hook</>;

export default App;

class Contract {
  constructor(name) {
    this.name = name;
  }

  sign() {
    const capturedName = this.name
    setTimeout(() => console.log("서명인: ", capturedName), 3000);
  }
}

// const contract = new Contract("사용자 1")
// contract.sign()

function createContract(name) {
    const sign = () => {
        setTimeout(() => console.log("서명인: ", name), 3000);
    }

    return {
        sign
    }
}
const contract = createContract("사용자3")
contract.sign();