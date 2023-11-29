#include <iostream>
#include <iomanip> // for setprecision

int main()
{
    std::cout << "Enter a floating point number followed by [RETURN]\n";
    double d1{};
    std::cin >> d1;
    std::cout << std::scientific << std::setprecision(3) << "Rounded down: " << std::floor(d1) << "\nRounded up: " << std::ceil(d1) << "\nSquare root: " << std::sqrt(d1) << "\n";
}

// Square root of -ve number returns nan