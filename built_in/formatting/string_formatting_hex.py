"""
Examples for format-string usage with hex values
"""
import random

# headings
a_header = "address"
d_header = "data"

num_samples = 10
# number values
alst = [i + 1000 for i in range(num_samples)]
dlst = [[random.randint(0, 255) for i in range(8)] for j in alst]

# header
print(f"{'addr':>7}{'data':^26}")

# underline
print("-" * 33)

# loop over the data
for a, d in zip(alst, dlst):

    # build a string of hex numbers
    d = " ".join([f"{i:02x}" for i in d])

    # print out the data
    print(f"{a:>7}{d:>25}")


#    addr           data
# ---------------------------------
#    1000   4f 17 4b cf f4 82 38 50
#    1001   86 1e 50  0 42  e e9 2b
#    1002   ed 65 17 41 78 80 ca 87
#    1003   75 73  8 a0  e e4 ae bd
#    1004   37 11 6b 27 28 34 e4 55
#    1005   c4 75 58 9b  f 61 91 f6
#    1006   df c4 f0 f2 63 1e a3  2
#    1007   25 e9 a7 5a dd a0 50 a4
#    1008   4e 6d 16 ae a6 62 b1 60
#    1009   92 f3 3d 50 6c 40 9d  1
