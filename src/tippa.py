import numpy as np

class TippaRows:
    _rows = []

    def __init__(self):
        pass    

    def create_all_rows(self):
        
        # for x in range(3):
        #     row = []
        #     for y in range(13):
        #         if x == 0:
        #             row.append('1')
        #         elif x == 1:
        #             row.append('X')
        #         else:
        #             row.append('2')
        #     print('Row {} = {}'.format(x, row))
        #     print()
        #     self._rows.append(row)

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
                                                            row = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]
                                                            self._rows.append(str(row))
                    

    
    def add_row(self, row, odds):
        newrow = {}
        newrow["row"] = row
        newrow["odds"] = odds
        self._rows.append(newrow)

    def sort_rows(self):
         self._rows = sorted(self._rows, key=lambda d: d['odds'])

    def print_rows(self):
         for row in self._rows:
            print(row)

    def set_odds(self, index, odds):
        self._rows[index - 1]["odds"] = odds

    def create_numpy_array(self):
        arr = np.array(self._rows)
        print(arr)


def main():
    Tippa = TippaRows()

    Tippa.create_all_rows()

    # Tippa.add_row("XXX", 2)
    # Tippa.add_row("111", 1)
    # Tippa.add_row("222", 99)
    
    # Tippa.sort_rows()
    # print("Original")
    # Tippa.print_rows()
    # Tippa.set_odds(1, 77)
    # Tippa.sort_rows()
    # print("Changed")
    # Tippa.print_rows()
    Tippa.create_numpy_array()
    

if __name__ == "__main__":
    main()
