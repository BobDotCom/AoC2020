import itertools

def get_data(filename) -> list:
    """Returns a list of data from a text file"""
    filename += ".txt" if not filename.endswith(".txt") else ""
    data = [int(val) for val in open(filename, "r").readlines()]
    return data

class day1:
    def __init__(self):
        self.input = get_data("day-1-input") # could put the list here, just didn't for now
    def part1(self):
        for x, y in itertools.product(self.input,self.input):
            if x + y == 2020:
                return x * y 
    def part2(self):
        for x, y, z in itertools.product(self.input,self.input,self.input):
            if x + y + z == 2020:
                return x * y * z
    def final(self):
        solution = f"""
--------------------------

    Part 1      Part 2    

--------------------------

    {self.part1()}      {self.part2()}

--------------------------
"""
        return print(solution)