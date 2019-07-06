class OutlierDetector:
    number_instances = 0

    def __init__(self, bound_factor_standard_deviation=2, size_current_sample=20, size_initial_ignore=5):
        self.bound_factor_standard_deviation = bound_factor_standard_deviation
        self.size_current_sample = size_current_sample
        self.size_initial_ignore = size_initial_ignore
        self.total_sum = {'total': 0 , 'without_outliers': 0}
        self.sum = {'total': 0 , 'without_outliers': 0}
        self.variance = {'total': 0 , 'without_outliers': 0}
        self.queue = []
        OutlierDetector.number_instances += 1

    def push(self, value, callback=None):
        if callback is not None:
            return callback(self.push(value=value, callback=None))
        else:
            last_mean = {
                'total': self.sum['total'] / max(1, len(self.queue)),
                'without_outliers': self.sum['without_outliers'] / max(1, self.__len_without_outlier(self.queue))}
            last_variance = self.variance
            ############
            is_outlier = False
            if len(self.queue) > self.size_initial_ignore:
                if value > last_mean['without_outliers'] + self.bound_factor_standard_deviation * (last_variance['without_outliers'] ** (1/ 2)) or \
                    value < last_mean['without_outliers'] - self.bound_factor_standard_deviation * (last_variance['without_outliers'] ** (1 / 2)):
                    is_outlier = True
            ############

            if len(self.queue) <= self.size_current_sample or self.size_current_sample <= 0:
                self.queue.append({'v':value, 'outlier':is_outlier})
                self.sum['total'] += value
                if is_outlier is False:
                    self.sum['without_outliers'] += value
            else:
                old_val = self.queue.pop(0)
                self.queue.append({'v':value, 'outlier':is_outlier})
                if is_outlier is False:
                    self.sum['without_outliers'] += value
                elif old_val['outlier'] is False:
                    self.sum['without_outliers'] -= old_val['v']

            mean = {'total': self.sum['total'] / len(self.queue),
                    'without_outliers': self.sum['without_outliers'] / self.__len_without_outlier(self.queue)}
            self.variance['total'] = sum(((xi['v'] - mean['total']) ** 2) for xi in self.queue) / len(self.queue)
            self.variance['without_outliers'] = sum((xi['v'] - mean['without_outliers']) ** 2 for xi in self.queue if xi['outlier'] is False) / self.__len_without_outlier(self.queue)

            return is_outlier

    @staticmethod
    def __len_without_outlier(mlist):
        return len([item for item in mlist if item['outlier'] is False])
