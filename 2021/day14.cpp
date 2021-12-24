#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ar array

void solve1() {
    map<string, string> rules;

    string t;
    cin >> t;

    string pair, arrow, res;
    while(cin >> pair >> arrow >> res) {
        rules[pair] = res;
    }

    for(int iter=0; iter<10; iter++) {
        for(int i=1; i<t.length(); i++) {
            t.insert(i, rules[t.substr(i-1,2)]);
            ++i;
        }
    }

    set<char> chars;
    set<int> counts;
    for(char c: t) chars.insert(c);
    for(auto it=chars.begin(); it!=chars.end(); ++it) {
        counts.insert(count(t.begin(), t.end(), *it));
    }
    cout << *counts.rbegin() - *counts.begin() << "\n";

}

void solve2() {
    map<string, string> rules;
    map<string, ll> paircounts;

    string t;
    cin >> t;
    t = "#" + t + "#";

    string pair, arrow, res;
    while(cin >> pair >> arrow >> res) {
        rules[pair] = res;
    }

    for(int i=0; i<t.length()-1; ++i) {
        ++paircounts[t.substr(i,2)];
    }

    for(int i=0; i<40; ++i) {
        map<string, ll> newpaircounts;

        for(auto const& p: paircounts) {
            /* cout << "qwert " << p.first << ", " << p.second << "\n"; */
            string key = p.first;
            if(rules.find(key) == rules.end()) {
                newpaircounts[key] = p.second;
                continue;
            }
            string pair1 = key[0] + rules[key];
            string pair2 = rules[key] + key[1];
            newpaircounts[pair1] += p.second;
            newpaircounts[pair2] += p.second;
        }
        paircounts = newpaircounts;
        
    }

    map<char, ll> lettercounts;
    for(auto const& p: paircounts) {
        lettercounts[p.first[0]] += p.second;
        lettercounts[p.first[1]] += p.second;
    }
    set<ll> sorted;
    for(auto const& l: lettercounts) {
        if (l.first == '#') continue;
        sorted.insert(l.second/2);
    }
    cout << *sorted.rbegin() - *sorted.begin() << "\n";

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    /* solve1(); */
    solve2();
}
