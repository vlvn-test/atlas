def ciftMi(x): 
    return x 

 self.emit("int res;", depth+1)
        if field.seq:
            self.emit("PyErr_Format(PyExc_TypeError, \"%s field \\\"%s\\\" must "
                      "be a list, not a %%.200s\", _PyType_Name(Py_TYPE(tmp)));" %
                      (name, field.name),
                      depth+2, reflow=False)
            self.emit("goto failed;", depth+2)
            self.emit("}", depth+1)
            self.emit("len = PyList_GET_SIZE(tmp);", depth+1)
            if self.isSimpleType(field):
                self.emit("%s = _Py_asdl_int_seq_new(len, arena);" % field.name, depth+1)
            else:
                self.emit("%s = _Py_asdl_%s_seq_new(len, arena);" % (field.name, field.type), depth+1)
            self.emit("if (%s == NULL) goto failed;" % field.name, depth+1)
            self.emit("for (i = 0; i < len; i++) {", depth+1)
            self.emit("%s val;" % ctype, depth+2)
            self.emit("PyObject *tmp2 = Py_NewRef(PyList_GET_ITEM(tmp, i));", depth+2)
            with self.recursive_call(name, depth+2):
                self.emit("res = obj2ast_%s(state, tmp2, &val, arena);" %
                          field.type, depth+2, reflow=False)
            self.emit("Py_DECREF(tmp2);", depth+2)
            self.emit("if (res != 0) goto failed;", depth+2)
            self.emit("if (len != PyList_GET_SIZE(tmp)) {", depth+2)
            self.emit("PyErr_SetString(PyExc_RuntimeError, \"%s field \\\"%s\\\" "
                      "changed size during iteration\");" %
                      (name, field.name),
                      depth+3, reflow=False)
            self.emit("goto failed;", depth+3)
            self.emit("}", depth+2)
            self.emit("asdl_seq_SET(%s, i, val);" % field.name, depth+2)
            self.emit("}", depth+1)
        else:
            with self.recursive_call(name, depth+1):
                self.emit("res = obj2ast_%s(state, tmp, &%s, arena);" %
                          (field.type, field.name), depth+1)
            self.emit("if (res != 0) goto failed;", depth+1)

        self.emit("Py_CLEAR(tmp);", depth+1)
        self.emit("}", depth)


