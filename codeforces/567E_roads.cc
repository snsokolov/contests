// 567E_roads.cc - Codeforces.com/problemset/problem/567/E Roads program by Sergey 2015

#include <bits/stdc++.h>
using namespace std;

///////////////////////////////////////////////////////////////////////////////
// Unit tests base Class
///////////////////////////////////////////////////////////////////////////////


class Unittest { public:
    #define CHECK(a,b)  check<long long>(a, b, #a, #b, __FILE__, __LINE__, __FUNCTION__);
    #define CHECKT(a)   check<int>(a, 1, #a, "true", __FILE__, __LINE__, __FUNCTION__);
    #define CHECKS(a,b) check<cs>(a, b, #a, #b, __FILE__, __LINE__, __FUNCTION__);
    typedef const string& cs;
    int checks, fails; ostringstream serr; istringstream *in;
    Unittest() { checks = fails = 0;}
    test_cin(cs s){ in = new istringstream(s); cin.rdbuf(in->rdbuf()); }
    fail_hdr(cs stra, cs strb, cs file, int line, cs func) {
        serr << "==================================================" << endl;
        serr << "FAIL: " << func << endl;
        serr << "--------------------------------------------------" << endl;
        serr << "File \"" << file << "\", line " << line << " in " << func << endl;
        serr << "  Checking " << stra << " == " << strb << endl;
    }
    template <typename T> check(T a, T b, cs stra, cs strb, cs file, int line, cs func) {
        checks++; if (a == b) { cout << "."; return 0; }
        fails++; cout << "F"; fail_hdr(stra, strb, file, line, func);
        serr << "  Error: \"" << a << "\" ! = \"" << b << "\"" << endl << endl;
    }
    virtual single_test() {}
    virtual test_list() { single_test(); }
    double dclock() { return double(clock()) / CLOCKS_PER_SEC; }
    status() {
        cout << endl; if (fails) cout << serr.str();
        cout << "--------------------------------------------------" << endl;
        cout << "Ran " << checks << " checks in " << dclock() << "s" << endl << endl;
        if (fails) cout << "FAILED (failures=" << fails << ")"; else cout << "OK" << endl;
        return fails > 0;
    }
    run() { streambuf* ocin = cin.rdbuf(); test_list(); cin.rdbuf(ocin); return status(); }
};


///////////////////////////////////////////////////////////////////////////////
// Modulo Hash Class
///////////////////////////////////////////////////////////////////////////////


class Modh { public:
    typedef long long ll;
    vector<ll> val;
    ll MOD[4];
    static const int NMOD = 2; // Can be up to 4

    Modh(ll x=0): MOD {(ll)1e9+2277, (ll)1e9+5277, (ll)1e9+8277, (ll)1e9+9277} {
        for(int i=0; i<NMOD; i++) val.push_back(x);
    }
    void operator += (const Modh &x) {
         for(int i=0; i<NMOD; i++) { 
            val[i] += x.val[i];
            if (val[i] >= MOD[i]) val[i] -= MOD[i];
        }
    }
    Modh operator * (const Modh &x) const {
        Modh res;
        for(int i=0; i<NMOD; i++) res.val[i] = (val[i] * x.val[i]) % MOD[i];
        return res;
    }
    bool operator == (const Modh &x) const {
        for(int i=0; i<NMOD; i++) if (val[i] != x.val[i]) return false;
        return true;
    }
};


///////////////////////////////////////////////////////////////////////////////
// Graph Class
///////////////////////////////////////////////////////////////////////////////


class Graph { public:

    typedef long long ll;
    typedef pair<ll, ll> pll;
    const ll INF = 1e18;

    vector<vector<pll>> G; // Weighted graph adjacency list
    vector<pll> E; // Edge indexes in the adjacency list

    init(ll n) { G.resize(n+1); }

    add(ll a, ll b, ll w=0) { 
        G[a].push_back(make_pair(b, w));
        E.push_back(make_pair(a, G[a].size()-1));
    }

    ll min_dist(ll a, ll b){ return dijkstra(a)[b]; }

    ll adj_dist(ll a, ll b) { 
        for(pll e: G[a]) if(e.first == b) return e.second;
        return INF;
    }

    vector<ll> dijkstra(ll a) {
        vector<ll> dist(G.size(), INF);
        vector<bool> visited(G.size());
        priority_queue<pll, vector<pll>, greater<pll>> bestq;
        bestq.push(make_pair(0, a));
        dist[a] = 0;
        while (true) {
            if (bestq.empty()) break;
            pll best = bestq.top(); bestq.pop();
            if (visited[best.second]) continue; else visited[best.second] = true;
            for(pll e: G[best.second]) {
                if(dist[e.first] <= dist[best.second] + e.second) continue;
                dist[e.first] = dist[best.second] + e.second;
                bestq.push(make_pair(dist[e.first], e.first));
            }
        }
        return dist;
    }

    vector<Modh> dijkstra_paths(ll a) {
        vector<ll> dist(G.size(), INF);
        vector<Modh> paths(G.size(), 0);
        vector<bool> visited(G.size());
        priority_queue<pll, vector<pll>, greater<pll>> bestq;
        bestq.push(make_pair(0, a));
        dist[a] = 0;
        paths[a] = 1;
        while (true) {
            if (bestq.empty()) break;
            pll best = bestq.top(); bestq.pop();
            if (visited[best.second]) continue; else visited[best.second] = true;
            for(pll e: G[best.second]) {
                if (dist[e.first] <= dist[best.second] + e.second) {
                    if (dist[e.first] == dist[best.second] + e.second)
                        paths[e.first] += paths[best.second];
                    continue;
                }
                dist[e.first] = dist[best.second] + e.second;
                paths[e.first] = paths[best.second];
                bestq.push(make_pair(dist[e.first], e.first));
            }
        }
        return paths;
    }
};


///////////////////////////////////////////////////////////////////////////////
// Roads Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Roads { public:

    long long n, m, s, t;
    vector <long long> numa, numb, numw;

    Graph G, GI;
    vector <long long> D, DI;
    vector <Modh> P, PI;

    Roads(){

        // Reading single elements
        cin >> n >> m >> s >> t;
        G.init(n);
        GI.init(n);

        // Reading multiple lines of pair
        for(int i = 0; i < m; i++) {
            long long a, b, w;
            cin >> a; numa.push_back(a);
            cin >> b; numb.push_back(b);
            cin >> w; numw.push_back(w);
            G.add(a, b, w);
            GI.add(b, a, w);
        }

        D = G.dijkstra(s);
        DI = GI.dijkstra(t);

        P = G.dijkstra_paths(s);
        PI = GI.dijkstra_paths(t);
    }

    string calculate(){

        // Result calculation
        ostringstream resstr;

        for(int i=0; i<m; i++) {
            long long a = numa[i], b = numb[i], w = numw[i];

            if (D[a] >= G.INF or DI[b] >= G.INF) resstr << "NO" << endl;
            else if ((D[a] + DI[b] + w == D[t]) and (P[a] * PI[b]) == P[t]) resstr << "YES" << endl;
            else if ((D[t] - 1 - D[a] - DI[b]) < 1) resstr << "NO" << endl;
            else resstr << "CAN " << w - (D[t] - 1 - D[a] - DI[b]) << endl;
        }

        // Converting result to string
        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    Roads* d;

    single_test() {

        // Constructor test
        string test = "6 7 1 6\n1 2 2\n1 3 10\n2 3 7\n2 4 8\n3 5 3\n4 5 2\n5 6 1";
        test_cin(test);
        d = new Roads;
        CHECK(d->n, 6);
        CHECK(d->m, 7);
        CHECK(d->s, 1);
        CHECK(d->t, 6);
        CHECK(d->numa[0], 1);
        CHECK(d->numb[0], 2);
        CHECK(d->numw[0], 2);
        CHECK(d->G.G[1][1].first, 3);

        // Graph tests
        Graph G;
        G.init(6);
        G.add(1, 2, 2);
        G.add(2, 6, 4);
        CHECK(G.min_dist(1, 6), 6);
        CHECK(G.adj_dist(1, 6), G.INF);
        CHECK(G.adj_dist(2, 6), 4);

        // Sample test
        test_cin(test);
        CHECKS((new Roads)->calculate(), "YES\nCAN 2\nCAN 1\nCAN 1\nCAN 1\nCAN 1\nYES\n");

        // Sample test
        test_cin("3 3 1 3\n1 2 10\n2 3 10\n1 3 100");
        CHECKS((new Roads)->calculate(), "YES\nYES\nCAN 81\n");

        // Sample test
        test_cin("2 2 1 2\n1 2 1\n1 2 2");
        CHECKS((new Roads)->calculate(), "YES\nNO\n");

        // My test
        test_cin("");
        //CHECKS((new Roads)->calculate(), "0");

        // Time limit test
        time_limit_test(10000);
    }

    time_limit_test(int m){

        int n = 1000;
        ostringstream stest;

        // Random inputs
        stest << n << " " << m << " " << 1 << " " << n-1 << endl;
        for(int i = 0; i < m; i++) {
            int ra = rand() % n;
            int rb = rand() % n;
            while (ra == rb) ra = rand() % n; 
            stest << ra << " " << rb << " " << i%4+1 << endl;
        }

        // Run the test
        double start = dclock();
        test_cin(stest.str());
        d = new Roads;
        double calc = dclock();
        d->calculate();
        double stop = dclock();
        cout << endl << "Timelimit Test: " << stop - start << "s (init ";
        cout << calc - start << "s calc " << stop - calc << "s)" << endl;
    }
};

///////////////////////////////////////////////////////////////////////////////
// Main Execution
///////////////////////////////////////////////////////////////////////////////


int main(int argc, char *argv[]) {

    // Faster cin and cout
    ios_base::sync_with_stdio(0);cin.tie(0);

    if (argc > 1 && !strcmp(argv[1], "-ut")) {
        LocalUnittest lut;
        return lut.run();
    }
    cout << (new Roads)->calculate() << endl;
    return 0;
}

