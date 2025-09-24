#include "graph.h"
#include <fstream>
#include <iostream>
#include <queue>
#include <stack>
#include <algorithm>
#include <climits>
#include <tuple>
#include <set>

namespace fastgraphfpms {

using namespace std;

Graph::Graph() : num_nodes(0), is_directed(false) {}

Graph::Graph(const vector<vector<int>>& matrix, bool directed) 
    : adjacency_matrix(matrix), num_nodes(matrix.size()), is_directed(directed) {
    
    if (num_nodes > 0 && matrix[0].size() != num_nodes) {
        throw invalid_argument("Adjacency matrix must be square");
    }
}

Graph::Graph(const string& filename, bool directed) : is_directed(directed) {
    load_from_file(filename);
}

void Graph::load_from_file(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        throw runtime_error("Cannot open file: " + filename);
    }
    
    file >> num_nodes;
    adjacency_matrix.resize(num_nodes, vector<int>(num_nodes, 0));
    
    for (int i = 0; i < num_nodes; ++i) {
        for (int j = 0; j < num_nodes; ++j) {
            file >> adjacency_matrix[i][j];
        }
    }
    file.close();
}

void Graph::save_to_file(const string& filename) const {
    ofstream file(filename);
    if (!file.is_open()) {
        throw runtime_error("Cannot open file: " + filename);
    }
    
    file << num_nodes << "\n";
    for (int i = 0; i < num_nodes; ++i) {
        for (int j = 0; j < num_nodes; ++j) {
            file << adjacency_matrix[i][j] << " ";
        }
        if(i < num_nodes-1){
            file << "\n";
        }
    }
    file.close();
}

} // namespace fastgraphfpms