#include <iostream>

using namespace std;

int arr[100001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // int n, m, i, j, num;
    int n, m;
    cin >> n >> m;

    for (int a = 1; a <= n; a++)
    {
        int num;
        cin >> num;
        arr[a] = arr[a - 1] + num; // 구간합
    }

    for (int a = 0; a < m; a++)
    {
        int i, j;
        cin >> i >> j;

        if (i == 0)
            cout << arr[j] << endl;
        else
            cout << arr[j] - arr[i - 1] << endl;
    }

    return 0;
}