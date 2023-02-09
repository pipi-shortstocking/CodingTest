#include <iostream>

using namespace std;

int main()
{
    int n, m, i, j, num;

    cin >> n >> m;
    int *arr1 = new int[n + 1]{
        0,
    };
    int *arr2 = new int[m]{
        0,
    };

    for (int a = 1; a <= n; a++)
    {
        cin >> num;
        arr1[a] = arr1[a - 1] + num; // 구간합
    }

    for (int a = 0; a < m; a++)
    {
        cin >> i >> j;

        if (i == 0)
            arr2[a] = arr1[j];
        else
            arr2[a] = arr1[j] - arr1[i - 1];
    }

    for (int a = 0; a < m; a++)
    {
        cout << arr2[a] << endl;
    }

    delete[] arr1;
    delete[] arr2;

    return 0;
}