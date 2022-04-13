from app import rd


class Temp:
    def set(self, key, value, time=None):
        rd.set(key, value, time)

    def get(self, key):
        return rd.get(key).decode("utf-8")

    def delete(self, key):
        rd.delete(key)
