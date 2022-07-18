from re import search


class Helpers:

    @staticmethod
    def parse_weight(weight_string):
        return float(search('[0-9.]+', weight_string).group())
