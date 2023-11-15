#include <iostream>
#include <limits>

int main()                          
{
    char char_var{};
    short short_var{};
    int int_var{};
    long long_var{};
    long long long_long_var{};

    unsigned char uchar_var{};
    unsigned short ushort_var{};
    unsigned int uint_var{};
    unsigned long ulong_var{};
    unsigned long long ulong_long_var{};

    // https://learn.microsoft.com/en-us/cpp/c-language/cpp-integer-limits?view=msvc-170
    std::cout << "Char\n";
    std::cout << "Size: " << sizeof(char_var) << "\nMin: " << CHAR_MIN << "\nMax: " << CHAR_MAX << "\n";

    std::cout << "\nShort\n";
    std::cout << "Size: " << sizeof(short_var) << "\nMin: " << SHRT_MIN << "\nMax: " << SHRT_MAX << "\n";

    std::cout << "\nInt\n";
    std::cout << "Size: " << sizeof(int_var) << "\nMin: " << INT_MIN << "\nMax: " << INT_MAX << "\n";

    std::cout << "\nLong\n";
    std::cout << "Size: " << sizeof(long_var) << "\nMin: " << LONG_MIN << "\nMax: " << LONG_MAX << "\n";

    std::cout << "\nLong Long\n";
    std::cout << "Size: " << sizeof(long_long_var) << "\nMin: " << LLONG_MIN << "\nMax: " << LLONG_MAX << "\n";

    std::cout << "\nUnsigned Char\n";
    // No output when using std::numeric_limits<unsigned char>::min()
    // https://stackoverflow.com/questions/3499325/whats-a-portable-value-for-uint-min
    // "It's an unsigned integer - by definition its smallest possible value is 0."
    int uchar_min = std::numeric_limits<char>::min();
    std::cout << "Size: " << sizeof(uchar_var) << "\nMin: " << uchar_min << "\nMax: " << UCHAR_MAX << "\n";

    std::cout << "\nUnsigned Short\n";
    std::cout << "Size: " << sizeof(ushort_var) << "\nMin: " << std::numeric_limits<unsigned short>::min() << "\nMax: " << USHRT_MAX << "\n";

    std::cout << "\nUnsigned Int\n";
    std::cout << "Size: " << sizeof(uint_var) << "\nMin: " << std::numeric_limits<unsigned int>::min() << "\nMax: " << UINT_MAX << "\n";

    std::cout << "\nUnsigned Long\n";
    std::cout << "Size: " << sizeof(ulong_var) << "\nMin: " << std::numeric_limits<unsigned long>::min() << "\nMax: " << ULONG_MAX << "\n";

    std::cout << "\nUnsigned Long Long\n";
    std::cout << "Size: " << sizeof(ulong_long_var) << "\nMin: " << std::numeric_limits<unsigned long long>::min() << "\nMax: " << ULLONG_MAX << "\n";
}

// Assign value too large
// char too_large{128};
// error: constant expression evaluates to 128 which cannot be narrowed to type 'char'

// Assign value too small
// unsigned char too_small{-129};
// error: constant expression evaluates to -129 which cannot be narrowed to type 'unsigned char'

// Is this defined behaviour (according to the C++ standard)?