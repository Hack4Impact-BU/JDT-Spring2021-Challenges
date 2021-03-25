import TodoList from './TodoList';

function App() {
  return (
    <div className="App">
      <h1>To-do List</h1>
      <TodoList list = {["apple ", "banana ", "milk", "pizza"]}/>
    </div>
  );
}

export default App;
