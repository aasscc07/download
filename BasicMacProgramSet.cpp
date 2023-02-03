#include<stdio.h>
#include<stdlib.h>
#include<iostream>


int DownloadBrew() {
    
    try
    {
        const char* command = "/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"";
        printf("Execute command : %s\n",command);
        system(command);
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        return -1;
    }
    return 0;
}

int Download_Visual_Studio_Code() {
    try
    {
        const char* command = "brew install --cask visual-studio-code";
        printf("Execute command : %s\n",command);
        system(command);
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        return -1;
    }

    
    return 0;
}

int Download_NeoVim() {
    try
    {
        const char* command = "brew install neovim";
        printf("Execute command : %s\n",command);
        system(command);
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        return -1;
    }
    return 0;
}

int SettingFileAuthority(const std::string FilePath) {
    try
    {
        const std::string command = "sudo chmod -R 777 " + FilePath;
        printf("Execute command : %s\n",command.c_str());
        system(command.c_str());
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        return -1;
    }
    return 0;
}

int DownloadPrograms(int input) {
    switch (input)
    {
    case 1:
        /* code */
        break;
    
    default:
        break;
    }
}

int main(void) {
    int ECode = 0;
    ECode = DownloadBrew();
    // ECode = Download_Visual_Studio_Code();
    // ECode = Download_NeoVim();


    // SettingFileAuthority( <파일을 저장할 폴더 위치> );
    
    return ECode;
}
