// 566F_clique.cc - Codeforces.com/problemset/problem/566/F Clique program by Sergey 2015

// All standard modules
#include <bits/stdc++.h>

using namespace std;


///////////////////////////////////////////////////////////////////////////////
// Clique Class
///////////////////////////////////////////////////////////////////////////////


class Clique { public:

    static int const N = 1000002;

    int imax;
    int nums[N];
    int freq[N];
    int nummax;
    int max = 0;

    Clique(){

        // Decoding input max sizes
        cin >> imax;
        if (imax > N) {
            cout << "FATAL: Increase N to " << imax << endl; exit(1);
        }

        // Decoding input list
        for(int i = 0; i < imax; i++) cin >> nums[i];

    }

    string calculate(){

        nummax = nums[imax-1];

        for(int i = 0; i < imax; i++){
            int incr = nums[i];
            int num = incr;
            int prev = freq[num];
            while (num <= nummax) {
                int next = freq[num] + 1;
                if (prev + 1 >= next) {
                    freq[num] = next;
                    if (next > max) max = next;
                }
                num += incr;
            }
        }

        int result = max;

        ostringstream resstr;
        resstr << result;

        return resstr.str();
    }
};


///////////////////////////////////////////////////////////////////////////////
// Clique Class test helping functions
///////////////////////////////////////////////////////////////////////////////

Clique* class_wrap_input(const string& test="") {

    streambuf* orig = cin.rdbuf();
    istringstream input(test);
    if (test != "") {
        cin.rdbuf(input.rdbuf());
    };
    Clique* d = new Clique();
    if (test != "") cin.rdbuf(orig);
    return d;
}

string calculate(const string& test="") {
    Clique* d = class_wrap_input(test);
    string result = d->calculate();
    delete d;
    return result;
}

///////////////////////////////////////////////////////////////////////////////
// Unit tests base Class
///////////////////////////////////////////////////////////////////////////////


class Unittest { public:

    #define CHECK(a, b)\
        test_fail_err(a, b, #a, #b, __FILE__, __LINE__, __FUNCTION__);
    #define CHECKT(a)\
        test_fail_err(a, 1, #a, "true", __FILE__, __LINE__, __FUNCTION__);
    #define CHECKS(a, b)\
        test_fail_errs(a, b, #a, #b, __FILE__, __LINE__, __FUNCTION__);

    int test_cnt, fail_cnt, fail;
    string status, fail_msg;

    Unittest() {
        test_cnt = fail_cnt = fail = 0;
        int status = "OK";
    }

    // Override this function in derived class
    virtual test_list() {
        test_basic();
        test_done();
    }

    test_basic() { CHECKT("Base class basic test" == ""); }

    int run() {
        test_list();
        double elp_secs = double(clock()) / CLOCKS_PER_SEC;
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
        fail_cnt ++;
        fail = 1;
        ostringstream msg;
        msg << "==================================================" << endl;
        msg << "FAIL: " << function << endl;
        msg << "--------------------------------------------------" << endl;
        msg << "File \"" << file << "\", line " << line;
        msg << " in " << function << endl;
        msg << "  Checking " << stra << " == " << strb << endl;
        fail_msg += msg.str();
    }

    test_fail_err(long long a, long long b,
            const string& stra, const string& strb,
            const string& file, int line, const string& function) {
        if (a == b) return 0;
        test_fail_hdr(stra, strb, file, line, function);
        ostringstream msg;
        msg << "  Error: " << a << " ! = " << b << endl << endl;
        fail_msg += msg.str();
    }

    test_fail_errs(const string& a, const string& b,
            const string& stra, const string& strb,
            const string& file, int line, const string& function) {
        if (a == b) return 0;
        test_fail_hdr(stra, strb, file, line, function);
        ostringstream msg;
        msg << "  Error: \"" << a << "\" ! = \"" << b << "\"" << endl;
        msg << endl;
        fail_msg += msg.str();
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

    test_list() {
        test_class_basic_functions();
        test_done();
        test_sample_tests();
        test_done();
        test_time_limit_test();
        test_done();
    }

    test_class_basic_functions() {

        // Constructor test
        string test = "8\n3 4 6 8 10 18 21 24";
        Clique* d = class_wrap_input(test);
        CHECK(d->imax, 8);
        CHECK(d->nums[0], 3);

        // Sample test 1
        string result = d->calculate();
        CHECK(d->freq[1], 0);
        CHECK(d->freq[3], 1);
        CHECK(d->max, 3);
        CHECK(d->nummax, 24);
        CHECKS(result, "3");
    }

    test_sample_tests() {

        string test;

        // Sample test 2
        test = "3\n2 5 7";
        CHECKS(calculate(test), "1");

        // Sample test 3
        test = "3\n3 4 6";
        CHECKS(calculate(test), "2");

        // My test 4
        test = "5\n2 5 10 30 90";
        CHECKS(calculate(test), "4");
    }

    test_time_limit_test() {

        int imax = 9900;
        string test;
        ostringstream o_test;

        o_test << imax << endl;
        for(int i = 0; i < imax; i++) o_test << i+2 << " ";
        test = o_test.str();

        double start = double(clock()) / CLOCKS_PER_SEC;
        Clique* d = class_wrap_input(test);

        double calc = double(clock()) / CLOCKS_PER_SEC;
        d->calculate();

        double stop = double(clock()) / CLOCKS_PER_SEC;
        cout << "Time Test: " << stop - start << "s (input " << calc - start;
        cout << "s calc " << stop - calc << "s)" << endl;
    }
};

///////////////////////////////////////////////////////////////////////////////
// Main Execution
///////////////////////////////////////////////////////////////////////////////


int main(int argc, char *argv[]) {

    // Faster cin and cout
    ios_base::sync_with_stdio(0);cin.tie(0);

    cout << calculate() << endl;
    return 0;
}

