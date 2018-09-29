class Ship:

    change_num = 0
    compare_num = 0

    @staticmethod
    def change_count():
            Ship.change_num += 1
            return Ship.change_num

    @staticmethod
    def compare_count():
        Ship.compare_num += 1
        return Ship.compare_num

    @staticmethod
    def drop_count():
        Ship.change_num = 0
        Ship.compare_num = 0

    def __init__(self, capacity, name, num_of_cases):
        self.capacity = capacity
        self.name = name
        self.num_of_cases = num_of_cases

    def __repr__(self):
        return str(self.capacity) + " " + str(self.name) + " " + str(self.num_of_cases)