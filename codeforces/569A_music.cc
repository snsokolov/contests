// 569A_music.cc - Codeforces.com/problemset/problem/569/A Music program by Sergey 2015

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
    int status() {
        cout << endl; if (fails) cout << serr.str();
        cout << "--------------------------------------------------" << endl;
        cout << "Ran " << checks << " checks in " << dclock() << "s" << endl << endl;
        if (fails) cout << "FAILED (failures=" << fails << ")"; else cout << "OK" << endl;
        return fails > 0;
    }
    int run() { streambuf* ocin = cin.rdbuf(); test_list(); cin.rdbuf(ocin); return status(); }
};

///////////////////////////////////////////////////////////////////////////////
// Music Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Music { public:

    long long T, S, q;

    Music(){

        // Reading single elements
        cin >> T;
        cin >> S;
        cin >> q;

    }

    string calculate(){

        // Result calculation
        long long result = 1;

        long long cur = S * q;
        while (cur < T) {
            cur *= q;
            result++;
        }

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

    Music* d;

    single_test() {

        // Constructor test
        string test = "5 2 2";
        test_cin(test);
        d = new Music;
        CHECK(d->T, 5);
        CHECK(d->S, 2);
        CHECK(d->q, 2);

        // Sample test
        test_cin(test);
        CHECKS((new Music)->calculate(), "2");

        // Sample test
        test_cin("5 4 7");
        CHECKS((new Music)->calculate(), "1");

        // Sample test
        test_cin("6 2 3");
        CHECKS((new Music)->calculate(), "1");

        // My test
        test_cin("100000 1 2");
        CHECKS((new Music)->calculate(), "17");

        // Time limit test
        //time_limit_test(2000);
    }

    time_limit_test(int nmax){

        int smax = nmax;
        ostringstream stest;

        // Random inputs
        stest << nmax << " " << smax << endl;
        for(int i = 0; i < nmax; i++) stest << i << " " << i+1 << endl;
        for(int i = 0; i < smax; i++) stest << rand() % 40 << " ";

        // Run the test
        double start = dclock();
        test_cin(stest.str());
        d = new Music;
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

    cout << (new Music)->calculate() << endl;
    return 0;
}

