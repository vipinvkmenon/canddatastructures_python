# Chapter 8.8
# ERROR

USD = 1
UKP = 1

if (not(USD) or not(UKP)):
    print("ERROR: NO_CURRENCY rate is specified")

def main():
    currency_rate = 100
    rs = 10 * currency_rate
    print(rs)

main()
