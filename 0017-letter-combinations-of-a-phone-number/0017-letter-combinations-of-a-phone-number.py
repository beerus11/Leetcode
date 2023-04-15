class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        m = {"2":["a","b","c"],
             "3":["d","e","f"],
             "4":["g","h","i"],
             "5":["j","k","l"],
             "6":["m","n","o"],
             "7":["p","q","r","s"],
             "8":["t","u","v"],
             "9":["w","x","y","z"]
            }
        ans =[]
        def comb(digit,i,pre):
            if i == len(digit):
                ans.append("".join(pre))
                return
            for v in m[digits[i]]:
                pre.append(v)
                comb(digit,i+1,pre[:])
                pre.pop()
        comb(digits,0,[])
        return ans
                
        