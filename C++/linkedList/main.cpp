template <typename T>
class LinkedList
{
public:

    LinkedList();
    ~LinkedList();

    void push_back(T data);
    void pop_back();
    void push_front(T data);
    void pop_front();
    void insert(int index, T data);
    void removeAt(int index);
    int get_size(void);
    void clear(void);


    template <typename T1>
    class Node : public LinkedList<T1>
    {
    public:
        Node *pNext;
        T1 data;

        Node(T1 data = T1(), Node *pNext = nullptr)
        {
            this->data = data;
            this->pNext = pNext;
        }
    };

    Node<T> *head;
    int size;
};

template <typename T>
LinkedList<T>::LinkedList(/* args */)
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
void LinkedList<T>::push_back(T data)
{
    if (size == 0)
    {
        head = new Node<T>(data);
        size++;
    }else
    {
        insert(size, data);
    }
}

template <typename T>
void LinkedList<T>::pop_back()
{
    removeAt(size-1);
}

template <typename T>
void LinkedList<T>::push_front(T data)
{
    head = new Node<T>(data, head);
    size++;
}

template <typename T>
void LinkedList<T>::pop_front()
{
    if (size == 0)
    {
        return;
    }else
    {
        Node<T> *toDelete = head;
        head = head->pNext;
        delete toDelete;
        size--;
    }
}

template <typename T>
void LinkedList<T>::insert(int index, T data)
{
    if(size == 0)
    {
        push_front(data);
    }else
    {
        if (index > size)
        {
            return;
        }else
        {
            Node<T> *previous = head;

            for(int i = 0; i != index-1; i++)
            {
                previous = previous->pNext;
            }
            Node<T> *toInsert = new Node<T>(data, previous->pNext);
            previous->pNext = toInsert;

            size++;
        }
    }
}

template <typename T>
void LinkedList<T>::removeAt(int index)
{
    if (index == 0)
    {
        pop_front();
    }else
    {
        if (size == 0)
        {
            return;
        }else
        {
            Node<T> *previous = head;
            for(int i = 0; i != index-1; i++)
            {
                previous = previous->pNext;
            }
            Node<T> *toDelete = previous->pNext;
            previous->pNext = toDelete->pNext;
            delete toDelete;
            size--;
        }
    }
}

template <typename T>
void LinkedList<T>::clear()
{
    while (size != 0)
    {
        pop_front();
    }

}

int main(void){

    LinkedList<int> lst;

    lst.push_back(2);
    lst.push_back(22);
    lst.push_front(1);
    lst.push_front(0);
    lst.removeAt(0);
    lst.pop_front();
    lst.pop_back();

    lst.insert(3, 22);
    lst.clear();


    return 0;
}