class MAPS:

    @staticmethod
    def read_map (name):
        this_entire = open(name, "r")
        this_line = this_entire.readlines()
        lines_array = []
        for x in this_line:
            splitted = [char for char in x]
            if splitted[-1] == "\n":
                splitted.pop()
            lines_array.append(splitted)

        return lines_array
