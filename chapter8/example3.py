# Chapter 8.3
#  ifdef

USD = 1
UKP = 1

if(USD):
    currency_rate = 46

if(UKP):
    currency_rate = 46


def main():  # Main Function
    rs = 10 * currency_rate
    print(rs)


main()  # Main Function Entry
