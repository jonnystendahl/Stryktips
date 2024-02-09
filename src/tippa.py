import os
import numpy as np
import itertools as it
import pandas as pd

class TippaRows:

    np_rows = np.full(1594323, fill_value = '1111111111111', dtype = 'U13')
    np_odds = np.ones(1594323, dtype = float)
    np_sorted = np.zeros(1594323, dtype = int)
    np_odds_1 = np.ones(13, dtype = float)
    np_odds_x = np.ones(13, dtype = float)
    np_odds_2 = np.ones(13, dtype = float)

    df = pd.DataFrame
    
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
        
        # Generate all possible 1 594 323 row combinations
        # Also create an array with the total odds for each row
        for row_str in it.product(signs, repeat = 13):
            self.np_rows[row_num] = ''.join(list(row_str))
            row_num += 1

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

    def read_stats(self, file_name_sum, file_name_det):
            
        os.chdir('src')
        
        df_sum = pd.read_csv(file_name_sum, sep = ';')
        df_det = pd.read_csv(file_name_det, sep = ';')

        df_sum.sort_values(by = ['omg'], ignore_index = True, inplace = True)
        df_det.sort_values(by = ['omg', 'matchnummer'], ignore_index = True, inplace = True)

        # df_sum.to_csv('sum.csv', index = False, sep = ';')
        # df_det.to_csv('det.csv', index = False, sep = ';')
        
        self.df = pd.merge(df_sum, df_det, how='inner', on='omg', suffixes=('_left', '_right'), indicator = True)

        print(df_sum)
        print(df_det)
        print(self.df)

        self.df.info()

        for row_label, row in df_sum.iterrows():
            # print(row_label, row.omg, row.correct_row)
            df_rows = df_det.loc[df_det['omg'] == row.omg]
            if len(df_rows.index) != 13:
                print(row.omg)
                                 
        
        print('END')

def main():
    
    Tippa = TippaRows()
    # Tippa.read_stats('Stryktips_summering.csv', 'Stryktips_detaljer.csv')
    Tippa.read_stats('sum.csv', 'new_det.csv')
    Tippa.create_all_rows()
    Tippa.print_rows()

if __name__ == "__main__":
    main()
