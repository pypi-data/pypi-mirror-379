# Test basique
import fastgraphFPMS as fg
matrix = [[0,1],[1,0]]
g = fg.Graph(matrix)

g.load_from_file("tests/input_1.txt")

g.print()

g.save_to_file("tests/output_1.txt")

print('✅ Test réussi!')