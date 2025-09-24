# Test basique
import fastgraphFPMS as fg
matrix = [[0,1],[1,0]]
g = fg.Graph(matrix)
print('✅ Test réussi!')
g.save_to_file("test.txt")