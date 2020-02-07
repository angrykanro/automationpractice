import React from 'react';
import Iframe from 'react-iframe'
import './App.css';
import { RingLoader } from "react-spinners";

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      loading: false
    };
  }

  runTests = () => {
    this.setState({
      loading: true
    });
    fetch(`/tests/run`)
      .then(
        (result) => {
          this.setState({
            loading: false,
          });
        },
        (error) => {
          this.setState({
            isLoaded: false,
            error
          });
        }
      )
  }

  getLoaderMask = () => {
    return (
      <div className={"loader-mask"}>
          <RingLoader
            size={150}
            color={"black"}
            loading={this.state.loading}/>
        </div>
    );
  }

  render() {
    return (
      <div className="App">
        <header>
          <div className="actions-wrapper">
            <button onClick={this.runTests} className="btn-run-test">Run tests</button>
          </div>
        </header> 
        <Iframe url="http://localhost:4040"
          width="100%"
          height="100%"
          id="myId"
          className="allure-container"
          display="initial"
          position="relative"
          allowFullScreen/>
           { this.state.loading ? this.getLoaderMask() : null }
      </div>
    );
  }
}

export default App;