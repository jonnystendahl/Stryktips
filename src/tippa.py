import os
import numpy as np
import itertools as it
import pandas as pd

class TippaRows:

    # Create all possible stryktips rows where 1 = '1', 2 = 'X' and 4 = '2'
    # Store these in an nparray shape(1594323, 13)
    np_all_rows = np.array(np.meshgrid([1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4], [1, 2, 4]), dtype=np.uint8).T.reshape(-1, 13)
    
    # Array of shape(1594323, 13) holding the odds for each '1', 'X' and '2'
    np_all_odds = np.ones(20726199, dtype=float).reshape(1594323, 13)
    
    # Array holding the calculated odds for all rows shape(1594323)
    np_row_odds = np.zeros(1594323, dtype=float)

    # Array containing indexes to np_row_odds sorted low to high shape(1594323)
    np_sorted = np.zeros(1594323, dtype=np.int32)
    
    # Arrays holding the odds for '1', 'X' and '2' 13 values for each
    np_odds_1 = np.ones(13, dtype=float)
    np_odds_x = np.ones(13, dtype=float)
    np_odds_2 = np.ones(13, dtype=float)

    # Pandas data frame to hold historical data of outcome
    # is used to evaluate methods against
    df_sum = pd.DataFrame
    df_det = pd.DataFrame
    
    def __init__(self):
        pass

    def calculate_odds(self):

        # reset odds by setting all values to 1.0
        self.np_all_odds[:] = 1.0

        # Calc odds for each row in nr_rows
        # Odds are find in np_odds_1, np_odds_x and np_odds_2
        filter_1 = self.np_all_rows  == [1,1,1,1,1,1,1,1,1,1,1,1,1]
        filter_x = self.np_all_rows  == [2,2,2,2,2,2,2,2,2,2,2,2,2]
        filter_2 = self.np_all_rows  == [4,4,4,4,4,4,4,4,4,4,4,4,4]

        # set odds for '1' it is represented as number 1
        np.multiply(self.np_all_odds, self.np_odds_1, out = self.np_all_odds, where = filter_1)
        # set odds for 'X'  it is represented as number 2
        np.multiply(self.np_all_odds, self.np_odds_x, out = self.np_all_odds, where = filter_x)
        # set odds for '2'  it is represented as number 4
        np.multiply(self.np_all_odds, self.np_odds_2, out = self.np_all_odds, where = filter_2)

        self.np_row_odds = np.prod(self.np_all_odds, axis = 1)
        
        self.np_sorted = np.argsort(self.np_row_odds)

        print(self.np_sorted[0])

    def simulate_cost_win(self, correct_row):
        print(np.array(list(correct_row.replace('2', '4').replace('X', '2'))))

    def read_stats(self, file_name_sum, file_name_det):
            
        os.chdir('src')
        
        self.df_sum = pd.read_csv(file_name_sum, sep = ';')
        self.df_det = pd.read_csv(file_name_det, sep = ';')

        self.df_sum.sort_values(by = ['omg'], ignore_index = True, inplace = True)
        self.df_det.sort_values(by = ['omg', 'matchnummer'], ignore_index = True, inplace = True)
    
    def test_method_odds(self):
        self.read_stats('sum.csv', 'new_det.csv')

        for sum_label, sum_row in self.df_sum.iterrows():
            print(sum_row.omg, sum_row.correct_row, sum_row.utd13, sum_row.utd12, sum_row.utd11, sum_row.utd10)
            df = self.df_det.query("omg == @sum_row.omg")
            idx = 0
            for det_label, det_row in df.iterrows():
                # print(det_label, det_row.omg, det_row.matchnummer, det_row.oddset1, det_row.oddsetx, det_row.oddset2)
                self.np_odds_1[idx] = det_row.oddset1 if det_row.oddset1 > 0 else 1
                self.np_odds_x[idx] = det_row.oddsetx if det_row.oddsetx > 0 else 1
                self.np_odds_2[idx] = det_row.oddset2 if det_row.oddset2 > 0 else 1
                idx += 1
            
            self.calculate_odds()
            self.simulate_cost_win(sum_row.correct_row)

def main():
    
    Tippa = TippaRows()
    Tippa.test_method_odds()

if __name__ == "__main__":
    main()
