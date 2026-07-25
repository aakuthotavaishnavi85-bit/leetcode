class Solution:
    def maxProduct(self, n: int) -> int:
        res=[]
        while n>0:
            res.append(n%10)
            n//=10
        max_product=0
        product=0
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                product=res[i]*res[j]
                max_product=max(max_product,product)
        return max_product

            

