// 669D_dance.cc - Codeforces.com/problemset/problem/669/D by Sergey 2016

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
// Dance Class (Main Program)
///////////////////////////////////////////////////////////////////////////////
class Intlist { public:

    struct Node {
        int value;
        Node *next; 
    };

    Node *head = NULL, *tail = NULL;

    void push_back(int value){
        Node *node = new Node;
        node->value = value;
        if (tail == NULL) {
            head = node;
        } else {
            tail->next = node;
        }
        tail = node;
    };
        
};

class Dance { public:

    typedef long long ll;
    int n, q;
    vector <int> numq, nums;

    Intlist llist;

    Dance(){

        // Reading single elements
        cin >> n;
        cin >> q;

        // Reading multiple lines of pair
        for(int i=0; i<q; i++) {
            int qq; cin >> qq; numq.push_back(qq);
            if (qq == 2) {
                nums.push_back(0);
            } else {
                int s; cin >> s; nums.push_back(s);
            }
        }

        for (int i=0; i<n; i++) {
            llist.push_back(i+1);
        }
        llist.tail->next = llist.head;
    }

    string calculate(){

        for (int i=0; i<q; i++) {
            if (numq[i] == 1){
                int shift = -nums[i];
                if (shift < 0) shift += n;
                for (int j=0; j<shift; j++) llist.head = llist.head->next;
            }
            if (numq[i] == 2){
                Intlist::Node *it = llist.head->next;
                Intlist::Node *pr = llist.head;
                Intlist::Node *nxt = NULL;
                llist.head = llist.head->next;
                for (int j=0; j<n/2-1; j++){
                    nxt = it->next;
                    pr->next = nxt->next;
                    it->next = pr;
                    it = nxt->next;
                    pr = nxt;
                }
                pr->next = llist.head;
                it->next = pr;
            }
        }

        // Converting result to string
        ostringstream resstr;
        Intlist::Node *it = llist.head;
        for (int i=0; i<n; i++){
            resstr << it->value << " ";
            it = it->next;
        }
        return resstr.str();
    }
};

///////////////////////////////////////////////////////////////////////////////
// Unit tests
///////////////////////////////////////////////////////////////////////////////


class MyCppunit: public Cppunit {

    Dance* d;

    void single_test() {

        // Constructor test
        string test = "6 3\n1 2\n2\n1 2";
        test_cin(test);
        d = new Dance;
        CHECK(d->n, 6);
        CHECK(d->q, 3);
        CHECK(d->numq[2], 1);
        CHECK(d->nums[2], 2);

        // Sample test
        test_cin(test);
        CHECKS((new Dance)->calculate(), "4 3 6 5 2 1 ");

        // Sample test
        test_cin("2 3\n1 1\n2\n1 -2");
        CHECKS((new Dance)->calculate(), "1 2 ");

        // Sample test
        test_cin("4 2\n2\n1 3");
        CHECKS((new Dance)->calculate(), "1 4 3 2 ");

        // My test
        test_cin("8 2\n2\n1 0");
        //CHECKS((new Dance)->calculate(), "1 4 3 6 5 2");

        // Time limit
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
        d = new Dance;
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

    cout << (new Dance)->calculate();
    return 0;
}

