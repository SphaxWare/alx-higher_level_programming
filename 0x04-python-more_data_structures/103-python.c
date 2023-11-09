#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - function
 * @p: pyobject
 */
void print_python_list(PyObject *p)
{
	int size, allocate, loop;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocate = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (loop = 0; loop < size; loop++)
	{
		type = list->ob_item[loop]->ob_type->tp_name;
		printf("Element %d: %s\n", loop, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[loop]);
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
