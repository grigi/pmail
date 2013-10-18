import asyncore
from smtpd import SMTPServer
import threading

class EmailServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        print("Email %d:\n%s" % (self.no, data))
        self.no += 1

class smtpd:
    def __init__(self):
        self.start()

    def start(self):
        self.svr = EmailServer(('localhost', 1025), None)
        self.t = threading.Thread(target=asyncore.loop, kwargs = {'timeout':1})
        self.t.start()

    def stop(self):
        self.svr.close()
        self.t.join()

