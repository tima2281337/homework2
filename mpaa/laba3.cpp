#include <iostream>
#include <string>
#include <vector>
#include <random>
#include <chrono>


using namespace std;
using namespace std::chrono;

// Алгоритм полного перебора
string lcs_brute_force(const string& X, const string& Y) {
    int n = X.length();
    int m = Y.length();
    string max_lcs = "";

    // Перебор всех подпоследовательностей первой строки
    for (int i = 0; i < (1 << n); ++i) {
        string subsequence = "";
        for (int j = 0; j < n; ++j) {
            if (i & (1 << j)) {
                subsequence += X[j];
            }
        }

        // Проверка, является ли подпоследовательность подпоследовательностью второй строки
        int k = 0;
        bool is_subsequence = true;
        for (int j = 0; j < m; ++j) {
            if (k < subsequence.length() && subsequence[k] == Y[j]) {
                k++;
            }
        }
        if (k == subsequence.length() && subsequence.length() > max_lcs.length()) {
            max_lcs = subsequence;
        }
    }

    return max_lcs;
}

// Алгоритм динамического программирования
string lcs_dynamic_programming(const string& X, const string& Y) {
    int n = X.length();
    int m = Y.length();

    // Инициализация таблицы LCS
    vector<vector<int>> LCS(n + 1, vector<int>(m + 1, 0));

    // Заполнение таблицы LCS
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (X[i - 1] == Y[j - 1]) {
                LCS[i][j] = LCS[i - 1][j - 1] + 1;
            } else {
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1]);
            }
        }
    }

    // Восстановление НОП из таблицы LCS
    int i = n;
    int j = m;
    string lcs = "";
    while (i > 0 && j > 0) {
        if (X[i - 1] == Y[j - 1]) {
            lcs += X[i - 1];
            i--;
            j--;
        } else {
            if (LCS[i - 1][j] > LCS[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }
    }

    // Обратный порядок, чтобы получить НОП в правильном порядке
    //reverse(lcs.begin(), lcs.end());

    return lcs;
}

string generateRandomUpperCaseString(int length) {
  random_device rd;  // Используем random_device для более качественной случайности
  mt19937 generator(rd()); // Mersenne Twister 19937 - мощный генератор псевдослучайных чисел
  uniform_int_distribution<> distribution('A', 'Z'); // Диапазон от 'A' до 'Z'

  string randomString;
  for (int i = 0; i < length; ++i) {
    randomString += distribution(generator);
  }
  return randomString;
}


int main() {
    int desiredLength = 100000; // Задаем желаемую длину строки
    string X = generateRandomUpperCaseString(desiredLength);
    string Y = generateRandomUpperCaseString(desiredLength);
    auto t1 = steady_clock::now();

    string b = lcs_brute_force(X, Y);

    auto t2 = steady_clock::now();

    auto time = duration<double>(t2 - t1).count();

    auto t3 = steady_clock::now();

    string h = lcs_dynamic_programming(X, Y);

  auto t4 = steady_clock::now();

    auto time2 = duration<double>(t4 - t3).count();



    cout << "НОП (" << "X" << ", " << "Y" << ") методом полного перебора: " << time  << endl;
    cout << "НОП (" << "X" << ", " << "Y" << ") методом динамического программирования: " << time2 << endl;

    return 0;
}