import React, { Component } from "react";

class Header extends Component {
  state = {
    keywords: "",
  };

  inputChange = (event) => {
    this.setState({
      title: "The keyword are:",
      keywords: event.target.value,
    });
  };

  render() {
    return (
      <>
        <div>
          <div
            className="logo"
            onClick={() => {
              console.log("I was clicked");
            }}
          >
            Logo
          </div>
          <input onChange={(e) => this.inputChange(e)} />
          <br />
          <div>{this.state.title}</div>
          <div>{this.state.keywords}</div>
        </div>
      </>
    );
  }
}
