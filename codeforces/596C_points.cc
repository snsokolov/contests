// 596C_points.cc - Codeforces.com/problemset/problem/596/C by Sergey 2015

#include <bits/stdc++.h>
using namespace std;

// Cppunit - C++ Unit testing TDD framework (github.com/cppunit/cppunit)
class Cppunit { public:
    #define CHECK(a,b)  check<long long>(a, b, #a, #b, __FILE__, __LINE__, __FUNCTION__);
    #define CHECKT(a)   check<bool>(a, true, #a, "true", __FILE__, __LINE__, __FUNCTION__);
    #define CHECKS(a,b) check<cs>(a, b, #a, #b, __FILE__, __LINE__, __FUNCTION__);
    typedef const std::string& cs;
    int checks, fails; std::ostringstream serr; std::istringstream *in;
    Cppunit() { checks = fails = 0;}
    void test_cin(cs s){ in = new std::istringstream(s); std::cin.rdbuf(in->rdbuf()); }
    void fail_hdr(cs stra, cs strb, cs file, int line, cs func) {
        serr << "==================================================" << std::endl;
        serr << "FAIL: " << func << std::endl;
        serr << "--------------------------------------------------" << std::endl;
        serr << "File \"" << file << "\", line " << line << " in " << func << std::endl;
        serr << "  Checking " << stra << " == " << strb << std::endl;
    }
    template <typename T> void check(T a, T b, cs stra, cs strb, cs file, int line, cs func) {
        checks++; if (a == b) { std::cout << "."; return; }
        fails++; std::cout << "F"; fail_hdr(stra, strb, file, line, func);
        serr << "  Error: \"" << a << "\" ! = \"" << b << "\"" << std::endl << std::endl;
    }
    virtual void single_test() {}
    virtual void test_list() { single_test(); }
    double dclock() { return double(clock()) / CLOCKS_PER_SEC; }
    status() {
        std::cout << std::endl; if (fails) std::cout << serr.str();
        std::cout << "--------------------------------------------------" << std::endl;
        std::cout << "Ran " << checks << " checks in " << dclock() << "s" << std::endl << std::endl;
        if (fails) std::cout << "FAILED (failures=" << fails << ")"; else std::cout << "OK" << std::endl;
        return fails > 0;
    }
    run() { std::streambuf* ocin = std::cin.rdbuf(); test_list(); std::cin.rdbuf(ocin); return status(); }
};

///////////////////////////////////////////////////////////////////////////////
// Points Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Points { public:

    typedef long long ll;
    ll n, m;
    vector <ll> nums;
    vector <lldiv_t> answ;
    unordered_multimap <ll, ll> wh;
    map <ll, ll> mr, mc;
    ll MW;

    Points(){

        MW = 100001;

        // Reading single elements
        cin >> n;

        // Reading multiple lines of pair
        for(int i=0; i<n; i++) {
            ll a; cin >> a;
            ll b; cin >> b;
            wh.insert({b - a, b * MW + a}); 
        }

        // Reading a single line of multiple elements
        for(int i=0; i<n; i++) {
            ll s; cin >> s; nums.push_back(s);
        }
    }

    string calculate(){

        ostringstream resstr;
        resstr << "YES\n";

        for(int i=0; i<n; i++) {
            
            auto pit = wh.equal_range(nums[i]);
            if (pit.first == wh.end()) return "NO\n";

            auto minit = pit.first;
            lldiv_t mind = lldiv(minit->second, MW);

            for(auto it = pit.first; it != pit.second; ++it) {
                lldiv_t d = lldiv(it->second, MW);
                if (d.quot <= mind.quot and d.rem <= mind.rem) {
                    mind = d;
                    minit = it;
                }
            }
            answ.push_back(mind);
            wh.erase(minit);
        }

        for(auto a: answ){
            auto it = mr.find(a.rem);
            if (it != mr.end())
                if (it->second > a.quot) return "NO\n";
            mr.insert({a.rem, a.quot});
        }
        for(auto a: answ){
            auto it = mc.find(a.quot);
            if (it != mc.end())
                if (it->second > a.rem) return "NO\n";
            mc.insert({a.quot, a.rem});
        }

        for(auto a: answ){
            resstr << a.rem << " " << a.quot << "\n";
        }

        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Unit tests
///////////////////////////////////////////////////////////////////////////////


class MyCppunit: public Cppunit {

    Points* d;

    void single_test() {

        // Constructor test
        string test = "5\n1 1\n2 0\n1 0\n0 0\n0 1\n0 -1 -2 1 0";
        test_cin(test);
        d = new Points;
        CHECK(d->n, 5);
        CHECK(d->nums[1], -1);

        // Sample test
        test_cin(test);
        CHECKS((new Points)->calculate(), "YES\n0 0\n1 0\n2 0\n0 1\n1 1\n");

        // Sample test
        test_cin("3\n1 0\n0 0\n2 0\n0 1 2");
        CHECKS((new Points)->calculate(), "NO\n");

        // Sample test
        test_cin("2\n0 0\n1 0\n-1 0");
        CHECKS((new Points)->calculate(), "NO\n");

        // My test
        test_cin("");
        //CHECKS((new Points)->calculate(), "0");

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
        d = new Points;
        double calc = dclock();
        d->calculate();
        double stop = dclock();
        cout << endl << "Timelimit Test: " << stop - start << "s (init ";
        cout << calc - start << "s calc " << stop - calc << "s)" << endl;
    }
};


int main(int argc, char *argv[]) {

    // Faster cin and cout
    ios_base::sync_with_stdio(0);cin.tie(0);

    if (argc > 1 && !strcmp(argv[1], "-ut"))
        return (new MyCppunit)->run();

    cout << (new Points)->calculate();
    return 0;
}

