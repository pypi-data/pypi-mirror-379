#include "graph.h"
#include <fstream>
#include <iostream>
#include <queue>
#include <stack>
#include <algorithm>
#include <climits>
#include <tuple>
#include <set>
#include <map>

namespace fastgraphfpms {

using namespace std;

Graph::Graph() : num_nodes(0), is_directed(false) {}

Graph::Graph(const vector<vector<int>>& matrix) 
    : num_nodes(matrix.size()){
    
    if (num_nodes > 0 && matrix[0].size() != num_nodes) {
        throw invalid_argument("Adjacency matrix must be square");
    }

    Head.resize(num_nodes);

    int idx_Succ = 0;
    for(int i = 0; i < num_nodes; i++){
        Head[i] = idx_Succ;
        for(int j = 0; j < num_nodes; j++){
            if(matrix[i][j] != 0){
                Succ.push_back(j);
                Weights.push_back(matrix[i][j]);
                idx_Succ++;
            }
        }
    }

    Head.push_back(idx_Succ);

}

Graph::Graph(const string& filename) {
    load_from_file(filename);
}

void Graph::load_from_file(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        throw runtime_error("Cannot open file: " + filename);
    }
    
    Head.clear();
    Succ.clear();
    Weights.clear();

    file >> num_nodes;
    
    Head.resize(num_nodes);

    int idx_Succ = 0, temp;
    for (int i = 0; i < num_nodes; ++i) {
        Head[i] = idx_Succ;
        for (int j = 0; j < num_nodes; ++j) {
            file >> temp;
            if(temp != 0){
                Succ.push_back(j);
                Weights.push_back(temp);
                idx_Succ++;
            }
        }
    }

    Head.push_back(idx_Succ);

    file.close();
}

void Graph::save_to_file(const string& filename) const {
    ofstream file(filename);
    if (!file.is_open()) {
        throw runtime_error("Cannot open file: " + filename);
    }
    
    file << num_nodes << "\n";
    for (int i = 0; i < num_nodes; ++i) {
        
        int idxStart = Head[i];
        int idxEnd = Head[i+1];
        
        if(idxStart < idxEnd){
            
            int idx = idxStart, node = 0;
            while(node < num_nodes){
                if(Succ[idx] != node){
                    file << "0 ";
                    node++;
                }else{
                    file << Weights[idx] << " ";
                    node++;
                    idx++;
                }
            }

        }else{
            for(int j = 0; j < num_nodes; j++){
                file << "0 ";
            }
        }

        if(i < num_nodes-1){
            file << "\n";
        }

    }
    file.close();
}

void Graph::print() {
    cout << "Head :\n";
    for(auto elem : Head){
        cout << elem << " ";
    }
    cout << "\n" << "Succ :\n";
    for(auto elem : Succ){
        cout << elem << " ";
    }
    cout << "\n" << "Weights :\n";
    for(auto elem : Weights){
        cout << elem << " ";
    }
    cout << "\n";
}

} // namespace fastgraphfpms