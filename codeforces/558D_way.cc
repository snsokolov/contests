// 558D_way.cc - Codeforces.com/problemset/problem/558/D Way quiz by Sergey 2015

// Standard modules
#include <bits/stdc++.h>

using namespace std;


///////////////////////////////////////////////////////////////////////////////
// Way Class
///////////////////////////////////////////////////////////////////////////////


class Way { public:

    static int const N = 100001;
    static int const H = 51;

    int hmax, qmax;
    long long numh[N], numl[N], numr[N], numa[N];

    pair <long long, long long> ay[N], an[N];
    int aymax, anmax;


    Way(){

        // Decoding input max sizes
        cin >> hmax;
        if (hmax > H) {
            cout << "FATAL: Increase H to " << hmax << endl; exit(1);
        }

        cin >> qmax;
        if (qmax > N) {
            cout << "FATAL: Increase N to " << qmax << endl; exit(1);
        }

        // Decoding questions
        for(int i = 0; i < qmax; i++)
            cin >> numh[i] >> numl[i] >> numr[i] >> numa[i];

        // Translating questions to the last row
        aymax = anmax = 0;
        for(int i = 0; i < qmax; i++) {
            numl[i] = transl(numh[i], hmax, numl[i], 0);
            numr[i] = transl(numh[i], hmax, numr[i], 1);
            if (numa[i] == 1) ay[aymax++] = make_pair(numl[i], numr[i]);
            else an[anmax++] = make_pair(numl[i], numr[i]);
        }

        sort(an, an + anmax);
    }

    int add_range(long long *ranges, int sz, long long l, long long r, int a) {
        long long new_ranges[N];
        int index = 0;
        for(int i=0; i< sz; i += 2) {
            long long ll = ranges[i];
            long long rr = ranges[i+1];
            if (a == 1) {
                if (r < ll or l > rr) {
                    // Do nothing
                } else if (l <= ll and r < rr) {
                    new_ranges[index++] = ll;
                    new_ranges[index++] = r;
                } else if (l < rr and r < rr) {
                    new_ranges[index++] = l;
                    new_ranges[index++] = r;
                } else if (l > ll and r >= rr) {
                    new_ranges[index++] = l;
                    new_ranges[index++] = rr;
                } else {
                    new_ranges[index++] = ll;
                    new_ranges[index++] = rr;
                }
            } else {
                if (r < ll or l > rr) {
                    new_ranges[index++] = ll;
                    new_ranges[index++] = rr;
                } else if (l <= ll and r < rr) {
                    new_ranges[index++] = r+1;
                    new_ranges[index++] = rr;
                } else if (l < rr and r < rr) {
                    new_ranges[index++] = ll;
                    new_ranges[index++] = l-1;
                    new_ranges[index++] = r+1;
                    new_ranges[index++] = rr;
                } else if (l > ll and r >= rr) {
                    new_ranges[index++] = ll;
                    new_ranges[index++] = l-1;
                } else {
                    // Do nothing l==ll r==rr
                }
            }
        }
        for (int i = 0; i < index; i++) ranges[i] = new_ranges[i];

        return index;
    }

    long long transl(int h, int hm, long long n, int right) {

        long long result = n;
        for(int i = h; i < hm; i++)
            result = result*2 + (right ? 1 : 0);
        return result;
    }

    string calculate(){

        long long ranges[N];
        ranges[0] = (long long)1 << (hmax - 1);
        ranges[1] = ((long long)1 << (hmax)) - 1;
        int sz = 2;

        for(int i = 0; i < aymax; i++)
            sz = add_range(ranges, sz, ay[i].first, ay[i].second, 1);

        for(int i = 0; i < anmax; i++) {
            sz = add_range(ranges, sz, an[i].first, an[i].second, 0);
            if (sz > 6) break;
        }

        long long result = ranges[0];
        ostringstream resstr;
        resstr << result;

        string final = resstr.str();
        if (sz > 2 or ranges[0] != ranges[1]) final = "Data not sufficient!";
        if (sz == 0) final = "Game cheated!";

        return final;
    }
};


///////////////////////////////////////////////////////////////////////////////
// Way Class test helping functions
///////////////////////////////////////////////////////////////////////////////

Way* class_wrap_input(const string& test="") {

    streambuf* orig = cin.rdbuf();
    istringstream input(test);
    if (test != "") {
        cin.rdbuf(input.rdbuf());
    };
    Way* d = new Way();
    if (test != "") cin.rdbuf(orig);
    return d;
}

string calculate(const string& test="") {
    Way* d = class_wrap_input(test);
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
        ostringstream o_msg;
        o_msg << "  Error: " << a << " ! = " << b << endl << endl;
        fail_msg += o_msg.str();
    }

    test_fail_errs(const string& a, const string& b,
            const string& stra, const string& strb,
            const string& file, int line, const string& function) {
        if (a == b) return 0;
        test_fail_hdr(stra, strb, file, line, function);
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
        string test = "3 1\n3 4 6 0";
        Way* d = class_wrap_input(test);
        CHECK(d->hmax, 3);
        CHECK(d->qmax, 1);
        CHECK(d->numh[0], 3);

        // Translate range
        CHECK(d->transl(1, 3, 4, 1), 19);
        CHECK(d->transl(1, 3, 4, 0), 16);

        // Merge ranges
        long long ranges[10];
        ranges[0] = 10;
        ranges[1] = 15;
        CHECK(d->add_range(ranges, 2, 15, 15, 0), 2);
        CHECK(ranges[0], 10);
        CHECK(ranges[1], 14);
        CHECK(d->add_range(ranges, 2, 11, 12, 0), 4);
        CHECK(ranges[0], 10);
        CHECK(ranges[1], 10);
        CHECK(ranges[2], 13);
        CHECK(ranges[3], 14);
        CHECK(d->add_range(ranges, 4, 10, 13, 1), 4);
        CHECK(ranges[0], 10);
        CHECK(ranges[1], 10);
        CHECK(ranges[2], 13);
        CHECK(ranges[3], 13);

        ranges[0] = 4;
        ranges[1] = 7;
        CHECK(d->add_range(ranges, 2, 4, 6, 0), 2);
        CHECK(ranges[0], 7);
        CHECK(ranges[1], 7);

        // Calculate test
        string result = d->calculate();
        CHECKS(result, "7");
    }

    test_sample_tests() {

        string test;

        // Sample test 2
        test = "4 3\n4 10 14 1\n3 6 6 0\n2 3 3 1";
        CHECKS(calculate(test), "14");

        // Sample test 3
        test = "4 2\n3 4 6 1\n4 12 15 1";
        CHECKS(calculate(test), "Data not sufficient!");

        // Sample test 4
        test = "4 2\n3 4 5 1\n2 3 3 1";
        CHECKS(calculate(test), "Game cheated!");
    }

    test_time_limit_test() {

        int hmax = 50;
        int qmax = 10000;
        string test;
        ostringstream o_test;

        o_test << hmax << " " << qmax << endl;
        for(int i = 0; i < qmax; i++) {
            long long l = ((long long)1 << 49) + i*i;
            long long r = ((long long)1 << 49) + (i+1) * (i+1) - 10;
            o_test << 50 << " " << l << " " << r << " 0" << endl;
        }
        test = o_test.str();

        double start = double(clock()) / CLOCKS_PER_SEC;
        Way* d = class_wrap_input(test);

        double calc = double(clock()) / CLOCKS_PER_SEC;
        //d->calculate();

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

    cout << calculate() << endl;
    return 0;
}

