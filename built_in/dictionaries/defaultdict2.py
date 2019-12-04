from collections import defaultdict

unlimited_key_dictionary_factory = lambda: lambda: defaultdict(unlimited_key_dictionary_factory())

d = defaultdict(unlimited_key_dictionary_factory())

d['A']['B']['C']['D'] = 10

print(d['A']['B']['C']['D'])

for a, a_values in d.items():
    print(a)
    for b, b_values in a_values.items():
        print(b)
        for c, c_values in b_values.items():
            print(c)
            for d, d_values in c_values.items():
                print(d)
                print(d_values)




