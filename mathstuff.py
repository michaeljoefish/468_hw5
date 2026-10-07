import numpy as np

C = [[0,0,0,0,0,0,0,0,0], [1,1,1,0,0,0,0,0,0], [1,0,0,1,0,0,1,0,0], [1,0,0,0,1,1,1,0,0],
     [0,1,0,0,1,0,0,1,0], [0,1,0,0,1,0,1,0,1], [0,1,1,1,0,0,1,0,0], [0,1,1,0,1,1,1,0,0],
     [1,0,1,0,1,0,0,1,0], [1,0,1,0,1,0,1,0,1], [0,0,0,1,1,1,0,0,0], [1,1,0,1,1,0,1,1,0],
     [1,1,0,1,1,0,0,0,1], [1,1,0,0,0,1,1,1,0], [1,1,0,0,0,1,0,0,1], [0,0,0,0,0,0,1,1,1],
     [1,1,1,1,1,1,0,0,0], [0,0,1,1,1,0,1,1,0], [0,0,1,1,1,0,0,0,1], [0,1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,1,0,1], [1,0,0,0,1,1,0,1,1], [1,0,1,1,0,1,0,1,0], [1,0,1,1,0,1,1,0,1],
     [0,1,1,1,0,0,0,1,1], [0,1,1,0,1,1,0,1,1], [0,0,0,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1],
     [0,0,1,0,0,1,1,1,0], [0,0,1,0,0,1,0,0,1], [1,1,1,0,0,0,1,1,1], [1,0,0,1,0,0,0,1,1]]

def find_coset_leaders(coset_vector):
    coset = (C + coset_vector) % 2

    coset_weights = np.sum(coset, axis=1)

    min_weight = np.min(coset_weights)

    coset_leaders = []

    length_of_coset = 32
    i = 0

    for i in range(0,32):
        if coset_weights[i] == min_weight:
            coset_leaders.append(coset[i])

    print(f"Coset leaders for coset containing {coset_vector} are:")
    for leader in coset_leaders:
        print(leader)

    print()

def main():
    a = np.array([1,1,1,1,0,1,0,0,0])
    b = np.array([1,1,0,1,0,1,0,1,1])
    c = np.array([0,1,0,0,1,0,0,1,0])

    find_coset_leaders(a)

    find_coset_leaders(b)

    find_coset_leaders(c)

if __name__ == "__main__":
    main()
