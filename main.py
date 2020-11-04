from FA import FA

if __name__ == '__main__':
    fa = FA()
    fa.read_from_file("fa.txt")
    print(fa)

    if fa.is_deterministic():
        print("the given FA is deterministic")
    else:
        print("the given FA is nondeterministic")