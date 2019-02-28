#pragma once

struct Vector3 {
	float x;
	float y;
	float z;
};

struct Matrix3x3 {
	Vector3 a;
	Vector3 b;
	Vector3 c;
};


struct PyMethodDef
{
	char *ml_name;
	void *ml_meth;
	int ml_flags;
	char *ml_doc;
};

struct PyMod
{
	char *name;
	void *init_func;
};

struct Module
{
	PyMod *mod;
	map<string, PyMethodDef> methods;
};
