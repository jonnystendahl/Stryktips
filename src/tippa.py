class TippaRows:
    _rows = []

    def __init__(self):
        pass    

    def create_all_rows(self):
        pass
    
    def addrow(self, row, odds):
        newrow = {}
        newrow["row"] = row
        newrow["odds"] = odds
        self._rows.append(newrow)

    def sortrows(self):
         self._rows = sorted(self._rows, key=lambda d: d['odds'])

    def printrows(self):
         for row in self._rows:
            print(row)

    def setodds(self, index, odds):
        self._rows[index - 1]["odds"] = odds


def main():
    tippa = TippaRows()

    tippa.addrow("XXX", 2)
    tippa.addrow("111", 1)
    tippa.addrow("222", 99)
    
    tippa.sortrows()
    print("Original")
    tippa.printrows()
    tippa.setodds(1, 77)
    tippa.sortrows()
    print("Changed")
    tippa.printrows()
    

if __name__ == "__main__":
    main()
