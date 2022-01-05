class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = -float("inf")
        for i in self.__elements:
            for j in self.__elements:
                self.maximumDifference = abs(i - j) if self.maximumDifference < abs(i - j) else self.maximumDifference


# End of Difference class

_ = input()
a = [int(e) for e in input().split(" ")]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
