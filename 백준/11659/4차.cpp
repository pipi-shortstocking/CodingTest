#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int arr[100001];
    int N, M, num, a, b;

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
    {
        cin >> num;

        arr[i] = arr[i - 1] + num;
    }

    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;

        if (a == 0)
            cout << arr[b] << "\n";
        else
            cout << arr[b] - arr[a - 1] << "\n";
    }
    return 0;
}