#include <iostream>
#include <string>

bool equal(std::string a, std::string b) {
    return a == b;
}

bool lessOrEqual(std::string a, std::string b) {
    if (a != "0" && b == "0") {
        return false;
    } else if (a == "0" && b == "0") {
        return true;
    } else if (a == "0" && b != "0") {
        return true;
    } else if (a != "0" && b != "0") {
        return lessOrEqual(a.substr(1), b.substr(1));
    }
}

bool greaterOrEqual(std::string a, std::string b) {
    if (a != "0" && b == "0") {
        return true;
    } else if (a == "0" && b == "0") {
        return true;
    } else if (a == "0" && b != "0") {
        return false;
    } else if (a != "0" && b != "0") {
        return greaterOrEqual(a.substr(1), b.substr(1));
    }
}

bool less(std::string a, std::string b) {
    if (a != "0" && b == "0") {
        return false;
    } else if (a == "0" && b != "0") {
        return true;
    } else if (a == "0" && b == "0") {
        return false;
    } else if (a != "0" && b != "0") {
        return less(a.substr(1), b.substr(1));
    }
}

bool greater(std::string a, std::string b) {
    if (a != "0" && b == "0") {
        return true;
    } else if (a == "0" && b != "0") {
        return false;
    } else if (a == "0" && b == "0") {
        return false;
    } else if (a != "0" && b != "0") {
        return greater(a.substr(1), b.substr(1));
    }
}

std::string addition(std::string a, std::string b) {
    if (b == "0") {
        return a;
    } else {
        return addition("s" + a, b.substr(1));
    }
}

std::string multiplication(std::string a, std::string b) {
    if (b == "0") {
        return 0;
    } else {
        return addition(multiplication(a, b.substr(1)), a);
    }
}

std::string subtraction(std::string a, std::string b) {
    if (b == "0") {
        return a;
    } else if (a == "0" && b != "0") {
        return "NOT DEFINED!";
    } else if (a != "0" && b != "0") {
        return subtraction(a.substr(1), b.substr(1));
    }
}

std::string division(std::string a, std::string b) {
    if (b == "0") {
        return "NOT DEFINED!";
    } else if (a.find("s") < b.find("s")) {
        return "0";
    } else if (a.find("s") >= b.find("s")) {
        return "s" + division(subtraction(a, b), b);
    }
}

int main() {
    std::cout << std::boolalpha;
    std::cout << equal("sss0", "sss0") << std::endl; // true
    std::cout << lessOrEqual("ss0", "sss0") << std::endl; // true
    std::cout << greaterOrEqual("ss0", "sss0") << std::endl; // false
    std::cout << less("s0", "ss0") << std::endl; // true
    std::cout << greater("ssss0", "s0") << std::endl; // false
    return 0;
}

