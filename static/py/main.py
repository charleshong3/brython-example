from browser import bind, document, alert, worker

w = worker.Worker("simulator")

# Listener for the button
def test(ev):
    w.send({"code": document['zone'].value})
    print("Should print first")

document["mybutton"].bind("click", test)

# Listens for messages from the worker
@bind(w, "message")
def onmessage(obj):
    print("Main thread received:", obj.data)
