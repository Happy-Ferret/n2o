#ifndef N2O_VALUE_ARG_INCLUDED
#define N2O_VALUE_ARG_INCLUDED

#include <boost/mpl/if.hpp>
#include <boost/type_traits/add_reference.hpp>
#include <boost/type_traits/add_const.hpp>

namespace n2o { namespace detail {

//template <typename T>
//struct value_arg :
//    boost::mpl::if_<
//        copy_ctor_mutates_rhs<T>,
//        T,
//        typename boost::add_reference<
//            typename boost::add_const<T>::type
//        >::type
//    >
//{};

template <typename T>
struct value_arg  {
   typedef typename boost::add_reference<
            typename boost::add_const<T>::type
        >::type type;
};

}} // end of namespace detail, n2o

#endif // N2O_VALUE_ARG_INCLUDED
