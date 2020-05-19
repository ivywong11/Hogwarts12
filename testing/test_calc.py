import sys

from python.calc import Calc

sys.path.append('..')
class TestCalc:
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1,2)
        assert result == 3