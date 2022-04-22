#include <bits/stdc++.h>
#include <functional>

#include <iostream>

using namespace std;

void foreach_comb(string n, int k, std::function<void(string *)> f) {
  int indexes[k];
  recursive_comb(indexes, n - 1, k, f);
}

int main(){
  string s;
  int k;

  cin >> s >> k;
  // cout << s << endl;

  foreach_comb(s, s.length(), [](string *indexes) {
    std::cout << indexes[0] << ',' << indexes[1] << ',' << indexes[2] << std::endl;
  });

  return 0;
}


