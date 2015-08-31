// 572C_sticks.cc - Codeforces.com/problemset/problem/572/C Sticks program by Sergey 2015

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
// Sticks Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Sticks { public:

    typedef long long ll;
    ll a, b, c, l;
    vector <ll> sums, trg;

    Sticks(){

        // Reading single elements
        cin >> a >> b >> c >> l;

        // Precalucalating regular and rotated triangle sums
        for(ll i=0; i<=l+1; i++) {
            sums.push_back((i*(i+1))/2);
            trg.push_back(sums[(int)i/2]*2 + (i%2)*(i/2+1));
        }
    }

    ll cnt(ll ai, ll bi, ll ci, ll li) {
        if (li <= ci-ai-bi) return 0;
        ll result = 0;
        result += sums[(int)(li+1)];
        if (ci > ai+bi-1) result -= sums[(int)(ci-ai-bi+1)];
        if (li > ci+ai-bi-1) result -= trg[(int)(li-ci-ai+bi+1)];
        if (li > ci-ai+bi-1) result -= trg[(int)(li-ci+ai-bi+1)];
        return result;
    }

    string calculate(){

        ll result = 0;
        if (a > c) swap(a, c);
        if (b > c) swap(b, c);
        for(ll i=0; i<=l; i++) result += cnt(a, b, c+i, l-i);

        // Converting result to string
        ostringstream resstr;
        resstr << result;
        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    Sticks* d;

    void single_test() {

        // Constructor test
        string test = "1 1 1 2";
        test_cin(test);
        d = new Sticks;
        CHECK(d->a, 1);
        CHECK(d->b, 1);
        CHECK(d->trg[2], 2);
        
        // Count subprolem for one level of C
        CHECK(d->cnt(1, 1, 1, 2), 2)
        CHECK(d->cnt(1, 1, 3, 0), 0)

        // Sample test
        test_cin(test);
        CHECKS((new Sticks)->calculate(), "4");

        // Sample test
        test_cin("1 2 3 1");
        CHECKS((new Sticks)->calculate(), "2");

        // Sample test
        test_cin("10 2 1 7");
        CHECKS((new Sticks)->calculate(), "0");

        // My test
        test_cin("1 2 1 5");
        CHECKS((new Sticks)->calculate(), "20");

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
        d = new Sticks;
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
    cout << (new Sticks)->calculate() << endl;
    return 0;
}

