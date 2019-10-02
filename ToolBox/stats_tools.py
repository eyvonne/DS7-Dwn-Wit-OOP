
class Stats():
    """A collection of stats helper tools"""

    def __init__(self, list=[3, 4, 5, 6, 7, 8]):
        self.list = sorted(list)

    def mean(self):
        return sum(self.list)/len(self.list)

    def evenMedian(self):
        print("running even median")
        first = int(len(self.list)/2)
        second = int(len(self.list)/2-1)
        output = (self.list[first]+self.list[second])/2
        return output

    def oddMedian(self):
        print("running Odd Median")
        index = int((len(self.list)-1)/2)
        return self.list[index]

    def median(self):
        if len(self.list) % 2 == 1:
            return self.oddMedian()
        else:
            return self.evenMedian()
