class OutlierDetector:
    number_instances = 0

    def __init__(self, target_standard_deviation=2, size_current_sample=20, size_initial_ignore=10):
        self.target_standard_deviation = target_standard_deviation
        self.size_current_sample = size_current_sample
        self.size_initial_ignore = size_initial_ignore
        self.total_mean = 0
        self.queue = []
        OutlierDetector.number_instances += 1



    def push(self, value, callback=None):
        if callback is not None:
            callback(self.push(value=value, callback=None))
        else:
            pass
