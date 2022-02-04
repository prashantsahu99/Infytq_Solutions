# Question16. OTP Generation
# Input Format: 13456
# Output Format:1925
# Explanation:
# Take the string of numbers and generate a four digit OTP such that
# 1. 1f the number is odd square it.
# 2.If the number is even ignore it.

if __name__ == '__main__':
    num = input()
    otp = ""
    for i in num:
        if int(i) % 2 != 0:
            otp += str(int(i)**2)
    print(otp)