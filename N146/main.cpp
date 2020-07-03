#include <iostream>
#include<unordered_map>

using namespace std;

struct DlinkedNode{
    int key, value;
    DlinkedNode* prev;
    DlinkedNode* next;
    DlinkedNode(): key(0), value(0), prev(nullptr), next(nullptr) {}
    DlinkedNode(int _key, int _value): key(_key), prev(nullptr), next(nullptr) {}
};


class LRUCache{
private:
    unordered_map<int, DlinkedNode*> cache;
    DlinkedNode* head;
    DlinkedNode* tail;
    int size;
    int capacity;

public:
    LRUCache(int _capacity): capacity(_capacity), size(0){
        head = new DlinkedNode();
        tail = new DlinkedNode();
        head -> next = tail;
        tail -> prev = head;
    }

    int get(int key){
        if (!cache.count(key)){
            return -1;
        }
        DlinkedNode* node = cache[key];
        moveToHead(node);
        return node -> value;
    }

    void put(int key, int value) {
        if (!cache.count(key)) {
            DlinkedNode *node = new DlinkedNode(key, value);
            cache[key] = node;
            addToHead(node);
            size++;
            if (size > capacity) {
                DlinkedNode *removed = removeTail();
                cache.erase(removed->key);
                delete removed;
                size--;
            }
        } else {
            DlinkedNode *node = cache[key];
            node->value = value;
            moveToHead(node);
        }
    }

    void addToHead(DlinkedNode* node){
        node -> prev = head;
        node -> next = head -> next;
        head -> next -> prev = node;
        head -> next = node;
    }

    void removeNode(DlinkedNode* node){
        node -> prev -> next = node -> next;
        node -> next -> prev = node -> prev;
    }

    void moveToHead(DlinkedNode* node){
        removeNode(node);
        addToHead(node);
    }

    DlinkedNode* removeTail(){
    DlinkedNode* node = tail -> prev;
    removeNode(node);
    return node;
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
