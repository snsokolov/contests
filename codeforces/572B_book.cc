// 572B_book.cc - Codeforces.com 572B Book program by Sergey 2015

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
// Book Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Book { public:

    typedef long long ll;
    ll n;
    int s;
    vector <ll> numd, nump, numq;
    vector <pair<ll, ll>> bo, so, cbo, cso;

    Book(){

        // Reading single elements
        cin >> n;
        cin >> s;

        // Reading multiple lines of pair
        for(int i=0; i<n; i++) {
            char d; cin >> d; numd.push_back((d == 'B') ? 1 : 0);
            ll p; cin >> p; nump.push_back(p);
            ll q; cin >> q; numq.push_back(q);
        }

        for(int i=0; i<n; i++) {
            auto pq = make_pair(nump[i], numq[i]);
            if (numd[i]) bo.push_back(pq);
            else so.push_back(pq);
        }

        sort(bo.rbegin(), bo.rend());
        sort(so.begin(), so.end());
    }

    string calculate(){

        for (auto& v: so)
            if (cso.size() > 0 and cso.back().first == v.first)
                cso.back().second += v.second;
            else cso.push_back(v);

        for (auto& v: bo)
            if (cbo.size() > 0 and cbo.back().first == v.first)
                cbo.back().second += v.second;
            else cbo.push_back(v);

        ostringstream resstr;

        for (int i=s-1; i>=0; i--)
            if (i < (int)cso.size())
                resstr << "S " << cso[i].first << " " << cso[i].second << endl;
        for (int i=0; i<s; i++)
            if (i < (int)cbo.size())
                resstr << "B " << cbo[i].first << " " << cbo[i].second << endl;

        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    Book* d;

    void single_test() {

        // Constructor test
        string test = "6 2\nB 10 3\nS 50 2\nS 40 1\nS 50 6\nB 20 4\nB 25 10";
        test_cin(test);
        d = new Book;
        CHECK(d->n, 6);
        CHECK(d->s, 2);
        CHECK(d->numd[0], 1);
        CHECK(d->nump[0], 10);
        CHECK(d->numq[0], 3);
        CHECK(d->bo[0].first, 25);
        CHECK(d->so[0].first, 40);


        // Sample test
        test_cin(test);
        CHECKS((new Book)->calculate(), "S 50 8\nS 40 1\nB 25 10\nB 20 4\n");

        // Sample test
        test_cin("");
        //CHECKS((new Book)->calculate(), "0");

        // Sample test
        test_cin("");
        //CHECKS((new Book)->calculate(), "0");

        // My test
        test_cin("");
        //CHECKS((new Book)->calculate(), "0");

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
        d = new Book;
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
    cout << (new Book)->calculate() << endl;
    return 0;
}

