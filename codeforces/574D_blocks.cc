// 574D_blocks.cc - Codeforces.com/problemset/problem/574/D Blocks program by Sergey 2015

#include <bits/stdc++.h>
using namespace std;

// CPlusPlusUnit - C++ Unit testing TDD framework (github.com/cppunit/cppunit)
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
    int status() {
        std::cout << std::endl; if (fails) std::cout << serr.str();
        std::cout << "--------------------------------------------------" << std::endl;
        std::cout << "Ran " << checks << " checks in " << dclock() << "s" << std::endl << std::endl;
        if (fails) std::cout << "FAILED (failures=" << fails << ")"; else std::cout << "OK" << std::endl;
        return fails > 0;
    }
    int run() { std::streambuf* ocin = std::cin.rdbuf(); test_list(); std::cin.rdbuf(ocin); return status(); }
};

///////////////////////////////////////////////////////////////////////////////
// Blocks Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Blocks { public:

    typedef long long ll;
    int n, m;
    vector <int> nums, left, right;
    int mmax;

    Blocks(){

        // Reading single elements
        cin >> n;

        // Reading a single line of multiple elements
        mmax = 0;
        for(int i=0; i<n; i++) {
            int s; cin >> s; nums.push_back(s);
        }
    }

    string calculate(){

        for(int i=0; i<n; i++) 
            left.push_back(min(i == 0 ? 1 : left[i-1]+1, nums[i]));
        for(int i=0; i<n; i++) 
            right.push_back(min(i == 0 ? 1 : right[i-1]+1, nums[n-i-1]));
        for(int i=0; i<n; i++) 
            mmax = max(mmax, min(left[n-i-1], right[i]));

        // Converting result to string
        ostringstream resstr;
        resstr << mmax;
        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Unit tests
///////////////////////////////////////////////////////////////////////////////


class MyCppunit: public Cppunit {

    Blocks* d;

    void single_test() {

        // Constructor test
        string test = "6\n2 1 4 6 2 2";
        test_cin(test);
        d = new Blocks;
        CHECK(d->n, 6);
        CHECK(d->nums[0], 2);

        // Sample test
        test_cin(test);
        CHECKS((new Blocks)->calculate(), "3");

        // Sample test
        test_cin("7\n3 3 3 1 3 3 3");
        CHECKS((new Blocks)->calculate(), "2");

        // Sample test
        test_cin("5\n0 1 2 1 0");
        CHECKS((new Blocks)->calculate(), "2");

        // My test
        test_cin("");
        //CHECKS((new Blocks)->calculate(), "0");

        // Time limit test
        time_limit_test(100000);
    }

    void time_limit_test(int nmax){

        ostringstream stest;

        // Random inputs
        stest << nmax << endl;
        for(int i = 0; i < nmax; i++) stest << 1000000000 << " ";

        // Run the test
        double start = dclock();
        test_cin(stest.str());
        d = new Blocks;
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

    cout << (new Blocks)->calculate() << endl;
    return 0;
}

