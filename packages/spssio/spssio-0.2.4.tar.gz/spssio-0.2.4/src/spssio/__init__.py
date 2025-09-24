import ctypes
import dataclasses
import enum
import functools
import logging
import math
import pathlib
import platform
import struct

import numpy

log = logging.getLogger("spss")

this_dir = pathlib.Path(__file__).parent
libs_dir = this_dir / "libspss"

PTR = ctypes.POINTER
ptr = ctypes.pointer

c_char_p = ctypes.c_char_p
c_char_pp = PTR(c_char_p)
c_char_ppp = PTR(c_char_pp)

c_int = ctypes.c_int
c_int_p = PTR(c_int)

c_double = ctypes.c_double
c_double_p = PTR(c_double)
c_double_pp = PTR(c_double_p)


# CODES
NUMERIC = 0

# MISSING VALUE TYPE CODES

NO_MISSVAL = 0
ONE_MISSVAL = 1
TWO_MISSVAL = 2
THREE_MISSVAL = 3
MISS_RANGE = -2
MISS_RANGEANDVAL = -3

# ERROR CODES


class Error(enum.IntEnum):
    OK = 0
    FILE_OERROR = 1
    FILE_WERROR = 2
    FILE_RERROR = 3
    FITAB_FULL = 4
    INVALID_HANDLE = 5
    INVALID_FILE = 6
    NO_MEMORY = 7
    OPEN_RDMODE = 8
    OPEN_WRMODE = 9
    INVALID_VARNAME = 10
    DICT_EMPTY = 11
    VAR_NOTFOUND = 12
    DUP_VAR = 13
    NUME_EXP = 14
    STR_EXP = 15
    SHORTSTR_EXP = 16
    INVALID_VARTYPE = 17
    INVALID_MISSFOR = 18
    INVALID_COMPSW = 19
    INVALID_PRFOR = 20
    INVALID_WRFOR = 21
    INVALID_DATE = 22
    INVALID_TIME = 23
    NO_VARIABLES = 24
    MIXED_TYPES = 25
    DUP_VALUE = 27
    INVALID_CASEWGT = 28
    INCOMPATIBLE_DICT = 29
    DICT_COMMIT = 30
    DICT_NOTCOMMIT = 31
    NO_TYPE2 = 33
    NO_TYPE73 = 41
    INVALID_DATEINFO = 45
    NO_TYPE999 = 46
    EXC_STRVALUE = 47
    CANNOT_FREE = 48
    BUFFER_SHORT = 49
    INVALID_CASE = 50
    INTERNAL_VLABS = 51
    INCOMPAT_APPEND = 52
    INTERNAL_D_A = 53
    FILE_BADTEMP = 54
    DEW_NOFIRST = 55
    INVALID_MEASURELEVEL = 56
    INVALID_7SUBTYPE = 57
    INVALID_VARHANDLE = 58
    INVALID_ENCODING = 59
    FILES_OPEN = 60
    INVALID_MRSETDEF = 70
    INVALID_MRSETNAME = 71
    DUP_MRSETNAME = 72
    BAD_EXTENSION = 73
    INVALID_EXTENDEDSTRING = 74
    INVALID_ATTRNAME = 75
    INVALID_ATTRDEF = 76
    INVALID_MRSETINDEX = 77
    INVALID_VARSETDEF = 78
    INVALID_ROLE = 79
    INVALID_PASSWORD = 80
    EMPTY_PASSWORD = 81

    # WARNING CODES

    EXC_LEN64 = -1
    EXC_LEN120 = -2
    EXC_VARLABEL = -2
    EXC_LEN60 = -4
    EXC_VALLABEL = -4
    FILE_END = -5
    NO_VARSETS = -6
    EMPTY_VARSETS = -7
    NO_LABELS = -8
    NO_LABEL = -9
    NO_CASEWGT = -10
    NO_DATEINFO = -11
    NO_MULTRESP = -12
    EMPTY_MULTRESP = -13
    NO_DEW = -14
    EMPTY_DEW = -15


# FORMAT TYPE CODES


class Format(enum.IntEnum):
    A = 1  # Alphanumeric */
    AHEX = 2  # Alphanumeric hexadecimal */
    COMMA = 3  # F Format with commas */
    DOLLAR = 4  # Commas and floating dollar sign */
    F = 5  # Default Numeric Format */
    IB = 6  # Integer binary */
    PIBHEX = 7  # Positive integer binary - hex */
    P = 8  # Packed decimal */
    PIB = 9  # Positive integer binary unsigned */
    PK = 10  # Positive integer binary unsigned */
    RB = 11  # Floating point binary */
    RBHEX = 12  # Floating point binary hex */
    Z = 15  # Zoned decimal */
    N = 16  # N Format- unsigned with leading 0s */
    E = 17  # E Format- with explicit power of 10 */
    DATE = 20  # Date format dd-mmm-yyyy */
    TIME = 21  # Time format hh:mm:ss.s  */
    DATE_TIME = 22  # Date and Time           */
    ADATE = 23  # Date format mm/dd/yyyy */
    JDATE = 24  # Julian date - yyyyddd   */
    DTIME = 25  # Date-time dd hh:mm:ss.s */
    WKDAY = 26  # Day of the week         */
    MONTH = 27  # Month                   */
    MOYR = 28  # mmm yyyy                */
    QYR = 29  # q Q yyyy                */
    WKYR = 30  # ww WK yyyy              */
    PCT = 31  # Percent - F followed by % */
    DOT = 32  # Like COMMA, switching dot for comma */
    CCA = 33  # User Programmable currency format   */
    CCB = 34  # User Programmable currency format   */
    CCC = 35  # User Programmable currency format   */
    CCD = 36  # User Programmable currency format   */
    CCE = 37  # User Programmable currency format   */
    EDATE = 38  # Date in dd.mm.yyyy style            */
    SDATE = 39  # Date in yyyy/mm/dd style            */
    MTIME = 85  # Time format mm:ss.ss                */
    YMDHMS = 86  # Data format yyyy-mm-dd hh:mm:ss.ss  */


# MEASUREMENT LEVEL CODES


class MeasurementLevel(enum.IntEnum):
    UNK = 0  # Unknown */
    NOM = 1  # Nominal */
    ORD = 2  # Ordinal */
    RAT = 3  # Scale (Ratio) (Continues) */
    FLA = 4  #  Flag */
    TPL = 5  #  Typeless */


# ALIGNMENT CODES


class Alignment(enum.IntEnum):
    LEFT = 0
    RIGHT = 1
    CENTER = 2


# ROLE CODES


class Role(enum.IntEnum):
    INPUT = 0  # Input Role */
    TARGET = 1  # Target Role */
    BOTH = 2  # Both Roles */
    NONE = 3  # None Role */
    PARTITION = 4  # Partition Role */
    SPLIT = 5  # Split Role */
    FREQUENCY = 6  # Frequency Role */
    RECORDID = 7  # Record ID */


# DIAGNOSTICS REGARDING VAR NAMES


class NameResult(enum.IntEnum):
    OK = 0  # Valid standard name */
    SCRATCH = 1  # Valid scratch var name */
    SYSTEM = 2  # Valid system var name */
    BADLTH = 3  # Empty or longer than MAX_VARNAME */
    BADCHAR = 4  # Invalid character or imbedded blank */
    RESERVED = 5  # Name is a reserved word */
    BADFIRST = 6  # Invalid initial character */


# MAXIMUM LENGTHS OF DATA FILE OBJECTS

MAX_VARNAME = 64  # Variable name */
MAX_SHORTVARNAME = 8  # Short (compatibility) variable name */
MAX_SHORTSTRING = 8  # Short string variable */
MAX_IDSTRING = 64  # File label string */
MAX_LONGSTRING = 32767  # Long string variable */
MAX_VALLABEL = 120  # Value label */
MAX_VARLABEL = 256  # Variable label */
MAX_ENCODING = 64  # Maximum encoding text */
MAX_7SUBTYPE = 40  # Maximum record 7 subtype */
MAX_PASSWORD = 10  # Maximum password */

# Type 7 record subtypes


class Type7(enum.IntEnum):
    DOCUMENTS = 0  # Documents (actually type 6 */
    VAXDE_DICT = 1  # VAX Data Entry - dictionary version */
    VAXDE_DATA = 2  # VAX Data Entry - data */
    SOURCE = 3  # Source system characteristics */
    HARDCONST = 4  # Source system floating pt constants */
    VARSETS = 5  # Variable sets */
    TRENDS = 6  # Trends date information */
    MULTRESP = 7  # Multiple response groups */
    DEW_DATA = 8  # Windows Data Entry data */
    TEXTSMART = 10  # TextSmart data */
    MSMTLEVEL = 11  # Msmt level, col width, & alignment */
    DEW_GUID = 12  # Windows Data Entry GUID */
    XVARNAMES = 13  # Extended variable names */
    XSTRINGS = 14  # Extended strings */
    CLEMENTINE = 15  # Clementine Metadata */
    NCASES = 16  # 64 bit N of cases */
    FILE_ATTR = 17  # File level attributes */
    VAR_ATTR = 18  # Variable attributes */
    EXTMRSETS = 19  # Extended multiple response groups */
    ENCODING = 20  # Encoding, aka code page */
    LONGSTRLABS = 21  # Value labels for long strings */
    LONGSTRMVAL = 22  # Missing values for long strings */
    SORTINDEX = 23  # Sort Index information */


# Encoding modes


class Encoding(enum.IntEnum):
    CODEPAGE = 0  # Text encoded in current code page */
    UTF8 = 1  # Text encoded as UTF-8 */


class CMultipleResponse(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char * (MAX_VARNAME + 1)),
        ("label", ctypes.c_char * (MAX_VARLABEL + 1)),
        ("is_dichotomy", c_int),
        ("is_numeric", c_int),
        ("use_category_labels", c_int),
        ("use_first_variable_label", c_int),
        ("_reserved", c_int * 14),
        ("counts", ctypes.c_long),
        ("counted_value", c_char_p),
        ("variable_names", c_char_pp),
        ("nb_variables", c_int),
    ]


CMultipleResponse_p = PTR(CMultipleResponse)


sentinel = object()


def get_lib_path():
    system = platform.system().lower()
    if system.startswith("win"):
        return libs_dir / "win64" / "spssio64.dll"
    elif system.startswith("darwin"):
        return libs_dir / "macos" / "libspssdio.dylib"
    elif system.startswith("lin"):
        return libs_dir / "lin64" / "libspssdio.so.1"


def _load_library(path: pathlib.Path):
    log.info("loading %s...", path.name)
    while True:
        try:
            result = ctypes.CDLL(path)
        except OSError as error:
            dependency = error.args[0].split(":", 1)[0]
            log.info("loading %s failed: missing dependency %s", path.name, dependency)
            dependency = path.parent / dependency
            _load_library(dependency)
            continue
        log.info("Success loading %s", path.name)
        return result


class SPSSError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return f"{self.error.value}: {self.error.name}"


def _errcheck(result, func, arguments):
    if func.restype == Error:
        if result > 0:
            raise SPSSError(result)
        elif result < 0:
            log.warning("%s: %s", func.__name__, result.name)
    return result


def _register(func, argtypes, restype, errcheck=sentinel):
    func.argtypes = argtypes
    func.restype = restype
    if errcheck is sentinel and restype == Error:
        func.errcheck = _errcheck


def _init_library(spss):
    _register(spss.spssOpenAppend, [c_char_p, c_int_p], Error)
    _register(spss.spssOpenAppend, [c_char_p, c_char_p, c_int_p], Error)
    _register(spss.spssOpenAppendU8, [c_char_p, c_int_p], Error)
    _register(spss.spssOpenAppendU8Ex, [c_char_p, c_char_p, c_int_p], Error)
    _register(spss.spssOpenRead, [c_char_p, c_int_p], Error)
    _register(spss.spssOpenReadEx, [c_char_p, c_char_p, c_int_p], Error)
    _register(spss.spssOpenReadU8, [c_char_p, c_int_p], Error)
    _register(spss.spssOpenReadU8Ex, [c_char_p, c_char_p, c_int_p], Error)
    _register(spss.spssOpenWrite, [c_char_p, c_int_p], Error)
    _register(spss.spssOpenWriteEx, [c_char_p, c_char_p, c_int_p], Error)
    _register(spss.spssOpenWriteU8, [c_char_p, c_int_p], Error)
    _register(spss.spssOpenWriteU8Ex, [c_char_p, c_char_p, c_int_p], Error)
    _register(spss.spssOpenWriteCopy, [c_char_p, c_char_p, c_int_p], Error)
    _register(spss.spssOpenWriteCopyEx, [c_char_p, c_char_p, c_char_p, c_int_p], Error)
    _register(
        spss.spssOpenWriteCopyExFile, [c_char_p, c_char_p, c_char_p, c_int_p], Error
    )
    _register(
        spss.spssOpenWriteCopyExDict, [c_char_p, c_char_p, c_char_p, c_int_p], Error
    )
    _register(spss.spssOpenWriteCopyU8, [c_char_p, c_char_p, c_int_p], Error)
    _register(
        spss.spssOpenWriteCopyU8Ex,
        [c_char_p, c_char_p, c_char_p, c_char_p, c_int_p],
        Error,
    )
    _register(
        spss.spssOpenWriteCopyU8ExFile, [c_char_p, c_char_p, c_char_p, c_int_p], Error
    )
    _register(
        spss.spssOpenWriteCopyU8ExDict, [c_char_p, c_char_p, c_char_p, c_int_p], Error
    )
    _register(spss.spssCloseAppend, [c_int], Error)
    _register(spss.spssCloseRead, [c_int], Error)
    _register(spss.spssCloseWrite, [c_int], Error)
    _register(spss.spssGetCompression, [c_int, c_int_p], Error)
    _register(spss.spssGetIdString, [c_int, c_char_p], Error)
    _register(spss.spssGetVariableSets, [c_int, c_char_pp], Error)
    _register(
        spss.spssGetFileAttributes, [c_int, c_char_ppp, c_char_ppp, c_int_p], Error
    )
    _register(spss.spssFreeAttributes, [c_char_pp, c_char_pp, c_int], Error)
    _register(
        spss.spssFreeMultRespDefStruct,
        [
            CMultipleResponse_p,
        ],
        Error,
    )
    _register(
        spss.spssGetVarNValueLabels,
        [c_int, c_char_p, c_double_pp, c_char_ppp, c_int_p],
        Error,
    )
    _register(
        spss.spssGetVarPrintFormat, [c_int, c_char_p, c_int_p, c_int_p, c_int_p], Error
    )
    _register(spss.spssGetVarRole, [c_int, c_char_p, c_int_p], Error)
    _register(spss.spssGetVarAlignment, [c_int, c_char_p, c_int_p], Error)
    _register(spss.spssGetVarColumnWidth, [c_int, c_char_p, c_int_p], Error)
    _register(spss.spssGetMultRespDefs, [c_int, c_char_pp], Error)
    _register(spss.spssGetMultRespDefsEx, [c_int, c_char_pp], Error)
    _register(spss.spssFreeMultRespDefs, [c_char_p], Error)
    _register(
        spss.spssGetMultRespDefByIndex, [c_int, c_int, PTR(CMultipleResponse_p)], Error
    )
    _register(spss.spssReadCaseRecord, [c_int], Error)
    _register(spss.spssSeekNextCase, [c_int, ctypes.c_long], Error)
    _register(spss.spssGetValueChar, [c_int, c_double, c_char_p, c_int], Error)
    _register(spss.spssGetValueNumeric, [c_int, c_double, c_double_p], Error)
    _register(spss.spssWholeCaseIn, [c_int, ctypes.c_void_p], Error)

    _register(spss.spssGetFileEncoding, [c_int, c_char_p], Error)
    _register(spss.spssQueryType7, [c_int, c_int, c_int_p], Error)

    _register(spss.spssGetFileCodePage, [c_int, c_int_p], Error)
    _register(spss.spssSysmisVal, [], c_double)
    _register(spss.spssLowHighVal, [c_double_p, c_double_p], None)
    _register(spss.spssGetInterfaceEncoding, [], Encoding)
    _register(spss.spssSetInterfaceEncoding, [c_int], Error)
    _register(spss.spssValidateVarname, [c_char_p], NameResult)
    _register(spss.spssSetTempDir, [c_char_p], Error)


def _parse_range(start, stop, step, size):
    if start is None:
        start = 0
    if stop is None:
        stop = size
    if step is None:
        step = 1
    return start, stop, step


def load_library():
    if (path := get_lib_path()) is None:
        raise SPSSError("Cannot find spss dynamic library")
    spss = _load_library(path)
    _init_library(spss)
    return spss


def numpy_dtype(variable):
    if variable.type:
        size = max(8, variable.type)
        return numpy.dtype(f"|S{size}")
    return numpy.float64


def numpy_dtypes(variables):
    return numpy.dtype(
        [(variable.name, numpy_dtype(variable)) for variable in variables]
    )


def struct_dtype(variable):
    if variable.type:
        size = max(8, variable.type)
        return f"{size}s"
    return "d"


def struct_dtypes(variables):
    return struct.Struct("".join(struct_dtype(variable) for variable in variables))


lib = load_library()


def encoding():
    return lib.spssGetInterfaceEncoding()


def set_encoding(encoding):
    return lib.spssSetInterfaceEncoding(encoding)


def low_high_value():
    low, high = c_double(), c_double()
    lib.spssLowHighVal(ptr(low), ptr(high))
    return low.value, high.value


def missing_value():
    return lib.spssSysmisVal()


def open(filename, mode="r"):
    path = pathlib.Path(filename)
    if "w" in mode:
        raise NotImplementedError()
    elif "a" in mode:
        raise NotImplementedError()
    else:
        handle = c_int()
        lib.spssOpenRead(bytes(path), ptr(handle))
        return SPSSFile(filename, handle, mode)


def close(handle, mode):
    if "w" in mode:
        lib.spssCloseWrite(handle)
    else:
        lib.spssCloseRead(handle)


def id_(handle):
    result = ctypes.create_string_buffer(64)
    lib.spssGetIdString(handle, result)
    return result.value.decode()


def file_encoding(handle):
    result = ctypes.create_string_buffer(MAX_ENCODING)
    lib.spssGetFileEncoding(handle, result)
    return result.value.decode()


def variable_count(handle):
    result = c_int()
    lib.spssGetNumberofVariables(handle, ptr(result))
    return result.value


def case_count(handle):
    result = c_int()
    lib.spssGetNumberofCases(handle, ptr(result))
    return result.value


def case_size(handle):
    size = ctypes.c_long()
    lib.spssGetCaseSize(handle, ptr(size))
    return size.value


def compression(handle):
    result = c_int()
    lib.spssGetCompression(handle, ptr(result))
    return result.value


def attributes(handle):
    names = c_char_pp()
    text = c_char_pp()
    n = c_int()
    lib.spssGetFileAttributes(handle, ptr(names), ptr(text), ptr(n))
    result = {names[i].decode(): text[i].decode() for i in range(n.value)}
    lib.spssFreeAttributes(names, text, n)
    return result


def variable_sets(handle):
    result = c_char_p()
    reply = lib.spssGetVariableSets(handle, ptr(result))
    if reply == Error.EMPTY_VARSETS:
        return None
    if (value := result.value) is not None:
        lib.spssFreeVariableSets(result)
    return value


def variables(handle):
    names = c_char_pp()
    n = c_int()
    types = c_int_p()
    lib.spssGetVarNames(handle, ptr(n), ptr(names), ptr(types))
    result = [(names[i].decode(), types[i]) for i in range(n.value)]
    lib.spssFreeVarNames(names, types, n.value)
    return result


def weight_variable_name(handle):
    name = ctypes.create_string_buffer(65)
    lib.spssGetCaseWeightVar(handle, name)
    return name.value.decode()


def variable_column_width(handle, name: str):
    result = c_int()
    lib.spssGetVarColumnWidth(handle, name.encode(), ptr(result))
    return result.value


def variable_alignment(handle, name: str):
    result = c_int()
    lib.spssGetVarAlignment(handle, name.encode(), ptr(result))
    return Alignment(result.value)


def variable_label(handle, name: str):
    label = ctypes.create_string_buffer(256)
    label_len = c_int()
    lib.spssGetVarLabelLong(handle, name.encode(), label, 256, ptr(label_len))
    return label.value.decode()


def variable_handle(handle, name: str):
    var_handle = c_double()
    lib.spssGetVarHandle(handle, name.encode(), ptr(var_handle))
    return var_handle


def variable_attributes(handle, name):
    names = c_char_pp()
    text = c_char_pp()
    n = c_int()
    lib.spssGetVarAttributes(handle, name.encode(), ptr(names), ptr(text), ptr(n))
    result = {names[i].decode(): text[i].decode() for i in range(n.value)}
    lib.spssFreeAttributes(names, text, n)
    return result


def variable_labels(handle, name):
    n = c_int()
    values = c_double_p()
    labels = c_char_pp()
    lib.spssGetVarNValueLabels(handle, name.encode(), ptr(values), ptr(labels), ptr(n))
    result = {labels[i].decode(): values[i] for i in range(n.value)}
    lib.spssFreeVarNValueLabels(values, labels, n)
    return result


def variable_role(handle, name):
    result = c_int()
    lib.spssGetVarRole(handle, name.encode(), ptr(result))
    return Role(result.value)


def variable_measure_level(handle, name):
    result = c_int()
    lib.spssGetVarMeasureLevel(handle, name.encode(), ptr(result))
    return MeasurementLevel(result.value)


def variable_missing_values(handle, name):
    fmt = c_int()
    v1, v2, v3 = c_double(), c_double(), c_double()
    lib.spssGetVarNMissingValues(
        handle, name.encode(), ptr(fmt), ptr(v1), ptr(v2), ptr(v3)
    )
    value = fmt.value
    if value == MISS_RANGE:
        return (v2.value, v1.value), ()
    elif value == MISS_RANGEANDVAL:
        return (v2.value, v1.value), (v3.value,)
    elif value == 0:
        return (), ()
    elif value == 1:
        return (), (v1.value,)
    elif value == 2:
        return (), (v1.value, v2.value)
    return (), (v1.value, v2.value, v3.value)


def variable_print_format(handle, name):
    typ = c_int()
    dec = c_int()
    width = c_int()
    lib.spssGetVarPrintFormat(handle, name.encode(), ptr(typ), ptr(dec), ptr(width))
    return Format(typ.value), dec.value, width.value


def value_string(handle, var_handle, size):
    value = ctypes.create_string_buffer(size)
    lib.spssGetValueChar(handle, var_handle, value, size)
    return value.value


def value_numeric(handle, var_handle):
    value = c_double()
    lib.spssGetValueNumeric(handle, var_handle, ptr(value))
    return value.value


def text_info(handle):
    result = ctypes.create_string_buffer(42)
    lib.spssGetTextInfo(handle, result)
    return result.value.decode()


def system(handle):
    result = ctypes.create_string_buffer(256)
    lib.spssGetSystemString(handle, result)
    return result.value.decode()


def read_case(handle):
    return lib.spssReadCaseRecord(handle)


def seek(handle, i):
    return lib.spssSeekNextCase(handle, i)


def raw_row(handle, buffer=None):
    if buffer is None:
        size = case_size(handle)
        buffer = ctypes.create_string_buffer(size)
    lib.spssWholeCaseIn(handle, buffer)
    return buffer


def raw_row_at(handle, index, buffer=None):
    seek(handle, index)
    return raw_row(handle, buffer)


def multiple_response_count(handle):
    result = c_int()
    lib.spssGetMultRespCount(handle, ptr(result))
    return result.value


def multiple_responses(handle):
    mr_ptr = CMultipleResponse_p()
    result = []
    for i in range(multiple_response_count(handle)):
        lib.spssGetMultRespDefByIndex(handle, i, ptr(mr_ptr))
        mr = mr_ptr.contents
        result.append(MultipleResponse.from_c(mr))
        lib.spssFreeMultRespDefStruct(mr_ptr)
    return result


def has_type_7_record(handle, subtype: Type7):
    result = c_int()
    lib.spssQueryType7(handle, subtype, ptr(result))
    return bool(result)


def code_page(handle):
    result = c_int()
    lib.spssGetFileCodePage(handle, ptr(result))
    return result.value


class Variable:
    def __init__(self, fobj, name, type, index) -> None:
        self.fobj = fobj
        self.name = name
        self.type = type
        self.index = index
        if type:

            def value():
                return fobj.value_string(self.handle, type + 1)
        else:

            def value():
                return fobj.value_numeric(self.handle)

        self.value = value

    @functools.cached_property
    def label(self):
        return self.fobj.variable_label(self.name)

    @functools.cached_property
    def labels(self):
        if self.type:
            return None
        return self.fobj.variable_labels(self.name)

    @functools.cached_property
    def column_width(self):
        return self.fobj.variable_column_width(self.name)

    @functools.cached_property
    def alignment(self):
        return self.fobj.variable_alignment(self.name)

    @functools.cached_property
    def role(self):
        return self.fobj.variable_role(self.name)

    @functools.cached_property
    def handle(self):
        return self.fobj.variable_handle(self.name)

    @functools.cached_property
    def measure_level(self):
        return self.fobj.variable_measure_level(self.name)

    @functools.cached_property
    def missing_values(self):
        return self.fobj.variable_missing_values(self.name)

    @functools.cached_property
    def print_format(self):
        return self.fobj.variable_print_format(self.name)

    @functools.cached_property
    def attributes(self):
        return self.fobj.variable_attributes(self.name)

    def __repr__(self):
        t = f"str[{self.type + 1}]" if self.type else "f64"
        return f"V({self.index}, {self.name}, {t})"


class SPSSFile:
    def __init__(self, filename, handle, mode):
        self.filename = filename
        self.handle = handle
        self.mode = mode
        self.closed = False

    def __int__(self):
        return self.handle.value

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __len__(self):
        return self.case_count()

    def __iter__(self):
        return self.iter_read_many()

    def __del__(self):
        self.close()

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.row_at(item)
        if isinstance(item, tuple):
            st = self._row_struct
            buffer = ctypes.create_string_buffer(st.size)
            return tuple(self.row_at(index, buffer) for index in item)
        elif isinstance(item, slice):
            return tuple(self.iter_read_many(item.start, item.stop, item.step))
        raise TypeError(type(item).__name__)

    @functools.cached_property
    def _row_struct(self):
        return struct_dtypes(self.variable_cache)

    @functools.cached_property
    def variable_cache(self):
        return [
            Variable(self, name, type, index)
            for index, (name, type) in enumerate(self.variables())
        ]

    @functools.cached_property
    def variable_name_cache(self):
        return {variable.name: variable for variable in self.variable_cache}

    @functools.cached_property
    def shape(self):
        return self.case_count(), self.variable_count()

    @functools.cached_property
    def dtype(self):
        return numpy_dtypes(self.variable_cache)

    @functools.cached_property
    def weight_variable_name(self):
        return weight_variable_name(self.handle)

    @functools.cached_property
    def weight_variable(self):
        if not self.weight_variable_name:
            return None
        return self.variable_name_cache[self.weight_variable_name]

    def compression(self):
        return compression(self.handle)

    def close(self):
        if self.closed:
            return
        close(self.handle, self.mode)
        self.closed = True

    def id(self):
        return id_(self.handle)

    def encoding(self):
        return file_encoding(self.handle)

    def variable_count(self):
        return variable_count(self.handle)

    def case_count(self):
        return case_count(self.handle)

    def case_size(self):
        return case_size(self.handle)

    def attributes(self):
        return attributes(self.handle)

    def variable_sets(self):
        return variable_sets(self.handle)

    def variables(self):
        return variables(self.handle)

    def variable_column_width(self, name: str):
        return variable_column_width(self.handle, name)

    def variable_alignment(self, name: str):
        return variable_alignment(self.handle, name)

    def variable_label(self, name: str):
        return variable_label(self.handle, name)

    def variable_handle(self, name: str):
        return variable_handle(self.handle, name)

    def variable_attributes(self, name):
        return variable_attributes(self.handle, name)

    def variable_labels(self, name):
        return variable_labels(self.handle, name)

    def variable_role(self, name):
        return variable_role(self.handle, name)

    def variable_measure_level(self, name):
        return variable_measure_level(self.handle, name)

    def variable_missing_values(self, name):
        return variable_missing_values(self.handle, name)

    def variable_print_format(self, name):
        return variable_print_format(self.handle, name)

    def value_string(self, handle, size):
        return value_string(self.handle, handle, size)

    def value_numeric(self, handle):
        return value_numeric(self.handle, handle)

    def text_info(self):
        return text_info(self.handle)

    def system(self):
        return system(self.handle)

    def read_case(self):
        return read_case(self.handle)

    def seek(self, row):
        return seek(self.handle, row)

    def raw_row(self, buffer=None):
        return raw_row(self.handle, buffer)

    def raw_row_at(self, index, buffer=None):
        return raw_row_at(self.handle, index, buffer)

    def row(self, buffer=None):
        buffer = self.raw_row(buffer)
        return self._row_struct.unpack(buffer)

    def row_at(self, index, buffer=None):
        buffer = self.raw_row_at(index, buffer)
        return self._row_struct.unpack(buffer)

    def multiple_response_count(self):
        return multiple_response_count(self.handle)

    @functools.cached_property
    def multiple_responses(self):
        return multiple_responses(self.handle)

    def has_type_7_record(self, subtype: Type7):
        return has_type_7_record(self.handle, subtype)

    def code_page(self):
        return code_page(self.handle)

    def read_many(self, start=None, stop=None, step=None):
        total_rows = self.case_count()
        start, stop, step = _parse_range(start, stop, step, total_rows)
        rng = range(stop - start) if step == 1 else range(start, stop, step)
        nb_rows = len(rng)
        buffer = numpy.ndarray((nb_rows,), dtype=self.dtype)
        base = buffer.ctypes.data
        row_size = buffer.dtype.itemsize

        if step == 1:
            self.seek(start)
            for i in rng:
                self.raw_row(base + i * row_size)
            return buffer

        for i, row in enumerate(rng):
            self.raw_row_at(row, base + i * row_size)
        return buffer

    def iter_read_many(self, start=None, stop=None, step=None):
        total_rows = self.case_count()
        start, stop, step = _parse_range(start, stop, step, total_rows)
        row_size = self.case_size()
        buffer = ctypes.create_string_buffer(row_size)

        if step == 1:
            self.seek(start)
            for i in range(stop - start):
                yield self.row(buffer)
        else:
            for i in range(start, stop, step):
                yield self.row_at(i, buffer)


@dataclasses.dataclass
class MultipleResponse:
    name: str
    label: str
    is_dichotomy: bool
    is_numeric: bool
    use_category_labels: bool
    use_first_variable_label: bool
    counted_value: float | str | None
    variable_names: list[str]

    @classmethod
    def from_c(cls, mr):
        if mr.is_numeric:
            counted_value = mr.counts
        else:
            counted_value = (
                None if mr.counted_value is None else mr.counted_value.decode()
            )
        return cls(
            name=mr.name.decode(),
            label=mr.label.decode(),
            is_dichotomy=bool(mr.is_dichotomy),
            is_numeric=bool(mr.is_numeric),
            use_category_labels=bool(mr.use_category_labels),
            use_first_variable_label=bool(mr.use_first_variable_label),
            counted_value=counted_value,
            variable_names=[
                mr.variable_names[i].decode() for i in range(mr.nb_variables)
            ],
        )
