# Chapter 8.5
#  if

USD = 1
UKP = 1

if((1>0) and (USD)):
    currency_rate = 46

if(UKP):
    currency_rate = 1000

def main():
    rs = 10 * currency_rate
    print(rs)


main()
