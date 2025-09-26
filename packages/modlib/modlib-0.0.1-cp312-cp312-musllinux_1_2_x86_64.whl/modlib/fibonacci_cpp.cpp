#include <Python.h>


int fibonacci(int n) {
    if (n <= 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}


static PyObject* fibonacci_cpp(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }

    int result = fibonacci(n);
    return PyLong_FromLong(result);
}


static PyMethodDef methods[] = {
    {"fibonacci_cpp", (PyCFunction)fibonacci_cpp, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "fibonacci_cpp",
    NULL,
    -1,
    methods,
};

PyMODINIT_FUNC PyInit_fibonacci_cpp(void)
{
    return PyModule_Create(&module);
}