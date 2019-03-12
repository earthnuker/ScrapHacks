#pragma once
template<typename T>
struct HashTableEntry;
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
	map<string, PyMethodDef*> methods;
};

struct Entity {
	void* vmt;
	const char* name;
};

struct EntityList {
	const char* name;
	void* unk_1;
	void* unk_2;
	const char* mod;
	const char* func;
};

template<typename T>
struct HashTable {
	uint32_t size;
	HashTableEntry<T>** chains;
};

template<typename T>
struct HashTableEntry {
	T* data;
	const char* name;
	HashTableEntry* next;
};