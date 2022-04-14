class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        Transaction = namedtuple('Transaction', ('name', 'time', 'amount', 'city'))
        result, n = [], len(transactions)
        for i in range(n):
            t1 = Transaction(*transactions[i].split(','))
            if int(t1.amount) > 1000:
                result.append(transactions[i])
                continue
            for j in range(n):
                t2 = Transaction(*transactions[j].split(','))
                if i == j or t1.name != t2.name or t1.city == t2.city:
                    continue
                if abs(int(t1.time)-int(t2.time)) <= 60:
                    result.append(transactions[i])
                    break
        return result
        
