template <typename T>
class LinkedList
{
public:

    LinkedList();
    ~LinkedList();

    void push_back(T value);
    void pop_back();
    void push_front(T value);
    void pop_front();
    void insert(int index, T value);
    void removeAt(int index);
    int get_size();
    void clear();


    template <typename T1>
    class Node : public LinkedList<T1>
    {
    public:
        Node *pNext;
        T1 value;

        Node(T1 value = T1(), Node *pNext = nullptr)
        {
            this->value = value;
            this->pNext = pNext;
        }
    };

    Node<T> *head;
    int size;
};

template <typename T>
LinkedList<T>::LinkedList()
{
    head = nullptr;
    size = 0;
};

template <typename T>
LinkedList<T>::~LinkedList()
{
    clear();
};

template <typename T>
void LinkedList<T>::push_back(T value)
{
    // Add an item to the end of the list.
    if (this->size == 0)
    {
        this->head = new Node<T>(value);
        this->size++;
    }else
        insert(this->size, value);
}

template <typename T>
void LinkedList<T>::pop_back()
{
    // Remove the back item of the list.
    removeAt(this->size-1);
}

template <typename T>
void LinkedList<T>::push_front(T value)
{
    // Add item to the front of the list.
    this->head = new Node<T>(value, this->head);
    this->size++;
}

template <typename T>
void LinkedList<T>::pop_front()
{
    // Remove the first item from the list.
    if (this->size == 0)
        return;
    else
    {
        Node<T> *toDelete = this->head;
        this->head = this->head->pNext;
        delete toDelete;
        this->size--;
    }
}

template <typename T>
void LinkedList<T>::insert(int index, T value)
{
    // Insert an item at a given index.
    if(this->size == 0)
        push_front(value);
    else if (index > this->size)
        return;
    else if (index == 0)
    {
        Node<T> *toInsert = new Node<T>(value, this->head);
        head = toInsert;
        this->size++;
    }
    else
    {
        Node<T> *previous = this->head;
        for(int i = 0; i != index-1; i++)
            previous = previous->pNext;
        Node<T> *toInsert = new Node<T>(value, previous->pNext);
        previous->pNext = toInsert;
        this->size++;
    }
}

template <typename T>
void LinkedList<T>::removeAt(int index)
{
    // Remove an item from a given index.
    if (index == 0)
        pop_front();
    else if (index > this->size)
        return;
    else if (this->size == 0)
        return;
    else
    {
        Node<T> *previous = this->head;
        for(int i = 0; i != index-1; i++)
            previous = previous->pNext;
        Node<T> *toDelete = previous->pNext;
        previous->pNext = toDelete->pNext;
        delete toDelete;
        this->size--;
    }
}

template <typename T>
void LinkedList<T>::clear()
{
    while (this->size != 0)
    {
        pop_front();
    }
}

template<typename T>
int LinkedList<T>::get_size() {
    return this->size;
}

int main(){

    LinkedList<int> lst;

    // Check push_back
    lst.push_back(0);
    lst.push_back(1);
    lst.push_back(2);

    // Check pop_back
    lst.pop_back();
    lst.pop_back();
    lst.pop_back();

    // Check push_front
    lst.push_front(-3);
    lst.push_front(-2);
    lst.push_front(-1);

    // Check pop_front
    lst.pop_front();
    lst.pop_front();
    lst.pop_front();

    // Check insert
    lst.insert(0, 0);
    lst.insert(0, -1);
    lst.insert(2, 1);
    lst.insert(3, 2);
    lst.insert(5, 2);

    // Check removeAt
    lst.removeAt(0);
    lst.removeAt(0);
    lst.removeAt(1);
    lst.removeAt(2);

    // Check get_size
    int size = lst.get_size();

    // Check clear
    lst.clear();
    lst.clear();

    return 0;
}