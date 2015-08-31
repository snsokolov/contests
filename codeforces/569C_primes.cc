// 569C_primes.cc - Codeforces.com 569C Primes program by Sergey 2015

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
// Primes Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Primes { public:

    long long p, q;
    vector <long long> pal;
    vector <bool> primes;
    long long max;

    Primes(){

        // Reading single elements
        cin >> p;
        cin >> q;

        max = 2e6;

        for(int j=0; j < 4; j++){
            long long start = fexp(10, j);
            for(long long i = start; i < start*10; i++)
                pal.push_back(i * start + reverse(i/10));
            for(long long i = start; i < start*10; i++)
                pal.push_back(i * start * 10 + reverse(i));
        }
        primes.resize(max, true);
        primes[0] = false;
        primes[1] = false;
        for(long long i=2; i*i < max; i++)
            if (primes[i] == true)
                for(long long j=i*i; j < max; j += i)
                    primes[j] = false;
            
    }

    long long reverse(long long a){
        long long result = 0;
        while (a != 0) {
            result = result * 10 + a % 10;
            a = a/10;
        }
        return result;
    }

    long long fexp(long long a, unsigned int e){
        long long result = 1;
        while (e > 0) {
            if (e & 1) result *= a;
            e >>= 1;
            a *= a;
        }
        return result;
    }

    string calculate(){

        // Result calculation
        long long result = 0;

        long long primes_cnt=0, pal_cnt = 0;
        for(int i=1; i < max; i++){
            if (primes[i]) primes_cnt++;
            while (pal[pal_cnt] <= i and pal_cnt < pal.size()) pal_cnt++;
            if (primes_cnt * q <= p * pal_cnt) result = i;
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

    Primes* d;

    single_test() {

        // Constructor test
        string test = "1 1";
        test_cin(test);
        d = new Primes;
        CHECK(d->p, 1);
        CHECK(d->q, 1);

        // Reverse number
        CHECK(d->reverse(1), 1);
        CHECK(d->reverse(12), 21);

        // Fast exponent
        CHECK(d->fexp(10, 2), 100);
        CHECK(d->fexp(10, 5), 100000);

        // Sample test
        test_cin(test);
        CHECKS((new Primes)->calculate(), "40");

        // Sample test
        test_cin("1 42");
        //CHECKS((new Primes)->calculate(), "1");

        // Sample test
        test_cin("6 4");
        //CHECKS((new Primes)->calculate(), "172");

        // Sample test
        test_cin("7 11");
        //CHECKS((new Primes)->calculate(), "16");

        // My test
        test_cin("42 1");
        //CHECKS((new Primes)->calculate(), "1179858");

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
        d = new Primes;
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
    cout << (new Primes)->calculate() << endl;
    return 0;
}

