// 567B_lib.cc - Codeforces.com/problemset/problem/567/B Lib program by Sergey 2015

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
    int run() { streambuf* ocin = cin.rdbuf(); test_list(); cin.rdbuf(ocin); return status(); }
    virtual void test_list() { single_test(); }
    virtual void single_test() {}
    void test_cin(cs s){ in = new istringstream(s); cin.rdbuf(in->rdbuf()); }
    template <typename T> int check(T a, T b, cs stra, cs strb, cs file, int line, cs func) {
        checks++; if (a == b) { cout << "."; return 0; }
        fails++; cout << "F"; hdr(stra, strb, file, line, func);
        serr << "  Error: \"" << a << "\" ! = \"" << b << "\"" << endl << endl;
    }
    void hdr(cs stra, cs strb, cs file, int line, cs func) {
        serr << "==================================================" << endl;
        serr << "FAIL: " << func << endl;
        serr << "--------------------------------------------------" << endl;
        serr << "File \"" << file << "\", line " << line << " in " << func << endl;
        serr << "  Checking " << stra << " == " << strb << endl;
    }
    int status() {
        cout << endl; if (fails) cout << serr.str();
        cout << "--------------------------------------------------" << endl;
        cout << "Ran " << checks << " checks in " << dclock() << "s" << endl << endl;
        if (fails) cout << "FAILED (failures=" << fails << ")"; else cout << "OK" << endl;
        return fails > 0;
    }
    double dclock() { return double(clock()) / CLOCKS_PER_SEC; }
};

///////////////////////////////////////////////////////////////////////////////
// Lib Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Lib { public:

    static int const N = 101;
    static int const P = 1000001;

    int nmax;
    string stra[N];
    int numa[N];
    int numb[N];

    int lib[P];

    Lib(){

        // Decoding input max sizes
        cin >> nmax;

        // Check
        if (nmax > N) cout << "FATAL: Increase N to " << nmax << endl;

        // Decoding input pairs
        for(int i = 0; i < nmax; i++) {
            cin >> stra[i] >> numb[i];
            numa[i] = (stra[i] == "+") ? 1 : -1;
        }

        for(int i = 0; i < P; i++) lib[i] = 0;

    }

    string calculate(){

        int max_cap = 0;
        int cap = 0;
        for(int i=0; i < nmax; i++){
            int ev = numa[i];
            int p = numb[i];
            int libstat = lib[p];
            if (ev == -1 and libstat == 0) max_cap++;
            else if (ev == -1 and libstat == 1) { cap--; lib[p] = 0; }
            else if (ev == 1 and libstat == 0) { cap++; lib[p] = 1; }
            else cout << "Error!";
            if (cap > max_cap) max_cap = cap;
        }

        ostringstream resstr;
        resstr << max_cap;

        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    Lib* d;

    void single_test() {

        // Constructor test
        string test = "6\n+ 12001\n- 12001\n- 1\n- 1200\n+ 1\n+ 7";
        test_cin(test);
        d = new Lib;
        CHECK(d->nmax, 6);
        CHECK(d->numa[0], 1);
        CHECK(d->numa[1], -1);
        CHECK(d->numb[0], 12001);

        // Sample test
        test_cin(test);
        CHECKS((new Lib)->calculate(), "3");

        // Sample test
        test_cin("2\n- 1\n- 2");
        CHECKS((new Lib)->calculate(), "2");

        // Sample test
        test_cin("2\n+ 1\n- 1");
        CHECKS((new Lib)->calculate(), "1");

        // My test
        test_cin("5\n+ 3\n- 1\n+ 1\n- 2\n+ 2");
        CHECKS((new Lib)->calculate(), "3");

        // Time limit test
        // time_limit_test(10000);
    }

    void time_limit_test(int nmax){

        int smax = nmax;
        ostringstream stest;

        // Random inputs
        stest << nmax << " " << smax << endl;
        for(int i = 0; i < nmax; i++) stest << i << " " << i+1 << endl;
        for(int i = 0; i < smax; i++) stest << i * 5 % 40 << " ";

        // Run the test
        double start = dclock();
        test_cin(stest.str());
        d = new Lib;
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
    cout << (new Lib)->calculate() << endl;
    return 0;
}

