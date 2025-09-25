#include "pypp_text_io.h"
#include "exceptions/common.h"
#include <iostream>
#include <sstream>
#include <string>

namespace pypp {
void PyTextIO::check_file_open() const {
    if (!file_stream.is_open()) {
        throw RuntimeError("File not open: " + filename_.str());
    }
}

void PyTextIO::check_file_open_for_writing() const {
    if (!file_stream.is_open()) {
        throw RuntimeError("File not open for writing: " + filename_.str());
    }
}

void PyTextIO::open_file(const PyStr &filename, const PyStr &mode) {
    std::ios_base::openmode cpp_mode = std::ios_base::in;

    if (mode.str() == "r") {
        cpp_mode = std::ios_base::in;
    } else if (mode.str() == "w") {
        cpp_mode = std::ios_base::out | std::ios_base::trunc;
    } else if (mode.str() == "a") {
        cpp_mode = std::ios_base::out | std::ios_base::app;
    } else if (mode.str() == "r+") {
        cpp_mode = std::ios_base::in | std::ios_base::out;
    } else if (mode.str() == "w+") {
        cpp_mode =
            std::ios_base::in | std::ios_base::out | std::ios_base::trunc;
    } else if (mode.str() == "a+") {
        cpp_mode = std::ios_base::in | std::ios_base::out | std::ios_base::app;
    } else {
        throw RuntimeError("Unsupported file mode: " + mode.str());
    }

    file_stream.open(filename.str(), cpp_mode);
    if (!file_stream.is_open()) {
        throw RuntimeError("Could not open file: " + filename.str() +
                           " with mode " + mode.str());
    }
}

PyTextIO::PyTextIO(const PyStr &filename, const PyStr &mode)
    : filename_(filename), mode_(mode) {
    open_file(filename_, mode_);
}

PyTextIO::~PyTextIO() {
    if (file_stream.is_open()) {
        file_stream.close();
    }
}

PyStr PyTextIO::read() {
    check_file_open();
    file_stream.clear();
    file_stream.seekg(0, std::ios::end);
    std::streamsize size = file_stream.tellg();
    file_stream.seekg(0, std::ios::beg);

    std::string buffer;
    buffer.resize(static_cast<size_t>(size));
    if (size > 0) {
        file_stream.read(&buffer[0], size);
    }
    return PyStr(std::move(buffer));
}

PyStr PyTextIO::readline() {
    check_file_open();
    std::string line;
    if (std::getline(file_stream, line)) {
        line.push_back('\n');
        return PyStr(std::move(line));
    }
    return PyStr("");
}

PyList<PyStr> PyTextIO::readlines() {
    check_file_open();
    file_stream.clear();
    file_stream.seekg(0);

    PyList<PyStr> lines;
    std::string line;
    while (std::getline(file_stream, line)) {
        line.push_back('\n');
        lines.append(PyStr(std::move(line)));
        line.clear();
    }
    return lines;
}

void PyTextIO::write(const PyStr &content) {
    check_file_open_for_writing();
    file_stream << content.str();
    if (file_stream.fail()) {
        throw RuntimeError("Error writing to file: " + filename_.str());
    }
}

void PyTextIO::writelines(const PyList<PyStr> &lines) {
    check_file_open_for_writing();
    for (const PyStr &line : lines) {
        file_stream << line.str();
    }
    if (file_stream.fail()) {
        throw RuntimeError("Error writing lines to file: " + filename_.str());
    }
}

bool PyTextIO::good() const { return file_stream.good(); }

bool PyTextIO::eof() const { return file_stream.eof(); }

bool PyTextIO::fail() const { return file_stream.fail(); }
} // namespace pypp