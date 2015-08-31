// 570A_elections.cc - Codeforces.com 570A Elections program by Sergey 2015

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
// Elections Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Elections { public:

    long long nmax, mmax;
    vector < vector <long long>> nums;
    vector <long long> winners;

    Elections(){

        // Reading single elements
        cin >> nmax;
        cin >> mmax;

        // Reading multiple lines of pair
        for(int im = 0; im < mmax; im++) {
            vector <long long> tmp;
            nums.push_back(tmp);
            for(int in = 0; in < nmax; in++) {
                long long a;
                cin >> a; nums[nums.size()-1].push_back(a);
            }
        }
    }

    string calculate(){

        // Filling winners for each city
        winners.resize(nmax);
        for(int im = 0 ; im < mmax; im++) {
            long long maxc = -1, maxc_idx= -1;
            for(int in = 0; in < nmax; in++) {
                if (nums[im][in] > maxc) {
                    maxc = nums[im][in];
                    maxc_idx = in;
                }
            }
            winners[maxc_idx]++;
        }

        // Searching for overall winner
        long long result=-1, wmax = -1;
        for(int in = 0; in < nmax; in++) {
            if (winners[in] > wmax) {
                wmax = winners[in];
                result = in;
            }
        }
        result++;

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

    Elections* d;

    single_test() {

        // Constructor test
        string test = "3 3\n1 2 3\n2 3 1\n1 2 1";
        test_cin(test);
        d = new Elections;
        CHECK(d->nmax, 3);
        CHECK(d->mmax, 3);
        CHECK(d->nums[1][1], 3);
        CHECK(d->nums[2][2], 1);

        // Sample test
        test_cin(test);
        CHECKS((new Elections)->calculate(), "2");

        // Sample test
        test_cin("3 4\n10 10 3\n5 1 6\n2 2 2\n1 5 7");
        CHECKS((new Elections)->calculate(), "1");

        // Sample test
        test_cin("");
        //CHECKS((new Elections)->calculate(), "0");

        // My test
        test_cin("");
        //CHECKS((new Elections)->calculate(), "0");

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
        d = new Elections;
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
    cout << (new Elections)->calculate() << endl;
    return 0;
}

