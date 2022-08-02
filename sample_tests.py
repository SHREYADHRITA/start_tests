class IncrementalCounter:
    _count = 0

    def increment(self):
        self._count += 1
        print(self._count)


testConter = IncrementalCounter()
testConter.increment()
testConter.increment()
print(testConter._count)
