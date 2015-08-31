// 566D_restruct.cc - Codeforces.com 566D Restruct program by Sergey 2015

// All standard modules
#include <bits/stdc++.h>

using namespace std;


///////////////////////////////////////////////////////////////////////////////
// Disjoint Set Class
///////////////////////////////////////////////////////////////////////////////


class DisjointSet{ public:

    vector<int> root;

    void init(int n) { root.resize(n+1); for(int i=1; i<=n; i++) root[i] = i; }

    void join(int a, int b) { root[find(b)] = find(a); }

    int find(int a){ return a == root[a] ? a : root[a] = find(root[a]); }

    bool check(int a, int b){ return find(a) == find(b); }
};


///////////////////////////////////////////////////////////////////////////////
// Restruct Class
///////////////////////////////////////////////////////////////////////////////


class Restruct { public:

    static int const N = 200001;
    static int const Q = 500001;

    int nmax;
    int nums[N];

    int qmax;
    int numq[Q], numa[Q], numb[Q];

    map <int, int> nmap;
    DisjointSet ds;

    Restruct(){

        // Decoding input max sizes
        cin >> nmax;
        if (nmax > N) {
            cout << "FATAL: Increase N to " << nmax << endl; exit(1);
        }

        cin >> qmax;
        if (qmax > Q) {
            cout << "FATAL: Increase Q to " << qmax << endl; exit(1);
        }

        // Decoding input pairs
        for(int i = 0; i < qmax; i++) cin >> numq[i] >> numa[i] >> numb[i];

        for(int i = 1; i < nmax+1; i++) {
            nmap[i] = i;
        }

        ds.init(nmax);
    }

    merge(int i, int j){
        if (i == j) return 1;
        auto vi = --nmap.upper_bound(i);
        auto vj = --nmap.upper_bound(j);
        ds.join(vj->second, vi->second);
    }

    join(int i, int j){
        if (i == j) return 1;
        auto vi = --nmap.upper_bound(i);
        auto vj = nmap.upper_bound(j);
        for(auto it=vi; it!=vj; it++){
            ds.join(vi->second, it->second);
        }
        nmap.erase(++vi, vj);
    }

    check(int i, int j){
        if (i == j) return 1;
        auto vi = --nmap.upper_bound(i);
        auto vj = --nmap.upper_bound(j);
        return ds.check(vj->second, vi->second);
    }

    string calculate(){

        ostringstream resstr;

        for(int i=0;i < qmax; i++){
            int a = numa[i];
            int b = numb[i];
            if (a > b) swap (a, b);

            if (numq[i] == 1){
                merge(a,b);
            }
            if (numq[i] == 2){
                join(a, b);
            }
            if (numq[i] == 3){
                int result = check(a, b);
                string out = result ? "YES" : "NO";
                resstr << out << endl;
            }
            // cout << i << " " << numq[i] << " " << a << " " << b << endl;
            // for(auto it=nmap.begin(); it!=nmap.end(); it++) cout << it->first << "=>" << *it->second << endl;
        }

        return resstr.str();
    }
};


///////////////////////////////////////////////////////////////////////////////
// Restruct Class test helping functions
///////////////////////////////////////////////////////////////////////////////

Restruct* class_wrap_input(const string& test="") {

    streambuf* orig = cin.rdbuf();
    istringstream input(test);
    if (test != "") {
        cin.rdbuf(input.rdbuf());
    };
    Restruct* d = new Restruct();
    if (test != "") cin.rdbuf(orig);    
    return d;
}

string calculate(const string& test="") {
    Restruct* d = class_wrap_input(test);
    string result = d->calculate();
    delete d;
    return result;
}

///////////////////////////////////////////////////////////////////////////////
// Unit tests base Class
///////////////////////////////////////////////////////////////////////////////


class Unittest { public:

    #define CHECK(a, b)\
        test_fail_err(a, b, #a, #b, __FILE__, __LINE__, __FUNCTION__);
    #define CHECKT(a)\
        test_fail_err(a, 1, #a, "true", __FILE__, __LINE__, __FUNCTION__);
    #define CHECKS(a, b)\
        test_fail_errs(a, b, #a, #b, __FILE__, __LINE__, __FUNCTION__);

    int test_cnt, fail_cnt, fail;
    string status, fail_msg;

    Unittest() {
        test_cnt = fail_cnt = fail = 0;
        status = "OK";
    }

    // Override this function in derived class
    virtual test_list() {
        test_basic();
        test_done();
    }

    test_basic() { CHECKT("Base class basic test" == ""); }

    run() {
        test_list();
        double elp_secs = double(clock()) / CLOCKS_PER_SEC;
        cout << endl;
        if (fail_cnt > 0) cout << fail_msg;
        cout << "--------------------------------------------------" << endl;
        cout << "Ran " << test_cnt << " tests in " << elp_secs << "s" << endl;
        cout << endl;
        if (fail_cnt > 0) cout << "FAILED (failures=" << fail_cnt << ")";
        else cout << status << endl;
        if (fail_cnt > 0) return 1;
    }

    test_fail_hdr(const string& stra, const string& strb,
            const string& file, int line, const string& function) {
        fail_cnt ++;
        fail = 1;
        ostringstream msg;
        msg << "==================================================" << endl;
        msg << "FAIL: " << function << endl;
        msg << "--------------------------------------------------" << endl;
        msg << "File \"" << file << "\", line " << line;
        msg << " in " << function << endl;
        msg << "  Checking " << stra << " == " << strb << endl;
        fail_msg += msg.str();
    }

    test_fail_err(long long a, long long b,
            const string& stra, const string& strb,
            const string& file, int line, const string& function) {
        if (a == b) return 0;
        test_fail_hdr(stra, strb, file, line, function);
        ostringstream msg;
        msg << "  Error: " << a << " ! = " << b << endl << endl;
        fail_msg += msg.str();
    }

    test_fail_errs(const string& a, const string& b,
            const string& stra, const string& strb,
            const string& file, int line, const string& function) {
        if (a == b) return 0;
        test_fail_hdr(stra, strb, file, line, function);
        ostringstream msg;
        msg << "  Error: \"" << a << "\" ! = \"" << b << "\"" << endl;
        msg << endl;
        fail_msg += msg.str();
    }

    test_done() {
        test_cnt ++;
        if (fail == 0) cout << ".";
        else cout << "F";
        fail = 0;
    }
};


///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    test_list() {
        test_class_basic_functions();
        test_done();
        test_sample_tests();
        test_done();
        //test_time_limit_test();
        test_done();
    }

    test_class_basic_functions() {

        // Constructor test
        string test = "8 6\n3 2 5\n1 2 5\n3 2 5\n2 4 7\n2 1 2\n3 1 7";
        Restruct* d = class_wrap_input(test);
        CHECK(d->nmax, 8);
        CHECK(d->qmax, 6);
        CHECK(d->numq[0], 3);

        CHECK(d->nmap[2], 2);
        d->merge(2, 4);
        CHECK(d->nmap[4], 4);
        d->merge(2, 3);
        d->merge(1, 3);
        CHECK(d->nmap[2], 2);

        d->join(1, 4);
        d->join(6, 8);

        // Sample test 1
        d = class_wrap_input(test);
        string result = d->calculate();
        CHECKS(result, "NO\nYES\nYES\n");

        // Disjoint set
        DisjointSet ds;
        ds.init(4);
        ds.join(1, 3);
        CHECK(ds.find(3), 1);
        CHECK(ds.find(2), 2);
        ds.join(3, 2);
        CHECKT(ds.check(2, 1));

        int nmax = 500000;
        ds.init(nmax);
        for (int i=0; i<nmax; i++) {
            int r = rand() % 10;
            if (r == 0) ds.find(rand() % nmax);
            if (r > 0) ds.join(rand() % nmax, rand() % nmax);
        }
    }

    test_sample_tests() {

        string test;

        // Sample test 2
        test = "";
        // CHECKS(calculate(test), "0");

        // My test
        test = "20 34\n3 2 8\n3 19 18\n2 11 16\n1 12 13\n1 19 16\n3 6 20\n1 3 13\n3 5 2\n";
        test += "1 12 20\n3 14 7\n2 13 17\n2 13 16\n1 15 1\n1 8 12\n1 17 13\n2 3 15\n";
        test += "2 14 14\n2 12 13\n2 6 14\n2 10 20\n1 1 4\n3 7 8\n3 5 13\n1 8 13\n2 4 6\n";
        test += "2 1 14\n1 17 8\n3 1 16\n3 4 17\n3 14 16\n2 5 5\n1 20 10\n3 3 6\n3 3 5\n";
        //CHECKS(calculate(test), "0");
    }

    test_time_limit_test() {

        int nmax = 10000;
        int qmax = nmax;
        string test;
        ostringstream o_test;
        
        o_test << nmax << " " << qmax << endl;
        for(int i = 0; i < qmax; i++) o_test << i << " " << i+1 << endl;
        for(int i = 0; i < qmax; i++) o_test << i << " " << i+1 << endl;
        for(int i = 0; i < qmax; i++) o_test << i << " " << i+1 << endl;
        test = o_test.str();

        double start = double(clock()) / CLOCKS_PER_SEC;
        Restruct* d = class_wrap_input(test);

        double calc = double(clock()) / CLOCKS_PER_SEC;
        d->calculate();

        double stop = double(clock()) / CLOCKS_PER_SEC;
        cout << "Time Test: " << stop - start << "s (input " << calc - start;
        cout << "s calc " << stop - calc << "s)" << endl;
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
    cout << calculate() << endl;
    return 0;
}

