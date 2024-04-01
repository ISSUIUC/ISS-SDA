# NOGO -- helper library for determining conditions for a launch go/no go
# ISS-SDA 2024
from typing import List
    
class LaunchConditions:

    class Condition:
        # A condition to be satisfied when a launch can be a "GO".

        def __init__(self, name, min, max) -> None:
            self.y_min__ = min
            self.y_max__ = max
            self.m_last__ = False

        def set_condition(self, min, max) -> None:
            self.y_min__ = min
            self.y_max__ = max

        def met(self, v) -> bool:
            # Returns whether the condition is met for the given x value (usually hour)
            self.m_last__ = v >= self.y_min__ and v <= self.y_max__
            return self.m_last__

    def __init__(self) -> None:
        self.conds__: List[LaunchConditions.Condition] = []

    def add_cond(self, condition_name, min, max) -> None:
        self.conds__.append(LaunchConditions.Condition(condition_name, min, max))

    def go_nogo(self):
        go = True
        for condition in self.conds__:
            go = go and condition.m_last__
        return go

    