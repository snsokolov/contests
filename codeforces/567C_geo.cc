// 567C_geo.cc - Codeforces.com 567C Geo program by Sergey 2015

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
    run() { streambuf* ocin = cin.rdbuf(); test_list(); cin.rdbuf(ocin); return status(); }
    virtual test_list() { single_test(); }
    virtual single_test() {}
    test_cin(cs s){ in = new istringstream(s); cin.rdbuf(in->rdbuf()); }
    template <typename T> check(T a, T b, cs stra, cs strb, cs file, int line, cs func) {
        checks++; if (a == b) { cout << "."; return 0; } 
        fails++; cout << "F"; hdr(stra, strb, file, line, func);
        serr << "  Error: \"" << a << "\" ! = \"" << b << "\"" << endl << endl;
    }
    hdr(cs stra, cs strb, cs file, int line, cs func) {
        serr << "==================================================" << endl;
        serr << "FAIL: " << func << endl;
        serr << "--------------------------------------------------" << endl;
        serr << "File \"" << file << "\", line " << line << " in " << func << endl;
        serr << "  Checking " << stra << " == " << strb << endl;
    }
    status() {
        cout << endl; if (fails) cout << serr.str();
        cout << "--------------------------------------------------" << endl;
        cout << "Ran " << checks << " checks in " << dclock() << "s" << endl << endl;
        if (fails) cout << "FAILED (failures=" << fails << ")"; else cout << "OK" << endl;
        return fails > 0;
    }
    double dclock() { return double(clock()) / CLOCKS_PER_SEC; }
};

///////////////////////////////////////////////////////////////////////////////
// Geo Class (Main Program)
///////////////////////////////////////////////////////////////////////////////



class Geo { public:

    static int const N = 300001;

    int nmax;
    int k;
    int nums[N];

    unordered_map <long long, long long> p1, p2, p3;

    Geo(){

        // Decoding input max sizes
        cin >> nmax;
        cin >> k;

        // Decoding input list
        for(int i = 0; i < nmax; i++) cin >> nums[i];
    }

    string calculate(){

        long long result = 0;

        for (int i = 0; i < nmax; i++) {
            long long x = nums[i];
            long long dvd, div;

            dvd = (long long)k * k;
            div = x / dvd;
            if ((div != 0 or x == 0) and (x % dvd == 0)) p3[div] += p2[div];
            dvd = k;
            div = x / dvd;
            if ((div != 0 or x == 0) and (x % dvd == 0)) p2[div] += p1[div];
            p1[x] += 1;
        }

        for (auto it = p3.begin(); it != p3.end(); ++it) result += it->second;

        ostringstream resstr;
        resstr << result;

        return resstr.str();
    }
};


///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    Geo* d;

    single_test() {

        // Constructor test
        string test = "5 2\n1 1 2 2 4";
        test_cin(test);
        d = new Geo;
        CHECK(d->nmax, 5);
        CHECK(d->nums[0], 1);

        // Sample test
        test_cin(test);
        CHECKS((new Geo)->calculate(), "4");

        // Sample test
        test_cin("");
        //CHECKS((new Geo)->calculate(), "0");

        // Sample test
        test_cin("3 1\n1 1 1");
        CHECKS((new Geo)->calculate(), "1");

        // Sample test
        test_cin("10 3\n1 2 6 2 3 6 9 18 3 9");
        CHECKS((new Geo)->calculate(), "6");

        // My tests
        test_cin("12 2\n0 0 -1 -1 -4 -2 -1 -2 -1 -4 -8 -1");
        CHECKS((new Geo)->calculate(), "7");

        test_cin("4 1\n-3 -3 -3 -3");
        CHECKS((new Geo)->calculate(), "4");

        test_cin("3 110000\n1 110000 -784901888");
        CHECKS((new Geo)->calculate(), "0");

        // Time limit test
        // time_limit_test(10000);
    }

    time_limit_test(int nmax){

        int smax = nmax;
        ostringstream stest;
        
        // Random inputs
        stest << nmax << " " << smax << endl;
        for(int i = 0; i < nmax; i++) stest << i << " " << i+1 << endl;
        for(int i = 0; i < smax; i++) stest << i * 5 % 40 << " ";

        // Run the test
        double start = dclock();
        test_cin(stest.str());
        d = new Geo;
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
    cout << (new Geo)->calculate() << endl;
    return 0;
}

