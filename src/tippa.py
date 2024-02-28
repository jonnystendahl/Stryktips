import os
import numpy as np
import itertools as it
import pandas as pd

class TippaRows:

    np_rows = np.array(np.meshgrid([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], )).T.reshape(-1, 13)
    np_odds = np.ones(20726199, dtype = float).reshape(1594323, 13)
    np_sorted = np.zeros(20726199, dtype = int).reshape(1594323, 13)
    np_odds_1 = np.ones(13, dtype = float)
    np_odds_x = np.ones(13, dtype = float)
    np_odds_2 = np.ones(13, dtype = float)

    df_sum = pd.DataFrame
    df_det = pd.DataFrame
    
    def __init__(self):
        pass

    def print_rows(self):
        print(self.np_rows)
        print("END")

    def calculate_odds(self):

        # reset odds by setting all values to 1.0
        self.np_odds[:] = 1.0

        # Calc odds for each row in nr_rows
        # Odds are find in np_odds_1, np_odds_x and np_odds_2
        filter_1 = self.np_rows  == [1,1,1,1,1,1,1,1,1,1,1,1,1]
        filter_x = self.np_rows  == [2,2,2,2,2,2,2,2,2,2,2,2,2]
        filter_2 = self.np_rows  == [3,3,3,3,3,3,3,3,3,3,3,3,3]

        np.multiply(self.np_odds, self.np_odds_1, out = self.np_odds, where = filter_1)
        np.multiply(self.np_odds, self.np_odds_x, out = self.np_odds, where = filter_x)
        np.multiply(self.np_odds, self.np_odds_2, out = self.np_odds, where = filter_2)

        np_row_odds = np.prod(self.np_odds, axis = 1)

        print(self.np_odds[0])
        print(np_row_odds[0])
        
        self.np_sorted = np.argsort(np_row_odds)

        print(np_row_odds[self.np_sorted[0]])
        print(np.min(np_row_odds))

    def read_stats(self, file_name_sum, file_name_det):
            
        os.chdir('src')
        
        self.df_sum = pd.read_csv(file_name_sum, sep = ';')
        self.df_det = pd.read_csv(file_name_det, sep = ';')

        self.df_sum.sort_values(by = ['omg'], ignore_index = True, inplace = True)
        self.df_det.sort_values(by = ['omg', 'matchnummer'], ignore_index = True, inplace = True)
    
    def simulate(self):
        self.read_stats('sum.csv', 'new_det.csv')

        for sum_label, sum_row in self.df_sum.iterrows():
            print(sum_label, sum_row)
            df = self.df_det.query("omg == @sum_row.omg")
            idx = 0
            for det_label, det_row in df.iterrows():
                print(det_label, det_row.omg, det_row.matchnummer, det_row.oddset1, det_row.oddsetx, det_row.oddset2)
                self.np_odds_1[idx] = det_row.oddset1 if det_row.oddset1 > 0 else 1
                self.np_odds_x[idx] = det_row.oddsetx if det_row.oddsetx > 0 else 1
                self.np_odds_2[idx] = det_row.oddset2 if det_row.oddset2 > 0 else 1
                idx += 1
            
            self.calculate_odds()

def main():
    
    Tippa = TippaRows()
    Tippa.simulate()
    Tippa.print_rows()

if __name__ == "__main__":
    main()

np.array(np.meshgrid([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], )).T.reshape(-1, 13)