from Summarize import SummarizeOnGroups
from math import sqrt


class Variance(SummarizeOnGroups):
    """
        Calculates the maximum of a column (of a DataFrame).

        ...

        Attributes
        ----------
        __get_var : bool
            boolean indicating if variance is calculated or not
        __get_sd : bool
            boolean indicating if standard deviation is calculated or not

        Methods
        -------
        _operation(col) : dict
            Calculates the variance and/or standard deviation on the col object,
            assuming this DataFrame represents a single group.
            The output variable is called "Variable_Var" if the variance is calculated and
            called "Variable_SD" for the standard deviation (if col = Variable).
    """
    def __init__(self, *on_vars, delete_na=True, delete_nan=True, get_var=True, get_sd=True):
        super().__init__(*on_vars, delete_na=delete_na, delete_nan=delete_nan)
        self.__get_var = get_var
        self.__get_sd = get_sd

    def _operation(self, col):
        n = len(col)
        partial_average = None
        partial_average_squared = None
        for val in col:
            if partial_average is None and partial_average_squared is None:
                partial_average = val / n
                partial_average_squared = val**2 / n
            else:
                partial_average += val / n
                partial_average_squared += val**2 / n
        var = (partial_average_squared - partial_average**2)
        sd = sqrt(var)
        res = dict()
        if self.__get_var:
            res["Var"] = var
        if self.__get_sd:
            res["SD"] = sd
        return res
