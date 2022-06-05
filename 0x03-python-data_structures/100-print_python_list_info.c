#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - shows info about Python lists
 * @p: The pointer to generic PyObject which is of PyListObject type
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	long int list_size, b, i;

	i = 0;
	PyObject *obj;

	list_size = PyList_Size(p);
	b = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", b);
	while (i < list_size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
