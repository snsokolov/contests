// 570D_tree.cc - Codeforces.com/problemset/problem/570/D Tree program by Sergey 2015

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
    void test_cin(cs s){ in = new istringstream(s); cin.rdbuf(in->rdbuf()); }
    void fail_hdr(cs stra, cs strb, cs file, int line, cs func) {
        serr << "==================================================" << endl;
        serr << "FAIL: " << func << endl;
        serr << "--------------------------------------------------" << endl;
        serr << "File \"" << file << "\", line " << line << " in " << func << endl;
        serr << "  Checking " << stra << " == " << strb << endl;
    }
    template <typename T> void check(T a, T b, cs stra, cs strb, cs file, int line, cs func) {
        checks++; if (a == b) { cout << "."; return; }
        fails++; cout << "F"; fail_hdr(stra, strb, file, line, func);
        serr << "  Error: \"" << a << "\" ! = \"" << b << "\"" << endl << endl;
    }
    virtual void single_test() {}
    virtual void test_list() { single_test(); }
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
// Tree Class (Main Program)
///////////////////////////////////////////////////////////////////////////////

class Node { public:
    char c;
    int num;
    vector <Node*> ch;
    int dfss, dfse, h;
};

class Tree { public:

    int n, m;
    string s;
    vector <int> nump, numv, numh;
    Node* tree;
    vector <Node*> nodes, dfs;
    vector <vector <int>> layers;
    map <pair<int, int>, bool> mem;
    int hmax;

    Tree(){

        // Reading single elements
        cin >> n;
        cin >> m;

        nump.push_back(0);
        for(int i=1; i<n; i++) {
            int p; cin >> p; p--; nump.push_back(p);
        }

        cin >> s;

        // Reading multiple lines of pair
        for(int i = 0; i<m; i++) {
            int v; cin >> v; v--; numv.push_back(v);
            int h; cin >> h; h--; numh.push_back(h);
        }

        // Building a tree
        hmax = 0;
        for(int i=0; i<n; i++) {

            // New node
            Node* tmp = new Node;
            tmp->c = (char)(s[i] - 'a');
            tmp->num = i;
            tmp->dfss = -1;
            tmp->dfse = -1;
            tmp->h = 0;
            
            // Inserting the root
            if (i == 0) { nodes.push_back(tmp); continue; }

            // Updating the height and hmax
            tmp->h = nodes[nump[i]]->h + 1;
            if (tmp->h > hmax) hmax = tmp->h;

            // Inserting the node into children vector
            nodes[nump[i]]->ch.push_back(tmp);

            // Inserting the node into nodes vector
            nodes.push_back(nodes[nump[i]]->ch.back());
        }
        tree = nodes[0];

        // DFS
        deque <Node*> st;
        st.push_front(tree);
        while (not st.empty()){

            // Pop stack
            Node* v = st.front();
            // Saving start and end pointers
            if (v->dfss == -1) {
                v->dfss = dfs.size();
                dfs.push_back(v);
            } else {
                v->dfse = dfs.size();
                st.pop_front();
                continue;
            }

            // Push stack
            for(auto vv=v->ch.rbegin(); vv !=v->ch.rend(); vv++)
                st.push_front(*vv);
        }

        // BFS
        deque <Node*> qu;
        qu.push_back(tree);
        layers.resize(hmax+1);
        while (not qu.empty()){

            // Pop queu
            Node* v = qu.front();
            // Saving start and end pointers
            layers[v->h].push_back(v->dfss);
            qu.pop_front();

            // Push queue
            for(auto vv=v->ch.begin(); vv !=v->ch.end(); vv++)
                qu.push_back(*vv);
        }

    }

    bool check(int v, int h){
        auto b = layers[h].begin(), e = layers[h].end();
        auto st  = lower_bound(b, e, nodes[v]->dfss);
        auto end = lower_bound(b, e, nodes[v]->dfse);
        unsigned int p=0;
        for(auto i=st; i!=end; i++)
            p ^= (1 << dfs[*i]->c);
        return not(p & (p-1));
    }

    string calculate(){

        // Converting result to string
        ostringstream resstr;
        
        for(int i=0; i<m; i++){
            int v = numv[i], h = numh[i];
            pair <int, int> vh = make_pair(v, h);
            if (h <= nodes[v]->h or h > hmax) resstr << "Yes";
            else {
                bool res;
                if (mem.count(vh) == 1){
                    res = mem[vh];
                } else {
                    res = check(v, h);
                    mem[vh] = res;
                }
                resstr << (res ? "Yes" : "No");
            }
            resstr << "\n";
        }

        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    Tree* d;

    void single_test() {

        // Constructor test
        string test = "6 5\n1 1 1 3 3\nzacccd\n1 1\n3 3\n4 1\n6 1\n1 2";
        test_cin(test);
        d = new Tree;
        CHECK(d->n, 6);
        CHECK(d->m, 5);
        CHECK(d->nump[4], 2);
        CHECKS(d->s, "zacccd");
        CHECK(d->numv[0], 0);
        CHECK(d->numh[0], 0);

        // Tree
        CHECK(d->nodes[5]->c, 3);
        CHECK(d->tree->num, 0);
        CHECK(d->tree->ch[1]->ch[1]->num, 5);
        CHECK(d->tree->ch[1]->ch[1]->h, 2);
        CHECK(d->dfs[4]->c, 3);
        CHECK(d->tree->dfss, 0);
        CHECK(d->tree->dfse, 6);

        // Sample test
        test_cin(test);
        //CHECKS((new Tree)->calculate(), "Yes\nNo\nYes\nYes\nYes\n");

        // Sample test
        test_cin("1 1\n\na\n1 2");
        //CHECKS((new Tree)->calculate(), "Yes\n");

        // Sample test
        test_cin("8 2\n1 1 1 2 1 1 4\ncbecdcce\n2 3\n1 3");
        CHECKS((new Tree)->calculate(), "Yes\nNo\n");

        // My test
        test_cin("");
        //CHECKS((new Tree)->calculate(), "0");

        // Time limit test
        //time_limit_test(2000);
    }

    void time_limit_test(int nmax){

        int mmax = nmax;
        ostringstream stest;

        // Random inputs
        stest << nmax << " " << mmax << endl;
        for(int i = 0; i < nmax; i++) stest << i << " " << i+1 << endl;
        for(int i = 0; i < mmax; i++) stest << rand() % 40 << " ";

        // Run the test
        double start = dclock();
        test_cin(stest.str());
        d = new Tree;
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
    cout << (new Tree)->calculate();
    return 0;
}

