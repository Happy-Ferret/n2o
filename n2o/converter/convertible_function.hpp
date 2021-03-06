#ifndef N2O_CONVERTER_CONVERTIBLE_FUNCTION_INCLUDED
#define N2O_CONVERTER_CONVERTIBLE_FUNCTION_INCLUDED

#include <v8.h>

namespace n2o { namespace converter {

typedef void* (*convertible_function)(v8::Handle<v8::Value>);
}} // end of namespace converter, n2o

#endif // N2O_CONVERTER_CONVERTIBLE_FUNCTION_INCLUDED
