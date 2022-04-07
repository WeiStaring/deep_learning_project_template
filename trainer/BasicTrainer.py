class BasicTrainer:
    def __init__(self):
        pass

    def get_train_data(self):
        pass

    def before_train(self):
        pass

    def after_train(self):
        pass

    def train(self):
        pass

    def train_end(self):
        pass

    def train_pipeline(self):
        self.before_train()
        self.train()
        self.after_train()
        self.train_end()