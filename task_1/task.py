import json


class JsonParser:

    def __init__(self, path):
        file = open(path)
        self.__obj = json.load(file)

    def __eq__(self, other):
        return COMPARER.compare(self, other)

    def __ne__(self, other):
        return not COMPARER.compare(self, other)

    def __len__(self):
        return len(self.__obj)

    def __iter__(self):
        for key, value in self.__obj.items():
            yield key, value

    def __contains__(self, item):
        return item in self.__obj

    def __getitem__(self, item):
        return self.__obj[item]


class COMPARER:

    @staticmethod
    def compare(obj, other_obj):
        if len(obj) != len(other_obj):
            return False

        for key, value in obj:
            if key not in other_obj:
                return False

            other_value = other_obj[key]

            if isinstance(value, float) and isinstance(other_value, float):
                value = round(value, 5)
                other_value = round(other_value, 5)

            if value != other_value:
                return False

        return True


if __name__ == '__main__':
    obj1 = JsonParser('file_one.json')
    obj2 = JsonParser('file_two.json')
    obj3 = JsonParser('file_three.json')

    print(obj1 == obj2)

    print(obj1 == obj3)
    print(obj1 != obj3)
