import React from 'react';

class TodoList extends React.Component
{
    constructor(props)
    {
        super(props);
        
        this.state = {
            error: undefined,
            list: props.list
        };
    }
    handleAddItem = (e) =>
    {
        e.preventDefault();

        console.log(`${e.target.item.value} has been added`);
        const option = e.target.item.value.trim();
        const error = this.addItem(option);

        this.setState(() => ({error: error}))

        if (!error)
        {
            e.target.item.value = ''
        }
    }
    addItem = (option) =>
    {
        this.setState((prevState) => ({
            list: prevState.list.concat(option)
        }))
        
        // console.log(`${option} has been added`);
    }
    render()
    {
        return(
            <div>
                <h3>Current list: 
                    <ul>
                        {this.state.list.map((item, index) => <li key={index}>{item}</li>)}
                    </ul>
                </h3>

                <form onSubmit={this.handleAddItem}>
                    <input type='text' name='item' />
                    <button>Add</button>
                </form>
            </div>
        );
    }
}

export default TodoList;