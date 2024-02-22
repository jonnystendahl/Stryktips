import os
import numpy as np
import itertools as it
import pandas as pd

class TippaRows:

    np_rows = np.full(1594323, fill_value = '1111111111111', dtype = 'U13')
    np_odds_new = np.array(np.meshgrid([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], )).T.reshape(-1, 13)
    np_odds = np.ones(1594323, dtype = float)
    np_sorted = np.zeros(1594323, dtype = int)
    np_odds_1 = np.ones(13, dtype = float)
    np_odds_x = np.ones(13, dtype = float)
    np_odds_2 = np.ones(13, dtype = float)

    df_sum = pd.DataFrame
    df_det = pd.DataFrame
    
    def __init__(self):
        pass

    def create_all_rows(self):
        
        rows = []
        signs = '1X2'
        row_num = 0
        
        # Generate all possible 1 594 323 row combinations
        # Also create an array with the total odds for each row
        for row_str in it.product(signs, repeat = 13):
            self.np_rows[row_num] = ''.join(list(row_str))
            row_num += 1
            
    def print_rows(self):
        print(self.np_rows)
        print("END")

    def calculate_odds(self):

        # reset odds
        np_odds = np.ones(1594323, dtype = float)
        
        r = 0
        for row in self.np_rows:
            print("Calculate odd for row ", r)
            x = 0
            for chr in row:
                if chr == '1':
                    self.np_odds[r] *= self.np_odds_1[x]
                elif chr == 'X':
                    self.np_odds[r] *= self.np_odds_x[x]
                else:
                    self.np_odds[r] *= self.np_odds_2[x]
                x += 1
            r += 1
        
        self.np_sorted = np.argsort(self.np_odds)

    def read_stats(self, file_name_sum, file_name_det):
            
        os.chdir('src')
        
        self.df_sum = pd.read_csv(file_name_sum, sep = ';')
        self.df_det = pd.read_csv(file_name_det, sep = ';')

        self.df_sum.sort_values(by = ['omg'], ignore_index = True, inplace = True)
        self.df_det.sort_values(by = ['omg', 'matchnummer'], ignore_index = True, inplace = True)

        # self.df_sum.to_csv('sum.csv', index = False, sep = ';')
        # self.df_det.to_csv('det.csv', index = False, sep = ';')
        
        # self.df = pd.merge(self.df_sum, self.df_det, how='inner', on='omg', suffixes=('_left', '_right'), indicator = True)
    
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
            
            odds = np.array(np.meshgrid(self.np_odds_1, self.np_odds_x, self.np_odds_2)).T.reshape(-1, 13)

            self.calculate_odds()
            self.np_sorted = np.argsort(self.np_odds)

def main():
    
    Tippa = TippaRows()
    Tippa.create_all_rows()
    Tippa.simulate()
    Tippa.print_rows()

if __name__ == "__main__":
    main()

np.array(np.meshgrid([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], )).T.reshape(-1, 13)