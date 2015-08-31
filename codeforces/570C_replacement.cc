// 570C_replacement.cc - Codeforces.com/problemset/problem/570/C Replacement program by Sergey 2015

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
// Replacement Class (Main Program)
///////////////////////////////////////////////////////////////////////////////


class Replacement { public:

    int n, m;
    string s;
    vector <int> numa;
    vector <char> numb;
    map <int,int> dots;
    int f;

    Replacement(){

        // Reading single elements
        cin >> n;
        cin >> m;
        cin >> s;

        // Reading multiple lines of pair
        for(int i = 0; i < m; i++) {
            int a;
            char b;
            cin >> a; numa.push_back(a);
            cin >> b; numb.push_back(b);
        }

        gendots();
    }

    void gendots(){
        // Filling the dots array
        dots.clear();
        int firstdot = 0;
        for(int i=0; i<n; i++)
            if (s[i] != '.') firstdot = i+1;
            else dots[firstdot]++;

        f = 0;
        for(auto n: dots) f += n.second-1;
    }

    void remove(int a){
        auto it = dots.lower_bound(a);
        if (it != dots.end()) {
            if (a == it->first) {
                if (it->second > 1) { dots[a+1] = dots[a]-1; f--; }
                dots.erase(a);
                return;
            }
        }
        if (it == dots.begin()) return;
        it--;
        int end = it->first + it->second - 1;
        if (a > end) return;
        if (a == end){
            if (it->second == 1) dots.erase(a); 
            else { it->second--; f--; }
            return;
        }
        dots[a+1] = end - a;
        it->second = a - it->first;
        f -= 2;
    }

    void add(int a){
        auto it = dots.lower_bound(a);
        auto previt = dots.lower_bound(a);
        if (it != dots.end()) {
            if (a == it->first-1) {
                bool merged = false;
                if (it != dots.begin()){ 
                    previt--; 
                    merged = (a == previt->first + previt->second); 
                }
                if(merged) {
                    previt->second += it->second + 1;
                    f+= 2;
                } else {
                    dots[a] = it->second+1;
                    f++;
                }
                dots.erase(a+1);
                return;
            }
            if (a == it->first) return;
        }
        if (it == dots.begin()) { dots[a] = 1; return; }
        previt--;
        int end = previt->first + previt->second - 1;
        if (a <= end) return;
        if (a == end + 1){
            previt->second++;
            f++;
            return;
        }
        dots[a] = 1;
    }

    string calculate(){

        // Converting result to string
        ostringstream resstr;

        for(int i=0; i<m; i++){
            if (numb[i] == '.') add(numa[i]-1); else remove(numa[i]-1);
            resstr << f << endl;
        }
        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Local Unit tests
///////////////////////////////////////////////////////////////////////////////


class LocalUnittest: public Unittest {

    Replacement* d;

    single_test() {

        // Constructor test
        string test = "10 3\n.b..bz....\n1 h\n3 c\n9 f";
        test_cin(test);
        d = new Replacement;
        CHECK(d->n, 10);
        CHECK(d->m, 3);
        CHECKS(d->s, ".b..bz....");
        CHECK(d->numa[0], 1);
        CHECK(d->numb[0], 'h');

        // Dots array
        CHECK(d->dots[0], 1);
        CHECK(d->dots[2], 2);
        CHECK(d->dots[6], 4);
        CHECK(d->f, 4);

        // Remove dot
        d->remove(0);
        d->remove(8);
        CHECK(d->dots[6], 2);
        CHECK(d->dots[9], 1);
        CHECK(d->f, 2);
        d->remove(2);
        CHECK(d->dots[3], 1);
        CHECK(d->f, 1);
        d->remove(6);
        CHECK(d->dots[7], 1);
        CHECK(d->f, 0);

        // Add dot
        d->s = ".b..bz....";
        d->gendots();
        d->add(0);
        d->add(5);
        CHECK(d->dots[5], 5);
        CHECK(d->f, 5);
        d->add(1);
        CHECK(d->dots[0], 4);
        CHECK(d->f, 7);
        d->add(4);
        CHECK(d->dots[0], 10);
        CHECK(d->f, 9);

        // Sample test
        test_cin(test);
        CHECKS((new Replacement)->calculate(), "4\n3\n1\n");

        // Sample test
        test_cin("4 4\n.cc.\n2 .\n3 .\n2 a\n1 a");
        CHECKS((new Replacement)->calculate(), "1\n3\n1\n1\n");

        // Sample test
        test_cin("2 7\nab\n1 w\n2 w\n1 c\n2 .\n2 .\n1 .\n2 b");
        CHECKS((new Replacement)->calculate(), "0\n0\n0\n0\n0\n1\n0\n");

        // My test
        test_cin("");
        //CHECKS((new Replacement)->calculate(), "0");

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
        d = new Replacement;
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
    cout << (new Replacement)->calculate() << endl;
    return 0;
}

