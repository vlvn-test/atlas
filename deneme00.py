class SequenceConstructorVisitor(EmitVisitor):
    def visitModule(self, mod):
        for dfn in mod.dfns:
            self.visit(dfn)

    def visitType(self, type):
        self.visit(type.value, type.name)

    def visitProduct(self, prod, name):
        self.emit_sequence_constructor(name, get_c_type(name))

    def visitSum(self, sum, name):
        if not is_simple(sum):
            self.emit_sequence_constructor(name, get_c_type(name))

    def emit_sequence_constructor(self, name, type):
        self.emit(f"GENERATE_ASDL_SEQ_CONSTRUCTOR({name}, {type})", depth=0)

class PyTypesDeclareVisitor(PickleVisitor):

    def visitProduct(self, prod, name):
        self.emit("static PyObject* ast2obj_%s(struct ast_state *state, void*);" % name, 0)
        if prod.attributes:
            self.emit("static const char * const %s_attributes[] = {" % name, 0)
            for a in prod.attributes:
                self.emit('"%s",' % a.name, 1)
            self.emit("};", 0)
        if prod.fields:
            self.emit("static const char * const %s_fields[]={" % name,0)
            for f in prod.fields:
                self.emit('"%s",' % f.name, 1)
            self.emit("};", 0)

yazı="Selam herkese, burada bazı sayılar var. Bunlar: 1, 2, 3, 4, 5"
dizi1=yazı.split()#Eğer parantez içerisine herhangi bir şey yazılmazsa bu durumda boşluğu baz alır.
dizi2=yazı.split(",")#Parantez içerisine herhangi bir şey yazıldığında o karakteri ayraç olarak görür ve dizi oluşturur.
print(dizi1)
print(dizi2)

