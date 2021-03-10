import React from 'react';

class Counter extends React.Component
{
    constructor(props)
    {
        super(props);
        this.addOne = this.addOne.bind(this);
        this.minusOne = this.minusOne.bind(this);
        this.resetCounter = this.resetCounter.bind(this);
        this.state = {
            count: props.count
        };
    }
    addOne = () =>
    {
        this.setState((prevState) =>
        {
            return{
                count: prevState.count + 1
            };
        });
    }
    minusOne = () =>
    {
        this.setState((prevState) =>
        {
            return{
                count: prevState.count - 1,
            };
        });
    }
    resetCounter = () =>
    {
        this.setState(() =>
        {
            return{
                count: 0
            };
        });
    }
    render()
    {
        return(
            <div>
                <h1>Count: {this.state.count}</h1>
                <button class='button' onClick={this.addOne}>+1</button>
                <button class='button' onClick={this.minusOne}>-1</button>
                <button class='button' onClick={this.resetCounter}>Reset</button>
            </div>
        );
    }
}
  
export default Counter;
  