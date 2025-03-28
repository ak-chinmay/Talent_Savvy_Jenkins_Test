class Calculator:
    def add(self, a, b):
        """
        Method adds the two numbers and returns the sum

        :param a: 1st number
        :param b: 2nd number
        :return: sum of the two numbers
        """
        if not a or not b:
            print("a or b value is invalid")
            return None
        return a + b


    def subtract(self, a, b):
        """
        This method substracts b from b and returns difference

        :param a:
        :param b:
        :return:
        """
        if not a or not b:
            print("a or b value is invalid")
            return None
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
