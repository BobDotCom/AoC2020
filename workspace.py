import itertools

def get_data(filename) -> list:
    """Returns a list of data from a text file"""
    filename += ".txt" if not filename.endswith(".txt") else ""
    data = [val.replace("\n","") for val in open(filename, "r").readlines()]
    return data

class day1:
    def __init__(self):
        self.input = get_data("day-1-input") # this is a list of the input, split by each line
    def part1(self):
        for x, y in itertools.product(self.input,self.input):
            if int(x) + int(y) == 2020:
                return int(x) * int(y)
    def part2(self):
        for x, y, z in itertools.product(self.input,self.input,self.input):
            if int(x) + int(y) + int(z) == 2020:
                return int(x) * int(y) * int(z)
    def final(self):
        solution = f"""
--------------------------

    Part 1      Part 2    

--------------------------

    {self.part1()}      {self.part2()}

--------------------------
"""
        return print(solution)
