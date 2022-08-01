class Caluculator():
    def sum(self, left, right):
        if left < 0 or right < 0:
            raise ValueError("sum error!")
        return left + right

    def save(self, value):
        accessor = DbAccessor()
        accessor.save(value)

class DbAccessor():
    def save(self, value):
        raise ValueError("Not implemented")