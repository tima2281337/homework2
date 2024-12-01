#include <iostream>
#include <string>
#include <vector>
#include <random>
#include <chrono>


using namespace std;
using namespace std::chrono;
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
    //for(int i = 1; i<=1000; i*=10){
    int desiredLength = 100;//*i; 
    string X = generateRandomUpperCaseString(desiredLength);
    string Y = generateRandomUpperCaseString(desiredLength);
    auto t1 = steady_clock::now();

    string b = lcs_brute_force(X, Y);

  
    auto t2 = steady_clock::now();

    auto time = duration<double>(t2 - t1).count();
    //cout << X << "\n" << Y << "\n";
    //cout << b;
    cout << "Длина:" << " " << desiredLength << "\n";
    cout << "НОП (" << "X" << ", " << "Y" << ") методом полного перебора: " << time  << endl;
                                                                            
   // }
    return 0;
}