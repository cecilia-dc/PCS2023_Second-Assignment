'''
Rosalind TREE exercise by Di Cicco Cecilia
'''
# Completing a Tree

# Defining the function minimum edges
def min_edges_to_tree(n, edges):
    m = len(edges)
    return n - 1 - m

def main():
    with open('rosalind_tree.txt', 'r') as file:
        n = int(file.readline().strip())
        edges = [tuple(map(int, line.strip().split())) for line in file]

    result = min_edges_to_tree(n, edges)
    print(result)

if __name__ == "__main__":
    main()
