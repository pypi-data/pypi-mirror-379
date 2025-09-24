"""""" # start delvewheel patch
def _delvewheel_patch_1_11_1():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, '.'))
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-py4dgeo-0.8.0')
        if os.path.isfile(load_order_filepath):
            import ctypes.wintypes
            with open(os.path.join(libs_dir, '.load-order-py4dgeo-0.8.0')) as file:
                load_order = file.read().split()
            kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
            kernel32.LoadLibraryExW.restype = ctypes.wintypes.HMODULE
            kernel32.LoadLibraryExW.argtypes = ctypes.wintypes.LPCWSTR, ctypes.wintypes.HANDLE, ctypes.wintypes.DWORD
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                if os.path.isfile(lib_path) and not kernel32.LoadLibraryExW(lib_path, None, 8):
                    raise OSError('Error loading {}; {}'.format(lib, ctypes.FormatError(ctypes.get_last_error())))


_delvewheel_patch_1_11_1()
del _delvewheel_patch_1_11_1
# end delvewheel patch

from py4dgeo.logger import set_py4dgeo_logfile
from py4dgeo.cloudcompare import CloudCompareM3C2
from py4dgeo.epoch import (
    Epoch,
    read_from_las,
    read_from_xyz,
    save_epoch,
    load_epoch,
)
from _py4dgeo import SearchTree
from py4dgeo.m3c2 import M3C2, write_m3c2_results_to_las
from py4dgeo.m3c2ep import M3C2EP
from py4dgeo.registration import (
    iterative_closest_point,
    point_to_plane_icp,
    icp_with_stable_areas,
)
from py4dgeo.segmentation import (
    RegionGrowingAlgorithm,
    SpatiotemporalAnalysis,
    regular_corepoint_grid,
    temporal_averaging,
)
from py4dgeo.util import (
    __version__,
    find_file,
    MemoryPolicy,
    set_memory_policy,
    get_num_threads,
    set_num_threads,
    initialize_openmp_defaults,
)

initialize_openmp_defaults()

from py4dgeo.pbm3c2 import *
