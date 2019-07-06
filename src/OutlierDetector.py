class OutlierDetector:
    number_instances = 0

    def __init__(self, bound_factor_standard_deviation=2, size_current_sample=20, size_initial_ignore=10):
        self.target_standard_deviation = bound_factor_standard_deviation
        self.size_current_sample = size_current_sample
        self.size_initial_ignore = size_initial_ignore
        self.total_sum = 0
        self.sum = 0
        self.variance = 0
        self.queue = []
        OutlierDetector.number_instances += 1

    def push(self, value, callback=None):
        if callback is not None:
            return callback(self.push(value=value, callback=None))
        else:
            last_mean = self.sum / max(1, len(self.queue))
            last_variance = self.variance

            if len(self.queue) <= self.size_current_sample or self.size_current_sample <= 0:
                self.queue.append(value)
                self.sum += value
            else:
                old_val = self.queue.pop(0)
                self.queue.append(value)
                self.sum += value - old_val

            mean = self.sum / len(self.queue)
            self.variance = sum((xi - mean) ** 2 for xi in self.queue) / len(self.queue)

            print("mean:", mean, "variance:", self.variance)

            return True
