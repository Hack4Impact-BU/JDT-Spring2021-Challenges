console.log("Hello World");

let count = 0;

const countHeader = document.getElementById('counter')

countHeader.innerHTML = 'Counter: ' + count

const addOne = () =>
{
    count = count + 1;

    countHeader.innerHTML = 'Counter: ' + count;
}
const minusOne = () =>
{
    count = count - 1;

    countHeader.innerHTML = 'Counter: ' + count;
}
const reset = () =>
{
    count = 0;

    countHeader.innerHTML = 'Counter: ' + count;
}