
#type hints:类型提示
class Calc:
    def add(self,a,b):
        return a + b;

    def div(self,a,b):
        return a / b;


calc = Calc()
print(calc.add(-4.4, 0.4343))