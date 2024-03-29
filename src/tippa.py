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

    # Keep track of hor much we bet and win
    amount_bet = 0
    amount_win = 0

    # Keep track of MIN and MAX number of rows to bet
    min_num_of_rows = 0
    max_num_of_rows = 0

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

    def simulate_cost_win(self, correct_row, utd_13, utd_12, utd_11, utd_10):

        # Convert the row as string to a array shape(13) where '1' = 1, 'X' = 2 and '2' = 4
        row_to_check = np.array(list(correct_row.replace('2', '4').replace('X', '2'))).astype(dtype=np.int8)
        
        # Compare the row against all rows, returning a array of True/False for each entry (match)
        comp_result = self.np_all_rows == row_to_check

        # Count numer of True (1) values this is eaqual to number of correct results in each row
        # this returns an array shape(1594323) with number of correct result in each row in np_all_rows
        num_of_correct_result = np.count_nonzero(comp_result, axis=1)

        # Find the index of value 13, that is the one row with 13 correct result
        # should always and only be one
        idx_13 = np.where(num_of_correct_result == 13)[0][0]

        # Find that index in np_sorted
        idx_in_sorted_odds = np.where(self.np_sorted == idx_13)[0][0]
        number_of_rows_to_bet = idx_in_sorted_odds

        # Get all rows that we need to bet on to win 13 correct matches
        rows_to_bet = self.np_all_rows[self.np_sorted[:idx_in_sorted_odds+1]]

        # Calculate number of rows with 13, 12, 11 and 10 correct matches
        comp_result = rows_to_bet == row_to_check

        # Count numer of True (1) values this is eaqual to number of correct results in each row
        # this returns an array shape(xx, 13) with number of correct result in each row in rows_to_bet
        num_of_correct_result = np.count_nonzero(comp_result, axis=1)

        cnt_13 = np.count_nonzero(num_of_correct_result == 13)
        cnt_12 = np.count_nonzero(num_of_correct_result == 12)
        cnt_11 = np.count_nonzero(num_of_correct_result == 11)
        cnt_10 = np.count_nonzero(num_of_correct_result == 10)

        amount_bet = number_of_rows_to_bet
        amount_win = utd_13 * cnt_13 + utd_12 * cnt_12 + utd_11 * cnt_11 + utd_10 * cnt_10

        return amount_bet, amount_win
             
        # Get the row with result 13
        row_result_13 = self.np_sorted[idx_in_sorted_odds]

        print('Correct row ', correct_row)
        print('Converted row ', row_to_check)
        print('Guess of row  ', self.np_all_rows[row_result_13])
        print('Number of rows to bet ', number_of_rows_to_bet)

        print('END')

    def read_stats(self, file_name_sum, file_name_det):
            
        os.chdir('src')
        
        self.df_sum = pd.read_csv(file_name_sum, sep = ';')
        self.df_det = pd.read_csv(file_name_det, sep = ';')

        self.df_sum.sort_values(by = ['omg'], ignore_index = True, inplace = True)
        self.df_det.sort_values(by = ['omg', 'matchnummer'], ignore_index = True, inplace = True)
    
    def test_method_odds(self):

        # Reset values
        self.amount_bet = 0
        self.amount_win = 0
        self.min_num_of_rows = 2000000
        self.max_num_of_rows = 0
        
        self.read_stats('sum.csv', 'new_det.csv')

        for sum_label, sum_row in self.df_sum.iterrows():
            # print(sum_row.omg, sum_row.correct_row, sum_row.utd13, sum_row.utd12, sum_row.utd11, sum_row.utd10)
            df = self.df_det.query("omg == @sum_row.omg")
            idx = 0
            for det_label, det_row in df.iterrows():
                # print(det_label, det_row.omg, det_row.matchnummer, det_row.oddset1, det_row.oddsetx, det_row.oddset2)
                self.np_odds_1[idx] = det_row.oddset1 if det_row.oddset1 > 0 else 1
                self.np_odds_x[idx] = det_row.oddsetx if det_row.oddsetx > 0 else 1
                self.np_odds_2[idx] = det_row.oddset2 if det_row.oddset2 > 0 else 1
                idx += 1
            
            self.calculate_odds()
            amount_bet, amount_win = self.simulate_cost_win(sum_row.correct_row, sum_row.utd13, sum_row.utd12, sum_row.utd11, sum_row.utd10)
            
            self.amount_bet += amount_bet
            self.amount_win += amount_win

            self.min_num_of_rows = amount_bet if amount_bet < self.min_num_of_rows else self.min_num_of_rows
            self.max_num_of_rows = amount_bet if amount_bet > self.max_num_of_rows else self.max_num_of_rows

            print('Total amount bet: ', self.amount_bet)
            print('Total amount win: ', self.amount_win)
            print('Net win/loss: ', self.amount_win - self.amount_bet)
            print('Min rows = ', self.min_num_of_rows, 'Max rows = ', self.max_num_of_rows)

def main():
    
    Tippa = TippaRows()
    Tippa.test_method_odds()

if __name__ == "__main__":
    main()
