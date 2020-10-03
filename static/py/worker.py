from browser import bind, self
import time

class Test():
    def __init__(self):
        self.x = 11
    
    def sleep(self):
        end_time = time.time() + 5
        while time.time() < end_time:
            pass

# Listens for messages from the main thread
@bind(self, "message")
def thread_fn(obj):
    t = Test()
    env = {"t": t}
    exec(obj.data["code"], env)
    fn = env["fn"]
    fn()
    self.send("hi")
