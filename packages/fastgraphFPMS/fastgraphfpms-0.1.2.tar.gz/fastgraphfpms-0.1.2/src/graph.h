#ifndef FASTGRAPHFPMS_GRAPH_H
#define FASTGRAPHFPMS_GRAPH_H

#include <vector>
#include <string>
#include <memory>
#include <queue>
#include <stack>
#include <algorithm>
#include <limits>
#include <tuple>

using namespace std;

namespace fastgraphfpms {

class Graph {
private:
    int num_nodes;
    vector<vector<int>> adjacency_matrix;
    bool is_directed;
    
public:
    // Constructeurs
    Graph();
    Graph(const vector<vector<int>>& matrix, bool directed = false);
    Graph(const string& filename, bool directed = false);
    
    // Méthodes de base
    void load_from_file(const string& filename);
    void save_to_file(const string& filename) const;
    int get_num_nodes() const { return num_nodes; }
    bool get_is_directed() const { return is_directed; }
    
    
};

} // namespace fastgraphfpms

#endif