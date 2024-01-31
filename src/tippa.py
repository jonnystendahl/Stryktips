import numpy as np

class TippaRows:
    
    def __init__(self):
        np_rows = np.empty(1594323, dtype = str)
        np_odds = np.empty(1594323, dtype = float)
        np_sorted = np.zeros(1594323, dtype = int)

    def create_all_rows(self):
        
        rows = []
        signs = '1X2'
        
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
                                                            rows.append(''.join([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]))
        self.np_rows = np.array(rows)
        rng = np.random.default_rng()
        self.np_odds = rng.integers(low = 4, high = 10, size = 1594323)
        self.np_sorted = np.argsort(self.np_odds)
                    
    def print_rows(self):
        print("Min = ", np.min(self.np_odds))
        print(self.np_odds[0:4])
        print(self.np_sorted[0:4])
        print(self.np_odds[self.np_sorted[0]])
        print("END")

    def set_odds(self, index, odds):
        self.np_odds[index] = odds

def main():
    import time
    
    Tippa = TippaRows()

    Tippa.create_all_rows()
    Tippa.print_rows()

if __name__ == "__main__":
    main()
