import random


def is_sorted(array):
    return all(array[i - 1] <= array[i] for i in range(1, len(array)))


def thanos_sort(universe):
    if is_sorted(universe):
        return universe

    size = len(universe)
    indexes = range(size)
    half = size // 2

    to_die = random.sample(indexes, half)
    universe = [i for j, i in enumerate(universe) if j not in to_die]

    return thanos_sort(universe)


def main():
    random_universe = random.sample(range(1, 1000), 100)
    print("Universe: ", random_universe)

    ordered_universe = thanos_sort(random_universe)
    print("Ordered universe: ", ordered_universe)


if __name__ == "__main__":
    main()
