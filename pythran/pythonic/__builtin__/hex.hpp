#ifndef PYTHONIC_BUILTIN_HEX_HPP
#define PYTHONIC_BUILTIN_HEX_HPP

#include "pythonic/utils/proxy.hpp"
#include "pythonic/types/str.hpp"
#include <sstream>

namespace pythonic {

    namespace __builtin__ {
        template <class T>
            types::str hex(T const & v) {
                std::ostringstream oss;
                oss << "0x" << std::hex << v;
                return oss.str();
            }
        PROXY(pythonic::__builtin__, hex);

    }

}

#endif

