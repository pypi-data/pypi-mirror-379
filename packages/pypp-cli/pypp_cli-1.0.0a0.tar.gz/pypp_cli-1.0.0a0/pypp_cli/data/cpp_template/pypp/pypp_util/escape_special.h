#pragma once

#include "py_str.h"

namespace pypp {

// TODO later: Use this when printing in collections (it looks way better). But
// it is a little tricky to set this up
PyStr escape_specials(const PyStr &input);

} // namespace pypp