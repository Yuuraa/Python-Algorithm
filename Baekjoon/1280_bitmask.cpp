#include <iostream>

using namespace std;

int main() {
    unsigned char A[11] = {0, };
    unsigned char B[11] = {0, };
    unsigned char ans[11] = {0, };
    int i;

    cin >> A >> B;
    cout << A << endl;
    cout << B << endl;

    for (i = 0; i < 10; i++)
        ans[i] = A[i] & B[i];
    cout << ans << endl;
    for (i = 0; i < 10; i++)
        ans[i] = A[i] | B[i];
    cout << ans << endl;
    for (i = 0; i < 10; i++)
        ans[i] = A[i] == B[i] ? '0' : '1';
    cout << ans << endl;
    for (i = 0; i < 10; i++)
        ans[i] = A[i] == '1' ? '0' : '1';
    cout << ans << endl;
    for (i = 0; i < 10; i++)
        ans[i] = B[i] == '1' ? '0' : '1';
    cout << ans << endl;

    return 0;
}