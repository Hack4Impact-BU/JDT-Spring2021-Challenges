console.log("Hello World");

let count = 0;

const me = {name:"Jason", year:"Junior", major:"Computer Science"};

document.getElementById('name').innerHTML = me.name;

document.getElementById('year').innerHTML = me.year;

document.getElementById('major').innerHTML = me.major;

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