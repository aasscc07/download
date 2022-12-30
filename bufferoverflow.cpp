#define _CRT_SECURE_NO_WARNNINGS
#pragma warning(disable: 4996)

void vulnerableFunction(char* userInput)
{
	char buffer[10]; // The buffer has a size of 10 bytes

	// Copy the user input into the buffer, without checking the size

	strcpy(buffer, userInput);
	printf("Input received: %s\n", buffer);
}


int main(int argc, char** argv)
{
    if (argc < 2)
    {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }

    vulnerableFunction(argv[1]);
    return 0;
}
