class OutlierDetector:
    number_instances = 0
    TOTAL = 't'
    WITHOUT_OUTLIERS = 'wo'
    VALUE = 'v'
    IS_OUTLIER = 'io'

    def __init__(self, bound_factor_standard_deviation=3, window_size=20, first_learning_number=10):
        self.bound_factor_standard_deviation = bound_factor_standard_deviation
        self.size_current_sample = window_size
        self.first_learning_number = first_learning_number
        self.total_sum = {OutlierDetector.TOTAL: 0 , OutlierDetector.WITHOUT_OUTLIERS: 0}
        self.sum = {OutlierDetector.TOTAL: 0 , OutlierDetector.WITHOUT_OUTLIERS: 0}
        self.variance = {OutlierDetector.TOTAL: 0 , OutlierDetector.WITHOUT_OUTLIERS: 0}
        self.queue = []
        OutlierDetector.number_instances += 1

    def push(self, value, callback=None):
        if callback is not None:
            callback(self.push(value=value, callback=None))
            return None
        else:
            last_mean = {
                OutlierDetector.TOTAL: self.sum[OutlierDetector.TOTAL] / max(1, len(self.queue)),
                OutlierDetector.WITHOUT_OUTLIERS: self.sum[OutlierDetector.WITHOUT_OUTLIERS] / max(1, self.__len_without_outlier(self.queue))}
            last_variance = self.variance
            ############
            is_outlier = False
            if len(self.queue) > self.first_learning_number:
                if self.__detect_outlier(value, last_mean[OutlierDetector.WITHOUT_OUTLIERS],
                                         last_variance[OutlierDetector.WITHOUT_OUTLIERS], self.bound_factor_standard_deviation):
                    is_outlier = True
                    # try to correct if majority is outlier
                    if 2 * self.__len_without_outlier(self.queue) < len(self.queue):
                        # assume outliers are normals and normals are outliers
                        for item in self.queue:
                            item[OutlierDetector.IS_OUTLIER] = not item[OutlierDetector.IS_OUTLIER]
                        self.sum[OutlierDetector.WITHOUT_OUTLIERS] = sum(xi[OutlierDetector.VALUE] for xi in self.queue if xi[OutlierDetector.IS_OUTLIER] is False)
                        last_mean[OutlierDetector.WITHOUT_OUTLIERS] = self.sum[OutlierDetector.WITHOUT_OUTLIERS] / max(1, self.__len_without_outlier(self.queue))
                        last_variance[OutlierDetector.WITHOUT_OUTLIERS] = sum((xi[OutlierDetector.VALUE] - last_mean[OutlierDetector.WITHOUT_OUTLIERS]) ** 2 for xi in self.queue if xi[OutlierDetector.IS_OUTLIER] is False) / self.__len_without_outlier(self.queue)

                        # calculate new outliers
                        for item in self.queue:
                            if self.__detect_outlier(item[OutlierDetector.VALUE], last_mean[OutlierDetector.WITHOUT_OUTLIERS],
                                         last_variance[OutlierDetector.WITHOUT_OUTLIERS], self.bound_factor_standard_deviation):
                                item[OutlierDetector.IS_OUTLIER] = True
                        # correct class values
                        self.sum[OutlierDetector.WITHOUT_OUTLIERS] = sum(xi[OutlierDetector.VALUE] for xi in self.queue if xi[OutlierDetector.IS_OUTLIER] is False)
                        last_mean[OutlierDetector.WITHOUT_OUTLIERS] = self.sum[OutlierDetector.WITHOUT_OUTLIERS] / max(1, self.__len_without_outlier(self.queue))
                        last_variance[OutlierDetector.WITHOUT_OUTLIERS] = sum((xi[OutlierDetector.VALUE] - last_mean[OutlierDetector.WITHOUT_OUTLIERS]) ** 2 for xi in self.queue if xi[OutlierDetector.IS_OUTLIER] is False) / self.__len_without_outlier(self.queue)

                        # is current item still outlier or not?
                        if self.__detect_outlier(value, last_mean[OutlierDetector.WITHOUT_OUTLIERS],
                                         last_variance[OutlierDetector.WITHOUT_OUTLIERS], self.bound_factor_standard_deviation):
                            is_outlier = True
                        else:
                            is_outlier = False
            ############

            if len(self.queue) < self.size_current_sample or self.size_current_sample <= 0:
                self.queue.append({OutlierDetector.VALUE:value, OutlierDetector.IS_OUTLIER:is_outlier})
                self.sum[OutlierDetector.TOTAL] += value
                if is_outlier is False:
                    self.sum[OutlierDetector.WITHOUT_OUTLIERS] += value
            else:
                old_val = self.queue.pop(0)
                self.sum[OutlierDetector.TOTAL] += value - old_val[OutlierDetector.VALUE]
                self.queue.append({OutlierDetector.VALUE:value, OutlierDetector.IS_OUTLIER:is_outlier})
                if is_outlier is False:
                    self.sum[OutlierDetector.WITHOUT_OUTLIERS] += value
                if old_val[OutlierDetector.IS_OUTLIER] is False:
                    self.sum[OutlierDetector.WITHOUT_OUTLIERS] -= old_val[OutlierDetector.VALUE]

            mean = {OutlierDetector.TOTAL: self.sum[OutlierDetector.TOTAL] / len(self.queue),
                    OutlierDetector.WITHOUT_OUTLIERS: self.sum[OutlierDetector.WITHOUT_OUTLIERS] / self.__len_without_outlier(self.queue)}

            self.variance[OutlierDetector.TOTAL] = sum(((xi[OutlierDetector.VALUE] - mean[OutlierDetector.TOTAL]) ** 2) for xi in self.queue) / len(self.queue)
            self.variance[OutlierDetector.WITHOUT_OUTLIERS] = sum((xi[OutlierDetector.VALUE] - mean[OutlierDetector.WITHOUT_OUTLIERS]) ** 2 for xi in self.queue if xi[OutlierDetector.IS_OUTLIER] is False) / self.__len_without_outlier(self.queue)

            return is_outlier

    @staticmethod
    def __len_without_outlier(mlist):
        return len([item for item in mlist if item[OutlierDetector.IS_OUTLIER] is False])

    @staticmethod
    def __detect_outlier(value, mean, variance, factor):
        return value > mean + factor * (variance ** (1 / 2)) or value < mean - factor * (variance ** (1 / 2))

