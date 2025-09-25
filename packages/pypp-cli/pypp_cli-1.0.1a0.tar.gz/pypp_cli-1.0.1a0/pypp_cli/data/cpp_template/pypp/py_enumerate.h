#pragma once

#include <cstddef>
#include <iterator>
#include <tuple> // Use std::tuple instead of PyTup
#include <utility>

namespace pypp {
// Forward declaration of the iterator class
template <typename T> class py_enumerate_iterator;

// The main PyEnumerate class (the "range")
template <typename T> class PyEnumerate {
  public:
    // Constructor uses a universal reference to handle both lvalues and rvalues
    PyEnumerate(T &&iterable) : _iterable(std::forward<T>(iterable)) {}

    // The begin() method returns our custom iterator
    auto begin() { return py_enumerate_iterator<T>(std::begin(_iterable), 0); }

    // The end() method
    auto end() { return py_enumerate_iterator<T>(std::end(_iterable), 0); }

  private:
    T _iterable;
};

// C++17 Deduction Guide for easier instantiation
template <typename T> PyEnumerate(T &&) -> PyEnumerate<T>;

// The iterator for PyEnumerate, now updated to yield std::tuple
template <typename T> class py_enumerate_iterator {
  private:
    // Deduces the type of the underlying container's iterator
    using InnerIterator = decltype(std::begin(std::declval<T &>()));
    // Deduces the value type (e.g., int, std::string)
    using InnerValue = typename std::iterator_traits<InnerIterator>::value_type;
    // Deduces the reference type (e.g., int&, std::string&)
    using InnerReference = const InnerValue &;

  public:
    // --- C++ Standard Iterator Traits ---
    using iterator_category = std::input_iterator_tag;
    // The value type is now a std::tuple of the index and the container's value
    // type
    using value_type = std::tuple<size_t, InnerValue>;
    // The reference type (what operator* returns) is a std::tuple of the index
    // and a reference to the value
    using reference = std::tuple<size_t, InnerReference>;
    using difference_type = std::ptrdiff_t;
    using pointer = void;
    // --- End of Traits ---

    // Constructor for the iterator
    py_enumerate_iterator(InnerIterator it, size_t index)
        : _it(it), _index(index) {}

    // Dereference operator (*it)
    // This now returns a std::tuple containing the index and a reference to the
    // element.
    reference operator*() const { return reference{_index, *_it}; }

    // Pre-increment operator (++it)
    py_enumerate_iterator &operator++() {
        ++_it;
        ++_index;
        return *this;
    }

    // Comparison operator (it != end())
    bool operator!=(const py_enumerate_iterator &other) const {
        return _it != other._it;
    }

  private:
    InnerIterator _it;
    size_t _index;
};
} // namespace pypp