import Header from './Header';
import Counter from './Counter';

function App() {
  return (
    <div className='app'>
      <Header />
      <Counter count={0} />
    </div>
  );
}

export default App;
