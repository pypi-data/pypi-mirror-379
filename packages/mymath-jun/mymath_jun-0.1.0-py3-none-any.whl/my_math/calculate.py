from typing import Union , Final


class MyMath:
    """ 간단한 연산하는 계산기 
    """
    def __init__(
            self, 
            a: Union[int, float], 
            b: Union[int, float] 
        ):
        self.a = a
        self.b = b
         
    
    def add(self) -> Union[int, float]:
        """ 더하기 함수
        """
        return(self.a + self.b)

    def minus(self) -> Union[int, float]:
        """ 빼기 함수
        """
        return (self.a - self.b)

    def multiply(self) -> Union[int, float]:
        """ 곱하기 함수
        """
        return (self.b * self.a)








