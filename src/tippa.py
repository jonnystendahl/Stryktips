import numpy as np

class TippaRows:

    np_rows = np.full(1594323, fill_value = '1111111111111', dtype = 'U13')
    np_odds = np.ones(1594323, dtype = float)
    np_sorted = np.zeros(1594323, dtype = int)
    np_odds_1 = np.ones(13, dtype = float)
    np_odds_x = np.ones(13, dtype = float)
    np_odds_2 = np.ones(13, dtype = float)
    
    def __init__(self):
        self.np_odds_1[0] = 1.0
        self.np_odds_1[1] = 1.0
        self.np_odds_1[2] = 1.0
        self.np_odds_1[3] = 1.0
        self.np_odds_1[4] = 1.0
        self.np_odds_1[5] = 1.0
        self.np_odds_1[6] = 1.0
        self.np_odds_1[7] = 1.0
        self.np_odds_1[8] = 1.0
        self.np_odds_1[10] = 1.0
        self.np_odds_1[11] = 1.0
        self.np_odds_1[12] = 1.0

        self.np_odds_x[0] = 2.0
        self.np_odds_x[1] = 2.0
        self.np_odds_x[2] = 2.0
        self.np_odds_x[3] = 2.0
        self.np_odds_x[4] = 2.0
        self.np_odds_x[5] = 2.0
        self.np_odds_x[6] = 2.0
        self.np_odds_x[7] = 2.0
        self.np_odds_x[8] = 2.0
        self.np_odds_x[10] = 2.0
        self.np_odds_x[11] = 2.0
        self.np_odds_x[12] = 2.0

        self.np_odds_2[0] = 3.0
        self.np_odds_2[1] = 3.0
        self.np_odds_2[2] = 3.0
        self.np_odds_2[3] = 3.0
        self.np_odds_2[4] = 3.0
        self.np_odds_2[5] = 3.0
        self.np_odds_2[6] = 3.0
        self.np_odds_2[7] = 3.0
        self.np_odds_2[8] = 3.0
        self.np_odds_2[10] = 3.0
        self.np_odds_2[11] = 3.0
        self.np_odds_2[12] = 3.0

    def create_all_rows(self):
        
        rows = []
        signs = '1X2'
        row_num = 0
        
        for p1 in signs:
            for p2 in signs:
                for p3 in signs:
                    for p4 in signs:
                        for p5 in signs:
                            for p6 in signs:
                                for p7 in signs:
                                    for p8 in signs:
                                        for p9 in signs:
                                            for p10 in signs:
                                                for p11 in signs:
                                                    for p12 in signs:
                                                        for p13 in signs:
                                                            self.np_rows[row_num] = ''.join([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13])
                                                            self.calculate_odds(row_num)
                                                            row_num += 1
        # self.np_rows = np.array(rows)
        self.np_sorted = np.argsort(self.np_odds)
                    
    def print_rows(self):
        print(self.np_rows)
        print("END")

    def calculate_odds(self, index):
        row = 0
        for chr in self.np_rows[index]:
            if chr == '1':
                self.np_odds[index] *= self.np_odds_1[row]
            elif chr == 'X':
                self.np_odds[index] *= self.np_odds_x[row]
            else:
                self.np_odds[index] *= self.np_odds_2[row]
            row += 1

def main():
    import time
    
    Tippa = TippaRows()

    Tippa.create_all_rows()
    Tippa.print_rows()

if __name__ == "__main__":
    main()
