
class Solution:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.initial_state = []

        with open(self.file_name, 'r') as f:
            self.initial_state = f.read().split(',')

    def give_number_of_fish(self, number_of_days: int) -> int:
        """
        Computes the total fish population after the number of days specified in the argument
        via the use of counts and a hash map/dictionary

        Arguments: 
            number_of_days: an int
            Implicit Argument is self.initial_state

        Returns:
            The total fish population after number of days specified in the argument
        """

        dict = {'0': 0,
                '1': 0,
                '2': 0,
                '3': 0,
                '4': 0,
                '5': 0,
                '6': 0,
                '7': 0,
                '8': 0}

        for ele in list(self.initial_state):
            dict[ele] += 1

        for _ in range(number_of_days):
            new_dict = {'0': 0, '1': 0,
                        '2': 0,
                        '3': 0,
                        '4': 0,
                        '5': 0,
                        '6': 0,
                        '7': 0,
                        '8': 0}

            for (k, v) in dict.items():
                if k == '0':
                    new_dict['6'] += dict['0']
                    new_dict['8'] += dict['0']
                else:
                    new_key = str(int(k) - 1)
                    new_dict[new_key] += dict[k]

            dict = new_dict

        final_count = 0
        for (k, v) in dict.items():
            final_count += dict[k]

        return final_count

    def print_data(self):
        print(self.data)

    def print_initial_state(self):
        print(self.initial_state)
