#include <iostream>
#include <string>
#include <random>


using namespace std;

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
  int desiredLength = 10; // Задаем желаемую длину строки
  string X = generateRandomUpperCaseString(desiredLength);
  string Y = generateRandomUpperCaseString(desiredLength);
  
  return 0;
}