#include<windows.h>
#include<iostream>
#include<string>

using namespace std;

int main(int argc, char const *argv[])
{
	string cmd = "python E:/WorkSpace/HelperUsingPython/helper.py";
	for (int i = 1; i < argc; ++i)
	{
		string tmp = argv[i];
		cmd += " " + tmp;
	}
	// cout << cmd << endl;
	system(cmd.c_str());
	return 0;
}