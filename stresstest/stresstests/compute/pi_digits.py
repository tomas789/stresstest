from stresstest.stresstest import BaseStresstest, Parameter


class CalculatePiDigitsStresstest(BaseStresstest):
    name = ["compute", "pi_digits", "CalculatePiDigitsStresstest"]

    parameters = [Parameter("iterations", default=10000000, type=int)]

    def run_test(self, iterations: int):
        pi = 0

        with self:
            for i in range(iterations):
                pi += 4 * (1 - (i % 2) * 2) / (2 * i + 1)
