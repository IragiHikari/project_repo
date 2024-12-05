#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // Проверяем количество аргументов
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <input>\n", argv[0]);
        return 1;
    }

    FILE *secret = fopen("/challenge/app-systeme/ch5/.passwd", "rt");
    if (!secret) {
        perror("Error opening file");
        return 1;
    }

    char buffer[32];
    if (fgets(buffer, sizeof(buffer), secret) == NULL) {
        perror("Error reading file");
        fclose(secret);
        return 1;
    }
    fclose(secret);

    // Экранируем вывод пользовательского ввода
    printf("%s\n", argv[1]);

    return 0;
}
