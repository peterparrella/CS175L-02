#Peter Parrella
#CS175-02
#stocks

Commission_rate = float (input("Please enter commission rate: "))
Num_Shares = int(input('Please enter the number of shares: '))
Purchase_price=int(input ("Please enter purchase price as a whole number:"))
Selling_Price=  float(input("Please enter selling price: "))

amountPaidForStock = Num_Shares * Purchase_price
purchasecommission = Commission_rate * amountPaidForStock
totalPaid= amountPaidForStock + purchasecommission
stockSoldFor= Num_Shares*Selling_Price
sellingCommission= Commission_rate * stockSoldFor
totalRecieved = stockSoldFor - sellingCommission
profitOrLoss = totalRecieved - totalPaid

print(f'Amount paid for stock: ${amountPaidForStock:,.2f}')
print(f'Commission paid on the purchase: ${purchasecommission:,.2f}')
print(f'Amount the stock sold for: ${stockSoldFor:,.2f}')
print(f'Commission paid on the sale: ${sellingCommission:,.2f}')
print(f'Profit (or loss if negative): ${profitOrLoss:,.2f}')

