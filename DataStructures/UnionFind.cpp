#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

/*
    Author: Michele Cattaneo
    inspired by example in "Algorithms 4th Edition", R. Sedgewick, K. Wayne
*/

class UnionFind {

    int gen = 0;
    int size;
    int number_components;
    std::vector<int> sizes;
    std::vector<int> id;

    int generator() {
        return gen++;
    }

public:
    UnionFind() : size(0), number_components(0) {}

    UnionFind(unsigned size) :  size(size), 
                                number_components(size) { 
        std::generate_n(std::back_inserter(id), size, [&] {return generator(); });
        std::fill_n(std::back_inserter(sizes), size, 1);

    }

    /**
     *  Create space to represent a new object in the Union-Find, initially in a new component.
     *  @return The new id for the newly added object. Return -1 on failed mem allocation.
     */
    int add() {
        try{
            id.push_back(size); // new element is representet by itself
            sizes.push_back(1); // size of new component is 1
        }
        catch(std::bad_alloc & ex) {
            std::cerr << "UF failed to allocate new element" << std::endl;
            return -1;
        }
        number_components++;
        return size++;
    }

    /**
     * Find the representant's id of an element in the UF.
     * @param p The id of the element to find.
     * @return The id of the representant.
     */
    int find(int p) {
        int parent = p;
        // find the representant of the component ( when the representant is itself )
        while( parent != id[parent])
            parent = id[parent];
        
        // path compression
        // to obtain amortized time complexity; everytime we execute a find() we can make sure all elements from p to the one before the parent
        // will directly link to the parent, making the path to the parent shorter each time
        while(p != parent) {
            int next = id[p];
            id[p] = parent;
            p = next;
        }
        return parent;
    }

    /**
     * Checks whether two elements belong to the same component.
     * @param a first element
     * @param b second element
     * @return true if elements belong to the same component, false otherwise
     */ 
    bool are_connected(const int & a,const int & b) {
        return find(a) == find(b);
    }

    /**
     * Unify the two component in which p and q belong
     * @param p first element
     * @param q second element
     */
    void do_union(const int & p,const int & q) {
        int parent1 = find(p);
        int parent2 = find(q);
        if(parent1 == parent2) // if already in the same component, do nothing
            return;

        // merge smaller group ito bigger one (update the size of the component and the representant of the smaller component)
        if(sizes[parent1] < sizes[parent2]) {
            sizes[parent2] += sizes[parent1];
            id[parent1] = parent2;
        }
        else {
            sizes[parent1] += sizes[parent2];
            id[parent2] = parent1;
        }
        // there is one component less after the union
        number_components--;
    }

    /**
     * Return the size of the component in which an element belong
     * @param p The id of the element
     * @return The size of the component
     */ 
    int component_size(const int & p) {
        // the size of the whole component is in the array at the position of the representant
        return sizes[find(p)];
    }

    /**
     * Return the number of components which size is bigger than one.
     */ 
    int components_size_gt_one() {
        int comps_size_one = 0;
        for(int i=0; i < size; ++i) {
            if(component_size(i) == 1)
                comps_size_one++;
        }
        return number_components - comps_size_one;
    }

    /**
     * Print the representant relationship
     */ 
    void printParents() {
        for (int i=0; i<size; ++i) {
            std::cout << ' ' << i;
        }
        std::cout << std::endl;
        for(auto & s : id)
            std::cout << ' ' << s;
        std::cout << std::endl;
    }

    /**
     * Reset the UnionFind while keeping the size.
     */
    void reset() {
        for(int i=0; i<size; ++i) {
            sizes[i] = 1;
            id[i] = i;
        }
        
        number_components = size;
    }

    /**
     * Change the size of the union-find and reset all relationship as if newly instantiated
     * @param new_size The new size desired
     * @return true if the reallocation was succesful, false otherwise
     */ 
    bool resize_and_reset(int new_size) {
        if (new_size < 0)
            return false;
        
        try {
            sizes.resize(new_size);
            id.resize(new_size);
            size = new_size;
            reset(); 
        }
        catch(std::bad_alloc & err) {
            return false;
        }
        return true;
    }

};

//int main(int argc, char ** argv) {}