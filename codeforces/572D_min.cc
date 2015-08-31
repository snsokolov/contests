// 572D_min.cc - Codeforces.com/problemset/problem/572/D Min program by Sergey 2015

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
// Min Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Min { public:

    typedef long long ll;
    ll n, k;
    vector <ll> nums;
    vector <vector <ll>> dp; // dp[L][S]

    Min(){

        // Reading single elements
        cin >> n;
        cin >> k;

        // Reading a single line of multiple elements
        for(int i=0; i<n; i++) {
            ll s; cin >> s; nums.push_back(s);
        }
        sort(nums.begin(), nums.end());

        for(int l=0; l<=n%k; l++){
            vector <ll> tmp;
            dp.push_back(tmp);
            for(int s=0; s<=(k-(n%k)); s++){
                int len = (int)(n/k);
                int end = (s + l)*len + l - 1;
                ll res = 0, ress = 1e18, resl = 1e18;
                if (s != 0) ress = dp[l][s-1] + nums[end] - nums[end-len+1];
                if (l != 0) resl = dp[l-1][s] + nums[end] - nums[end-len];
                res = min(ress, resl);
                if (s == 0 and l == 0) res = 0;
                dp[l].push_back(res);
            }
        }
    }

    string calculate(){

        // Result calculation
        ll result = dp[(int)(n%k)][(int)(k-(n%k))];

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

    Min* d;

    void single_test() {

        // Constructor test
        string test = "3 2\n1 2 4";
        test_cin(test);
        d = new Min;
        CHECK(d->n, 3);
        CHECK(d->k, 2);
        CHECK(d->nums[0], 1);

        // Sample test
        test_cin(test);
        CHECKS((new Min)->calculate(), "1");

        // Sample test
        test_cin("5 2\n3 -5 3 -5 3");
        CHECKS((new Min)->calculate(), "0");

        // Sample test
        test_cin("6 3\n4 3 4 3 2 5");
        CHECKS((new Min)->calculate(), "3");

        // My test
        test_cin("");
        //CHECKS((new Min)->calculate(), "0");

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
        d = new Min;
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
    cout << (new Min)->calculate() << endl;
    return 0;
}

