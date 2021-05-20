class Node:
    def __init__(self,value=None , parent=None, is_root=False,is_left=False,is_right=False):
        self.value=value
        self.left=None
        self.right=None
        self.parent=parent
        self.is_root=is_root
        self.is_left=is_left
        self.is_right=is_right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    #esta vacio o no el nodo
    def empty(self):
        if self.root ==None:
            return True
        else:
            return False
    def add (self, value):
        if self.empty():
            self.root = Node(value=value , is_root=True)
        else:
            # __get_place   al ser inicializado de esta forma es un metodo privado
            node = self.__get_place(value)
            if value <= node.value:
                node.left = Node(value=value,parent=node,is_left=True)
            else:
                node.right= Node(value=value,parent=node,is_right=True)
        
    def __get_place(self, value):
        aux = self.root
        #while aux: =mientras contenga algo ejecuta ,<==> while aux !=None:  <==> while aux is not None:
        while aux:
            temp = aux
            if value <= aux.value:
                aux = aux.left
            else:
                aux = aux.right
        return temp


    def show_in_order(self, node):
        #izquierda - raiz - derecha  1,3,4,6,7,8,10,13,14
        if node:
            self.show_in_order(node.left)
            print(node.value)
            self.show_in_order(node.right)

    def show_pre_order(self,node):
        #raiz - izquierda - derecha   8,3,1,6,4,7,10,14,13
        if node:
            print(node.value)
            self.show_pre_order(node.left)
            self.show_pre_order(node.right)
    def show_pos_order(self,node):
        #izquierda - derecha - raiz   1,4,7,6,3,13,14,10,8
        if node:
            self.show_pos_order(node.left)
            self.show_pos_order(node.right)
            print(node.value)
    def search(self,node,value):
        if node==Node:
            return Node
        else:
            if node.value == value:
                return node
            elif value <= node.value:
                return self.search(node.left,value)
            else:
                return self.search(node.right,value)





def main():
    tree = BinarySearchTree()
    # 8,10,3,14,13,1,6,4,7
    tree.add(8)
    tree.add(10)
    tree.add(3)
    tree.add(14)
    tree.add(13)
    tree.add(1)
    tree.add(6)
    tree.add(4)
    tree.add(7)

    #tree.show_in_order(tree.root)
    #tree.show_pre_order(tree.root)
    tree.show_pos_order(tree.root)

    print(tree.search(tree.root,6))
    print(tree.search(tree.root,6).value)
    print(tree.search(tree.root,6).is_root)
    print(tree.search(tree.root,6).is_left)
    print(tree.search(tree.root,6).is_right)
    print(tree.search(tree.root,6).parent.value)

if __name__=='__main__':
    main()

