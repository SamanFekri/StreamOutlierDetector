class OutlierDetector:

    def __init__(self, target_standard_deviation=2, size_current_sample=20, size_initial_ignore=10):
        self.target_standard_deviation = target_standard_deviation
        self.size_current_sample = size_current_sample
        self.size_initial_ignore = size_initial_ignore
        self.total_mean = 0



    def push(self, value):
        pass


    def push_async(self, value, result_callback):
        pass