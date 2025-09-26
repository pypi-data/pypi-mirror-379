
import copy as _copy
import ctypes as _cty
import errno
import math
import os as _os
import pathlib
import sys as _sys
import tempfile
import warnings
import weakref
from collections import namedtuple
from threading import Lock
from urllib import request

from pyfie import _config
from pyfie import _cty_util
from pyfie import _dbg
from pyfie import _util
from pyfie._util import _set_toplevel, _get_toplevel, _is_toplevel, _del_toplevel
from pyfie import version
from pyfie.version import __version__
try:
    from pyfie._decl_skelton import *
    from pyfie import _decl_skelton
except ImportError as e:
    if _config.auto_init:
        raise e
from pyfie._imports import _ENABLE_NUMPY, _ENABLE_PYPLOT, _raise_if_pyplot_unavailable
from pyfie import _basic_types

if _ENABLE_NUMPY:
    import numpy as _np
    import numpy.lib.stride_tricks

if _ENABLE_PYPLOT:
    import matplotlib.pyplot as _pyplot
    from matplotlib.ticker import FuncFormatter
    from pyfie import _pyplot_util
    from pyfie import mpltools
_ENABLE_FIE = True


_util._set_toplevel_target(__name__)


class _BreakError(Exception):
    pass


class _DeclManager:

    def __init__(self, decl_file_path):
        self.file_list = []
        self.dict_list = []
        self.add_decl_files(decl_file_path)
        self.platform = _util.get_platform(default="Default")

    def add_decl_files(self, decl_file_path):
        if isinstance(decl_file_path, str):
            decl_file_path = [decl_file_path]
        file_list = self.file_list
        for p in decl_file_path:
            p = _util.resolve_path(p)
            if _os.path.exists(p):
                file_list.append(p)
            else:
                _dbg.DEBUG_PRINT("> decl file not found ({0})".format(p))

    def load_decl_files(self):
        dict_list = self.dict_list = []
        for f in self.file_list:
            d = _util.load_json_obj(f, [], {})
            dict_list.append(d)

    def unload_decl_files(self):
        self.dict_list = []

    @staticmethod
    def _merge_list(root_list, sub_list, merge_elem_getter=None):
        if merge_elem_getter is None:
            root_list.extend(sub_list)
        else:
            merge_elem_list = [merge_elem_getter(e) for e in root_list]
            for e in sub_list:
                merge_elem = merge_elem_getter(e)
                if merge_elem in merge_elem_list:
                    continue

                root_list.append(e)
                merge_elem_list.append(merge_elem)

        return root_list

    @staticmethod
    def _load_decl_list(dict_list, key_list):
        if len(dict_list) < 0:
            return []

        decl_list = _util.get_dict_value_recursive(dict_list[0], key_list, [])
        if len(dict_list) == 1:
            return decl_list

        for d in dict_list[1:]:
            other_decl_list = _util.get_dict_value_recursive(d, key_list, [])
            decl_list = __class__._merge_list(decl_list, other_decl_list)

        return decl_list

    @staticmethod
    def _load_platform_value(dict_list, key_list, platform, default=None):
        for d in dict_list:
            decl_dict = _util.get_dict_value_recursive(d, key_list, None)
            if not decl_dict:
                continue

            if platform in decl_dict:
                return decl_dict[platform]

        for d in dict_list:
            decl_dict = _util.get_dict_value_recursive(d, key_list, None)
            if not decl_dict:
                continue

            if "Default" in decl_dict:
                return decl_dict["Default"]

        return default

    def get_types_dict(self):
        key_list = ("DECL", "TYPES")

        decl_dict = {}
        for d in self.dict_list:
            other_decl_dict = _util.get_dict_value_recursive(d, key_list, {})
            if not decl_dict:
                decl_dict = other_decl_dict
                continue

            for category, elem_list in other_decl_dict.items():
                if category in decl_dict:
                    decl_dict[category] = __class__._merge_list(
                        decl_dict[category], elem_list, lambda e: e["name"]
                    )
                else:
                    decl_dict[category] = elem_list

        return decl_dict

    def get_function_list(self):
        func_list = __class__._load_decl_list(
            self.dict_list, ("DECL", "FUNCTIONS"))
        func_list.append({
            "args": [
                {
                    "name": "major",
                    "type": "USHORT.*"
                },
                {
                    "name": "minor",
                    "type": "USHORT.*"
                },
                {
                    "name": "rev",
                    "type": "USHORT.*"
                },
                {
                    "name": "build",
                    "type": "USHORT.*"
                },
                {
                    "name": "desc",
                    "type": "CHAR.*.*"
                },
            ],
            "brief": "",
            "name": "get_lib_version",
            "param_doc": "",
            "prototype_code": "INT get_lib_version( USHORT *major, USHORT *minor, USHORT *rev, USHORT *build, const CHAR **desc )",
            "restype": "f_err",
            "retval_doc": ""
        })
        return func_list

    def get_struct_list(self):
        return __class__._load_decl_list(
            self.dict_list, ("DECL", "STRUCT"))

    def get_union_list(self):
        return __class__._load_decl_list(
            self.dict_list, ("DECL", "UNION"))

    def get_enum_list(self):
        return __class__._load_decl_list(
            self.dict_list, ("DECL", "ENUM"))

    def get_define_list(self):
        return __class__._load_decl_list(
            self.dict_list, ("DECL", "DEFINE"))

    def get_struct_pack_size(self):
        default_val = 8
        return __class__._load_platform_value(
            self.dict_list, ("MISC_DATA", "struct_pack"), self.platform, default_val)

    def get_union_pack_size(self):
        default_val = 8
        return __class__._load_platform_value(
            self.dict_list, ("MISC_DATA", "union_pack"), self.platform, default_val)

    def get_calling_convention(self):
        ''' Returns : "stdcall", "cdecl" '''
        default_val = "stdcall"

        if "Linux" == self.platform:
            return "cdecl"

        return __class__._load_platform_value(
            self.dict_list, ("MISC_DATA", "call_convent"), self.platform, default_val)

    def get_alias_list(self):
        return __class__._load_decl_list(
            self.dict_list, ("MISC_DATA", "alias"))

    def get_struct_protocol_dict(self):
        key_list = ("MISC_DATA", "struct_protocol")

        decl_dict = {}
        for d in self.dict_list:
            other_decl_dict = _util.get_dict_value_recursive(d, key_list, {})
            if not decl_dict:
                decl_dict = other_decl_dict
                continue

            for protocol_type, elem_list in other_decl_dict.items():
                if protocol_type in decl_dict:
                    decl_dict[protocol_type] = __class__._merge_list(
                        decl_dict[protocol_type], elem_list, lambda e: e["struct_name"]
                    )
                else:
                    decl_dict[protocol_type] = elem_list

        return decl_dict


class _StructProtocolBase:

    @staticmethod
    def _get_attr(self, attr_code):
        attr_obj = self
        for attr_name in attr_code.split("."):
            attr_obj = getattr(attr_obj, attr_name)
        return attr_obj

    @staticmethod
    def _set_attr(self, attr_code, val):
        attr_code_list = attr_code.split(".")
        attr_obj = self
        for attr_name in attr_code_list[: -1]:
            attr_obj = getattr(attr_obj, attr_name)
        setattr(attr_obj, attr_code_list[-1], val)

    @staticmethod
    def _has_attr(cls, attr_code):
        try:
            ty = cls
            for attr_name in attr_code.split("."):
                ty = ty._get_field_type(attr_name)

            return True
        except Exception:
            return False

    @staticmethod
    def _gen_attr_getter(attr_code, converter=None):
        if converter:
            def getter_func(self): return converter(
                __class__._get_attr(self, attr_code))
        else:
            def getter_func(self): return __class__._get_attr(self, attr_code)
        return getter_func

    @staticmethod
    def _gen_attr_setter(attr_code):
        return lambda self, v: __class__._set_attr(self, attr_code, v)

    @staticmethod
    def _plot_list(self, num, plot_obj=None, pattern_obj=None, **kwargs):
        for i in range(int(num)):
            self[i].plot(plot_obj, pattern_obj, **kwargs)

    @staticmethod
    def _bless_attr(target_cls, attr_dict, converter=None):

        for abstract_attr, real_attr in attr_dict.items():
            getter_name = "_get_" + abstract_attr
            getter_func = __class__._gen_attr_getter(real_attr, converter)
            setattr(target_cls, getter_name, getter_func)

            setter_name = "_set_" + abstract_attr
            setter_func = __class__._gen_attr_setter(real_attr)
            setattr(target_cls, setter_name, setter_func)

            if abstract_attr != real_attr:
                setattr(target_cls, abstract_attr,
                        property(getter_func, setter_func))


class _PointProtocol (_StructProtocolBase):
    """
    - [ x-coordinate ] property : .x / method : _get_x(), _set_x( value )
    - [ y-coordinate ] property : .y / method : _get_y(), _set_y( value )
    """

    @staticmethod
    def _plot(self, plot_obj=None, pattern_obj=None, **kwargs):
        if pattern_obj is not None:
            warnings.warn("pattern_obj is provided but not used",
                          category=RuntimeWarning)
        return _pyplot_util.draw_points(self._get_x(), self._get_y(), plot_obj=plot_obj, **kwargs)

    @staticmethod
    def _plot_list(self, num, plot_obj=None, pattern_obj=None, **kwargs):
        if pattern_obj is not None:
            warnings.warn("pattern_obj is provided but not used",
                          category=RuntimeWarning)

        x, y = [], []

        for i in range(int(num)):
            x.append(self[i]._get_x())
            y.append(self[i]._get_y())

        return _pyplot_util.draw_points(x, y, plot_obj=plot_obj, **kwargs)

    @staticmethod
    def bless(point_cls, attr_name_x, attr_name_y):
        __class__._bless_attr(
            point_cls, {"x": attr_name_x, "y": attr_name_y}, float)

        if _ENABLE_PYPLOT:
            point_cls.plot = __class__._plot
            _basic_types._Referable.get_ptr_cls(
                point_cls).plot = __class__._plot_list


class _LineProtocol (_StructProtocolBase):
    """
    - [ coefficient a ] property : .a / method : _get_a(), _set_a( value )
    - [ coefficient b ] property : .b / method : _get_b(), _set_b( value )
    - [ coefficient c ] property : .c / method : _get_c(), _set_c( value )
    """

    @staticmethod
    def _plot(self, plot_obj=None, pattern_obj=None, **kwargs):
        if pattern_obj is not None:
            warnings.warn("pattern_obj is provided but not used",
                          category=RuntimeWarning)
        EPS = 1e-10
        CHECKPOINTS = _np.array([-1, 1000, 10000, 1000000])
        a = self._get_a()
        b = self._get_b()
        c = self._get_c()
        if abs(a) < EPS and abs(b) < EPS:
            raise ValueError(
                "cannot draw line because a and b are both close to zero")
        if abs(a) <= abs(b):
            xx = CHECKPOINTS
            yy = (- a * xx - c) / b
        else:
            yy = CHECKPOINTS
            xx = (- b * yy - c) / a

        return _pyplot_util.draw_polygon_opened(
            _np.hstack((xx[:, _np.newaxis], yy[:, _np.newaxis])), plot_obj=plot_obj, **kwargs
        )

    @staticmethod
    def bless(line_cls, attr_name_a, attr_name_b, attr_name_c):
        __class__._bless_attr(line_cls, {
            "a": attr_name_a, "b": attr_name_b, "c": attr_name_c
        }, float)

        if _ENABLE_PYPLOT:
            line_cls.plot = __class__._plot
            _basic_types._Referable.get_ptr_cls(
                line_cls).plot = __class__._plot_list


class _SegmentProtocol (_StructProtocolBase):
    """
    - [ start x-coordinate ] property : sx / method : _get_sx(), _set_sx()
    - [ start y-coordinate ] property : sy / method : _get_sy(), _set_sy()
    - [ end   x-coordinate ] property : ex / method : _get_ex(), _set_ex()
    - [ end y-coordinate   ] property : ey / method : _get_ey(), _set_ey()
    """

    @staticmethod
    def _plot(seg_obj, plot_obj=None, pattern_obj=None, **kwargs):
        if pattern_obj is not None:
            warnings.warn("pattern_obj is provided but not used",
                          category=RuntimeWarning)

        sx, ex = seg_obj._get_sx(), seg_obj._get_ex()
        sy, ey = seg_obj._get_sy(), seg_obj._get_ey()

        return _pyplot_util.draw_polygon_opened(((sx, sy), (ex, ey)), plot_obj=plot_obj, **kwargs)

    @staticmethod
    def bless(seg_cls, attr_name_sx, attr_name_sy, attr_name_ex, attr_name_ey):
        __class__._bless_attr(seg_cls, {
            "sx": attr_name_sx, "sy": attr_name_sy,
            "ex": attr_name_ex, "ey": attr_name_ey
        }, float)

        if _ENABLE_PYPLOT:
            seg_cls.plot = __class__._plot
            _basic_types._Referable.get_ptr_cls(
                seg_cls).plot = _StructProtocolBase._plot_list


class _RectProtocol (_StructProtocolBase):
    """
    - [ start x-coordinate ] property : sx / method : _get_sx(), _set_sx()
    - [ start y-coordinate ] property : sy / method : _get_sy(), _set_sy()
    - [ end   x-coordinate ] property : ex / method : _get_ex(), _set_ex()
    - [ end y-coordinate   ] property : ey / method : _get_ey(), _set_ey()
    """

    @staticmethod
    def _plot(rect_obj, plot_obj=None, pattern_obj=None, **kwargs):
        if pattern_obj is not None:
            warnings.warn("pattern_obj is provided but not used",
                          category=RuntimeWarning)

        sx, ex = rect_obj._get_sx(), rect_obj._get_ex()
        sy, ey = rect_obj._get_sy(), rect_obj._get_ey()

        sx, ex = min(sx, ex), max(sx, ex)
        sy, ey = min(sy, ey), max(sy, ey)

        return _pyplot_util.draw_rect(sx, sy, ex-sx, ey-sy, plot_obj=plot_obj, **kwargs)

    @staticmethod
    def bless(rect_cls, attr_name_sx, attr_name_sy, attr_name_ex, attr_name_ey):
        __class__._bless_attr(rect_cls, {
            "sx": attr_name_sx, "sy": attr_name_sy,
            "ex": attr_name_ex, "ey": attr_name_ey
        }, float)

        if _ENABLE_PYPLOT:
            rect_cls.plot = __class__._plot
            _basic_types._Referable.get_ptr_cls(
                rect_cls).plot = _StructProtocolBase._plot_list


class _GsResultProtocol (_StructProtocolBase):
    """
    - [ x-coordinate（100倍値） ] property : .x / method : _get_x(), _set_x( value )
    - [ y-coordinate（100倍値） ] property : .y / method : _get_y(), _set_y( value )
    - [ score ] property : .score / method : _get_score(), _set_score( value )
    """
    @staticmethod
    def _get_pattern_and_offset_size(hgs_pat):
        if not hasattr(hgs_pat, "objtag") or (hgs_pat.objtag != F_OBJID_GS_PATTERN and hgs_pat.objtag != F_OBJID_GS_PATTERN_GPU):
            raise ValueError(
                "pattern object of gray search is required (got {})".format(hgs_pat))
        if hgs_pat.objtag == F_OBJID_GS_PATTERN:
            gs2_pattern_get_image = fnFIE_gs2_pattern_get_image
            gs2_pattern_get_offset = fnFIE_gs2_pattern_get_offset
        else:
            gs2_pattern_get_image = fnFGA_gs2_pattern_get_image
            gs2_pattern_get_offset = fnFGA_gs2_pattern_get_offset
        hpat_cp = FHANDLE()
        err = gs2_pattern_get_image(hgs_pat, hpat_cp)
        if F_ERR_NONE != err:
            raise RuntimeError(
                "failed fnFIE_gs2_pattern_get_image / {0}".format(f_err(err)))
        off_x = INT()
        off_y = INT()
        err = gs2_pattern_get_offset(hgs_pat, off_x, off_y)
        if F_ERR_NONE != err:
            raise RuntimeError(
                "failed fnFIE_gs2_pattern_get_offset / {0}".format(f_err(err)))
        return (hpat_cp.width, hpat_cp.height, off_x / 100, off_y / 100)

    @staticmethod
    def _plot(self, plot_obj=None, pattern_obj=None, **kwargs):
        return __class__._plot_list([self], 1, plot_obj=plot_obj, pattern_obj=pattern_obj, **kwargs)

    @staticmethod
    def _plot_list(self, num, plot_obj=None, pattern_obj=None, **kwargs):
        xs, ys = [], []

        for i in range(int(num)):
            xs.append(self[i]._get_x() / 100)
            ys.append(self[i]._get_y() / 100)

        axes = _pyplot_util.draw_points(xs, ys, plot_obj=plot_obj, **kwargs)
        if pattern_obj is not None:
            pat_w, pat_h, offset_x, offset_y = __class__._get_pattern_and_offset_size(
                pattern_obj)
            for x, y in zip(xs, ys):
                axes = _pyplot_util.draw_rect(
                    x - offset_x, y - offset_y, pat_w - 1, pat_h - 1, plot_obj=axes, **kwargs)
        return axes

    @staticmethod
    def bless(point_cls, attr_name_x, attr_name_y, attr_name_score):
        __class__._bless_attr(point_cls, {
            "x": attr_name_x, "y": attr_name_y, "score": attr_name_score
        }, float)

        if _ENABLE_PYPLOT:
            point_cls.plot = __class__._plot
            _basic_types._Referable.get_ptr_cls(
                point_cls).plot = __class__._plot_list


class _SearchResultProtocol (_StructProtocolBase):
    """
    - [ x-coordinate ] property : .x / method : _get_x(), _set_x( value )
    - [ y-coordinate ] property : .y / method : _get_y(), _set_y( value )
    - [ angle (deg) ] property : .q / method : _get_q(), _set_q( value )
    - [ scale (%) ] property : .s / method : _get_s(), _set_s( value )
    - [ score ] property : .score / method : _get_score(), _set_score( value )
    """
    @staticmethod
    def _get_pattern_and_offset_size(hfpm):
        if not hasattr(hfpm, "objtag") or hfpm.objtag != F_OBJID_FPM:
            raise ValueError(
                "FPM object (F_OBJID_FPM) is required (got {})".format(hfpm))
        w = INT()
        h = INT()
        err = fnFIE_fpm_get_pattern_size(hfpm, w, h)
        if F_ERR_NONE != err:
            raise RuntimeError(
                "failed fnFIE_fpm_get_pattern_size / {0}".format(f_err(err)))
        offset = DPNT_T()
        err = fnFIE_fpm_get_pattern_offset(hfpm, offset)
        if F_ERR_NONE != err:
            raise RuntimeError(
                "failed fnFIE_fpm_get_pattern_offset / {0}".format(f_err(err)))
        return (w, h, offset)

    @staticmethod
    def _get_bbox(x, y, q, s, pat_w, pat_h, offset):
        """FPMサーチ結果形式の座標値とパタン情報からバウンディングボックスを取得する。

        Parameters
        ----------
        x : float
        y : float
        q : float
            角度 (deg)
        s : float
            スケール (%)
        pat_w : int
        pat_h : int
        offset : DPNT_T

        Returns
        -------
        list
            pyplot.Polygon()に渡せる形式のバウンディングボックス
        """
        assert _ENABLE_NUMPY
        rad = q * math.pi / 180
        cos = math.cos(rad) * s / 100
        sin = math.sin(rad) * s / 100
        tform = _np.array([
            [cos, -sin, x],
            [+sin, cos, y],
            [0.0, 0.0, 1.0],
        ])
        bbox_homo = _np.array([
            [0.0,       0.0,       1.0],
            [pat_w - 1, 0.0,       1.0],
            [pat_w - 1, pat_h - 1, 1.0],
            [0.0,       pat_h - 1, 1.0]
        ])
        bbox_homo -= _np.array([offset.x, offset.y, 0])
        transed_bbox_homo = tform.dot(bbox_homo.T).T
        bbox = [(transed_bbox_homo[i, 0], transed_bbox_homo[i, 1])
                for i in range(4)]
        return bbox

    @staticmethod
    def _plot(self, plot_obj=None, pattern_obj=None, **kwargs):
        return __class__._plot_list([self], 1, plot_obj=plot_obj, pattern_obj=pattern_obj, **kwargs)

    @staticmethod
    def _plot_list(self, num, plot_obj=None, pattern_obj=None, **kwargs):
        xs, ys, qs, ss = [], [], [], []

        for i in range(int(num)):
            xs.append(self[i]._get_x())
            ys.append(self[i]._get_y())
            qs.append(self[i]._get_q())
            ss.append(self[i]._get_s())

        axes = _pyplot_util.draw_points(xs, ys, plot_obj=plot_obj, **kwargs)
        if pattern_obj is not None:
            pat_w, pat_h, offset = __class__._get_pattern_and_offset_size(
                pattern_obj)
            for x, y, q, s in zip(xs, ys, qs, ss):
                bbox = __class__._get_bbox(x, y, q, s, pat_w, pat_h, offset)
                axes = _pyplot_util.draw_polygon(bbox, plot_obj=axes, **kwargs)
        return axes

    @staticmethod
    def bless(point_cls, attr_name_x, attr_name_y, attr_name_q, attr_name_s, attr_name_score):
        __class__._bless_attr(point_cls, {
            "x": attr_name_x, "y": attr_name_y,
            "q": attr_name_q, "s": attr_name_s,
            "score": attr_name_score
        }, float)

        if _ENABLE_PYPLOT:
            point_cls.plot = __class__._plot
            _basic_types._Referable.get_ptr_cls(
                point_cls).plot = __class__._plot_list


class _LibRegister:

    __ctypes_type_tbl = {
        "c_bool": _cty.c_bool,
        "c_char": _cty.c_char,
        "c_wchar": _cty.c_wchar,
        "c_byte": _cty.c_byte,
        "c_ubyte": _cty.c_ubyte,
        "c_short": _cty.c_short,
        "c_ushort": _cty.c_ushort,
        "c_int": _cty.c_int,
        "c_uint": _cty.c_uint,
        "c_long": _cty.c_long,
        "c_ulong": _cty.c_ulong,
        "c_longlong": _cty.c_longlong,
        "c_ulonglong": _cty.c_ulonglong,
        "c_float": _cty.c_float,
        "c_double": _cty.c_double,
        "c_longdouble": _cty.c_longdouble,
        "c_char_p": _cty.c_char_p,
        "c_wchar_p": _cty.c_wchar_p,
        "c_void_p": _cty.c_void_p
    }

    __ignore_type_name = [
        "void"
    ]

    __ignore_func_name = []

    def __init__(self):
        self._type_tbl = {}

        self._conv_ctypes_tbl = _LibRegister.__ctypes_type_tbl.copy()

        self._ignore_type_name = _LibRegister.__ignore_type_name.copy()
        self._ignore_func_name = _LibRegister.__ignore_func_name.copy()

        self._replace_func = {}

        self.missing_builtin_type = []
        self.missing_typedef = []
        self.missing_deriv_typedef = []
        self.missing_struct = []
        self.missing_union = []
        self.missing_function = []

        self.export_struct = {}
        self.export_union = {}
        self.export_function = {}

        self.lib_list = None

    def set_type_tbl(self, type_cls, type_name=None):
        if not type_name:
            type_name = type_cls.__name__

        self._type_tbl[type_name] = type_cls

    def get_type(self, type_name):
        '''
        type_name (str) で指定された型のクラスオブジェクトを返す.
        type_name で指定する型は set_type_tbl() により登録した型, もしくはその派生型(ポインタ または 配列)
        でなければならない. (派生型が存在しない場合は生成される)

        ex)
        get_type("INT")
        get_type("PNT_T")
        get_type("INT.*.*")
        get_type("INT.[3].[4]")
        '''

        if not "." in type_name:
            return self._type_tbl.get(type_name, None)

        type_cls = self._type_tbl.get(type_name.split(".")[0], None)
        if not type_cls:
            return None

        suffix_list = type_name.split(".")[1:]

        while 0 < len(suffix_list):
            if '*' != suffix_list[-1]:
                break

            suffix_list.pop()
            type_cls = _basic_types._Referable.get_ptr_cls(type_cls)

        if len(suffix_list) < 1:
            return type_cls

        array_size_list = []
        for array_str in suffix_list:
            array_str = array_str.strip()
            array_size = -1

            try:
                if ("[" != array_str[0]) or ("]" != array_str[-1]):
                    raise ValueError()

                array_size = int(array_str[1:-1])
            except Exception:
                array_size = -1

            if array_size < 1:
                return None

            array_size_list.append(array_size)

        if 0 < len(array_size_list):
            type_cls = _basic_types._Arrayble.create_cls(
                type_cls, *array_size_list)

        return type_cls

    def set_replace_func(self, func_name, replace_name="__noname"):
        self._replace_func[func_name] = replace_name

    def regist_enum(self, enum_decl_list):
        if not enum_decl_list:
            return

        for enum_decl in enum_decl_list:
            tag = enum_decl["name"].strip()
            contents = enum_decl["contents"]

            if tag:
                if _is_toplevel(tag):
                    enum_cls = _get_toplevel(tag)
                else:
                    enum_cls = _basic_types._EnumRepr.create_cls(tag)
                    _set_toplevel(enum_cls, tag)

                for item in contents:
                    enum_cls.set_enum_item(item["name"], item["val"])

                self.set_type_tbl(enum_cls, type_name=tag)

            for item in contents:
                _set_toplevel(item["val"], item["name"])

    def regist_define(self, define_decl_list):
        if not define_decl_list:
            return

        for define_decl in define_decl_list:
            defname = define_decl.get("name", "").strip()
            defval = define_decl.get("val",  None)

            if not defname:
                continue

            _set_toplevel(defval, defname)

    def regist_types(self, types_decl_dict):
        if not types_decl_dict:
            return

        void_cls = type("void", (), {})
        void_cls.PTR = type(
            "C_void_p", (_basic_types._VoidPointer, ), {})
        void_cls.has_PTR = True

        void_cls.PTR.__value_org = void_cls.PTR.value

        def _vp_value_getter(_self):
            return _self.__value_org

        def _vp_value_setter(_self, v):
            _basic_types._PointerManage.share_resource(v, _self)

            if not v:
                v = None
            if isinstance(v, void_cls.PTR):
                v = v.__value_org
            elif hasattr(v, "contents"):
                v = _cty.addressof(v.contents)

            _self.__value_org = v

        void_cls.PTR.value = property(_vp_value_getter, _vp_value_setter)

        void_cls.PTR.bless_ptr()
        self.set_type_tbl(void_cls, "void")
        _set_toplevel(void_cls, "void")

        builtin_decl_list = types_decl_dict.get("builtin", [])

        for builtin_decl in builtin_decl_list:
            new_name = builtin_decl.get("name",   "").strip()
            ctypes_str = builtin_decl.get("ctypes", "").strip()
            if not new_name:
                continue
            if new_name in self._ignore_type_name:
                continue

            if not ctypes_str in self._conv_ctypes_tbl:
                if not new_name in self.missing_builtin_type:
                    self.missing_builtin_type.append(new_name)
                continue

            ctypes_cls = self._conv_ctypes_tbl[ctypes_str]

            new_cls = _basic_types._Numerical.create_cls(new_name, ctypes_cls)

            self.set_type_tbl(new_cls, new_name)
            _set_toplevel(new_cls, new_name)

        typedef_decl_list = types_decl_dict.get("typedef", [])

        for typedef_decl in typedef_decl_list:
            new_name = typedef_decl.get("name",   "").strip()
            ctypes_str = typedef_decl.get("ctypes", "").strip()
            if not new_name:
                continue
            if new_name in self._ignore_type_name:
                continue

            if ctypes_str == "VOID_MARK":
                alias_void = self.get_type("void")
                self.set_type_tbl(alias_void, new_name)
                _set_toplevel(alias_void, new_name)
                continue

            if not ctypes_str in self._conv_ctypes_tbl:
                if not new_name in self.missing_typedef:
                    self.missing_typedef.append(new_name)
                continue

            ctypes_cls = self._conv_ctypes_tbl[ctypes_str]

            new_cls = _basic_types._Numerical.create_cls(new_name, ctypes_cls)

            self.set_type_tbl(new_cls, new_name)
            _set_toplevel(new_cls, new_name)

        deriv_typedef_decl_list = types_decl_dict.get(
            "ptr_typedef", []) + types_decl_dict.get("array_typedef", [])

        for deriv_typedef_decl in deriv_typedef_decl_list:
            new_name = deriv_typedef_decl.get("name", "").strip()
            type_str = deriv_typedef_decl.get("type", "").strip()
            if not new_name:
                continue
            if new_name in self._ignore_type_name:
                continue

            base_cls = self.get_type(type_str)
            if not base_cls:
                if not new_name in self.missing_deriv_typedef:
                    self.missing_deriv_typedef.append(new_name)
                continue

            new_cls = type(new_name, (base_cls, ), {})
            self.set_type_tbl(new_cls, new_name)
            _set_toplevel(new_cls, new_name)

    def _regist_struct(self, struct_decl_list, struct_pack=8):
        '''
        Returns : list of registered structure name.
        '''

        fixed_struct_name_list = []
        for struct_decl in struct_decl_list:
            struct_name = struct_decl.get("name", "").strip()
            if not struct_name:
                continue

            wrap_fields_list = []
            for member_decl in struct_decl.get("members", []):
                member_name = member_decl.get("name", "").strip()

                type_str = member_decl.get("type", "").strip()
                type_cls = self.get_type(type_str)

                if (not type_cls) or (not member_name):
                    wrap_fields_list = None
                    break

                wrap_fields_list.append(
                    _basic_types._SUBase._wrap_field_item(member_name, type_cls))

            if not wrap_fields_list:
                continue

            struct_cls = _basic_types._StructBase._create_cls(
                struct_name, struct_pack, wrap_fields_list)
            self.set_type_tbl(struct_cls, struct_name)
            _set_toplevel(struct_cls, struct_name)
            self.export_struct[struct_name] = struct_cls

            fixed_struct_name_list.append(struct_name)

        return fixed_struct_name_list

    def _regist_union(self, union_decl_list, union_pack=8):
        '''
        Returns : list of registered union name.
        '''

        fixed_union_name_list = []
        for union_decl in union_decl_list:
            union_name = union_decl.get("name", "").strip()
            if not union_name:
                continue

            wrap_fields_list = []
            for member_decl in union_decl.get("members", []):
                member_name = member_decl.get("name", "").strip()

                type_str = member_decl.get("type", "").strip()
                type_cls = self.get_type(type_str)

                if (not type_cls) or (not member_name):
                    wrap_fields_list = None
                    break

                wrap_fields_list.append(
                    _basic_types._SUBase._wrap_field_item(member_name, type_cls))

            if not wrap_fields_list:
                continue

            union_cls = _basic_types._UnionBase._create_cls(
                union_name, union_pack, wrap_fields_list)
            self.set_type_tbl(union_cls, union_name)
            _set_toplevel(union_cls, union_name)
            self.export_union[union_name] = union_cls

            fixed_union_name_list.append(union_name)

        return fixed_union_name_list

    def regist_struct_union(self, struct_decl_list, union_decl_list, struct_pack=8, union_pack=8):
        struct_decl_list = struct_decl_list.copy()
        union_decl_list = union_decl_list.copy()
        loop_limit = 100
        for i in range(loop_limit):
            fixed_struct_name_list = self._regist_struct(
                struct_decl_list, struct_pack)
            fixed_union_name_list = self._regist_union(
                union_decl_list,  union_pack)

            struct_decl_list = [
                struct_decl for struct_decl in struct_decl_list
                if not struct_decl["name"] in fixed_struct_name_list]
            union_decl_list = [
                union_decl for union_decl in union_decl_list
                if not union_decl["name"] in fixed_union_name_list]

            if(
                (len(struct_decl_list) < 1 or len(fixed_struct_name_list) < 1) and
                (len(union_decl_list) < 1 or len(fixed_union_name_list) < 1)
            ):
                break

        for e in struct_decl_list:
            if not e["name"] in self.missing_struct:
                self.missing_struct.append(e["name"])

        for e in union_decl_list:
            if not e["name"] in self.missing_union:
                self.missing_union.append(e["name"])

    @staticmethod
    def _wrap_function(result, func, args):

        if hasattr(func, "_hook_after_execute"):
            func._hook_after_execute(result, args)

        for arg_cls, arg_obj in zip(func.argtypes, args):
            if hasattr(arg_cls, "_as_out_param_"):
                arg_cls._as_out_param_(func, arg_obj)

        if _cty_util.is_ptr(result):
            if not result.value:
                return None

        if hasattr(result, "_as_result_") and hasattr(result._as_result_, "__call__"):
            return result._as_result_(func, args)

        return result

    def regist_function(self, func_decl_list, lib_path_list, calling_convention):

        dlltype = None
        if "stdcall" == calling_convention:
            dlltype = _cty.windll
        elif "cdecl" == calling_convention:
            dlltype = _cty.cdll
        elif hasattr(_cty, calling_convention):
            dlltype = getattr(_cty, calling_convention)

        if not dlltype:
            raise RuntimeError(
                "invalid dll type ({0})".format(calling_convention))
        is_py38_or_more = _sys.version_info.major > 3 or (_sys.version_info.major == 3 and _sys.version_info.minor >= 8)
        if _util.get_platform() == "Windows" and is_py38_or_more:
            wil_dll_dir = _os.path.expandvars("%WIL3_1_0X64%")
            if wil_dll_dir == "%WIL3_1_0X64%":
                _dbg.DEBUG_PRINT("Failed to expand env var: %WIL3_1_0X64%")
            else:
                _os.add_dll_directory(wil_dll_dir)
                _dbg.DEBUG_PRINT("Added DLL directory: " + wil_dll_dir)

        lib_list = []
        libs_not_found = []
        libs_load_failed = []
        for arg_lib_path in lib_path_list:

            arg_lib_path = _util.resolve_path(arg_lib_path)
            lib_path = None

            if not lib_path:
                if _os.path.exists(arg_lib_path):
                    lib_path = arg_lib_path

            if not lib_path:
                cur_lib_path = _util.resolve_path(
                    _os.path.basename(arg_lib_path))
                if _os.path.exists(cur_lib_path):
                    lib_path = cur_lib_path

            if not lib_path:
                _dbg.DEBUG_PRINT("> can't find Library: ", arg_lib_path)
                libs_not_found.append(arg_lib_path)
                continue

            try:
                lib_list.append(
                    dlltype.LoadLibrary(lib_path)
                )
                _dbg.DEBUG_PRINT("> Load Library Succeed:", lib_path)
            except Exception:
                _dbg.DEBUG_PRINT("> (!!) Load Library Failed:", lib_path)
                _dbg.DEBUG_TRACE_PRINT()
                _dbg.DEBUG_PRINT()
                libs_load_failed.append(lib_path)

        if not lib_list:
            _dbg.DEBUG_PRINT("> no Library ...")
        
        if len(libs_not_found) > 0 or len(libs_load_failed) > 0:
            err_msg = "Failed to load some libraries. "
            if len(libs_not_found) > 0:
                err_msg += f"Not found: {libs_not_found}. "
            if len(libs_load_failed) > 0:
                err_msg += f"Load failed: {libs_load_failed}."
            raise ValueError(err_msg)

        if _dbg.ENABLE_DEBUG:
            self.lib_list = lib_list

        fie_doc_root = None
        doc_root_candidates = [
            _util.resolve_path("./fvalg_reference"),
        ]
        for doc_root in doc_root_candidates:
            if _os.path.exists(doc_root):
                fie_doc_root = pathlib.Path(doc_root).as_uri()

        for func_decl in func_decl_list:
            func_name = func_decl.get("name", "").strip()
            if not func_name:
                continue
            if func_name in self._ignore_func_name:
                continue

            try:
                func_obj = None
                for lib in lib_list:
                    func_obj = getattr(lib, func_name, None)
                    if func_obj is not None:
                        break

                if func_obj is None:
                    raise _BreakError()

                arg_list = []
                for arg_decl in func_decl["args"]:
                    arg_cls = self.get_type(arg_decl.get("type", "").strip())
                    if not arg_cls:
                        raise _BreakError()
                    if issubclass(arg_cls, _cty.Array):
                        arg_cls = _basic_types._Referable.get_ptr_cls(
                            arg_cls._type_)

                    arg_list.append(arg_cls)

                res_cls = None
                res_str = func_decl.get("restype", "").strip()
                if res_str in ("void", "VOID"):
                    res_cls = None
                else:
                    res_cls = self.get_type(res_str)
                    if res_cls is None:
                        raise _BreakError()

                if "param_doc" in func_decl:
                    param_doc = "Params:\n" + func_decl["param_doc"]
                else:
                    param_doc = ""
                if "retval_doc" in func_decl:
                    retval_doc = "Returns:\n" + func_decl["retval_doc"]
                else:
                    retval_doc = ""
                if fie_doc_root is not None and "doc_rel_url" in func_decl:
                    doc_url_str = "Detail:\n" +\
                        _os.path.join(fie_doc_root, func_decl["doc_rel_url"])
                else:
                    doc_url_str = ""

                func_obj.argtypes = arg_list
                func_obj.restype = res_cls
                func_obj.errcheck = __class__._wrap_function

                doc_str = "{0}\n{1}\n\n{2}\n\n{3}\n\n{4}".format(
                    func_decl.get("prototype_code", "").strip(),
                    func_decl.get(
                        "brief", ""), param_doc, retval_doc, doc_url_str
                )
                func_obj.__doc__ = doc_str

                if func_name in self._replace_func:
                    func_obj.__doc__ = "!!! don't call me ... {0}() !!!".format(
                        func_name)
                    func_name = self._replace_func[func_name]

                _set_toplevel(func_obj, func_name)
                self.export_function[func_name] = func_obj
                if func_name.startswith("fnFIE_"):
                    func_name_short = func_name[6:]
                    if func_name_short in _decl_skelton.__dict__:
                        _decl_skelton.__dict__[
                            func_name_short].__doc__ = doc_str

            except _BreakError:
                self.missing_function.append(func_name)

    def regist_alias(self, alias_decl_list):
        for alias_decl in alias_decl_list:
            alias_name, alias_type, alias_val = (
                alias_decl["name"], alias_decl["type"], alias_decl["value"]
            )

            if "eval" == alias_type:
                try:
                    target_obj = eval(alias_val)
                except Exception:
                    _dbg.DEBUG_PRINT(
                        "missing alias {0} = {1}".format(alias_name, alias_val))
                else:
                    _set_toplevel(target_obj, alias_name)
            else:
                pass

    def extension_type_char_p(self):

        def _from_param(cls, obj):
            if isinstance(obj, (str, bytes)):
                conv_obj = _cty_util.convert_string(obj, cls)
                if conv_obj is not None:
                    obj = conv_obj

            return obj

        @property
        def _value_as_bytes(self):
            return _cty.cast(self, _cty.c_char_p).value

        for type_name, type_cls in self._type_tbl.items():
            if not issubclass(type_cls, (_cty.c_char, _cty.c_byte)):
                continue

            type_ptr_cls = self.get_type(type_name + ".*")
            if not type_ptr_cls:
                continue

            type_ptr_cls.from_param = classmethod(_from_param)
            type_ptr_cls.value_as_bytes = _value_as_bytes

    def extension_struct_protocol(self, protocol_decl_dict):
        if not isinstance(protocol_decl_dict, dict):
            return

        def get_class_and_attr_names(proto_decl, proto_names):
            struct_name = proto_decl.get("struct_name")
            if struct_name is None:
                raise ValueError()
            struct_cls = self.get_type(struct_name)
            if not struct_cls:
                raise ValueError()
            attr_names = [proto_decl.get(proto_name)
                          for proto_name in proto_names]
            if any(
                name is None or not _StructProtocolBase._has_attr(
                    struct_cls, name) for name in attr_names):
                raise ValueError()
            return (struct_cls, attr_names)

        for point_decl in protocol_decl_dict.get("point_protocol", []):
            try:
                struct_cls, attr_names = get_class_and_attr_names(
                    point_decl, ["x", "y"])
            except ValueError:
                continue
            _PointProtocol.bless(struct_cls, *attr_names)

        for line_decl in protocol_decl_dict.get("line_protocol", []):
            try:
                struct_cls, attr_names = get_class_and_attr_names(
                    line_decl, ["a", "b", "c"])
            except ValueError:
                continue
            _LineProtocol.bless(struct_cls, *attr_names)

        for segment_decl in protocol_decl_dict.get("segment_protocol", []):
            try:
                struct_cls, attr_names = get_class_and_attr_names(
                    segment_decl, ["sx", "sy", "ex", "ey"])
            except ValueError:
                continue
            _SegmentProtocol.bless(struct_cls, *attr_names)

        for rect_decl in protocol_decl_dict.get("rect_protocol", []):
            try:
                struct_cls, attr_names = get_class_and_attr_names(
                    rect_decl, ["sx", "sy", "ex", "ey"])
            except ValueError:
                continue
            _RectProtocol.bless(struct_cls, *attr_names)

        for gs_decl in protocol_decl_dict.get("gs_result_protocol", []):
            try:
                struct_cls, attr_names = get_class_and_attr_names(
                    gs_decl, ["x", "y", "score"])
            except ValueError:
                continue
            _GsResultProtocol.bless(struct_cls, *attr_names)

        for search_result_decl in protocol_decl_dict.get("search_result_protocol", []):
            try:
                struct_cls, attr_names = get_class_and_attr_names(
                    search_result_decl, ["x", "y", "q", "s", "score"])
            except ValueError:
                continue
            _SearchResultProtocol.bless(struct_cls, *attr_names)

    def register_all(self, decl_manager, lib_path_list):
        self.regist_enum(decl_manager.get_enum_list())
        self.regist_define(decl_manager.get_define_list())

        self.regist_types(decl_manager.get_types_dict())
        self.extension_type_char_p()

        self.regist_struct_union(
            decl_manager.get_struct_list(),
            decl_manager.get_union_list(),
            struct_pack=decl_manager.get_struct_pack_size(),
            union_pack=decl_manager.get_union_pack_size()
        )

        self.extension_struct_protocol(
            decl_manager.get_struct_protocol_dict()
        )

        self.regist_function(
            decl_manager.get_function_list(),
            lib_path_list,
            decl_manager.get_calling_convention()
        )

        self.regist_alias(
            decl_manager.get_alias_list()
        )

def _warn_if_fie_version_not_compatible():
    major = USHORT()
    minor = USHORT()
    rev = USHORT()
    build = USHORT()
    desc = CHAR.PTR()
    if "get_lib_version" not in globals():
        warnings.warn("Failed to obtaining FIE version.",
            category=RuntimeWarning)
        return
    if get_lib_version(major, minor, rev, build, desc) != F_ERR_NONE:
        warnings.warn("Failed to obtaining FIE version.",
            category=RuntimeWarning)
        return
    if version._major != major or version._minor != minor:
        warnings.warn("FIE version does not match PyFIE version. "
            "Compatibility is not guaranteed and some features may not work. "
            f"Detected FIE version is {major}.{minor}.{rev}. PyFIE version is {__version__}. "
            f"PyFIE expects FIE version to be {version._major}.{version._minor}.{version._rev}.",
            category=RuntimeWarning)
class _Patches:
    _patch_cls_list = []

    @classmethod
    def regist(cls, patch_cls):
        cls._patch_cls_list.append(patch_cls)
        return patch_cls

    @classmethod
    def apply(cls, lib_register, patches_conf):
        for patch_cls in cls._patch_cls_list:
            status = patches_conf.get(
                getattr(patch_cls, "CONFIG", None), False
            )

            if status is True:
                if hasattr(patch_cls, "is_apply"):
                    if not patch_cls.is_apply():
                        status = False
                        _dbg.DEBUG_PRINT(
                            "Patch {0}: no need...".format(patch_cls.__name__))

            if status in (True, "FORCE"):
                patch_cls.apply(lib_register)
            else:
                _dbg.DEBUG_PRINT(
                    "Patch {0}: SKIP...".format(patch_cls.__name__))


class _FuncArgsCustomizer:
    def __init__(self, func):
        self.argtypes = func.argtypes
        self.restype = func.restype
        self.errcheck = func.errcheck
        self.__doc__ = func.__doc__

        self._func = func
        self._converters = []

    def __call__(self, *args):
        arg_list = []

        for arg_type, arg_val in zip(self.argtypes, args):
            if hasattr(arg_type, "from_param"):
                arg_val = arg_type.from_param(arg_val)

            arg_list.append(arg_val)

        for converter in self._converters:
            arg_list = converter(arg_list)

        return self._func(*arg_list)

    def current_argtypes(self):
        return self._func.argtypes

    def regist_converter(self, converter, converted_argtypes):
        if (converter is None) or (converted_argtypes is None):
            return

        self._converters.append(converter)
        self._func.argtypes = converted_argtypes

@_Patches.regist
class _Patch_ARM_VFP_CPRC:

    HFA_STRUCT = namedtuple("HFA_STRUCT", ("type", "num"))
    HFA_TYPES = {}

    CONFIG = "patch_arm_vfp_cprc"

    @classmethod
    def is_apply(cls):
        cpu = _util.get_processor().lower()
        return cpu.startswith("arm")

    @classmethod
    def apply(cls, lib_register):

        for st_cls in lib_register.export_struct.values():
            hfa_type = cls._gen_hfa_struct(st_cls)
            if not hfa_type:
                continue

            cls.HFA_TYPES[st_cls] = hfa_type
            _dbg.DEBUG_PRINT(
                "Patch/ARM_VFP_CPRC: HFA_TYPES {0} / {1}".format(st_cls.__name__, hfa_type))

        missing_function = []
        for func_name, func in lib_register.export_function.items():
            if cls._is_vfp_cprc_restype(func.restype):
                _dbg.DEBUG_PRINT(
                    "Patch/ARM_VFP_CPRC: delete {0}()/ restype = {1}".format(
                        func_name, func.restype.__name__))
                _del_toplevel(func_name)
                missing_function.append(func_name)

        for func_name in missing_function:
            del lib_register.export_function[func_name]
            lib_register.missing_function.append(func_name)

        new_export_function = {}
        for func_name, func in lib_register.export_function.items():
            if not cls._is_vfp_cprc_argtypes(func.argtypes):
                continue

            new_func = cls._apply_func_patch(func)
            _dbg.DEBUG_PRINT(
                "Patch/ARM_VFP_CPRC: apply {0}()".format(func_name))

            _set_toplevel(new_func, func_name)
            new_export_function[func_name] = new_func

        for func_name, new_func in new_export_function.items():
            lib_register.export_function[func_name] = new_func

    @classmethod
    def _is_vfp_cprc_argtypes(cls, argtypes):
        for arg in argtypes:
            if arg in cls.HFA_TYPES:
                return True

        return False

    @classmethod
    def _is_vfp_cprc_restype(cls, restype):
        if restype in cls.HFA_TYPES:
            return True

        return False

    @classmethod
    def _apply_func_patch(cls, func):
        if not isinstance(func, _FuncArgsCustomizer):
            func = _FuncArgsCustomizer(func)

        cur_argtypes = func.current_argtypes()

        func.regist_converter(
            cls._convert_args,
            cls._convert_argtypes(cur_argtypes)
        )

        return func

    @classmethod
    def _gen_hfa_struct(cls, type_obj):
        if not issubclass(type_obj, _cty.Structure):
            return None

        elems = _cty_util.serialize_compound_type(type_obj)

        if not elems:
            return None
        base_type = elems[0]
        if not issubclass(base_type, _basic_types._Numerical):
            return None
        if base_type._python_type is not float:
            return None

        num = 0
        for elem_type in elems:
            if elem_type is not base_type:
                return None
            num += 1

        if 4 < num:
            return None

        return cls.HFA_STRUCT(base_type, num)

    @classmethod
    def _convert_argtypes(cls, src_argtypes):
        dst_argtypes = []

        for argtype in src_argtypes:
            if argtype in cls.HFA_TYPES:
                dst_argtypes.extend(
                    cls._decomp_hfa_type(argtype)
                )
            else:
                dst_argtypes.append(argtype)

        return dst_argtypes

    @classmethod
    def _convert_args(cls, src_args):
        dst_args = []

        for arg in src_args:
            if type(arg) in cls.HFA_TYPES:
                dst_args.extend(
                    cls._decomp_hfa_obj(arg)
                )
            else:
                dst_args.append(arg)

        return dst_args

    @classmethod
    def _decomp_hfa_type(cls, hfa_type):
        if _dbg.ENABLE_DEBUG and not isinstance(hfa_type, type):
            raise RuntimeError()

        hfa_struct = cls.HFA_TYPES.get(hfa_type, None)
        if not hfa_struct:
            return (hfa_type, )

        return (hfa_struct.type, ) * hfa_struct.num

    @classmethod
    def _decomp_hfa_obj(cls, hfa_obj):
        if _dbg.ENABLE_DEBUG and isinstance(hfa_obj, type):
            raise RuntimeError()

        hfa_struct = cls.HFA_TYPES.get(type(hfa_obj), None)
        if not hfa_struct:
            return (hfa_obj, )

        base_type = hfa_struct.type

        p = base_type.PTR.cast(hfa_obj.ref)
        elem_list = []
        for i in range(hfa_struct.num):
            elem_list.append(p[i])

        return tuple(elem_list)


class FHANDLE(_cty.c_void_p, _basic_types._Referable, _basic_types._Arrayble, _basic_types._FromParamSentinel):

    class _HandleManager:

        handle_table = weakref.WeakValueDictionary()
        table_mutex = Lock()

        class _HandleCore:
            __gc_manage__ = True

            def __init__(self, adrs):
                self.adrs = adrs

            def __del__(self):
                if (not self.adrs) or (not self.__gc_manage__):
                    _dbg.DEBUG_PRINT(
                        "GC Disable: handle={0}".format(self.adrs))
                    return

                objtag = int(fnFIE_get_objtype(self.adrs))
                if not objtag in f_objtag.get_enum_items():
                    _dbg.DEBUG_PRINT(
                        "GC Disable: objtag={0}, handle={1}".format(objtag, self.adrs))
                    return

                _dbg.DEBUG_PRINT("GC: objtag={0}, handle={1}".format(
                    f_objtag(objtag), self.adrs))
                _org_fnFIE_free_object(self.adrs)

            def dispose(self):
                if not int(fnFIE_get_objtype(self.adrs)) in f_objtag.get_enum_items():
                    return

                _org_fnFIE_free_object(self.adrs)
                self.adrs = 0

        @classmethod
        def get_handle(cls, adrs):
            if not adrs:
                return None

            with cls.table_mutex:
                if not adrs in cls.handle_table:
                    handle = cls._HandleCore(adrs)
                    cls.handle_table[adrs] = handle

            return cls.handle_table[adrs]

        @classmethod
        def dbg_get_manage_handles(cls):
            return tuple(cls.handle_table.keys())

    _handle_core = None

    def _as_result_(self, func, args):
        self._handle_core = __class__._HandleManager.get_handle(self.value)

        return self

    __value_org = _cty.c_void_p.value

    def __value_getter(self):
        return self.__value_org

    def __value_setter(self, v):

        if not v:
            self._handle_core = None
            self.__value_org = None
            _basic_types._PointerManage.clear_resource(self)
            return

        if not isinstance(v, self.__class__):
            raise RuntimeError("{0} is not FHANDLE".format(v))

        value = v.value
        self._handle_core = __class__._HandleManager.get_handle(value)
        self.__value_org = value
        _basic_types._PointerManage.share_resource(v, self)

    value = property(__value_getter, __value_setter)

    def __repr__(self):
        if self.is_image:
            return "FHANDLE: " + self.__repr_img()
        else:
            return "FHANDLE: " + self.objtag.__repr__()

    def _repr_png_(self):
        """IPythonで画像を表示する"""
        if not self.is_image:
            return None
        if self.is_gpu_image:
            himg_cpu = self.clone(device="cpu")
            return himg_cpu._repr_png_()
        if self.ch != 1 and self.ch != 3:
            return None
        if self.ch > 1 and (self.f_type == F_IMG_RGBQUAD or self.f_type == F_IMG_RGBTRIPLE):
            return None
        is_img_size_small_enough = self.width <= ctrl._IPYTHON_MAX_DISPLAY_IMAGE_SIZE and self.height <= ctrl._IPYTHON_MAX_DISPLAY_IMAGE_SIZE
        if not is_img_size_small_enough:
            warnings.warn(
                "Image display for IPython is disabled because the image is too large. "
                "To display this large image, "
                "please set a larger size limit with pyfie.ctrl.set_ipython_max_display_image_size() function.",
                category=RuntimeWarning)
            return None

        can_encode_as_png_natively = (
            (self.f_type == F_IMG_BIN and self.ch == 1) or
            (self.f_type == F_IMG_UC8) or
            (self.f_type == F_IMG_US16) or
            (self.f_type == F_IMG_RGBQUAD)
        )
        if can_encode_as_png_natively:
            himg = self
        else:
            if self.f_type == F_IMG_RGBTRIPLE:
                himg = self.empty_like(img_type=F_IMG_RGBQUAD)
                iret = fnFIE_img_copy(self, himg)
                if F_ERR_NONE != iret:
                    raise RuntimeError(
                        "failed fnFIE_img_copy / {0}".format(f_err(iret)))
            else:
                himg = self.empty_like(img_type=F_IMG_UC8)
                copy_ex_params = {
                    F_IMG_BIN: (0, 0, UC8_MAX),
                    F_IMG_S16: (0, S16_MIN, UC8_MAX / US16_MAX),
                    F_IMG_I32: (0, I32_MIN, UC8_MAX / UI32_MAX),
                    F_IMG_UI32: (0, 0, UC8_MAX / UI32_MAX),
                    F_IMG_I64: (0, L64_MIN, UC8_MAX / L64_MAX),
                    F_IMG_FLOAT: (1, 0, 0),
                    F_IMG_DOUBLE: (1, 0, 0),
                }[self.f_type]
                iret = fnFIE_img_copy_ex(self, himg, *copy_ex_params)
                if F_ERR_NONE != iret:
                    raise RuntimeError(
                        "failed fnFIE_img_copy_ex / {0}".format(f_err(iret)))
        try:
            png_bytes = imencode(himg, format_ext="png", comp_level=0)
            return png_bytes
        except Exception:
            warnings.warn(
                "imencode failed unexpectedly. Image display for IPython is disabled for this image.",
                category=RuntimeWarning)
        return None

    @classmethod
    def from_param(cls, obj):
        if _ENABLE_NUMPY:
            if isinstance(obj, _np.ndarray):
                conv_obj = __class__._import_from_ndarray(
                    obj, keep_nimg=False)
                if conv_obj is not None:
                    obj = conv_obj
        if isinstance(obj, (list, tuple)) and all(isinstance(e, FHANDLE) and e.is_image for e in obj):
            hstack = fnFIE_imgstack_alloc(F_IMGSTACK_CHILD_MODE, False)
            for himg in obj:
                iret = fnFIE_imgstack_push_back(hstack, himg)
                if F_ERR_NONE != iret:
                    break
            else:
                obj = hstack

        return super().from_param(obj)

    @property
    def objtag(self):
        """インスタンスの FIE オブジェクトタグ"""
        try:
            return f_objtag(fnFIE_get_objtype(self))
        except Exception:
            return None

    def clone(self, device=None):
        """
        FIE オブジェクトの複製を行います。

        FIE オブジェクトが画像オブジェクトである場合、 ``fnFIE_img_root_alloc()`` と
        ``fnFIE_img_copy()`` を用いて複製が行われます。

        それ以外の FIE オブジェクトでは、 ``fnFIE_copy_object()`` により複製が行われます。

        :return: 複製された FIE オブジェクト（``FHANDLE``） を返します。
        """
        dst = None
        if self.is_image:
            if device is None:
                root_alloc = self._img_root_alloc
                img_copy = self._img_copy
            elif device == "cpu":
                root_alloc = fnFIE_img_root_alloc
                img_copy = fnFIE_img_copy if self.is_cpu_image else fnFGA_img_copy
            elif device == "gpu":
                root_alloc = fnFGA_img_root_alloc
                img_copy = fnFGA_img_copy
            else:
                raise ValueError("Unsupported device {0}".format(device))
            params = self._img_params
            dst = root_alloc(
                params["type"], params["ch"], params["w"], params["h"])
            iret = img_copy(self, dst)
            if F_ERR_NONE != iret:
                raise RuntimeError(
                    "failed image clone / {0}".format(f_err(iret)))
        else:
            dst = fnFIE_copy_object(self)

        if dst is None:
            raise RuntimeError("failed clone handle")

        return dst

    def __repr_img(self):
        params = self._img_params
        if not params:
            return ""

        if self.is_gpu_image:
            return "{0} (GPU), {1} x {2}, ({3} ch)".format(
                params["type"], params["w"], params["h"], params["ch"])
        else:
            return "{0}, {1} x {2}, ({3} ch)".format(
                params["type"], params["w"], params["h"], params["ch"])

    @property
    def is_cpu_image(self):
        return (
            f_objtag.F_OBJID_IMG_ROOT == self.objtag or
            f_objtag.F_OBJID_IMG_CHILD == self.objtag)

    @property
    def is_gpu_image(self):
        return (
            F_OBJID_IMG_ROOT_GPU == self.objtag or
            F_OBJID_IMG_CHILD_GPU == self.objtag)

    @property
    def is_image(self):
        """
        インスタンスが画像オブジェクトの場合は True に、
        それ以外のオブジェクトの場合は False となります。
        """
        return self.is_cpu_image or self.is_gpu_image

    @property
    def is_imgstack(self):
        """
        インスタンスが画像スタックオブジェクトの場合は True に、
        それ以外のオブジェクトの場合は False となります。
        """
        return f_objtag.F_OBJID_IMG_STACK == self.objtag

    @property
    def _img_params(self):
        """
        dict {"ch": int, "type": f_imgtype, "step": int, "w": int, "h": int}
        """

        ch, t, w, h, s = INT(), INT(), INT(), INT(), INT_PTR()
        if self.is_gpu_image:
            get_params = fnFGA_img_get_params
        else:
            get_params = fnFIE_img_get_params
        if F_ERR_NONE != get_params(self, ch.adrs, t.adrs, s.adrs, w.adrs, h.adrs):
            return None

        return {"ch": ch.value, "type": f_imgtype(t), "step": s.value, "w": w.value, "h": h.value}

    @property
    def f_type(self):
        """インスタンスの画像型"""
        if self.is_gpu_image:
            val = fnFGA_img_get_type(self)
        else:
            val = fnFIE_img_get_type(self)
        if val == -1:
            raise TypeError("{0} is not image, or licensing error".format(self))
        return val.value

    @property
    def ch(self):
        """インスタンスのチャネル数"""
        if self.is_gpu_image:
            val = fnFGA_img_get_channels(self)
        else:
            val = fnFIE_img_get_channels(self)
        if val == -1:
            raise TypeError("{0} is not image, or licensing error".format(self))
        return val.value

    @property
    def width(self):
        """インスタンスの画像幅"""
        if self.is_gpu_image:
            val = fnFGA_img_get_width(self)
        else:
            val = fnFIE_img_get_width(self)
        if val == -1:
            raise TypeError("{0} is not image, or licensing error".format(self))
        return val.value

    @property
    def height(self):
        """インスタンスの画像高さ"""
        if self.is_gpu_image:
            val = fnFGA_img_get_height(self)
        else:
            val = fnFIE_img_get_height(self)
        if val == -1:
            raise TypeError("{0} is not image, or licensing error".format(self))
        return val.value

    @property
    def step(self):
        """インスタンスのステップ数"""
        if self.is_gpu_image:
            val = fnFGA_img_get_step(self)
        else:
            val = fnFIE_img_get_step(self)
        if val == -1:
            raise TypeError("{0} is not image, or licensing error".format(self))
        return val.value

    @property
    def _img_root_alloc(self):
        if self.is_gpu_image:
            return fnFGA_img_root_alloc
        else:
            return fnFIE_img_root_alloc

    @property
    def _img_child_alloc(self):
        if self.is_gpu_image:
            return fnFGA_img_child_alloc
        else:
            return fnFIE_img_child_alloc

    @property
    def _img_child_alloc_single_ch(self):
        if self.is_gpu_image:
            return fnFGA_img_child_alloc_single_ch
        else:
            return fnFIE_img_child_alloc_single_ch

    @property
    def _img_copy(self):
        if self.is_gpu_image:
            return fnFGA_img_copy
        else:
            return fnFIE_img_copy

    @property
    def _img_clear(self):
        if self.is_gpu_image:
            return fnFGA_img_clear
        else:
            return fnFIE_img_clear

    @property
    def _img_child_alloc_single_ch(self):
        if self.is_gpu_image:
            return fnFGA_img_child_alloc_single_ch
        else:
            return fnFIE_img_child_alloc_single_ch

    @property
    def _img_child_alloc_single_ch(self):
        if self.is_gpu_image:
            return fnFGA_img_child_alloc_single_ch
        else:
            return fnFIE_img_child_alloc_single_ch

    def roi(self, x, y, w=10, h=10, ch=None):
        """
        インスタンスの指定領域に対するチャイルド画像を生成します。
        (チャイルド画像については FIE ライブラリのリファレンスマニュアルを参照してください)

        パラメータ **x** 及び **y** で領域の左上座標を、
        パラメータ **w** 及び **h** で領域のサイズを指定してください。

        パラメータ **ch** にチャネル番号を指定すると、
        単一チャネルのチャイルド画像が生成されます。

        :param x: 領域の左上 x 座標を指定します。
        :param y: 領域の左上 y 座標を指定します。
        :param w: 領域の幅を指定します。
        :param h: 領域の高さを指定します。
        :param ch: チャネル番号を指定します。

        :return: 生成された画像オブジェクト（チャイルド画像）を返します。
        """
        if not self.is_image:
            raise RuntimeError("{0} is not image.".format(self))

        if ch is None:
            roi_img = self._img_child_alloc(self, x, y, w, h)
        else:
            roi_img = self._img_child_alloc_single_ch(self, ch, x, y, w, h)

        return roi_img

    def single_ch(self, ch):
        """
        インスタンスの指定チャネルに対するチャイルド画像を生成します。
        (チャイルド画像については FIE ライブラリのリファレンスマニュアルを参照してください)

        生成されるチャネル画像は（ インスタンスと）同じ画像サイズの単一チャネル画像となります。

        :param ch: チャネル番号を指定します。

        :return: 生成された画像オブジェクト（チャイルド画像）を返します。
        """
        if not self.is_image:
            raise RuntimeError("{0} is not image.".format(self))

        params = self._img_params
        return self._img_child_alloc_single_ch(self, ch, 0, 0, params["w"], params["h"])

    def empty_like(self, img_type=None, w=None, h=None, ch=None, device=None):
        """
        インスタンスと同サイズの画像オブジェクト（ルート画像）を新たに確保し返します。
        （ルート画像については FIE ライブラリのリファレンスマニュアルを参照してください）

        返される画像オブジェクトは確保直後の状態であり、
        したがってその画素値は不定な状態です。

        確保する画像オブジェクトの画像型・幅・高さ・チャネル数をそれぞれパラメータ **img_type**, **w**, **h**, **ch** で指定することができます。
        指定しなかった場合には インスタンスと同じ画像型・幅・高さ・チャネル数となります。

        インスタンスが NULL チャイルド画像であった場合には、
        新たな NULL チャイルド画像を確保し返します。
        （NULL チャイルド画像については FIE ライブラリのリファレンスマニュアルを参照してください）

        :param img_type: 画像型を指定します。
        :param w:  画像幅を指定します。
        :param h:  画像高さを指定します。
        :param ch: 画像チャネル数を指定します。

        :return: 生成された画像オブジェクトを返します。
        """
        if not self.is_image:
            raise RuntimeError("{0} is not image.".format(self))

        params = self._img_params
        if 0 == params["type"]:
            if device is None:
                child_alloc = self._img_child_alloc
            elif device == "cpu":
                child_alloc = fnFIE_img_child_alloc
            elif device == "gpu":
                child_alloc = fnFGA_img_child_alloc
            else:
                raise ValueError("Unsupported device {0}".format(device))
            return child_alloc(0, 0, 0, 0, 0)
        else:
            if img_type is None:
                img_type = params["type"]
            if w is None:
                w = params["w"]
            if h is None:
                h = params["h"]
            if ch is None:
                ch = params["ch"]

            if device is None:
                root_alloc = self._img_root_alloc
            elif device == "cpu":
                root_alloc = fnFIE_img_root_alloc
            elif device == "gpu":
                root_alloc = fnFGA_img_root_alloc
            else:
                raise ValueError("Unsupported device {0}".format(device))
            return root_alloc(img_type, ch, w, h)

    def full_like(self, fill_value, img_type=None, w=None, h=None, ch=None, device=None):
        """
        インスタンスと同サイズの画像オブジェクト（ルート画像）を新たに確保し返します。

        返される画像オブジェクトのすべての画素値はパラメータ **fill_value** の値で初期化されます。

        パラメータ **img_type**, **w**, **h**, **ch** の意味は
        ``FHANDLE.empty_like`` と等価です。

        :param fill_value: 塗りつぶす濃度値を指定します。
        :param img_type: 画像型を指定します。
        :param w:  画像幅を指定します。
        :param h:  画像高さを指定します。
        :param ch: 画像チャネル数を指定します。

        :return: 生成された画像オブジェクトを返します。
        """
        himg = self.empty_like(img_type, w, h, ch, device)
        ret = himg._img_clear(himg, fill_value)
        if ret != F_ERR_NONE:
            return None
        return himg

    if _ENABLE_NUMPY:

        @property
        def ndarray(self):
            """
            画像オブジェクトの画像メモリを共有する :class:`numpy.ndarray` を返します。

            :return: 画像オブジェクトの画像メモリを共有する :class:`numpy.ndarray` を返します。
                     アタッチできない場合は None を返します。

            .. note::
                このプロパティでは
                内部で :func:`~FHANDLE.attach_to_ndarray` の呼び出しが行われます。
            """
            return self._attach_to_ndarray()

        @property
        def dtype(self):
            """
            インスタンスが画像オブジェクトである場合、
            下記のように画像型に対応した
            :class:`numpy.ndarray` の dtype （データ型） を返します。
      
            .. list-table::
               :header-rows: 1
      
               * - 画像型
                 - dtype
      
               * - F_IMG_UC8
                 - numpy.uint8
               * - F_IMG_S16
                 - numpy.int16
               * - F_IMG_US16
                 - numpy.uint16
               * - F_IMG_I32
                 - numpy.int32
               * - F_IMG_UI32
                 - numpy.uint32
               * - F_IMG_I64
                 - numpy.int64
               * - F_IMG_FLOAT
                 - numpy.float32
               * - F_IMG_DOUBLE
                 - numpy.float64
               * - F_IMG_RGBQUAD
                 - numpy.uint8
               * - F_IMG_RGBTRIPLE
                 - numpy.uint8
      
            .. note::
               インスタンスが画像オブジェクトではない場合、
               及び画像オブジェクトであっても対応する :class:`numpy.ndarray` の dtype がない場合には例外が発生します。
            """
            return self.__get_pixel_desc(self.f_type)["dtype"]

        def attach_to_ndarray(self):
            """
            画像オブジェクトの画像メモリを共有する :class:`numpy.ndarray` を返します。

            このとき、返される :class:`numpy.ndarray` は以下のようなものとなります。

            |

            **1 チャネル画像オブジェクトの場合**

            画像オブジェクトのチャネル数が 1 であった場合、
            :class:`numpy.ndarray` は同形状の 2 次元配列となります。

            ただし画像型が ``F_IMG_RGBTRIPLE`` または ``F_IMG_RGBQUAD`` の場合は、
            3 または 4 のコンポーネント（RGB）から構成される各画素の次元が追加されるため、
            :class:`numpy.ndarray` は 3 次元配列となります。

            下記に画像サイズが *w × h* である 1 チャネル画像オブジェクトに対する、
            :class:`numpy.ndarray` の dtype （データ型） 及び shape （形状）の対応を示します。

            .. list-table:: 1 チャネル画像オブジェクト (画像サイズ *w × h* )
                :header-rows: 1

                * - 画像型
                  - dtype
                  - shape

                * - F_IMG_BIN [#about_bin_unsupported]_
                  - N/A
                  - N/A
                * - F_IMG_UC8
                  - numpy.uint8
                  - (h, w)
                * - F_IMG_S16
                  - numpy.int16
                  - (h, w)
                * - F_IMG_US16
                  - numpy.uint16
                  - (h, w)
                * - F_IMG_I32
                  - numpy.int32
                  - (h, w)
                * - F_IMG_UI32
                  - numpy.uint32
                  - (h, w)
                * - F_IMG_I64
                  - numpy.int64
                  - (h, w)
                * - F_IMG_FLOAT
                  - numpy.float32
                  - (h, w)
                * - F_IMG_DOUBLE
                  - numpy.float64
                  - (h, w)
                * - F_IMG_RGBQUAD
                  - numpy.uint8
                  - (h, w, 4)
                * - F_IMG_RGBTRIPLE
                  - numpy.uint8
                  - (h, w, 3)

            .. [#about_bin_unsupported] 画像型 F_IMG_BIN に対する :class:`numpy.ndarray` へのアタッチは対応されていません。

            |

            **複数チャネル画像オブジェクトの場合**

            画像オブジェクトのチャネル数が複数であった場合の :class:`numpy.ndarray` は、
            各チャネルに対する :class:`numpy.ndarray` を要素にもつ 1 次元配列となります。

            つまりチャネル数が *n* の画像オブジェクトに対する :class:`numpy.ndarray` は、
            shape が *(n, )* 、 dtype が :class:`numpy.object` （つまり Python オブジェクトを要素にもつ）の 1 次元配列となり、
            その要素として *n* 個の "1 チャネル画像オブジェクトに対する :class:`numpy.ndarray`" が格納されていることになります。

            .. note::
                この仕様は、 FIE の画像オブジェクトが複数チャネル分の画像メモリを連続したメモリ領域ではなく、
                （チャネル毎に）個別に管理していることに由来しています。

            |

            :return: 画像オブジェクトの画像メモリを共有する :class:`numpy.ndarray` を返します。
                    アタッチできない場合は None を返します。
            """
            return self._attach_to_ndarray()

        def clone_to_ndarray(self, layered=False):
            r"""
            画像オブジェクトまたは画像スタックオブジェクトの画像データがコピーされた :class:`numpy.ndarray` を返します。
      
            このとき、返される :class:`numpy.ndarray` は以下のようなものとなります。
      
            |
      
            **1 チャネル画像オブジェクトの場合**
      
            画像オブジェクトのチャネル数が 1 であった場合、
            :class:`numpy.ndarray` は同形状の 2 次元配列となります。
      
            ただし画像型が ``F_IMG_RGBTRIPLE`` または ``F_IMG_RGBQUAD`` の場合は、
            3 または 4 のコンポーネント（RGB）から構成される各画素の次元が追加されるため、
            :class:`numpy.ndarray` は 3 次元配列となります。
      
            下記に画像サイズが *w × h* である 1 チャネル画像オブジェクトに対する、
            :class:`numpy.ndarray` の dtype （データ型） 及び shape （形状）を示します。
      
            .. list-table:: 1 チャネル画像オブジェクト (画像サイズ w × h)
               :header-rows: 1
      
               * - 画像型
                 - dtype
                 - shape
      
               * - F_IMG_BIN
                 - numpy.bool\_
                 - (h, w)
               * - F_IMG_UC8
                 - numpy.uint8
                 - (h, w)
               * - F_IMG_S16
                 - numpy.int16
                 - (h, w)
               * - F_IMG_US16
                 - numpy.uint16
                 - (h, w)
               * - F_IMG_I32
                 - numpy.int32
                 - (h, w)
               * - F_IMG_UI32
                 - numpy.uint32
                 - (h, w)
               * - F_IMG_I64
                 - numpy.int64
                 - (h, w)
               * - F_IMG_FLOAT
                 - numpy.float32
                 - (h, w)
               * - F_IMG_DOUBLE
                 - numpy.float64
                 - (h, w)
               * - F_IMG_RGBQUAD
                 - numpy.uint8
                 - (h, w, 4)
               * - F_IMG_RGBTRIPLE
                 - numpy.uint8
                 - (h, w, 3)
      
            |
      
            **複数チャネル画像オブジェクトの場合**
      
            画像オブジェクトが複数チャネルの場合、
            パラメータ **layered** によりチャネルを階層化するか否かを指定することができます。
      
            **layered** に True を指定した場合、
            チャネルは階層化され、
            同じチャネルにおける各画素が画像メモリ上で連続に配置された状態となります。
            この場合、画像サイズ *w × h* 、 チャネル数 *n* の画像オブジェクトに対する :class:`numpy.ndarray` の shape は *(n, h, w)* となります。
      
            **layered** に False を指定した場合、
            チャネルは階層化されず、
            各チャネルにおける同座標の画素が画像メモリ上で連続に配置された状態（すなわちチャネルをインタリーブした状態）となります。
            この場合、画像サイズ *w × h* 、 チャネル数 *n* の画像オブジェクトに対する :class:`numpy.ndarray` の shape は *(h, w, n)* となります。
      
            ただし画像型が ``F_IMG_RGBTRIPLE`` または ``F_IMG_RGBQUAD`` である場合、
            **layered** の指定に関わらず常にチャネルは階層化されます。
      
            下記に画像サイズが *w × h* である *n* チャネル画像オブジェクトに対する、
            :class:`numpy.ndarray` の shape を示します。
      
            .. list-table:: n チャネル画像オブジェクト (画像サイズ w × h)
               :header-rows: 1
      
               * - 画像型
                 - | shape
                   | **layered** = True
                 - | shape
                   | **layered** = False
      
               * - F_IMG_RGBQUAD
                 - (n, h, w, 4)
                 - (n, h, w, 4)
      
               * - F_IMG_RGBTRIPLE
                 - (n, h, w, 3)
                 - (n, h, w, 3)
      
               * - others
                 - (n, h, w)
                 - (h, w, n)
      
            |
      
            **画像スタックオブジェクトの場合**

            画像スタックオブジェクトに対しては、スタック内の各画像に対してそれぞれ本メソッドを適用して得られた :class:`numpy.ndarray` を np.stack で結合したものが返されます。
            画像スタック内の各画像が同じ型、サイズ、チャネル数でなければなりません。
      
            |
      
            :param layered: 複数チャネル画像オブジェクトの場合にチャネルの階層化を行うか否かを指定します。
      
            :return: コピーされた :class:`numpy.ndarray` を返します。
            """

            def F_CALL(iret):
                if F_ERR_NONE != iret:
                    raise RuntimeError(
                        "FIE error ({0})".format(f_err(iret)))
                return iret

            if self.is_gpu_image:
                himg_cpu = self.clone(device="cpu")
                return himg_cpu.clone_to_ndarray(layered)

            if self.is_imgstack:
                imgs = []
                n = fnFIE_imgstack_getnum(self)
                for i in range(n):
                    iret = INT()
                    img = fnFIE_imgstack_getat(self, i, iret)
                    F_CALL(iret)
                    imgs.append(img.clone_to_ndarray(layered))
                return _np.stack(imgs, axis=0)

            params = self._img_params
            if not params:
                return None

            assert self.is_cpu_image

            itype, ch = params["type"], params["ch"]

            if f_imgtype.F_IMG_BIN == itype:
                w, h = params["w"], params["h"]

                img_uc8 = fnFIE_img_root_alloc(
                    f_imgtype.F_IMG_UC8, 1, w, h)
                view_array_uc8 = img_uc8._attach_to_ndarray()

                if ch == 1:
                    F_CALL(fnFIE_img_copy(self, img_uc8))

                    return view_array_uc8 > 0

                img_1ch = fnFIE_img_child_alloc(0, 0, 0, 0, 0)

                shape = (h, w, ch) if not layered else (ch, h, w)
                new_array = _np.empty(shape=shape, dtype=bool)

                for i in range(ch):
                    F_CALL(fnFIE_img_child_attach_single_ch(
                        img_1ch, self, i, 0, 0, w, h))
                    F_CALL(fnFIE_img_copy(img_1ch, img_uc8))

                    if not layered:
                        new_array[:, :, i] = view_array_uc8 > 0
                    else:
                        new_array[i, :] = view_array_uc8 > 0

                return new_array
            else:
                view_array = self._attach_to_ndarray(inverse_rgb=False)

                if itype in (f_imgtype.F_IMG_RGBQUAD, f_imgtype.F_IMG_RGBTRIPLE):
                    layered = True

                if ch == 1:
                    return view_array.copy()

                elif not layered:
                    new_array = _np.empty(
                        shape=view_array[0].shape + (ch, ), dtype=view_array[0].dtype)
                    for i in range(ch):
                        new_array[:, :, i] = view_array[i]

                    return new_array
                else:
                    new_array = _np.empty(
                        shape=(ch, ) + view_array[0].shape, dtype=view_array[0].dtype)
                    for i in range(ch):
                        new_array[i, :] = view_array[i]

                    return new_array

        @classmethod
        def attach_from_ndarray(cls, ndarray):
            r"""
            パラメータ **ndarray** に渡された :class:`numpy.ndarray` と
            画像メモリを共有する画像オブジェクトを返します。
      
            返される画像オブジェクトは **ndarray** が保持するデータメモリ空間に対して、
            ``fnFIE_img_root_import_alloc()`` [#about_fie_import_alloc]_ 
            により生成されたインポート版ルート画像となります。 
      
            .. [#about_fie_import_alloc]
               *fnFIE_img_root_import_alloc()* の詳細については、 FIE ライブラリのリファレンスマニュアルを参照してください。
      
            返される画像オブジェクトの画像型、 画像サイズ、 チャネル数は、
            **ndarray** の dtype （データ型） 及び shape （形状） によって下記のように決定されます。
      
            |
      
            **ndarray が 1 次元配列の場合**
      
            **ndarray** の shape が *(w, )* の場合、
            生成される画像オブジェクトの幅は *w* 、 高さは 1 、 チャネル数は 1 となります。
            このとき画像型は下記表 "dtype から画像型への対応" により決定されます。
      
            |
      
            **ndarray が 2 次元配列の場合**
      
            **ndarray** の shape が *(h, w)* の場合、
            生成される画像オブジェクトの幅は *w* 、 高さは *h* 、 チャネル数は 1 となります。
            このとき画像型は下記表 "dtype から画像型への対応" により決定されます。
      
            |
      
            **ndarray が 3 次元配列の場合**
      
            **ndarray** の shape が *(c, h, w)* の場合、
            生成される画像オブジェクトの幅は *w* 、 高さは *h* 、 チャネル数は *c* となります。
            このとき画像型は下記表 "dtype から画像型への対応" により決定されます。
      
            ただし dtype が numpy.uint8 であり、 かつ shape の最も内側の次元の要素数が 3 または 4 であった場合、
            下記のように ``F_IMG_RGBTRIPLE`` または ``F_IMG_RGBQUAD`` 型の画像オブジェクトが生成されます。
      
            - **ndarray** の shape が *(h, w, 3)* の場合、
              幅 *w* 、 高さ *h* 、 チャネル数 1 、 画像型が ``F_IMG_RGBTRIPLE`` の画像オブジェクトが生成されます。
      
            - **ndarray** の shape が *(h, w, 4)* の場合、
              幅 *w* 、 高さ *h* 、 チャネル数 1 、 画像型が ``F_IMG_RGBQUAD`` の画像オブジェクトが生成されます。
      
            |
      
            .. list-table:: dtype から画像型への対応
               :header-rows: 1
      
               * - dtype
                 - 画像型
      
               * - numpy.uint8
                 - F_IMG_UC8
               * - numpy.bool\_
                 - F_IMG_UC8
               * - numpy.int16
                 - F_IMG_S16
               * - numpy.uint16
                 - F_IMG_US16
               * - numpy.int32
                 - F_IMG_I32
               * - numpy.uint32
                 - F_IMG_UI32
               * - numpy.int64
                 - F_IMG_I64
               * - numpy.float32
                 - F_IMG_FLOAT
               * - numpy.float64
                 - F_IMG_DOUBLE
      
            |
      
            :param ndarray: :class:`numpy.ndarray` を指定します。
      
            :return: :class:`numpy.ndarray` と画像メモリを共有する画像オブジェクトを返します。
      
            .. note::
               **ndarray** の幅方向の画素がメモリ空間上で一続きに並んでいない場合
               （``F_IMG_RGBTRIPLE`` と ``F_IMG_RGBQUAD`` 以外の型においては
               :attr:`numpy.ndarray.strides` の最後の要素が
               :attr:`numpy.ndarray.itemsize` と異なる場合）はアタッチできません。
               
               処理に失敗した場合は例外が発生します。

            Example:

            .. code-block:: Python

                # img is F_IMG_UC8, 7 x 5.
                img = pyfie.FHANDLE.attach_from_ndarray(numpy.ones((5, 7), dtype=numpy.uint8))
            """
            return cls._import_from_ndarray(ndarray)

        @classmethod
        def clone_from_array(cls, array_like, img_type=None):
            """
            パラメータ **array_like** に渡された配列のデータがコピーされた画像オブジェクトを返します。

            返される画像オブジェクトは ``fnFIE_img_root_alloc()`` [#about_fie_alloc]_ により
            （または **array_like** を :class:`numpy.ndarray` にコピーした後に ``fnFIE_img_root_import_alloc()`` により）
            生成され、 **array_like** から画像データをコピーされたルート画像となります。

            .. [#about_fie_alloc] *fnFIE_img_root_alloc()* の詳細については、 FIE のリファレンスマニュアルを参照してください。

            **array_like** には :class:`numpy.ndarray` の他に、
            Python 組み込み型である :class:`list` や :class:`tuple` 等 "*array like* なオブジェクト" を渡すことが可能です。

            パラメータ **img_type** には生成される画像オブジェクトの画像型を指定します。
            **img_type** に None を指定した場合は :func:`~FHANDLE.attach_from_ndarray` と同じ変換規則にて
            画像型が決定されます。

            |

            :param array_like:   "*array like* なオブジェクト" を指定します。
            :param img_type:     生成される画像オブジェクトの画像型を指定します。

            :return: コピーされた画像オブジェクトを返します。
            """

            if f_imgtype.F_IMG_BIN == img_type:
                src = cls._import_from_ndarray(
                    _np.array(array_like, order="C", copy=None))
                params = src._img_params

                dst = fnFIE_img_root_alloc(
                    f_imgtype.F_IMG_BIN, params["ch"], params["w"], params["h"])
                if F_ERR_NONE != fnFIE_img_copy(src, dst):
                    raise RuntimeError("failed image clone / BIN")

                return dst

            elif img_type in (f_imgtype.F_IMG_RGBQUAD, f_imgtype.F_IMG_RGBTRIPLE):
                pixel_desc = __class__.__get_pixel_desc(img_type)
                dtype = pixel_desc["dtype"]
                elems = pixel_desc["elems"]

                ndarray = _np.array(
                    array_like, dtype=dtype, order="C", copy=True)
                shape = ndarray.shape
                if elems != shape[-1]:
                    shape = shape[:-1] + (-1, elems)
                if len(shape) == 2:
                    shape = (1,) + shape

                ndarray = ndarray.reshape(shape)
                return cls._import_from_ndarray(ndarray)
            else:
                dtype = None
                if img_type:
                    pixel_desc = __class__.__get_pixel_desc(img_type)
                    dtype = pixel_desc["dtype"] if pixel_desc else None

                ndarray = _np.array(
                    array_like, dtype=dtype, order="C", copy=True)
                return cls._import_from_ndarray(ndarray)

        @classmethod
        def clone_imgstack_from_array(cls, array_like, img_type=None):
            """
            パラメータ **array_like** に渡された配列のデータがコピーされた画像スタックオブジェクトを返します。

            返される画像スタックオブジェクトの要素数は len(**array_like**) となり、
            画像スタックオブジェクトの i 番目の要素は ``array_like[i]`` に  :func:`~FHANDLE.clone_from_array` を適用して得られた画像オブジェクトとなります。
            ``array_like[i]`` は "*array like* なオブジェクト" であるか、画像オブジェクトである必要があります。

            |

            :param array_like:   "*array like* なオブジェクト" を指定します。
            :param img_type:     生成される画像スタックオブジェクトに含まれる画像オブジェクトの画像型を指定します。

            :return: コピーされた画像スタックオブジェクトを返します。
            """
            n = len(array_like)
            imgstack = fnFIE_imgstack_alloc(F_IMGSTACK_ROOT_MODE, False)
            if not imgstack:
                raise RuntimeError("failed image stack alloc")

            for i in range(n):
                arr_elm = array_like[i]
                if isinstance(arr_elm, FHANDLE):
                    img = arr_elm
                else:
                    img = cls.clone_from_array(array_like[i], img_type)
                if not img:
                    raise RuntimeError("failed image clone")
                if F_ERR_NONE != fnFIE_imgstack_push_back(imgstack, img):
                    raise RuntimeError("failed image push back")

            return imgstack

        def __array__(self):
            return self._attach_to_ndarray()

        @staticmethod
        def __get_pixel_desc(img_type):
            if f_imgtype.F_IMG_BIN == img_type:
                return None
            if f_imgtype.F_IMG_UC8 == img_type:
                return {"ctypes": _cty.c_ubyte,  "dtype": _np.uint8,   "elems": 1}
            if f_imgtype.F_IMG_S16 == img_type:
                return {"ctypes": _cty.c_int16,  "dtype": _np.int16,   "elems": 1}
            if f_imgtype.F_IMG_US16 == img_type:
                return {"ctypes": _cty.c_uint16, "dtype": _np.uint16,  "elems": 1}
            if f_imgtype.F_IMG_I32 == img_type:
                return {"ctypes": _cty.c_int32,  "dtype": _np.int32,   "elems": 1}
            if f_imgtype.F_IMG_UI32 == img_type:
                return {"ctypes": _cty.c_uint32, "dtype": _np.uint32,  "elems": 1}
            if f_imgtype.F_IMG_I64 == img_type:
                return {"ctypes": _cty.c_int64,  "dtype": _np.int64,   "elems": 1}
            if f_imgtype.F_IMG_FLOAT == img_type:
                return {"ctypes": _cty.c_float,  "dtype": _np.float32, "elems": 1}
            if f_imgtype.F_IMG_DOUBLE == img_type:
                return {"ctypes": _cty.c_double, "dtype": _np.float64, "elems": 1}
            if f_imgtype.F_IMG_RGBQUAD == img_type:
                return {"ctypes": _cty.c_ubyte,  "dtype": _np.uint8,   "elems": 4}
            if f_imgtype.F_IMG_RGBTRIPLE == img_type:
                return {"ctypes": _cty.c_ubyte,  "dtype": _np.uint8,   "elems": 3}

            return None

        @staticmethod
        def __attach_to_ndarray_single_ch(adrs, cty_cls, width, height, elem_size,
                                          step, is_rgbtri, inverse_rgb=False):
            """ Returns : numpy.ndarray (or None). """

            cty_ptr = _cty.cast(adrs, _cty.POINTER(cty_cls))
            if not cty_ptr:
                return None
            step_as_elem = step // 3 if is_rgbtri else step

            if 1 == elem_size:
                shape = (height, step_as_elem)
            else:
                shape = (height, step_as_elem, elem_size)

            nim = _np.ctypeslib.as_array(cty_ptr, shape)
            nim = nim[:, :width]

            if is_rgbtri:
                nim = numpy.lib.stride_tricks.as_strided(
                    nim, strides=(step, 3, 1), subok=True, writeable=True
                )

            if (3 <= elem_size) and inverse_rgb:
                nim = nim[:, :, 2::-1]

            return nim

        def _attach_to_ndarray(self, inverse_rgb=False):
            params = self._img_params
            if not params:
                return None

            if self.is_gpu_image:
                raise TypeError("Attaching GPU image to ndarray is not supported")

            if f_imgtype.F_IMG_BIN == params["type"]:
                return None

            pixel_desc = __class__.__get_pixel_desc(params["type"])
            if not pixel_desc:
                return None

            w, h, ch, step = params["w"], params["h"], params["ch"], params["step"]
            cty_cls, elem_size = pixel_desc["ctypes"], pixel_desc["elems"]
            is_rgbtri = params["type"] == f_imgtype.F_IMG_RGBTRIPLE

            if ch == 1:
                adrs = fnFIE_img_get_adrs(self)

                return __class__.__attach_to_ndarray_single_ch(
                    adrs, cty_cls, w, h, elem_size, step, is_rgbtri, inverse_rgb)
            else:
                nims = _np.empty((ch,), dtype=object)

                for i in range(ch):
                    adrs = fnFIE_img_get_ch_adrs(self, i)
                    nims[i] = __class__.__attach_to_ndarray_single_ch(
                        adrs, cty_cls, w, h, elem_size, step, is_rgbtri, inverse_rgb)

                return nims

        @staticmethod
        def __dtype_to_ftype(dtype):
            if _np.uint8 == dtype:
                return f_imgtype.F_IMG_UC8
            if _np.bool_ == dtype:
                return f_imgtype.F_IMG_UC8
            if _np.int16 == dtype:
                return f_imgtype.F_IMG_S16
            if _np.uint16 == dtype:
                return f_imgtype.F_IMG_US16
            if _np.int32 == dtype:
                return f_imgtype.F_IMG_I32
            if _np.uint32 == dtype:
                return f_imgtype.F_IMG_UI32
            if _np.int64 == dtype:
                return f_imgtype.F_IMG_I64
            if _np.float32 == dtype:
                return f_imgtype.F_IMG_FLOAT
            if _np.float64 == dtype:
                return f_imgtype.F_IMG_DOUBLE

            return None

        @staticmethod
        def _import_from_ndarray(nimg, keep_nimg=True):
            """ Returns : FHANDLE. """

            if not isinstance(nimg, _np.ndarray):
                raise TypeError(
                    "image must be an ndarray, not {}".format(type(nimg)))

            if nimg.ndim < 1 or 3 < nimg.ndim:
                raise ValueError(
                    "unsupported image dimension (got ndim of {})".format(nimg.ndim))
            if nimg.itemsize != nimg.strides[-1]:
                raise ValueError(
                    "image must be contiguous along x-axis "
                    "(i.e. must be itemsize == strides[-1])"
                )
            for s in nimg.strides:
                if s < 1:
                    raise ValueError(
                        "stride must be positive (got strides {})".format(nimg.strides))

            typ = ch = w = h = step = None

            if 1 == nimg.ndim:
                typ = __class__.__dtype_to_ftype(nimg.dtype)
                if not typ:
                    raise ValueError(
                        "unsupported dtype (got {})".format(nimg.dtype))

                ch, w, h = 1, nimg.shape[0], 1
                step = w * nimg.itemsize

            elif (_np.uint8 == nimg.dtype) and (3 == nimg.ndim) and (3 == nimg.shape[-1]):
                typ, ch = f_imgtype.F_IMG_RGBTRIPLE, 1
                w, h = nimg.shape[-2], nimg.shape[-3]
                step = nimg.strides[0]

            elif (_np.uint8 == nimg.dtype) and (3 == nimg.ndim) and (4 == nimg.shape[-1]):
                typ, ch = f_imgtype.F_IMG_RGBQUAD, 1
                w, h = nimg.shape[-2], nimg.shape[-3]
                step = nimg.strides[0] // 4
                if nimg.strides[-2] % nimg.itemsize != 0:
                    raise ValueError(
                        "stride of {} must be divisible by 4"
                        "in order to convert to FIE step".format(
                            nimg.strides[-2])
                    )
            else:
                typ = __class__.__dtype_to_ftype(nimg.dtype)
                if not typ:
                    raise ValueError(
                        "unsupported dtype (got {})".format(nimg.dtype))

                ch = 1 if (2 == nimg.ndim) else nimg.shape[0]
                w, h = nimg.shape[-1], nimg.shape[-2]
                step = nimg.strides[-2] // nimg.itemsize
                if nimg.strides[-2] % nimg.itemsize != 0:
                    raise ValueError(
                        "stride of {} must be divisible by itemsize of {}"
                        "in order to convert to FIE step".format(
                            nimg.strides[-2], nimg.itemsize)
                    )

            adrss = void.PTR.ARRAY(ch)
            base_ptr = nimg.ctypes.data
            for i in range(ch):
                adrss[i] = base_ptr + nimg.strides[0] * i

            fimg = fnFIE_img_root_import_alloc(adrss, ch, typ, step, w, h)
            if fimg is None:
                raise RuntimeError("fnFIE_img_root_import_alloc() failed")

            if fimg and keep_nimg:
                _basic_types._PointerManage.store_private(
                    fimg, nimg)

            return fimg

    if _ENABLE_PYPLOT and _ENABLE_NUMPY:

        def __imshow_core(self, plot_obj=None, layered=False, scale=1.0,
                          axes_config_delegate=None, grid=False, **kwargs):
            params = self._img_params
            if not params:
                return None

            if self.is_gpu_image:
                himg_cpu = self.clone(device="cpu")
                return himg_cpu.__imshow_core(plot_obj, layered, scale,
                          axes_config_delegate, grid, **kwargs)

            itype, ch = params["type"], params["ch"]

            ndarray = None
            if ch == 1:
                layered = False
                ndarray = self._attach_to_ndarray(inverse_rgb=True)
                if None.__class__ == ndarray.__class__:
                    ndarray = self.clone_to_ndarray(layered=False)

            elif itype in (f_imgtype.F_IMG_RGBQUAD, f_imgtype.F_IMG_RGBTRIPLE):
                layered = True
                ndarray = self._attach_to_ndarray(inverse_rgb=True)
            else:
                if not layered and (ch in (3, 4)):
                    ndarray = self.clone_to_ndarray(layered=False)
                    if itype == f_imgtype.F_IMG_BIN:
                        ndarray = ndarray.astype(_np.uint8) * 255
                else:
                    layered = True
                    ndarray = self._attach_to_ndarray(inverse_rgb=True)
                    if None.__class__ == ndarray.__class__:
                        ndarray = self.clone_to_ndarray(layered=True)

            return _ExtensionFIE._imshow_body(
                ndarray,
                plot_obj=plot_obj, layered=layered, scale=scale,
                axes_config_delegate=axes_config_delegate, grid=grid,
                **kwargs
            )

        def _imshow_region(self, padding=0,
                           offset_x=None, offset_y=None, width=None, height=None,
                           plot_obj=None, scale=1.0, grid=False, **kwargs):
            """リージョンの描画"""
            if self.objtag != f_objtag.F_OBJID_REGION:
                raise ValueError("{0} is not a region".format(self))
            if all(x is None for x in [offset_x, offset_y, width, height]):
                xmin = INT()
                xmax = INT()
                ymin = INT()
                ymax = INT()
                if F_ERR_NONE != fnFIE_region_get_xyrange(self, xmin, xmax, ymin, ymax):
                    raise RuntimeError("fnFIE_region_get_xyrange failed")
                org_width = xmax - xmin + 1
                org_height = ymax - ymin + 1
                width = org_width + padding * 2
                height = org_height + padding * 2
                offset_x, offset_y = xmin - padding, ymin - padding
            
            if any(x is None for x in [offset_x, offset_y, width, height]):
                raise ValueError("ROI information is insufficient")
            
            if any(isinstance(x, float) and not x.is_integer() for x in [offset_x, offset_y, width, height]):
                warnings.warn("Given ROI is not an integer box. Fractional part of the ROI is ignored.",
                    category=RuntimeWarning)
                offset_x = int(round(offset_x))
                offset_y = int(round(offset_y))
                width = int(round(width))
                height = int(round(height))
            
            himg = img_uc8(width, height)
            if F_ERR_NONE != fnFIE_img_clear(himg, 0):
                raise RuntimeError("fnFIE_img_clear failed")
            if F_ERR_NONE != fnFIE_region_decode(self, himg, (offset_x, offset_y), 255):
                raise RuntimeError("fnFIE_region_decode failed")
            
            def create_offsetted_tick_formatter(offset):
                def ticks_formatter(x, pos):
                    x -= offset
                    if x == int(x):
                        return str(int(x))
                    else:
                        return str(x)
                return ticks_formatter
            def translate_axes(axes):
                axes.xaxis.set_major_formatter(FuncFormatter(
                    create_offsetted_tick_formatter(-offset_x)))
                axes.yaxis.set_major_formatter(FuncFormatter(
                    create_offsetted_tick_formatter(-offset_y)))
                
            return himg.__imshow_core(plot_obj=plot_obj, layered=False, scale=scale,
                                      axes_config_delegate=translate_axes, grid=grid, **kwargs)

        def imshow(self, plot_obj=None, layered=False, scale=1.0, grid=False, **kwargs):
            """
            画像オブジェクトまたはリージョンオブジェクトのプロットを行います。

            プロットは Pyplot の :func:`matplotlib.pyplot.imshow()` を用いて行われます。

            パラメータ **plot_obj** にはプロット対象とする Pyplot の :class:`~matplotlib.axes.Axes` または :class:`~matplotlib.figure.Figure` が指定できます。
            デフォルトでは None となっており、 この場合カレント :class:`~matplotlib.axes.Axes` がプロット対象となります。

            画像オブジェクトが複数チャネルである場合、 
            パラメータ **layered** に True を指定することで各チャネルを個別にプロットすることができます。

            パラメータ **scale** にはプロットの倍率を指定します。
            例えばデフォルトの 2 倍でプロットを行う場合には 2.0 と指定してください。

            パラメータ **grid** では罫線の表示/非表示を指定します。
            True を指定した場合罫線は表示され、 False を指定した場合表示されません。

            また、 これら以外のキーワード引数は
            Pyplot の :func:`matplotlib.pyplot.imshow()` に直接渡されますのでプロットの詳細な指定を行うことができます。


            :param plot_obj: プロットを行う :class:`~matplotlib.figure.Figure` もしくは :class:`~matplotlib.axes.Axes` を指定します。
                            None を指定した場合はカレント :class:`~matplotlib.axes.Axes` が使用されます。
            :param layered:  複数チャネル画像の場合 True を指定すると、 チャネル毎にプロットが行われます。
                            リージョンの場合は無視されます。
            :param scale:    プロットの倍率を指定します。
            :param grid:     罫線の表示/非表示を指定します。
            :param kwargs:   :func:`matplotlib.pyplot.imshow()` に渡すキーワード引数を指定します。

            :return: プロットが行われた :class:`~matplotlib.axes.Axes` を返します。
                    **layered** に True を指定し複数チャネル毎のプロットが行われた場合は :class:`~matplotlib.axes.Axes` のリストを返します。
            """
            if self.objtag == f_objtag.F_OBJID_REGION:
                return self._imshow_region(plot_obj=plot_obj, scale=scale, grid=grid, **kwargs)
            else:
                return self.__imshow_core(plot_obj=plot_obj, layered=layered, scale=scale, grid=grid, **kwargs)

        def imshow_roi(self, x, y, w=10, h=10, plot_obj=None,
                       layered=False, scale=1.0, grid=False, **kwargs):
            """
            画像オブジェクトまたはリージョンオブジェクトにおける指定範囲のプロットを行います。

            パラメータ **x** 及び **y** で処理範囲の左上座標を、
            **w** 及び **h** で処理範囲のサイズを指定します。

            これ以外のパラメータに関しては :func:`FHANDLE.imshow` と同様となります。

            :param x:   処理範囲の左上 x 座標
            :param y:   処理範囲の左上 y 座標
            :param w:   処理範囲の幅
            :param h:   処理範囲の高さ

            :param plot_obj: プロットを行う :class:`~matplotlib.figure.Figure` もしくは :class:`~matplotlib.axes.Axes` を指定します。
                            None を指定した場合はカレント :class:`~matplotlib.axes.Axes` が使用されます。
            :param layered:  複数チャネル画像の場合 True を指定すると、 チャネル毎にプロットが行われます。
                            リージョンの場合は無視されます。
            :param scale:    プロットの倍率を指定します。
            :param grid:     罫線の表示/非表示を指定します。
            :param kwargs:   :func:`matplotlib.pyplot.imshow()` に渡すキーワード引数を指定します。

            :return: プロットが行われた :class:`~matplotlib.axes.Axes` を返します。
                    **layered** に True を指定し複数チャネル毎のプロットが行われた場合は :class:`~matplotlib.axes.Axes` のリストを返します。
            """
            if self.objtag == f_objtag.F_OBJID_REGION:
                return self._imshow_region(
                    offset_x=x, offset_y=y, width=w, height=h,
                    plot_obj=plot_obj, scale=scale, grid=grid, **kwargs)

            def axes_set_roi(axes, xs, ys, xe, ye):
                assert (xs <= xe) and (ys <= ye)

                ticks_div = 10
                xticks = int((xe - xs) / ticks_div)
                xticks = max(1, xticks)
                yticks = int((ye - ys) / ticks_div)
                yticks = max(1, yticks)

                axes.set_xlim(xs-0.5, xe+0.5)
                axes.set_ylim(ye+0.5, ys-0.5)
                axes.set_xticks(_np.arange(xs, xe + 1, xticks))
                axes.set_yticks(_np.arange(ys, ye + 1, yticks))

                if grid:
                    axes.grid(True, color="red", alpha=0.7, linestyle="--")
                else:
                    axes.grid(False)

            params = self._img_params
            if not params:
                return None
            if w == 0 or h == 0:
                return None

            w = w - 1 if 0 < w else w + 1
            h = h - 1 if 0 < h else h + 1

            xs, xe = sorted((x, x + w))
            ys, ye = sorted((y, y + h))

            return self.__imshow_core(
                plot_obj=plot_obj, layered=layered, scale=scale,
                axes_config_delegate=lambda a: axes_set_roi(
                    a, xs, ys, xe, ye), grid=grid,
                **kwargs
            )


class _ExtensionFIE:

    if _ENABLE_PYPLOT:

        @staticmethod
        def _imshow_body(array_like, plot_obj=None, layered=False,
                         scale=1.0, axes_config_delegate=None, grid=False, **kwargs):
            """
            Parameters
            ----------
            axes_config_delegate :
               function. call just before imshow() as ...
                  axes_config_delegate( axes )
            """

            def axes_config(axes):
                assert isinstance(axes, _pyplot.Axes)

                axes.grid(grid)
                axes.xaxis.set_ticks_position("bottom")
                axes.yaxis.set_ticks_position("left")

                if 0.0 < scale and 1.0 != scale:
                    f = axes.figure
                    w = f.get_figwidth() * scale
                    h = f.get_figheight() * scale

                    f.set_figwidth(w)
                    f.set_figheight(h)

            ndarray = _np.asanyarray(array_like)

            default_mplrc = {
                "cmap": "gray",
                "interpolation": "none",
                "aspect": "equal",
                "origin": "upper"
            }

            for key, val in default_mplrc.items():
                if key not in kwargs:
                    kwargs[key] = val

            if ("vmin" not in kwargs) and ("vmax" not in kwargs):
                dtype = ndarray.dtype
                if dtype == object:
                    dtype = ndarray[0].dtype

                if bool == dtype:
                    kwargs["vmin"], kwargs["vmax"] = 0, 1
                elif _np.uint8 == dtype:
                    kwargs["vmin"], kwargs["vmax"] = 0, 255

            if layered and isinstance(plot_obj, _pyplot.Axes):

                axes = plot_obj
                _pyplot_util.set_common_figure_style(axes)

                ch = ndarray.shape[0]
                kwargs["alpha"] = 1.0 / ch

                for i in range(ch):
                    axes_config(axes)
                    if axes_config_delegate is not None:
                        axes_config_delegate(axes)
                    axes.imshow(ndarray[i], **kwargs)

                return axes

            elif layered:
                assert not isinstance(plot_obj, _pyplot.Axes)

                ch = ndarray.shape[0]
                axes_list = []

                if isinstance(plot_obj, _pyplot.Figure):
                    fig = plot_obj
                    _pyplot_util.set_common_figure_style(fig)

                    for i in range(ch):
                        axes_list.append(fig.add_subplot(ch, 1, i + 1))
                else:
                    base_fig_number = _pyplot.gcf().number

                    for i in range(ch):
                        fig = _pyplot.figure(base_fig_number + i)
                        _pyplot_util.set_common_figure_style(fig)

                        axes_list.append(fig.add_subplot(111))

                assert ch == len(axes_list)

                for i in range(ch):
                    axes = axes_list[i]
                    axes_config(axes)

                    axes.set_title("Ch {0}".format(i), loc="center")
                    axes.xaxis.set_ticks_position("bottom")

                    if axes_config_delegate is not None:
                        axes_config_delegate(axes)
                    axes.imshow(ndarray[i], **kwargs)

                return axes_list

            else:
                axes = _pyplot_util.get_axes(plot_obj)
                _pyplot_util.set_common_figure_style(axes)

                axes_config(axes)
                if axes_config_delegate is not None:
                    axes_config_delegate(axes)
                axes.imshow(ndarray, **kwargs)

                return axes

    @staticmethod
    def _wrap_fnFIE_free_object(h):
        """ VOID fnFIE_free_object( FHANDLE h ); """

        if not isinstance(h, FHANDLE):
            return

        if h._handle_core:
            h._handle_core.dispose()
            h._handle_core = None

        h.value = None

    @staticmethod
    def _as_out_param_FHANDLE_PTR(cls, func, arg_obj):
        if isinstance(arg_obj, cls):
            if not arg_obj:
                return
            fhandle = arg_obj.deref

        elif isinstance(arg_obj, cls._ref_cls):
            fhandle = arg_obj

        else:
            return

        if not fhandle:
            return
        fhandle._handle_core = FHANDLE._HandleManager.get_handle(
            fhandle.value)

    @classmethod
    def bless_FHANDLE(cls, lib_register):
        lib_register._ignore_type_name.append("FHANDLE")

        FHANDLE.bless_ptr()
        FHANDLE.PTR._as_out_param_ = classmethod(
            cls._as_out_param_FHANDLE_PTR)

        lib_register.set_type_tbl(FHANDLE, "FHANDLE")
        lib_register.set_replace_func(
            "fnFIE_free_object", "_org_fnFIE_free_object")
        _set_toplevel(cls._wrap_fnFIE_free_object, "fnFIE_free_object")

    @classmethod
    def bless_misc(cls):

        ctrl._bless_f_err()

        _dbg.get_managed_fhandle_adrss = staticmethod(
            FHANDLE._HandleManager.dbg_get_manage_handles)
        _dbg.is_managed_fhandle = staticmethod(
            lambda fhandle: getattr(
                fhandle, "value", None) in FHANDLE._HandleManager.dbg_get_manage_handles()
        )

        def oal_free(self):
            """ free memory by fnOAL_free(). """
            if not self:
                return
            fnOAL_free(self)
            self.value = None

        _basic_types._Referable._PointerBase.fnOAL_free = oal_free

        if _ENABLE_NUMPY:
            def _clone_fmatrix_to_ndarray(self, dtype=None):
                """FMATRIXをndarrayにコピーする。"""
                if dtype is None:
                    dtype = _np.float64
                new_array = _np.empty(shape=(self.row, self.col), dtype=dtype)
                for i in range(self.row):
                    new_array[i, :] = self.m[i][:self.col]
                return new_array

            @staticmethod
            def _clone_fmatrix_from_array(array_like):
                """新たに確保したFMATRIXに配列をコピーする。

                本関数が返すFMATRIXはPython のガベージコレクション対象となるため明示的に解放する必要はない。
                配列は1次元または2次元でなければならない。"""
                ndarray = _np.array(
                    array_like, dtype=_np.float64, copy=None)
                if ndarray.ndim == 1:
                    ndarray = ndarray.reshape(1, -1)
                if ndarray.ndim != 2:
                    raise ValueError(
                        "unsupported image dimension (got ndim of {})".format(ndarray.ndim))
                
                mat = FMATRIX()
                mat.row, mat.col = ndarray.shape
                arr_entity = DOUBLE.ARRAY(mat.row * mat.col)
                arr_pointers = VOID.PTR.ARRAY(mat.row)
                arr_entity.value = ndarray.flatten()
                for i in range(mat.row):
                    arr_pointers[i] = arr_entity[i * mat.col].ref
                mat.m = arr_pointers
                mat._stored_fmatrix_array_entity = arr_entity
                return mat
            
            FMATRIX.clone_to_ndarray = _clone_fmatrix_to_ndarray
            FMATRIX.clone_from_array = _clone_fmatrix_from_array

    @staticmethod
    def FIE_setup():
        iret = fnFIE_setup()
        _dbg.DEBUG_PRINT("> fnFIE_setup():", f_err(iret))
        if _is_toplevel("fnFGA_setup"):
            iret = fnFGA_setup()
            _dbg.DEBUG_PRINT("> fnFGA_setup():", f_err(iret))


def imshow(array_like, plot_obj=None, layered=False, scale=1.0, grid=False, **kwargs):
    _raise_if_pyplot_unavailable()

    if isinstance(array_like, FHANDLE):
        return array_like.imshow(plot_obj=plot_obj, layered=layered, scale=scale, **kwargs)

    return _ExtensionFIE._imshow_body(
        array_like, plot_obj=plot_obj, layered=layered, scale=scale, grid=grid, **kwargs)


def plot_show(*args, **kw):
    """
    :func:`matplotlib.pyplot.show()` を呼び出します。

    .. code-block:: Python

        # PyFIE 画像オブジェクトのプロットを実行
        img.imshow()

        # PyFIE 構造体のプロットを実行
        pnt.plot()

        # Matplotlib を非インタラクティブモードで使用している場合
        # この時点でプロットは行われていない


        # 下記関数を実行することにより上記プロットが行われる
        pyfie.plot_show()
    """
    _raise_if_pyplot_unavailable()
    return _pyplot.show(*args, **kw)


_decl = None


def init(lib_bin_path=None, auto_setup=True):
    """
    PyFIE モジュールの初期化をおこないます。

    自動初期化を有効に設定している場合、この関数を実行する必要はありません。
    詳しくは :doc:`/reference/extension/config_file` を参照してください。

    パラメータ **lib_bin_path** には
    バインディング対象となる FIE ライブラリバイナリファイルへのパスを指定します。
    パスの指定は文字列、 または文字列を要素とするリスト（バイナリが複数である場合）で行って下さい。
    パラメータ **lib_bin_path** に None を指定した場合、
    :doc:`設定ファイル </reference/extension/config_file>` におけるパス設定に従います。

    パラメータ **auto_setup** に True を指定した場合、
    初期化完了後 fnFIE_setup() による FIE ライブラリの初期化処理が行われます。

    この関数は PyFIE モジュールのトップレベル関数です。

    :param lib_bin_path: FIE ライブラリバイナリのパス
    :param auto_setup: FIE ライブラリの初期化実行の有無

    :return: None を返します
    """

    global _decl
    global _ENABLE_FIE

    if _util.get_platform() == "Windows" and "KMP_DUPLICATE_LIB_OK" not in _os.environ:
        _dbg.DEBUG_PRINT("setting environment variable 'KMP_DUPLICATE_LIB_OK' to TRUE")
        _os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    if not lib_bin_path:
        lib_bin_path = _config.lib_bin_path

    if isinstance(lib_bin_path, str):
        lib_bin_path = [lib_bin_path]
    
    lib_bin_pathes_not_existing = [p for p in lib_bin_path if not _os.path.exists(_util.resolve_path(p))]
    if len(lib_bin_pathes_not_existing) > 0:
        
        raise ValueError(
            "Some of FIE Library binaries not found. "
            "Please make sure that the correct version of FIE (or WIL on Windows) is properly installed. "
            f"Missing binaries are: {lib_bin_pathes_not_existing}"
        )

    _decl = _DeclManager(_config.lib_decl_file)
    _decl.load_decl_files()

    lib_register = _LibRegister()

    if _ENABLE_FIE:
        _ExtensionFIE.bless_FHANDLE(lib_register)

    lib_register.register_all(_decl, lib_bin_path)

    _decl.unload_decl_files()

    _Patches.apply(
        lib_register,
        _config.patches
    )

    if _ENABLE_FIE:
        _ExtensionFIE.bless_misc()

    _dbg.DEBUG_PRINT(
        "Struct: export {0}, missing {1}".format(
            len(lib_register.export_struct), len(lib_register.missing_struct)))
    _dbg.DEBUG_PRINT(
        "Union:  export {0}, missing {1}".format(
            len(lib_register.export_union), len(lib_register.missing_union)))
    _dbg.DEBUG_PRINT(
        "Function: export {0}, missing {1}".format(
            len(lib_register.export_function), len(lib_register.missing_function)))

    if _dbg.ENABLE_DEBUG:
        global _lib_register

        _lib_register = lib_register
    
    _warn_if_fie_version_not_compatible()

    if auto_setup:
        if _ENABLE_FIE:
            _ExtensionFIE.FIE_setup()
        else:
            pass

    if _dbg.ENABLE_DEBUG:
        from datetime import datetime
        _dbg.DEBUG_PRINT("\n", datetime.now())


def add_library(lib_bin_path, lib_decl_file):
    """
    PyFIE モジュールに任意の C 言語ライブラリへのバインディングを追加します。

    パラメータ **lib_bin_path** には
    バインディング対象となる C 言語ライブラリバイナリファイルへのパスを指定します。
    パスの指定は文字列で行って下さい。

    パラメータ **lib_decl_file** には
    バインディング対象となる C 言語ライブラリの :ref:`library_definition_file` 
    （ライブラリの関数や型の情報等が記された JSON 形式のファイル）へのパスを指定します。

    :param lib_bin_path: C 言語ライブラリバイナリのパス
    :param lib_decl_file: ライブラリ定義ファイル

    :return: None を返します

    .. note::
        本関数を Python 3.8 以上かつ Windows 環境にて使用する場合、
        それより前のバージョンの Python よりも DLL 依存関係の解決方法がよりセキュアとなります。
        状況によっては :func:`os.add_dll_directory()` 関数により明示的に DLL ファイルを含む
        ディレクトリを指定する必要があります。
    """

    lib_bin_path = _os.path.abspath(lib_bin_path)
    lib_decl_file = _os.path.abspath(lib_decl_file)

    _decl.add_decl_files([lib_decl_file])
    _decl.load_decl_files()

    lib_register = _LibRegister()

    if _ENABLE_FIE:
        _ExtensionFIE.bless_FHANDLE(lib_register)

    lib_register.register_all(
        _decl,
        _config.lib_bin_path + [lib_bin_path])

    _decl.unload_decl_files()

    _Patches.apply(
        lib_register,
        _config.patches
    )

    if _ENABLE_FIE:
        _ExtensionFIE.bless_misc()

    _dbg.DEBUG_PRINT(
        "Struct: export {0}, missing {1}".format(
            len(lib_register.export_struct), len(lib_register.missing_struct)))
    _dbg.DEBUG_PRINT(
        "Union:  export {0}, missing {1}".format(
            len(lib_register.export_union), len(lib_register.missing_union)))
    _dbg.DEBUG_PRINT(
        "Function: export {0}, missing {1}".format(
            len(lib_register.export_function), len(lib_register.missing_function)))


def sizeof(obj):
    """
    PyFIE データ型のデータサイズを取得します。

    パラメータ **obj** には PyFIE データ型インスタンスまたはクラスを指定してください。
    その型が内部で保持するデータのメモリサイズをバイト単位で返します。

    この関数は C 言語における sizeof 演算子に相当します。

    :param  obj: PyFIE データ型のインスタンスまたはクラスを指定します

    :return: データのメモリサイズをバイト単位で返します
    """
    return _cty.sizeof(obj)


class ctrl:
    _ENABLE_F_ERR_EXCEPTION = False

    _ENABLE_F_ERR_RETURN = True
    _IPYTHON_MAX_DISPLAY_IMAGE_SIZE = 8192

    @staticmethod
    def _bless_f_err():
        def __as_result__(self, func, args):
            if ctrl._ENABLE_F_ERR_EXCEPTION:
                if F_ERR_NONE != self:
                    raise RuntimeError(self.__repr__())

            if ctrl._ENABLE_F_ERR_RETURN:
                return self

            return INT(self)

        f_err._as_result_ = __as_result__

    @classmethod
    def enable_f_err_exception(cls, enable=False):
        """
        PyFIE 関数が返すエラーコードに応じて例外を発生させる機能の
        切り替えを行います。

        本関数の設定対象となるのは
        戻り値の型が ``INT`` であり、
        かつ仕様上その戻り値がエラーコードとなっている FIE(C 言語) 関数に対応した PyFIE 関数となります。

        パラメータ **enable** に True を指定した場合、
        これらの PyFIE 関数が戻り値として正常終了（``F_ERR_NONE``）以外を返す時、
        自動的に例外（``RuntimeError``）を発生させるようになります。

        パラメータ **enable** に False を指定した場合、
        このような例外の発生を行いません。

        :param enable: 機能の有効（True）無効（False）指定

        .. note::
            PyFIE の初期状態では
            本関数の機能は無効（つまり例外の発生を行わない）となっています。
        """
        cls._ENABLE_F_ERR_EXCEPTION = enable

    @classmethod
    def is_f_err_exception_enabled(cls):
        """
        PyFIE 関数が返すエラーコードに応じて例外を発生させる機能が有効であるかどうかを取得します。

        :return: 例外を発生させる機能が有効である場合は True 、そうでない場合は False 。
        """
        return cls._ENABLE_F_ERR_EXCEPTION

    @classmethod
    def enable_f_err_return(cls, enable=True):
        """
        エラーコード（``INT`` 型）を返す PyFIE 関数の戻り値の型を ``pyfie.f_err`` 型に切り替えます。

        本関数の設定対象となるのは
        戻り値の型が ``INT`` であり、
        かつ仕様上その戻り値がエラーコードとなっている FIE(C 言語) 関数に対応した PyFIE 関数となります。

        パラメータ **enable** に True を指定した場合、
        これらの PyFIE 関数は戻り値として ``pyfie.f_err`` 型の PyFIE 定数インスタンスを返すようになります。

        パラメータ **enable** に False を指定した場合、
        これらの PyFIE 関数は戻り値として ``pyfie.INT`` 型のインスタンスを返すようになります。

        :param enable: 機能の有効（True）無効（False）指定

        .. note::
            PyFIE の初期状態では
            本関数の機能は有効（つまり ``pyfie.f_err`` 型を返す）となっています。
        """
        cls._ENABLE_F_ERR_RETURN = enable

    @classmethod
    def is_f_err_return_enabled(cls):
        """
        エラーコード（``INT`` 型）を返す PyFIE 関数の戻り値の型を
        ``pyfie.f_err`` 型に切り替えているかどうかを取得します。

        :return: エラーコードを ``pyfie.f_err`` 型に切り替えている場合は True 、そうでない場合は False 。
        """
        return cls._ENABLE_F_ERR_RETURN

    @classmethod
    def set_ipython_max_display_image_size(cls, size):
        """
        IPython で PyFIE の画像オブジェクトを表示する際の、表示可能な最大の画像幅または画像高さを設定します。

        画像幅または画像高さがパラメータ **size** で設定した値より大きい場合、
        :func:`IPython.display.display()` 関数を使用した際に画像を表示しません。

        本機能は巨大な画像を表示する際の意図しない応答遅延を回避する目的で提供されます。

        :param size: IPython で表示可能な最大の画像幅または画像高さ
        """
        cls._IPYTHON_MAX_DISPLAY_IMAGE_SIZE = size

    @classmethod
    def get_ipython_max_display_image_size(cls):
        """
        IPython で PyFIE の画像オブジェクトを表示する際の、表示可能な最大の画像幅または画像高さを取得します。
        
        :return: IPython で PyFIE の画像オブジェクトを表示する際の、表示可能な最大の画像幅または画像高さ。
        """
        return cls._IPYTHON_MAX_DISPLAY_IMAGE_SIZE


def _img_root_alloc(type, ch, w, h, device=None):
    if device is None or device != "gpu":
        return fnFIE_img_root_alloc(type, ch, w, h)
    else:
        return fnFGA_img_root_alloc(type, ch, w, h)

def img_bin(w=32, h=32, ch=1, device=None):
    """
    ``F_IMG_BIN`` 型の画像オブジェクトの確保を行います。
    画像の確保は ``fnFIE_img_root_alloc()`` により行われます。

    :param w:  画像幅を指定します。
    :param h:  画像高さを指定します。
    :param ch: 画像チャネル数を指定します。

    :return: 確保された ``F_IMG_BIN`` 型の画像オブジェクトを返します。
    """
    return _img_root_alloc(f_imgtype.F_IMG_BIN, ch, w, h, device)


def img_uc8(w=32, h=32, ch=1, device=None):
    """
    ``F_IMG_UC8`` 型の画像オブジェクトの確保を行います。
    画像の確保は ``fnFIE_img_root_alloc()`` により行われます。

    :param w:  画像幅を指定します。
    :param h:  画像高さを指定します。
    :param ch: 画像チャネル数を指定します。

    :return: 確保された ``F_IMG_UC8`` 型の画像オブジェクトを返します。
    """
    return _img_root_alloc(f_imgtype.F_IMG_UC8, ch, w, h, device)


def img_s16(w=32, h=32, ch=1, device=None):
    """
    ``F_IMG_S16`` 型の画像オブジェクトの確保を行います。
    画像の確保は ``fnFIE_img_root_alloc()`` により行われます。

    :param w:  画像幅を指定します。
    :param h:  画像高さを指定します。
    :param ch: 画像チャネル数を指定します。

    :return: 確保された ``F_IMG_S16`` 型の画像オブジェクトを返します。
    """
    return _img_root_alloc(f_imgtype.F_IMG_S16, ch, w, h, device)


def img_us16(w=32, h=32, ch=1, device=None):
    """
    ``F_IMG_US16`` 型の画像オブジェクトの確保を行います。
    画像の確保は ``fnFIE_img_root_alloc()`` により行われます。

    :param w:  画像幅を指定します。
    :param h:  画像高さを指定します。
    :param ch: 画像チャネル数を指定します。

    :return: 確保された ``F_IMG_US16`` 型の画像オブジェクトを返します。
    """
    return _img_root_alloc(f_imgtype.F_IMG_US16, ch, w, h, device)


def img_dbl(w=32, h=32, ch=1, device=None):
    """
    ``F_IMG_DOUBLE`` 型の画像オブジェクトの確保を行います。
    画像の確保は ``fnFIE_img_root_alloc()`` により行われます。

    :param w:  画像幅を指定します。
    :param h:  画像高さを指定します。
    :param ch: 画像チャネル数を指定します。

    :return: 確保された ``F_IMG_DOUBLE`` 型の画像オブジェクトを返します。
    """
    return _img_root_alloc(f_imgtype.F_IMG_DOUBLE, ch, w, h, device)


def img_rgbq(w=32, h=32, ch=1, device=None):
    """
    ``F_IMG_RGBQUAD`` 型の画像オブジェクトの確保を行います。
    画像の確保は ``fnFIE_img_root_alloc()`` により行われます。

    :param w:  画像幅を指定します。
    :param h:  画像高さを指定します。
    :param ch: 画像チャネル数を指定します。

    :return: 確保された ``F_IMG_RGBQUAD`` 型の画像オブジェクトを返します。
    """
    return _img_root_alloc(f_imgtype.F_IMG_RGBQUAD, ch, w, h, device)


def _imread_file(file_name, layered=False, device=None):
    if layered:
        color_type = f_color_img_type.F_COLOR_IMG_TYPE_UC8
    else:
        color_type = f_color_img_type.F_COLOR_IMG_TYPE_RGBQ

    fimg = FHANDLE()
    ret = fnFIE_load_img_file(file_name, fimg.adrs, color_type)
    if F_ERR_NONE != ret:
        raise RuntimeError("failed ({0}) {1}".format(f_err(ret), file_name))
    
    if device == "gpu":
        return fimg.clone(device)
    else:
        return fimg


def imread(file_name, layered=False, device=None):
    """
    ファイルから画像の読み込みを行います。

    パラメータ **file_name** には読み込む画像の ファイルパス または URL を指定可能です。

    パラメータ **layered** は、 カラー画像を複数チャネルとして扱うか否かの指定となります。
    True を指定した場合は、
    ``F_IMG_UC8`` 型の 3 チャネル画像として読み込みを行います。
    False を指定した場合は、
    ``F_IMG_RGBQUAD`` 型の画像として読み込みを行います。

    :param file_name: 読み込む画像ファイル名（str オブジェクトや pathlib.PurePath オブジェクトとして表されるファイルパス、または URL）
    :param layered: カラー画像を複数チャネルとして扱うか否かの指定

    :return: 画像が読み込まれた画像オブジェクトを返します。
    """
    def _imread_url(url, layered=False, device=None):
        file_name = _os.path.basename(url)
        with request.urlopen(url) as req:
            with tempfile.TemporaryDirectory() as d:
                dir_name = d if isinstance(d, str) else d.name
                file_path = _os.path.join(dir_name, file_name)
                _dbg.DEBUG_PRINT("temporary file ...", file_path)

                with open(file_path, mode="wb") as f:
                    f.write(req.read())

                img = _imread_file(file_path, layered, device)

        return img

    if isinstance(file_name, pathlib.PurePath):
        file_name = str(file_name)

    if "://" in file_name:
        return _imread_url(file_name, layered, device)
    else:
        if not _os.path.exists(file_name):
            raise FileNotFoundError(
                errno.ENOENT, _os.strerror(errno.ENOENT), file_name)
        return _imread_file(file_name, layered, device)


def imdecode(buffer, layered=False, device=None):
    """
    パラメータ **buffer** に渡されたバイト列を画像オブジェクトに変換します。

    パラメータ **layered** の意味は ``pyfie.imread()`` と等価です。

    :param buffer: 特定のフォーマットで表現された画像を表すバイト列 (bytes)
    :param layered: カラー画像を複数チャネルとして扱うか否かの指定

    :return: 画像が読み込まれた画像オブジェクトを返します。

    .. note::
    
        本関数は内部で ``pyfie.imread()`` を使用しており、
        処理時間はそれよりも長くなる（ファイルを経由しないで済むことによる高速化が実施されていない）ことにご注意ください。
    """
    with tempfile.NamedTemporaryFile(delete=False, mode="wb") as f:
        f.write(buffer)
        temp_fname = f.name
    try:
        return _imread_file(temp_fname, layered, device)
    finally:
        _os.remove(temp_fname)


_DEFAULT_IMWRITE_COMP_LEVEL = -1
_DEFAULT_IMWRITE_QUALITY = 95


def imwrite(file_name, img,
            comp_level=_DEFAULT_IMWRITE_COMP_LEVEL, quality=_DEFAULT_IMWRITE_QUALITY):
    """
    パラメータ **img** に渡された画像オブジェクトを、 ファイルに書き込みます。

    ファイルへの書き込みは、拡張子に応じて ``fnFIE_save_bmp()``, ``fnFIE_save_jpeg()``, ``fnFIE_save_png()``,
    または ``fnFIE_save_tiff()`` により行われます。

    パラメータ **comp_level** は圧縮レベルを表します。
    PNG または TIFF 形式での保存時のみ有効です。
    TIFF 形式で圧縮レベルが 0 の場合は圧縮形式は
    ``F_TIFF_COMPRESSION_NONE`` となり、 0 でない場合は
    ``F_TIFF_COMPRESSION_DEFLATE`` になります。
    圧縮レベルについて詳細は対応する画像保存関数のリファレンスを参照ください。

    パラメータ **quality** は画質を表します。
    JPEG 形式での保存時のみ有効であり、0以上100以下で指定します。

    :param file_name: 書き込む画像ファイル名（str オブジェクトまたは pathlib.PurePath オブジェクト）
    :param img: 画像オブジェクト
    :param comp_level: 圧縮レベル。PNG または TIFF 形式のみ有効
    :param quality: 画質。JPEG 形式のみ有効
    """
    if isinstance(file_name, pathlib.PurePath):
        file_name = str(file_name)
    if isinstance(img, FHANDLE) and img.is_gpu_image:
        himg_cpu = img.clone(device="cpu")
        return imwrite(file_name, himg_cpu, comp_level, quality)

    ext = _os.path.splitext(file_name)[-1].lower()
    comp_level_available = False
    quality_available = False

    if ext in (".bmp",):
        ret = fnFIE_save_bmp(file_name, img)
    elif ext in (".jpg", ".jpeg"):
        quality_available = True
        ret = fnFIE_save_jpeg(file_name, img, quality)
    elif ext in (".png",):
        comp_level_available = True
        ret = fnFIE_save_png(file_name, img, comp_level)
    elif ext in (".tif", ".tiff"):
        comp_level_available = True
        if comp_level == 0:
            comp_type = f_tiff_compression.F_TIFF_COMPRESSION_NONE
        else:
            comp_type = f_tiff_compression.F_TIFF_COMPRESSION_DEFLATE
        ret = fnFIE_save_tiff(file_name, img, comp_type, comp_level)
    else:
        ret = fnFIE_save_bmp(file_name, img)

    if F_ERR_NONE != ret:
        raise RuntimeError("failed ({0}) / {1}".format(f_err(ret), file_name))

    if not comp_level_available and comp_level != _DEFAULT_IMWRITE_COMP_LEVEL:
        warnings.warn("comp_level is not supported for the image type and is ignored.",
                      category=RuntimeWarning)

    if not quality_available and quality != _DEFAULT_IMWRITE_QUALITY:
        warnings.warn("quality is not supported for the image type and is ignored.",
                      category=RuntimeWarning)


def imencode(img, format_ext="bmp",
             comp_level=_DEFAULT_IMWRITE_COMP_LEVEL, quality=_DEFAULT_IMWRITE_QUALITY):
    """
    指定されたフォーマットでパラメータ **img** に渡された画像オブジェクトをバイト列に変換します。

    パラメータ **comp_level** と **quality** の意味は ``pyfie.imwrite()`` と等価です。

    :param img: 画像オブジェクト
    :param format_ext: フォーマットを表す文字列。"bmp", "png", "jpg", "jpeg", "tif", "tiff"のいずれか
    :param comp_level: 圧縮レベル。PNG または TIFF 形式のみ有効
    :param quality: 画質。JPEG 形式のみ有効

    :return: 特定のフォーマットに変換された画像を表すバイト列 (bytes) を返します。

    .. note::
    
        本関数は内部で ``pyfie.imwrite()`` を使用しており、
        処理時間はそれよりも長くなる（ファイルを経由しないで済むことによる高速化が実施されていない）ことにご注意ください。
    """
    if not isinstance(img, FHANDLE) or not img.is_image:
        raise TypeError("img is not an FIE image object")
    if format_ext not in ["bmp", "png", "jpg", "jpeg", "tif", "tiff"]:
        raise ValueError("Unknown format: " + format_ext)
    with tempfile.TemporaryDirectory() as tempdir:
        img_path = pathlib.Path(tempdir, 'imagefile.' + format_ext)
        imwrite(img_path, img, comp_level, quality)
        with open(img_path, "rb") as f:
            buf = f.read()
        return buf


def malloc(instance_cls, num):
    """
    パラメータ **instance_cls** で指定される PyFIE データ型を要素とし、
    パラメータ **num** で指定された個数を要素数とする配列（メモリ領域）を確保し
    そのポインタを返します。

    つまり下記バイトサイズのメモリ領域の確保が行われます。

    ``sizeof(instance_cls) * num``

    本関数で確保されたメモリ領域は、 Python のガベージコレクション対象となるため
    解放する必要はありません。

    :param instance_cls: 要素となる PyFIE データ型のクラスを指定します
    :param num: 要素の個数を指定します

    :return: 確保されたメモリ領域への PyFIE ポインタインスタンスを返します.

    .. note::
        本関数により確保されたメモリ領域に対して、
        PyFIE 関数 ``fnOAL_free()`` による解放や
        ``fnOAL_realloc()`` によるサイズ変更を行うことは出来ません。
    """
    ptr_obj = instance_cls.PTR.cast((instance_cls * num)())
    if hasattr(ptr_obj, "fnOAL_free"):
        ptr_obj.fnOAL_free = None
    return ptr_obj


if _config.DEBUG:
    _dbg.ENABLE_DEBUG = True

_dbg.DEBUG_PRINT("DEBUG: ENABLE.")
_dbg.DEBUG_PRINT("numpy:", "ENABLE." if _ENABLE_NUMPY else "DISABLE.")
_dbg.DEBUG_PRINT("matplotlib:", "ENABLE." if _ENABLE_PYPLOT else "DISABLE.")

if _config.auto_init:
    _dbg.DEBUG_PRINT("\ninitialize ...")

    init(auto_setup=True)
