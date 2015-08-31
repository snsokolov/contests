// 574C_poker.cc - Codeforces.com 574C Poker program by Sergey 2015

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
// Poker Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Poker { public:

    typedef long long ll;
    ll n, m;
    vector <ll> numa, numb, nums;
    ll low;

    Poker(){

        // Reading single elements
        cin >> n;

        // Reading a single line of multiple elements
        for(int i=0; i<n; i++) {
            ll s; cin >> s; nums.push_back(s);
        }

        low = -1;    
        for(auto v: nums){
            while (v % 2 == 0) v /= 2;
            while (v % 3 == 0) v /= 3;
            if (low == -1) low = v;
            else if (v != low) { low = -1; break; }
        }

    }

    string calculate(){

        // Converting result to string
        ostringstream resstr;
        resstr << (low == -1 ? "No" : "Yes");
        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    Poker* d;

    void single_test() {

        // Constructor test
        string test = "4\n75 150 75 50";
        test_cin(test);
        d = new Poker;
        CHECK(d->n, 4);
        CHECK(d->nums[0], 75);

        // Sample test
        test_cin(test);
        CHECKS((new Poker)->calculate(), "Yes");

        // Sample test
        test_cin("3\n100 150 250");
        CHECKS((new Poker)->calculate(), "No");

        // Sample test
        test_cin("2\n3 2");
        CHECKS((new Poker)->calculate(), "Yes");

        // My test
        test_cin("");
        //CHECKS((new Poker)->calculate(), "0");

        // Time limit test
        time_limit_test(100000);
    }

    void time_limit_test(int nmax){

        ostringstream stest;

        // Random inputs
        stest << nmax << endl;
        for(int i = 0; i < nmax; i++) stest << 1274019840 << " ";

        // Run the test
        double start = dclock();
        test_cin(stest.str());
        d = new Poker;
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
    cout << (new Poker)->calculate() << endl;
    return 0;
}

