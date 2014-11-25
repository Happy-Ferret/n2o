{ 'targets': [
  { 'target_name' : 'n2o'
  , 'sources'     :
    [ 'n2o.hpp',
      'n2o/add_on.hpp',
      'n2o/arg_from_js.hpp',
      'n2o/constructor.hpp',
      'n2o/converter/arg_from_js.hpp',
      'n2o/converter/builtin_converters.hpp',
      'n2o/converter/constructor_function.hpp',
      'n2o/converter/convertible_function.hpp',
      'n2o/converter/from_js.hpp',
      'n2o/converter/registered.hpp',
      'n2o/converter/registrations.hpp',
      'n2o/converter/registry.hpp',
      'n2o/converter/rvalue_from_js_data.hpp',
      'n2o/converter/to_js_function_type.hpp',
      'n2o/default_call_policies.hpp',
      'n2o/detail/caller.hpp',
      'n2o/detail/destroy.hpp',
      'n2o/detail/exception_handler.hpp',
      'n2o/detail/make_function.hpp',
      'n2o/detail/property_value.hpp',
      'n2o/detail/referent_storage.hpp',
      'n2o/detail/translate_exception.hpp',
      'n2o/detail/void_ptr.hpp',
      'n2o/errors.hpp',
      'n2o/exception_translator.hpp',
      'n2o/function.hpp',
      'n2o/function_wrapper.hpp',
      'n2o/init.hpp',
      'n2o/invoke.hpp',
      'n2o/js_type_info.hpp',
      'n2o/object.hpp',
      'n2o/objects/object_base.hpp',
      'n2o/preprocessor.hpp',
      'n2o/signature.hpp',
      'n2o/to_js_value.hpp',
      'n2o/type_id.hpp',
      'n2o/type_list.hpp',
      'n2o/value_arg.hpp',
      'src/binding.cpp',
      'src/builtin_converters.cpp',
      'src/errors.cpp',
      'src/from_js.cpp',
      'src/function_wrapper.cpp',
      'src/registry.cpp',
      'src/type_id.cpp' 
    ]
  , 'includes': ['n2o.gypi']
  , 'all_dependent_settings': { 'includes': ['n2o.gypi'] }
  }
]}

