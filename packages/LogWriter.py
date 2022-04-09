from multiprocessing import Process

class LogWriter(Process):
    def __init__(self, file_path, save_path, message_queue):
        self.name = "logging process"
        Process.__init__(self, name=self.name)
        self.file_path = file_path
        self.save_path = save_path
        self.file = None
        self.message_queue = message_queue

    def run(self) -> None:
        self.file = open(self.file_path, "a")
        self.file.truncate(0)
        while True:
            message = self.message_queue.get()
            if message == "end":
                break
            self.file.write(message + "\n")

        self.file.close()