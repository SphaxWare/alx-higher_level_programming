#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list_info - function
 * @p: pyobject
 */
void print_python_list(PyObject *p)
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

		obj = PyList_GetItem(p, loop);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
/**
 * print_python_bytes - function
 * @p: pyobject
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *b = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", b->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", size);
	for (i = 0; size > i; i++)
	{
		printf("%02hhx", b->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
