class Reverse:
    def __init__(self,data):
        """Iterator for looping a sequence backwards."""
        self.data=data
        self.index=len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index-=1
        return self.data[self.index]

rev=Reverse("sriram")
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))


rev=Reverse("sriram2")
for char in rev:
    print(char)
