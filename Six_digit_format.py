# Input 0-1000
# Print the number in 6 digit format by adding zeroes in the beginning

while True:
    try:
        num = int(input("Enter a number from 0-1000: "))
        if 1 <= num <= 1000:
            print(f'{str(num)}'.zfill(6))







