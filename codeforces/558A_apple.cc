// 558A_apple.cc - Codeforces.com 558A Apple quiz by Sergey 2015

// Standard modules
#include <bits/stdc++.h>

using namespace std;


///////////////////////////////////////////////////////////////////////////////
// Apple Class
///////////////////////////////////////////////////////////////////////////////


class Apple { public:

    static int const N = 100001;
    int imax;
    long long numa[N], numb[N];
    pair <int, int> pos[N];
    pair <int, int> neg[N];

    Apple(){

        // Decoding input max sizes
        cin >> imax;

        if (imax > N) {
            cout << "FATAL: Increase N to " << imax << endl; exit(1);
        }

        // Decoding input pairs
        for(int i = 0; i < imax; i++) cin >> numa[i] >> numb[i];
    }

    string calculate(){

        int result = 0;
        
        int npos = 0, nneg = 0;

        for(int i = 0; i < imax; i++) {
            if (numa[i] > 0) {
                pos[npos].first = numa[i];
                pos[npos].second = numb[i];
                npos += 1;
            } else {
                neg[nneg].first = -numa[i];
                neg[nneg].second = numb[i];
                nneg += 1;
            }
        }
        sort(pos, pos+npos);
        sort(neg, neg+nneg);

        int tot = 0;
        for(int i=0; i < min(npos, nneg); i++)
            tot += pos[i].second + neg[i].second;

        if (npos > nneg) tot += pos[nneg].second;
        if (npos < nneg) tot += neg[npos].second;

        ostringstream resstr;
        resstr << tot;

        return resstr.str();
    }
};


///////////////////////////////////////////////////////////////////////////////
// Apple Class test helping functions
///////////////////////////////////////////////////////////////////////////////

Apple* class_wrap_input(const string& test="") {

    streambuf* orig = cin.rdbuf();
    istringstream input(test);
    if (test != "") {
        cin.rdbuf(input.rdbuf());
    };
    Apple* d = new Apple();
    if (test != "") cin.rdbuf(orig);    
    return d;
}

string calculate(const string& test="") {
    Apple* d = class_wrap_input(test);
    string result = d->calculate();
    delete d;
    return result;
}

///////////////////////////////////////////////////////////////////////////////
// Unit tests base Class
///////////////////////////////////////////////////////////////////////////////


class Unittest { public:

    #define CHECK(a, b)\
        if (a != b) {\
            test_fail_hdr(#a, #b, __FILE__, __LINE__, __FUNCTION__);\
            test_fail_err(a, b); }
    #define CHECKS(a, b)\
        if (a != b) {\
            test_fail_hdr(#a, #b, __FILE__, __LINE__, __FUNCTION__);\
            test_fail_errs(a, b); }
    #define CHECKT(a)\
        if (!(a)) {\
            test_fail_hdr(#a, "true", __FILE__, __LINE__, __FUNCTION__);\
            test_fail_err(a, 1); }

    int test_cnt, fail_cnt, fail;
    string status, fail_msg;

    Unittest() {
        test_cnt = fail_cnt = fail = 0;
        status = "OK";
    }

    // Override this function in derived class
    virtual test_list() {
        test_basic();
        test_done();
    }

    test_basic() { CHECKT("Base class basic test" == ""); }

    run() {
        // Run the test list and measure elapsed time
        test_list();
        double elp_secs = double(clock()) / CLOCKS_PER_SEC;
        // Print results
        cout << endl;
        if (fail_cnt > 0) cout << fail_msg;
        cout << "--------------------------------------------------" << endl;
        cout << "Ran " << test_cnt << " tests in " << elp_secs << "s" << endl;
        cout << endl;
        if (fail_cnt > 0) cout << "FAILED (failures=" << fail_cnt << ")";
        else cout << status << endl;
        if (fail_cnt > 0) return 1;
    }

    test_fail_hdr(const string& stra, const string& strb,
            const string& file, int line, const string& function) {
        // Combine test failure message
        fail_cnt ++;
        fail = 1;
        ostringstream o_msg;
        o_msg << "==================================================" << endl;
        o_msg << "FAIL: " << function << endl;
        o_msg << "--------------------------------------------------" << endl;
        o_msg << "File \"" << file << "\", line " << line;
        o_msg << " in " << function << endl;
        o_msg << "  Checking " << stra << " == " << strb << endl;
        fail_msg += o_msg.str();
    }

    test_fail_err(long long a, long long b) {
        ostringstream o_msg;
        o_msg << "  Error: " << a << " ! = " << b << endl << endl;
        fail_msg += o_msg.str();
    }

    test_fail_errs(const string& a, const string& b) {
        ostringstream o_msg;
        o_msg << "  Error: \"" << a << "\" ! = \"" << b << "\"" << endl;
        o_msg << endl;
        fail_msg += o_msg.str();
    }

    test_done() {
        test_cnt ++;
        if (fail == 0) cout << ".";
        else cout << "F";
        fail = 0;
    }
};


///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    test_class_basic_functions() {

        // Constructor test
        string test = "2\n-1 5\n1 5";
        Apple* d = class_wrap_input(test);
        CHECK(d->imax, 2);
        CHECK(d->numa[0], -1);

        // Calculate test
        CHECKS(d->calculate(), "10");
        CHECK(d->neg[0].first, 1);
    }

    test_sample_tests() {

        string test;

        // Sample test 1
        test = "2\n-1 5\n1 5";
        CHECKS(calculate(test), "10");

        // Sample test 2
        test = "3\n-2 2\n1 4\n-1 3";
         CHECKS(calculate(test), "9");

        // Sample test 3
        test = "3\n1 9\n3 5\n7 10";
         CHECKS(calculate(test), "9");

        // My test 4
        test = "3\n-1 9\n-3 5\n-7 10";
         CHECKS(calculate(test), "9");
    }

    test_time_limit_test() {

        int imax = 10000;
        int nmax = imax;
        string test;
        ostringstream o_test;
        
        o_test << imax << " " << nmax << endl;
        for(int i = 0; i < imax; i++) o_test << i-100 << " " << i+1 << endl;
        for(int i = 0; i < nmax; i++) o_test << i * 5 % 40 << " ";
        test = o_test.str();

        double start = double(clock()) / CLOCKS_PER_SEC;
        Apple* d = class_wrap_input(test);

        double calc = double(clock()) / CLOCKS_PER_SEC;
        d->calculate();

        double stop = double(clock()) / CLOCKS_PER_SEC;
        cout << "Time Test: " << stop - start << "s (input " << calc - start;
        cout << "s calc " << stop - calc << "s)" << endl;
    }

    test_list() {
        test_class_basic_functions();
        test_done();
        test_sample_tests();
        test_done();
        test_time_limit_test();
        test_done();
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
    cout << calculate() << endl;
    return 0;
}

