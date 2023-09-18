from .exception import *
from .common import *

# ========================================================================
#
# Field Class
#
# ========================================================================

class X3DField:
    def NODE_NAME(self):
        return self.__class__.__name__

class X3DArrayField:
    def NODE_NAME(self):
        return self.__class__.__name__


class SFBool(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFBool(value)
        self.__value = value

class MFBool(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFBool(value)
        self.__value = value

class SFColor(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFColor(value)
        self.__value = value

class MFColor(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFColor(value)
        self.__value = value

class SFColorRGBA(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFColorRGBA(value)
        self.__value = value

class MFColorRGBA(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFColorRGBA(value)
        self.__value = value

class SFDouble(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFDouble(value)
        self.__value = value

class MFDouble(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFDouble(value)
        self.__value = value

class SFFloat(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFFloat(value)
        self.__value = value

class MFFloat(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFFloat(value)
        self.__value = value

class SFImage(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFImage(value)
        self.__value = value

class MFImage(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFImage(value)
        self.__value = value

class SFInt32(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFInt32(value)
        self.__value = value

class MFInt32(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFInt32(value)
        self.__value = value

class SFNode(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFNode(value)
        self.__value = value

class MFNode(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFNode(value)
        self.__value = value

class SFRotation(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFRotation(value)
        self.__value = value

class MFRotation(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFRotation(value)
        self.__value = value

class SFString(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFString(value)
        self.__value = value

class MFString(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFString(value)
        self.__value = value

class SFTime(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFTime(value)
        self.__value = value

class MFTime(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFTime(value)
        self.__value = value

class SFVec2d(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFVec2d(value)
        self.__value = value

class MFVec2d(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFVec2d(value)
        self.__value = value

class SFVec2f(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFVec2f(value)
        self.__value = value

class MFVec2f(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFVec2f(value)
        self.__value = value

class SFVec3d(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFVec3d(value)
        self.__value = value

class MFVec3d(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFVec3d(value)
        self.__value = value

class SFVec3f(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFVec3f(value)
        self.__value = value

class MFVec3f(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFVec3f(value)
        self.__value = value

class SFVec4d(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFVec4d(value)
        self.__value = value

class MFVec4d(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFVec4d(value)
        self.__value = value

class SFVec4f(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFVec4f(value)
        self.__value = value

class MFVec4f(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFVec4f(value)
        self.__value = value

class SFMatrix3d(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFMatrix3d(value)
        self.__value = value

class MFMatrix3d(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFMatrix3d(value)
        self.__value = value

class SFMatrix3f(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFMatrix3f(value)
        self.__value = value

class MFMatrix3f(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFMatrix3f(value)
        self.__value = value

class SFMatrix4d(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFMatrix4d(value)
        self.__value = value

class MFMatrix4d(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFMatrix4d(value)
        self.__value = value

class SFMatrix4f(X3DField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertSFMatrix4f(value)
        self.__value = value

class MFMatrix4f(X3DArrayField):
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        assertMFMatrix4f(value)
        self.__value = value

# ========================================================================
#
# Specification Field Validation Functions
#
# ========================================================================

def assertValidGreaterThan(value, minValue):
    if value is None:
        raise X3DValueException

    if isinstance(value, X3DField):
        value = value.value
    elif isinstance(value, X3DArrayField):
        temp = []
        for element in value:
            if isinstance(element, X3DField):
                temp.append(element.value)
            else:
                temp.append(element)
        value = list(temp)

    if isinstance(value, list):
        for element in value:
            if isinstance(element, list):
                for e in element:
                    if e <= minValue:
                        raise X3DValueException
            else:
                if element <= minValue:
                    raise X3DValueException

    elif isinstance(value, (int, float)):
        if value <= minValue:
            raise X3DValueException

    else:
        raise X3DValueException

    return False

def assertValidGreaterThanEquals(value, minValue):
    if value is None:
        raise X3DValueException

    if isinstance(value, X3DField):
        value = value.value
    elif isinstance(value, X3DArrayField):
        temp = []
        for element in value:
            if isinstance(element, X3DField):
                temp.append(element.value)
            else:
                temp.append(element)
        value = list(temp)

    if isinstance(value, list):
        for element in value:
            if isinstance(element, list):
                for e in element:
                    if e < minValue:
                        raise X3DValueException
            else:
                if element < minValue:
                    raise X3DValueException

    elif isinstance(value, (int, float)):
        if value < minValue:
            raise X3DValueException

    else:
        raise X3DValueException

    return False

def assertValidLessThan(value, maxValue):
    if value is None:
        raise X3DValueException

    if isinstance(value, X3DField):
        value = value.value
    elif isinstance(value, X3DArrayField):
        temp = []
        for element in value:
            if isinstance(element, X3DField):
                temp.append(element.value)
            else:
                temp.append(element)
        value = list(temp)

    if isinstance(value, list):
        for element in value:
            if isinstance(element, list):
                for e in element:
                    if e >= maxValue:
                        raise X3DValueException
            else:
                if element >= maxValue:
                    raise X3DValueException

    elif isinstance(value, (int, float)):
        if value >= maxValue:
            raise X3DValueException

    else:
        raise X3DValueException

    return False

def assertValidLessThanEquals(value, maxValue):
    if value is None:
        raise X3DValueException

    if isinstance(value, X3DField):
        value = value.value
    elif isinstance(value, X3DArrayField):
        temp = []
        for element in value:
            if isinstance(element, X3DField):
                temp.append(element.value)
            else:
                temp.append(element)
        value = list(temp)

    if isinstance(value, list):
        for element in value:
            if isinstance(element, list):
                for e in element:
                    if e > maxValue:
                        raise X3DValueException
            else:
                if element > maxValue:
                    raise X3DValueException

    elif isinstance(value, (int, float)):
        if value > maxValue:
            raise X3DValueException

    else:
        raise X3DValueException

    return False

def assertValidTolerance(value):
    if value is None:
        raise X3DValueException

    if isinstance(value, SFFloat):
        value = value.value

    if value != -1 and value < 0:
        raise X3DValueException

def assertValidBboxSize(value):
    if value is None:
        raise X3DValueException

    if isinstance(value, SFVec3f):
        value = value.value

    if isinstance(value, list):
        if len(value) != 3:
            raise X3DValueException
        if value[0] == -1 and value[1] == -1 and value[2] == -1:
            return False
        elif value[0] >= 0 and value[1] >= 0 and value[2] >= 0:
            return False
        else:
            raise X3DValueException

def assertValidLODRange(value):
    if not isinstance(value, list) and not isinstance(value, MFFloat):
        raise X3DTypeException
    
    if isinstance(value, MFFloat):
        value = value.value
    
    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFFloat):
            raise X3DTypeException

        if isinstance(v, SFFloat):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        if v[0] < 0 and v[0] != -1:
            raise X3DValueException

    return False

def assertValidMaxCorrectionSpeed(value):
    if not isinstance(value, float) and not isinstance(value, SFFloat):
        raise X3DTypeException
    
    if isinstance(value, MFFloat):
        value = value.value

    if value < 0 and value != -1:
        raise X3DValueException

    return False

# ========================================================================
#
# Field Validation Functions
#
# ========================================================================

def assertX3DField(value):
    if not isinstance(value, X3DField):
        raise X3DTypeException

    return False

def assertX3DArrayField(value):
    if not isinstance(value, X3DArrayField):
        raise X3DTypeException

    return False

def assertSFBool(value):
    if not isinstance(value, bool) and not isinstance(value, SFBool):
        raise X3DTypeException

    if isinstance(value, SFBool):
        value = value.value

    if not isinstance(value, bool):
        raise X3DTypeException

    return False

def assertMFBool(value):
    if not isinstance(value, list) and not isinstance(value, MFBool):
        raise X3DTypeException

    if isinstance(value, MFBool):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, bool) and not isinstance(v, SFBool):
            raise X3DTypeException

        if isinstance(v, SFBool):
            v = v.value

        if not isinstance(v, bool):
            raise X3DTypeException

    return False

def assertSFColor(value):
    if not isinstance(value, list) and not isinstance(value, SFColor):
        raise X3DTypeException

    if isinstance(value, SFColor):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

        if v < 0 or v > 1:
            raise X3DValueException

    if count != 3:
        raise X3DValueException

    return False

def assertMFColor(value):
    if not isinstance(value, list) and not isinstance(value, MFColor):
        raise X3DTypeException

    if isinstance(value, MFColor):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFColor):
            raise X3DTypeException

        if isinstance(v, SFColor):
            v = v.value

        if not isinstance(v, list):
            raise X3DTypeExceptione

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

            if v2 < 0 or v2 > 1:
                raise X3DValueException

        if count != 3:
            raise X3DValueException

    return False

def assertSFColorRGBA(value):
    if not isinstance(value, list) and not isinstance(value, SFColorRGBA):
        raise X3DTypeException

    if isinstance(value, SFColorRGBA):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

        if v < 0 or v > 1:
            raise X3DValueException

    if count != 4:
        raise X3DValueException

    return False

def assertMFColorRGBA(value):
    if not isinstance(value, list) and not isinstance(value, MFColorRGBA):
        raise X3DTypeException

    if isinstance(value, MFColorRGBA):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFColorRGBA):
            raise X3DTypeException

        if isinstance(v, SFColorRGBA):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

            if v2 < 0 or v2 > 1:
                raise X3DValueException

        if count != 4:
            raise X3DValueException

    return False

def assertSFDouble(value):
    if not isinstance(value, float) and not isinstance(value, SFDouble):
        raise X3DTypeException

    if isinstance(value, SFDouble):
        value = value.value

    if not isinstance(value, float):
        raise X3DTypeException

    return False

def assertMFDouble(value):
    if not isinstance(value, list) and not isinstance(value, MFDouble):
        raise X3DTypeException

    if isinstance(value, MFDouble):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, float) and not isinstance(v, SFDouble):
            raise X3DTypeException

        if isinstance(v, SFDouble):
            v = v.value

        if not isinstance(v, float):
            raise X3DTypeException

    return False

def assertSFFloat(value):
    if not isinstance(value, float) and not isinstance(value, SFFloat):
        raise X3DTypeException

    if isinstance(value, SFFloat):
        value = value.value

    if not isinstance(value, float):
        raise X3DTypeException

    return False

def assertMFFloat(value):
    if not isinstance(value, list) and not isinstance(value, MFFloat):
        raise X3DTypeException

    if isinstance(value, MFFloat):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, float) and not isinstance(v, SFFloat):
            raise X3DTypeException

        if isinstance(v, SFFloat):
            v = v.value

        if not isinstance(v, float):
            raise X3DTypeException

    return False

def assertSFImage(value):
    if not isinstance(value, list) and not isinstance(value, SFImage):
        raise X3DTypeException

    if isinstance(value, SFImage):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    if len(value) > 0:
        width = value[0]
        height = value[1]
        components = value[2]
        pixels = value[3]

        if not isinstance(width, int) or not isinstance(height, int) or not isinstance(components, int) or not pixels(width, list):
            raise X3DTypeException

        if width < 0 or height < 0 or (components < 1 or components > 4):
            raise X3DValueException

        if len(pixels) != (width * height * components):
            raise X3DValueException

        for p in pixels:
            if not isinstance(p, int):
                raise X3DTypeException

            if p < 0 or p > 255:
                raise X3DValueException

    return False

def assertMFImage(value):
    if not isinstance(value, list) and not isinstance(value, MFImage):
        raise X3DTypeException

    if isinstance(value, MFImage):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if len(v) > 0:
            width = v[0]
            height = v[1]
            components = v[2]
            pixels = v[3]

            if not isinstance(width, int) or not isinstance(height, int) or not isinstance(components, int) or not pixels(width, list):
                raise X3DTypeException

            if width < 0 or height < 0 or (components < 1 or components > 4):
                raise X3DValueException

            if len(pixels) != (width * height * components):
                raise X3DValueException

            for p in pixels:
                if not isinstance(p, int):
                    raise X3DTypeException

                if p < 0 or p > 255:
                    raise X3DValueException
    return False

def assertSFInt32(value):
    if not isinstance(value, int) and not isinstance(value, SFInt32):
        raise X3DTypeException

    if isinstance(value, SFInt32):
        value = value.value

    if not isinstance(value, int):
        raise X3DTypeException

    return False

def assertMFInt32(value):
    if not isinstance(value, list) and not isinstance(value, MFInt32):
        raise X3DTypeException

    if isinstance(value, MFInt32):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, int) and not isinstance(v, SFInt32):
            raise X3DTypeException

        if isinstance(v, SFInt32):
            v = v.value

        if not isinstance(v, int):
            raise X3DTypeException

    return False

def assertSFNode(value, *args):
    if not value:
        return False

    if not isinstance(value, object) and not isinstance(value, SFNode):
        raise X3DTypeException

    if isinstance(value, SFNode):
        value = value.value

    flag = True
    if args is None or args == ():
        raise Exception
    else:
        for k, v in enumerate(args):
            if isinstance(value, v):
                flag = False
    
    if flag:
        raise Exception

    return False

def assertMFNode(value, *args):
    if not isinstance(value, list) and not isinstance(value, MFNode):
        raise X3DTypeException

    if isinstance(value, MFNode):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    if args is None or args == ():
        raise Exception
    else:
        for k, v in enumerate(value):
            flag = True

            if not isinstance(v, object) and not isinstance(v, SFNode):
                raise X3DTypeException

            if isinstance(v, SFNode):
                v = v.value

            for k2, v2 in enumerate(args):
                if isinstance(v, v2):
                    flag = False
            
            if flag:
                raise Exception

    return False

def assertSFRotation(value):
    if not isinstance(value, list) and not isinstance(value, SFRotation):
        raise X3DTypeException

    if isinstance(value, SFRotation):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 4:
        raise X3DValueException

    return False

def assertMFRotation(value):
    if not isinstance(value, list) and not isinstance(value, MFRotation):
        raise X3DTypeException

    if isinstance(value, MFRotation):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFRotation):
            raise X3DTypeException

        if isinstance(v, SFRotation):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 4:
            raise X3DValueException

    return False

def assertSFString(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if not isinstance(value, str):
        raise X3DTypeException

    return False

def assertMFString(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if not isinstance(v, str):
            raise X3DTypeException

    return False

def assertSFTime(value):
    if not isinstance(value, float) and not isinstance(value, SFTime):
        raise X3DTypeException

    if isinstance(value, SFTime):
        value = value.value

    if not isinstance(value, float):
        raise X3DTypeException

    return False

def assertMFTime(value):
    if not isinstance(value, list) and not isinstance(value, MFTime):
        raise X3DTypeException

    if isinstance(value, MFTime):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, float) and not isinstance(v, MFTime):
            raise X3DTypeException

        if isinstance(v, MFTime):
            v = v.value

        if not isinstance(v, float):
            raise X3DTypeException

    return False

def assertSFVec2d(value):
    if not isinstance(value, list) and not isinstance(value, SFVec2d):
        raise X3DTypeException

    if isinstance(value, SFVec2d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 2:
        raise X3DValueException

    return False

def assertMFVec2d(value):
    if not isinstance(value, list) and not isinstance(value, MFVec2d):
        raise X3DTypeException

    if isinstance(value, MFVec2d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFVec2d):
            raise X3DTypeException

        if isinstance(v, SFVec2d):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 2:
            raise X3DValueException

    return False

def assertSFVec2f(value):
    if not isinstance(value, list) and not isinstance(value, SFVec2f):
        raise X3DTypeException

    if isinstance(value, SFVec2f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 2:
        raise X3DValueException

    return False

def assertMFVec2f(value):
    if not isinstance(value, list) and not isinstance(value, MFVec2f):
        raise X3DTypeException

    if isinstance(value, MFVec2f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFVec2f):
            raise X3DTypeException

        if isinstance(v, SFVec2f):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 2:
            raise X3DValueException

    return False

def assertSFVec3d(value):
    if not isinstance(value, list) and not isinstance(value, SFVec3d):
        raise X3DTypeException

    if isinstance(value, SFVec3d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 3:
        raise X3DValueException

    return False

def assertMFVec3d(value):
    if not isinstance(value, list) and not isinstance(value, MFVec3d):
        raise X3DTypeException

    if isinstance(value, MFVec3d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFVec3d):
            raise X3DTypeException

        if isinstance(v, SFVec3d):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 3:
            raise X3DValueException

    return False

def assertSFVec3f(value):
    if not isinstance(value, list) and not isinstance(value, SFVec3f):
        raise X3DTypeException

    if isinstance(value, SFVec3f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 3:
        raise X3DValueException

    return False

def assertMFVec3f(value):
    if not isinstance(value, list) and not isinstance(value, MFVec3f):
        raise X3DTypeException

    if isinstance(value, MFVec3f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFVec3f):
            raise X3DTypeException

        if isinstance(v, SFVec3f):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 3:
            raise X3DValueException

    return False

def assertSFVec4d(value):
    if not isinstance(value, list) and not isinstance(value, SFVec4d):
        raise X3DTypeException

    if isinstance(value, SFVec4d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 4:
        raise X3DValueException

    return False

def assertMFVec4d(value):
    if not isinstance(value, list) and not isinstance(value, MFVec4d):
        raise X3DTypeException

    if isinstance(value, MFVec4d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFVec4d):
            raise X3DTypeException

        if isinstance(v, SFVec4d):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 4:
            raise X3DValueException

    return False

def assertSFVec4f(value):
    if not isinstance(value, list) and not isinstance(value, SFVec4f):
        raise X3DTypeException

    if isinstance(value, SFVec4f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 4:
        raise X3DValueException

    return False

def assertMFVec4f(value):
    if not isinstance(value, list) and not isinstance(value, MFVec4f):
        raise X3DTypeException

    if isinstance(value, MFVec4f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFVec4f):
            raise X3DTypeException

        if isinstance(v, SFVec4f):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 4:
            raise X3DValueException

    return False

def assertSFMatrix3d(value):
    if not isinstance(value, list) and not isinstance(value, SFMatrix3d):
        raise X3DTypeException

    if isinstance(value, SFMatrix3d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 9:
        raise X3DValueException

    return False

def assertMFMatrix3d(value):
    if not isinstance(value, list) and not isinstance(value, MFMatrix3d):
        raise X3DTypeException

    if isinstance(value, MFMatrix3d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFMatrix3d):
            raise X3DTypeException

        if isinstance(v, SFMatrix3d):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 9:
            raise X3DValueException

    return False

def assertSFMatrix3f(value):
    if not isinstance(value, list) and not isinstance(value, SFMatrix3f):
        raise X3DTypeException

    if isinstance(value, SFMatrix3f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 9:
        raise X3DValueException

    return False

def assertMFMatrix3f(value):
    if not isinstance(value, list) and not isinstance(value, MFMatrix3f):
        raise X3DTypeException

    if isinstance(value, MFMatrix3f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFMatrix3f):
            raise X3DTypeException

        if isinstance(v, SFMatrix3f):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 9:
            raise X3DValueException

    return False

def assertSFMatrix4d(value):
    if not isinstance(value, list) and not isinstance(value, SFMatrix4d):
        raise X3DTypeException

    if isinstance(value, SFMatrix4d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 16:
        raise X3DValueException

    return False

def assertMFMatrix4d(value):
    if not isinstance(value, list) and not isinstance(value, MFMatrix4d):
        raise X3DTypeException

    if isinstance(value, MFMatrix4d):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFMatrix4d):
            raise X3DTypeException

        if isinstance(v, SFMatrix4d):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 16:
            raise X3DValueException

    return False

def assertSFMatrix4f(value):
    if not isinstance(value, list) and not isinstance(value, SFMatrix4f):
        raise X3DTypeException

    if isinstance(value, SFMatrix4f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    count = 0
    for k, v in enumerate(value):
        count += 1
        if not isinstance(v, float) and not isinstance(v, int):
            raise X3DTypeException

    if count != 16:
        raise X3DValueException

    return False

def assertMFMatrix4f(value):
    if not isinstance(value, list) and not isinstance(value, MFMatrix4f):
        raise X3DTypeException

    if isinstance(value, MFMatrix4f):
        value = value.value

    if not isinstance(value, list):
        raise X3DTypeException

    for k, v in enumerate(value):
        if not isinstance(v, list) and not isinstance(v, SFMatrix4f):
            raise X3DTypeException

        if isinstance(v, SFMatrix4f):
            v = v.value

        if not isinstance(value, list):
            raise X3DTypeException

        count = 0
        for k2, v2 in enumerate(v):
            count += 1
            if not isinstance(v2, float) and not isinstance(v2, int):
                raise X3DTypeException

        if count != 16:
            raise X3DValueException

    return False

# ========================================================================
#
# Specification Common Field Validation Functions
#
# ========================================================================

def assertValidFogType(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
            raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in FOGTYPE:
        raise X3DValueException

    return False

def assertValidShaderLanguage(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
            raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in SHADERLANGUAGE:
        raise X3DValueException

    return False

def assertValidMatchCriterion(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
            raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in MATCHCRITERION:
        raise X3DValueException

    return False

def assertValidIntersectionType(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
            raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in INTERSECTIONTYPE:
        raise X3DValueException

    return False

def assertValidSortOrder(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
            raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in SORTORDER:
        raise X3DValueException

    return False

def assertValidObjectType(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in OBJECTTYPE:
            raise X3DValueException

    return False

def assertValidForceOutput(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in FORCEOUTPUT:
            raise X3DValueException

    return False

def assertValidFontJustify(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in FONTJUSTIFY:
            raise X3DValueException

    return False

def assertValidFontFamily(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in FONTFAMILY:
            raise X3DValueException

    return False

def assertValidFontStyle(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in FONTSTYLE:
        raise X3DValueException

    return False

def assertValidMultiTextureModes(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if v not in MULTITEXTUREMODES:
            raise X3DValueException

    return False

def assertValidMultiTextureSource(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in MULTITEXTURESOURCE:
            raise X3DValueException

    return False

def assertValidMultiTextureFunction(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in MULTITEXTUREFUNCTION:
            raise X3DValueException

    return False

def assertValidTextureCoordinateGenerationModes(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in TEXTURECOORDINATEGENRATIONMODES:
        raise X3DValueException

    return False

def assertValidTextureBoundaryModes(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in TEXTUREBOUNDARYMODES:
        raise X3DValueException

    return False

def assertValidTextureMagnificationModes(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in TEXTUREMAGNIFICATIONMODES:
        raise X3DValueException

    return False

def assertValidTextureMinificationModes(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in TEXTUREMINIFICATIONMODES:
        raise X3DValueException

    return False

def assertValidTextureCompressionModes(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in TEXTURECOMPRESSIONMODES:
        raise X3DValueException

    return False

def assertValidNavigationInfoTransitionType(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in NAVIGATIONINFOTRANSITIONTYPE:
            raise X3DValueException

    return False

def assertValidNavigationInfoType(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in NAVIGATIONINFOTYPE:
            raise X3DValueException

    return False

def assertValidGeoSystem(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in GEOSYSTEM:
            raise X3DValueException

    return False

def assertValidNetworkMode(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in NETWORKMODE:
        raise X3DValueException

    return False

def assertValidShaderType(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in SHADERTYPE:
        raise X3DValueException

    return False

def assertValidGenerateCubeMapTextureUpdate(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in GENERATECUBEMAPTEXTUREUPDATE:
        raise X3DValueException

    return False

def assertValidLayoutAlign(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in LAYOUTALIGN:
            raise X3DValueException

    return False

def assertValidLayoutOffsetUnits(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in LAYOUTOFFSETUNITS:
            raise X3DValueException

    return False
    
def assertValidLayoutScaleMode(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in LAYOUTSCALEMODE:
            raise X3DValueException

    return False

def assertValidLayoutSizeUnits(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in LAYOUTSIZEUNITS:
            raise X3DValueException

    return False

def assertValidCollisionAppliedParameters(value):
    if not isinstance(value, list) and not isinstance(value, MFString):
        raise X3DTypeException

    if isinstance(value, MFString):
        value = value.value

    for k, v in enumerate(value):
        if not isinstance(v, str) and not isinstance(v, SFString):
            raise X3DTypeException

        if isinstance(v, SFString):
            v = v.value

        if v not in COLLISIONAPPLIEDPARAMETERS:
            raise X3DValueException

    return False

def assertValidGeometryType(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in GEOMETRYTYPE:
        raise X3DValueException

    return False

def assertValidWeightFunctionType(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in WEIGHTFUNCTIONTYPE:
        raise X3DValueException

    return False

def assertValidProjectionVolumeStypeType(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in PROJECTIONVOLUMESTYLETYPE:
        raise X3DValueException

    return False

def assertValidPhaseFunction(value):
    if not isinstance(value, str) and not isinstance(value, SFString):
        raise X3DTypeException

    if isinstance(value, SFString):
        value = value.value

    if value not in PHASEFUNCTION:
        raise X3DValueException

    return False