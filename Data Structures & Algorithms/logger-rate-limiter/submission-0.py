class Logger:

    def __init__(self):
        self.limiter = defaultdict(list)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.limiter and timestamp - self.limiter[message][-1] < 10:
            return False
        self.limiter[message].append(timestamp)
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
