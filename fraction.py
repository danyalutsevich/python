import json


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        if denominator == 0:
            raise ZeroDivisionError
        self.denominator = denominator

    def __add__(self, frac):
        if self.denominator == frac.denominator:
            return Fraction(self.numerator + frac.numerator, self.denominator)
        else:
            return Fraction(
                (self.numerator * frac.denominator)
                + (frac.numerator * self.denominator),
                self.denominator * frac.denominator,
            )

    def __sub__(self, frac):
        if self.denominator == frac.denominator:
            return Fraction(self.numerator - frac.numerator, self.denominator)
        else:
            return Fraction(
                (self.numerator * frac.denominator)
                - (frac.numerator * self.denominator),
                self.denominator * frac.denominator,
            )

    def __mul__(self, frac):
        return Fraction(
            self.numerator * frac.numerator, self.denominator * frac.denominator
        )

    def __truediv__(self, frac):
        return Fraction(
            self.numerator * frac.denominator, self.denominator * frac.numerator
        )

    def __str__(self) -> str:
        return "[{n}/{d}]".format(n=self.numerator, d=self.denominator)

    def greatest_common_devider(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        common_devider = self.greatest_common_devider(self.numerator, self.denominator)
        return Fraction(
            self.numerator // common_devider, self.denominator // common_devider
        )

    def to_json(self) -> str:
        return json.dumps(
            {"numerator": self.numerator, "denominator": self.denominator}
        )

    def from_json(self, json_str):
        loaded_json = json.loads(json_str)
        if "numerator" in loaded_json and "denominator" in loaded_json:
            self.numerator = loaded_json["numerator"]
            self.denominator = loaded_json["denominator"]
            return self
        else:
            raise ValueError("Invalid JSON format for Fraction")

    def save_as_json(self):
        try:
            with open(
                "{n}_{d}.json".format(n=self.numerator, d=self.denominator), mode="w"
            ) as file:
                file.write(self.to_json())
        except Exception as ex:
            print(ex)

    def load_from_json(self, path):
        try:
            with open(path, mode="r") as file:
                return self.from_json(file.read())
        except Exception as ex:
            print(ex)


a = Fraction(1, 2)
b = Fraction(1, 2)
print((a * b).reduce().to_json())
print(Fraction(1, 2).from_json(a.to_json()))
a.save_as_json()
print(Fraction(1, 4).load_from_json("1_2.json"))
