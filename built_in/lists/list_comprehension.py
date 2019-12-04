"""
samples of list comprehension
"""


def main():
    """
    main function
    """
    # create a list from range()
    data = [i for i in range(5)]
    print(f"{data}")
    # [0, 1, 2, 3, 4]

    # create a list with filter
    data = [i for i in range(5) if i % 2 == 0]
    print(f"{data}")
    # [0, 2, 4]

    # modify existing list
    new_data = [d + 1 for d in data]
    print(f"{new_data}")
    # [1, 3, 5]

    # call function on each element
    data = ["a", "b", "c"]
    new_data = [d.upper() for d in data]
    print(new_data)
    # ['A', 'B', 'C']


if __name__ == "__main__":
    main()
