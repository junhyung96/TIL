function Contract(props) {
    const sign = () => {
      setTimeout(() => console.log("서명인: ", props.name), 3000);
    };
    return <button onClick={sign}>서명</button>;
  }
  
  class App extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        name: "사용자1",
      };
    }
  
    handleChange(e) {
      this.setState({ name: e.target.value });
    }
  
    render() {
      return (
        <>
          <select value={this.state.name} onChange={this.handleChange.bind(this)}>
            <option value="사용자1">사용자1</option>
            <option value="사용자2">사용자2</option>
          </select>
          <Contract name={this.state.name} />
        </>
      );
    }
  }
  
  export default App;