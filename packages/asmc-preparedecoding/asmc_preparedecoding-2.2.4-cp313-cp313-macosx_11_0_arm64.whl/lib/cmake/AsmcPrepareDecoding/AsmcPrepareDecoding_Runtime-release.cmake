#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "AsmcPrepareDecoding::prepare_decoding_lib" for configuration "Release"
set_property(TARGET AsmcPrepareDecoding::prepare_decoding_lib APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(AsmcPrepareDecoding::prepare_decoding_lib PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libprepare_decoding_lib.a"
  )

list(APPEND _cmake_import_check_targets AsmcPrepareDecoding::prepare_decoding_lib )
list(APPEND _cmake_import_check_files_for_AsmcPrepareDecoding::prepare_decoding_lib "${_IMPORT_PREFIX}/lib/libprepare_decoding_lib.a" )

# Import target "AsmcPrepareDecoding::smcpp_lib" for configuration "Release"
set_property(TARGET AsmcPrepareDecoding::smcpp_lib APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(AsmcPrepareDecoding::smcpp_lib PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libsmcpp_lib.a"
  )

list(APPEND _cmake_import_check_targets AsmcPrepareDecoding::smcpp_lib )
list(APPEND _cmake_import_check_files_for_AsmcPrepareDecoding::smcpp_lib "${_IMPORT_PREFIX}/lib/libsmcpp_lib.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
