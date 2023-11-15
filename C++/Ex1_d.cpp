#include <iostream>
#include <string>

int main()
{
    std::cout << "Enter string and number followed by [RETURN]\n";
    std::string s{};
    int i{};
    std::cin >> s >> i;
    std::cout << s[i] << "\n";
    std::cout << s.at(i) << "\n";
}

// When number is larger than the string is big, nothing is returned
// [] and .at() produce same output