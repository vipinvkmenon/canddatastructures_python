# Chapter 8.6
#  ifelse

USD = 1
UKP= 1

if (USD):  # if defined
    currency_rate = 46
else:
    currency_rate = 100

def main():  # Main Fuction
    rs = 10 * currency_rate
    print(rs)

main()  # Main function entry