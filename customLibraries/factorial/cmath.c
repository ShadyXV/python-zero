#include <Python.h>

int main()
{
	PyObject* pInt;

	Py_Initialize();

	PyRun_SimpleString("print('Hello World from Embedded Python!!!')");

	Py_Finalize();

	printf("\nPress any key to exit...\n");
	if(!_getch()) _getch();
	return 0;
}