from FA import FA

if __name__ == '__main__':
    fa = FA()
    fa.read_from_file("fa.txt")
    print(fa)

    if fa.is_deterministic():
        print("the given FA is deterministic")
        sequence = input("Give a sequence to be verified: ")

        if fa.is_accepted(sequence):
            print("The given sequence is accepted! ")
        else:
            print("The given sequence is not accepted :(")

    else:
        print("the given FA is nondeterministic")

