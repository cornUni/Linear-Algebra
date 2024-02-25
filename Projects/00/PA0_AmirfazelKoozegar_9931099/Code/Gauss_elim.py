import numpy as np

size = int(input())
class Gauss_Elim():
    def __init__(self):
        self.raw_array =[]
        self.augmented_array = np.zeros((size,size+1))
        self.solution_array = np.zeros((size))

    def get_raw_input(self):
        # getting the raw array in string form from user
        for i in range(size+1):
            self.raw_array.append(input())

    def create_linear_system(self):
        #converting the raw array to a numpy array
        #first, adding the main matrix
        for i in range(size):
            for j in range(size):
                self.augmented_array[i][j] = float(self.raw_array[i].split(" ")[j])
        #second, adding the augmented column
        for index,number in enumerate(self.raw_array[-1].split(" ")):
            self.augmented_array[index][size] = float(number)

    def gauss_eliminate(self):
        #applying the Gauss Elimination
        print("sloving system step by step...\n")
        for i in range(size):
            for j in range(i + 1, size):
                print('{array}\n'.format(array=np.around(self.augmented_array, decimals=2)))
                if self.augmented_array[i][i] !=0:
                    tmp = self.augmented_array[j][i] / self.augmented_array[i][i]
                    for k in range(size + 1):
                        self.augmented_array[j][k] = self.augmented_array[j][k] - tmp * self.augmented_array[i][k]

    def calculate_solution(self):
        # Getting the solution
        self.solution_array[size - 1] = self.augmented_array[size - 1][size] / self.augmented_array[size - 1][size - 1]

        for i in range(size - 2, -1, -1):
            self.solution_array[i] = self.augmented_array[i][size]

            for j in range(i + 1, size):
                self.solution_array[i] = self.solution_array[i] - self.augmented_array[i][j] * self.solution_array[j]

            self.solution_array[i] = self.solution_array[i] / self.augmented_array[i][i]



    def print_solution(self):
        for i in range (size):
            print('x{index}:{value}'.format(index=i+1, value=round(self.solution_array[i])))

if __name__ == "__main__":
    g = Gauss_Elim()
    g.get_raw_input()
    g.create_linear_system()
    g.gauss_eliminate()
    g.calculate_solution()
    g.print_solution()
