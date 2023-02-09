#include <iostream>

using namespace std;

int main()
{
    int n, m, i, j;
    int count = 0;

    cin >> n >> m;
    int *arr1 = new int[n];
    int *arr2 = new int[m]{
        0,
    };

    for (int a = 0; a < n; a++)
    {
        cin >> arr1[a];
    }

    for (int a = 0; a < m; a++)
    {
        cin >> i >> j;
        for (int b = i - 1; b < j; b++)
        {
            arr2[a] += arr1[b];
        }
    }

    for (int a = 0; a < m; a++)
    {
        cout << arr2[a] << endl;
    }

    return 0;
}