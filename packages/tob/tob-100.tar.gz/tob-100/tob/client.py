# This file is placed in the Public Domain.


"client"


import queue
import threading
import _thread


from .fleet   import Fleet
from .handler import Handler
from .thread  import launch


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        self.olock = threading.RLock()
        Fleet.add(self)

    def announce(self, txt):
        pass

    def display(self, event):
        with self.olock:
            for tme in sorted(event.result):
                self.dosay(event.channel, event.result[tme])

    def dosay(self, channel, txt):
        self.say(channel, txt)

    def raw(self, txt):
        raise NotImplementedError("raw")

    def say(self, channel, txt):
        self.raw(txt)

    def wait(self):
        pass


class Output(Client):

    def __init__(self):
        Client.__init__(self)
        self.oqueue = queue.Queue()
        self.ostop  = threading.Event()

    def oput(self, event):
        self.oqueue.put(event)

    def output(self):
        while not self.ostop.is_set():
            event = self.oqueue.get()
            if event is None:
                self.oqueue.task_done()
                break
            self.display(event)
            self.oqueue.task_done()

    def raw(self, txt):
        raise NotImplementedError("raw")

    def start(self, daemon=True):
        self.ostop.clear()
        launch(self.output, daemon=daemon)
        super().start()

    def stop(self):
        self.ostop.set()
        self.oqueue.put(None)
        super().stop()

    def wait(self):
        try:
            self.oqueue.join()
        except Exception:
            _thread.interrupt_main()


def __dir__():
    return (
        'Client',
        'Output'
   )
