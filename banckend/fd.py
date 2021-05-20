class nodo_arbol(object):
    def __init__(self,key = None, left = None, right = None):
        self.key=key
        self.left=left
        self.right=right

class binary_search_tree(object):
    def __init__(self,root=None):
        self.root=root

    def insertar(self,key):
        #metodo recursivo
        self.root=self._insertar(self.root, key)

    def _insertar(self,root,key):
        if not root:
            root=nodo_arbol(key)
        else:
            if key<root.key:
                root.left=self._insertar(root.left,key)
            elif key>root.key:
                root.right=self._insertar(root.right,key)
            else:
                print(key+"ya está en el árbol")

        return root
    def eliminar(self,key):
        self._eliminar(self.root,key)
    def _eliminar(self,root,key):
        if not root:
            print("El arbol binario de busqueda no existe")
            return
        else:
            if key<root.key:
                root.left=self._eliminar(root.left,key)
            elif key>root.key:
                root.right=self._eliminar(root.right,key)
            elif root.left and root.right:
                right_min=self._buscar_minimo(root)
                root.key=right_min.key
                root.right=self._eliminar(root.right,right_min.key)
            elif root.left:
                root=root.left
            elif root.right:
                root=root.right
            else:
                root=None
            return root
    def buscar_minimo(self):
        return self._buscar_minimo(self.root)
    def _buscar_minimo(self,root):
        if not root.left:
            return root
        return self._buscar_minimo(root.left)
    def buscar_maximo(self):
        return self._buscar_maximo(self.root)
    def _buscar_maximo(self,root):
        if not root.right:
            return root
        return self._buscar_maximo(root.right)
    def buscar(self,key):
        return self._buscar(self.root,key)
    def _buscar(self,root,key):
        if not root:
            print("El nodo no se encontró")
            return
        if key<root.key:
            return self._buscar(root.left,key)
        elif key>root.key:
            return self._buscar(root.right,key)
        else:
            print("El nodo no se encontró")
            return root

    def subarbol(self):
        return self._subarbol(self.root)
    def _subarbol(self,root):
        if not root:
            return 0
        left_subarbol=self._subarbol(root.left)
        right_subarbol=self._subarbol(root.right)
        return 1+left_subarbol+right_subarbol
    def ordenar(self):
        return self._ordenar(self.root)
    def _ordenar(self,root):
        if not root:
            return
        self._ordenar(root.left)
        print(root.key)
        self._ordenar(root.right)
    def reservar(self):
        return self._reservar(self.root)
    def _reservar(self,root):
        if not root:
            return
        print(root.key)
        self._reservar(root.left)
        self._reservar(root.right)
    def reservarSiguiente(self):
        return self._reservarSiguiente(self.root)
    def _reservarSiguiente(self,root):
        if not root:
            return
        self._reservarSiguiente(root.left)
        self._reservarSiguiente(root.right)
        print(root.key)


def main():
    import random
    test = binary_search_tree()
    print(type(test))
    for i in random.sample([j for j in range(1, 100)], 5):
        test.insertar(i)
    print('insertar: ')
    test.insertar(60)
    test.insertar(95)
    test.insertar(8)

    test.reservar()
    test.ordenar()
    test.reservarSiguiente()
    print('subarbol: ', test.subarbol())
    print('min: ', test.buscar_minimo().key)
    print('max: ', test.buscar_maximo().key)

    print( 'Eliminar: ')
    test.eliminar(95)
    test.eliminar(6)

    test.reservar()
    test.ordenar()
    test.reservarSiguiente()

    test.buscar(55)

    test.buscar(60)

    print('count: ', test.subarbol())
    print('min: ', test.buscar_minimo().key)
    print('max: ', test.buscar_maximo().key)

if __name__ == '__main__':
    main()