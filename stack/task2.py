from stack import Stack
from flask import Flask, render_template


seq = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{}",
    "{{[(])]}}",
    "[[{())}]"
    ]
pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
    }

def is_balance(seq):
    stack = Stack()
    for el in seq:
        if stack.is_empty() or el in ("[{("):
            stack.push(el)
            continue
        if pairs[el] == stack.peek():
            stack.pop()
        else:
            break
    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


app = Flask(__name__)

@app.route("/<inp>/<out>")
def index(inp, out):
    return render_template(
            'index.html',
            input=inp,
            output=out)

@app.route("/")
def start():
    return render_template("start.html")

if __name__ == "__main__":
    app.run()

