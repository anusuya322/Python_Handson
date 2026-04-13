class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>len(s):
            return s
        rows=[""]*numRows
        down=False
        current=0
        for ch in s:
            rows[current]+=ch
            if current ==0 or current==numRows-1:
                down=not down
            current+=1 if down else -1
        return "".join(rows)
