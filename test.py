from js import Element
from js import document
from pyodide import create_proxy
def my_function(*args,**kwargs):
    output= document.getElementById('word-input').value
    document.getElementById('display-metrix').innerText = f"Input is {output}"
book_flight = create_proxy(my_function)
document.getElementById("submit").addEventListener("click", book_flight)