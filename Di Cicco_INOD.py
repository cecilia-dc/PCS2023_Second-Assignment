'''
Rosalind INOD exercise by Di Cicco Cecilia
'''
# Counting Phylogenetic Ancestors

# Defining the function that calculates the internal nodes
def calculate_internal_nodes(leaves):
    return leaves - 2

def main():
    with open('rosalind_inod.txt', 'r') as file:
        leaves = int(file.readline().strip())

    internal_nodes = calculate_internal_nodes(leaves)
    print(internal_nodes)

if __name__ == "__main__":
    main()