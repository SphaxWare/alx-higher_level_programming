#include <Python.h>
/*
 * print_python_list_info - function
 * p: pyobject
 */
void print_python_list_info(PyObject *p)
{
	int size, allocate, loop;
	PyObject *obj;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (loop = 0; loop < size; loop++)
	{
		printf("Element %d: ", loop);

		obj = Pylist_GetItem(p, loop);
		printf("%s\n", PyTYPE(obj)->tp_name);
	}
}