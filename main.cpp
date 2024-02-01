#include <string> 
#include <stdlib.h>

int main() {
    for (int i = 0; i < 3400; i++) {
      std::string  file = static_cast<std::string>("touch new_file/") + std::to_string(i) + static_cast<std::string>(".txt");
      system(file.c_str());
      system("git add .");
      system("git commit -m 'add new file'");
      system("git push");

    }
    return 0;
}
