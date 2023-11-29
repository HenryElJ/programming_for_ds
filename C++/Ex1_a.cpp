#include <iostream> // I am a code comment!

int main()                          
{
    std::cout << "Hello, World!\n";
}

// $ g++ -std=c++17 -Wall -Wextra -Werror -pedantic YOUR_FILE.cpp -o hello
// $ ./hello

// https://caiorss.github.io/C-Cpp-Notes/compiler-flags-options.html
// https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html#index-pedantic-1
// -std         Specify the C++ version or ISO standard version
// -Wall        Turns on lots of compiler warning flags
// -Werror      Turn any warning into a compilation error
// -pedantic    Issue all the warnings demanded by strict ISO C and ISO C++
// -o           Output file