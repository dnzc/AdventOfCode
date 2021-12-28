#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

const int I_MAX = ~0U >> 1;

int solve(vector<vector<int>> grid) {
    int v = grid.size() * grid[0].size();
    vector< vector< pair<int, int> > > g(v); // node, dist
    
    // turn grid into adjacency list
    for(int y=0; y<grid.size(); ++y) {
        for(int x=0; x<grid[0].size(); ++x) {
            if(x>0) {
                g[y*grid.size()+x-1].emplace_back(y*grid.size()+x, grid[y][x]);
                g[y*grid.size()+x].emplace_back(y*grid.size()+x-1, grid[y][x-1]);
            }
            if(y>0) {
                g[(y-1)*grid.size()+x].emplace_back(y*grid.size()+x, grid[y][x]);
                g[y*grid.size()+x].emplace_back((y-1)*grid.size()+x, grid[y-1][x]);
            }
        }
    }

    // dijkstra
    vector<int> dist; // dist from start node
    auto shortestPath = [&](int start) {
        dist = vector<int>(v, I_MAX);
        priority_queue< pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > pq; // dist, node
        vector<bool> seen(v);
        dist[start] = 0;
        pq.emplace(0, start);
        while(!pq.empty()) {
            int node = pq.top().second;
            pq.pop();
            if(seen[node]) continue;
            seen[node] = true;

            for( pair<int, int> child: g[node]) {
                int d = dist[node] + child.second;
                if(!seen[child.first] && d < dist[child.first]) {
                    dist[child.first] = d;
                    pq.emplace(d, child.first);
                }
            }
        }
    };
    shortestPath(0);
    return dist[v-1];
}

void solve1() {
    string s;
    vector< vector<int> > grid;
    while(cin >> s) {
        vector<int> row;
        for(char c: s) row.emplace_back(c - '0');
        grid.emplace_back(row);
    }
    cout << solve(grid) << "\n";
}

string shift(string in, int n) {
    string out = "";
    for(char c: in)
        out += (c-'0' -1 + n)%9 + 1 + '0';
    return out;
}

void solve2() {
    string s;
    vector<string> grids[5];
    while(cin >> s) {
        string row = "";
        for(int i=0; i<5; ++i) row += shift(s, i);
        for(int i=0; i<5; ++i)
            grids[i].emplace_back(shift(row, i));
    }

    vector<string> cgrid;
    for(int i=0; i<5; ++i) {
        for(auto j: grids[i]) cgrid.emplace_back(j);
    }

    vector<vector<int>> grid;
    for(string s: cgrid) {
        vector<int> row;
        for( char c: s) row.emplace_back(c-'0');
        grid.emplace_back(row);
    }
    cout << solve(grid) << "\n";
}

int main() {
    /* ios::sync_with_stdio(0); */
    /* cin.tie(0); */
    solve2();
}
