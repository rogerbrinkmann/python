"""
Examples for format-string usage
"""

from math import sin, cos, pi

# headings
x_header = "x-values"
y1_header = "y1-values"
y2_header = "y2-values"

num_samples = 10
# number values
xlst = [i / num_samples * 2 * pi for i in range(num_samples)]
y1lst = [sin(i) for i in xlst]
y2lst = [cos(i) for i in xlst]

# reserved_space
# precision after the floating point

# format_code
# f(F): floating point
# e(E): engineering
# g(G):
# n: number
# %: multiplied by 100 and added % sign

# alignment
# left: <
# right: >
# centered: ^
# justified (signs to the left) =

# f"4{alignment}{reserved_space}.{precision}{format_code}"

print(f"{x_header:>10}|{y1_header:>10}|{y2_header:>10}")
print("-" * 32)
for x, y1, y2 in zip(xlst, y1lst, y2lst):
    print(f"{x:>10.3f}|{y1:>10.3f}|{y2:10.3f}")

# output:
#   x-values| y1-values| y2-values
# --------------------------------
#      0.000|     0.000|     1.000
#      0.628|     0.588|     0.809
#      1.257|     0.951|     0.309
#      1.885|     0.951|    -0.309
#      2.513|     0.588|    -0.809
#      3.142|     0.000|    -1.000
#      3.770|    -0.588|    -0.809
#      4.398|    -0.951|    -0.309
#      5.027|    -0.951|     0.309
#      5.655|    -0.588|     0.809