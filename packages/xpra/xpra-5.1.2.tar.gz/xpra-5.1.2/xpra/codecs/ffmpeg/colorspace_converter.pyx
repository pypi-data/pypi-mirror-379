# This file is part of Xpra.
# Copyright (C) 2013 Arthur Huillet
# Copyright (C) 2012-2023 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

from time import monotonic
from typing import Dict, Any

from xpra.log import Logger
log = Logger("csc", "swscale")

from xpra.util import typedict
from xpra.codecs.codec_constants import csc_spec
from xpra.codecs.image_wrapper import ImageWrapper
from xpra.codecs.ffmpeg.av_log cimport override_logger, restore_logger #@UnresolvedImport pylint: disable=syntax-error
from xpra.codecs.ffmpeg.av_log import SilenceAVWarningsContext
from xpra.buffers.membuf cimport padbuf, MemBuf

from libc.string cimport memset #pylint: disable=syntax-error
from libc.stdint cimport uintptr_t, uint8_t


cdef extern from "Python.h":
    int PyObject_GetBuffer(object obj, Py_buffer *view, int flags)
    void PyBuffer_Release(Py_buffer *view)
    int PyBUF_ANY_CONTIGUOUS

cdef extern from "libavcodec/version.h":
    int LIBSWSCALE_VERSION_MAJOR
    int LIBSWSCALE_VERSION_MINOR
    int LIBSWSCALE_VERSION_MICRO

ctypedef long AVPixelFormat
cdef extern from "libavutil/pixfmt.h":
    AVPixelFormat AV_PIX_FMT_YUV420P
    AVPixelFormat AV_PIX_FMT_YUV422P
    AVPixelFormat AV_PIX_FMT_YUV444P
    AVPixelFormat AV_PIX_FMT_RGB24
    AVPixelFormat AV_PIX_FMT_0RGB
    AVPixelFormat AV_PIX_FMT_BGR0
    AVPixelFormat AV_PIX_FMT_ARGB
    AVPixelFormat AV_PIX_FMT_BGRA
    AVPixelFormat AV_PIX_FMT_ABGR
    AVPixelFormat AV_PIX_FMT_RGBA
    AVPixelFormat AV_PIX_FMT_GBRP
    AVPixelFormat AV_PIX_FMT_BGR24
    AVPixelFormat AV_PIX_FMT_NV12
    AVPixelFormat AV_PIX_FMT_NONE
    AVPixelFormat AV_PIX_FMT_GBRP9LE

    ctypedef enum AVColorRange:
        AVCOL_RANGE_UNSPECIFIED
        AVCOL_RANGE_MPEG
        AVCOL_RANGE_JPEG

    ctypedef enum AVColorPrimaries:
        AVCOL_PRI_RESERVED0
        AVCOL_PRI_BT709
        AVCOL_PRI_UNSPECIFIED
        AVCOL_PRI_RESERVED
        AVCOL_PRI_BT470M
        AVCOL_PRI_BT470BG
        AVCOL_PRI_SMPTE170M
        AVCOL_PRI_SMPTE240M
        AVCOL_PRI_FILM
        AVCOL_PRI_BT2020
        AVCOL_PRI_SMPTE428
        AVCOL_PRI_SMPTEST428_1
        AVCOL_PRI_SMPTE431
        AVCOL_PRI_SMPTE432
        AVCOL_PRI_EBU3213
        AVCOL_PRI_JEDEC_P22
        AVCOL_PRI_NB

    ctypedef enum AVColorTransferCharacteristic:
        AVCOL_TRC_RESERVED0
        AVCOL_TRC_BT709
        AVCOL_TRC_UNSPECIFIED
        AVCOL_TRC_RESERVED
        AVCOL_TRC_GAMMA22
        AVCOL_TRC_GAMMA28
        AVCOL_TRC_SMPTE170M
        AVCOL_TRC_SMPTE240M
        AVCOL_TRC_LINEAR
        AVCOL_TRC_LOG
        AVCOL_TRC_LOG_SQRT
        AVCOL_TRC_IEC61966_2_4
        AVCOL_TRC_BT1361_ECG
        AVCOL_TRC_IEC61966_2_1
        AVCOL_TRC_BT2020_10
        AVCOL_TRC_BT2020_12
        AVCOL_TRC_SMPTE2084
        AVCOL_TRC_SMPTEST2084
        AVCOL_TRC_SMPTE428
        AVCOL_TRC_SMPTEST428_1
        AVCOL_TRC_ARIB_STD_B67
        AVCOL_TRC_NB

    ctypedef enum AVColorSpace:
        AVCOL_SPC_RGB
        AVCOL_SPC_BT709
        AVCOL_SPC_UNSPECIFIED
        AVCOL_SPC_RESERVED
        AVCOL_SPC_FCC
        AVCOL_SPC_BT470BG
        AVCOL_SPC_SMPTE170M
        AVCOL_SPC_SMPTE240M
        AVCOL_SPC_YCGCO
        AVCOL_SPC_YCOCG
        AVCOL_SPC_BT2020_NCL
        AVCOL_SPC_BT2020_CL
        AVCOL_SPC_SMPTE2085
        AVCOL_SPC_CHROMA_DERIVED_NCL
        AVCOL_SPC_CHROMA_DERIVED_CL
        AVCOL_SPC_ICTCP
        AVCOL_SPC_NB


ctypedef void SwsContext
cdef extern from "libswscale/swscale.h":
    ctypedef struct SwsFilter:
        pass
    unsigned int SWS_ACCURATE_RND
    unsigned int SWS_BICUBIC
    unsigned int SWS_BICUBLIN
    unsigned int SWS_BILINEAR
    unsigned int SWS_FAST_BILINEAR
    unsigned int SWS_FULL_CHR_H_INT

    SwsContext *sws_getContext(int srcW, int srcH, AVPixelFormat srcFormat,
                                int dstW, int dstH, AVPixelFormat dstFormat,
                                int flags, SwsFilter *srcFilter,
                                SwsFilter *dstFilter, const double *param)
    void sws_freeContext(SwsContext *context)

    int sws_scale(SwsContext *c, const uint8_t *const srcSlice[],
                  const int srcStride[], int srcSliceY, int srcSliceH,
                  uint8_t *const dst[], const int dstStride[]) nogil

    int sws_setColorspaceDetails(SwsContext *c, const int inv_table[4],
                             int srcRange, const int table[4], int dstRange,
                             int brightness, int contrast, int saturation);
    int sws_getColorspaceDetails(SwsContext *c, int **inv_table,
                             int *srcRange, int **table, int *dstRange,
                             int *brightness, int *contrast, int *saturation)


cdef class CSCPixelFormat:
    cdef AVPixelFormat av_enum
    cdef object av_enum_name
    cdef float width_mult[4]
    cdef float height_mult[4]
    cdef object pix_fmt
    def __init__(self, AVPixelFormat av_enum, av_enum_name, width_mult, height_mult, pix_fmt):
        self.av_enum = av_enum
        self.av_enum_name = av_enum_name
        for i in range(4):
            self.width_mult[i] = 0.0
            self.height_mult[i] = 0.0
        for i in range(4):
            self.width_mult[i] = width_mult[i]
            self.height_mult[i] = height_mult[i]
        self.pix_fmt = pix_fmt

    def __repr__(self):
        return "CSCPixelFormat(%s)" % self.av_enum_name

#we could use a class to represent these options:
COLORSPACES = []
#keeping this array in scope ensures the strings don't go away!
FORMAT_OPTIONS = [
    ("RGB24",   AV_PIX_FMT_RGB24,      (3, 0, 0, 0),       (1, 0, 0, 0),       "RGB"  ),
    ("BGR24",   AV_PIX_FMT_BGR24,      (3, 0, 0, 0),       (1, 0, 0, 0),       "BGR"  ),
    ("0RGB",    AV_PIX_FMT_0RGB,       (4, 0, 0, 0),       (1, 0, 0, 0),       "XRGB"  ),
    ("BGR0",    AV_PIX_FMT_BGR0,       (4, 0, 0, 0),       (1, 0, 0, 0),       "BGRX"  ),
    ("ARGB",    AV_PIX_FMT_ARGB,       (4, 0, 0, 0),       (1, 0, 0, 0),       "XRGB"  ),
    ("RGBA",    AV_PIX_FMT_RGBA,       (4, 0, 0, 0),       (1, 0, 0, 0),       "RGBX"  ),
    ("BGRA",    AV_PIX_FMT_BGRA,       (4, 0, 0, 0),       (1, 0, 0, 0),       "BGRX"  ),
    ("ABGR",    AV_PIX_FMT_ABGR,       (4, 0, 0, 0),       (1, 0, 0, 0),       "XBGR"  ),
    ("YUV420P", AV_PIX_FMT_YUV420P,    (1, 0.5, 0.5, 0),   (1, 0.5, 0.5, 0),   "YUV420P"),
    ("YUV422P", AV_PIX_FMT_YUV422P,    (1, 0.5, 0.5, 0),   (1, 1, 1, 0),       "YUV422P"),
    ("YUV444P", AV_PIX_FMT_YUV444P,    (1, 1, 1, 0),       (1, 1, 1, 0),       "YUV444P"),
    ("GBRP",    AV_PIX_FMT_GBRP,       (1, 1, 1, 0),       (1, 1, 1, 0),       "GBRP"   ),
    ("GBRP9LE", AV_PIX_FMT_GBRP9LE,    (1, 1, 1, 0),       (1, 1, 1, 0),       "GBRP9LE"),
    ("NV12",    AV_PIX_FMT_NV12,       (1, 1, 0, 0),       (1, 0.5, 0, 0),     "NV12"   ),
     ]
FORMATS = {}
for av_enum_name, av_enum, width_mult, height_mult, pix_fmt in FORMAT_OPTIONS:
    FORMATS[pix_fmt] = CSCPixelFormat(av_enum, av_enum_name, width_mult, height_mult, pix_fmt)
    if pix_fmt not in COLORSPACES:
        COLORSPACES.append(pix_fmt)
log("swscale pixel formats: %s", FORMATS)
COLORSPACES = tuple(COLORSPACES)
log("colorspaces: %s", COLORSPACES)

#(per plane)
BYTES_PER_PIXEL = {
    AV_PIX_FMT_NV12     : 1,
    AV_PIX_FMT_YUV420P  : 1,
    AV_PIX_FMT_YUV422P  : 1,
    AV_PIX_FMT_YUV444P  : 1,
    AV_PIX_FMT_RGB24    : 3,
    AV_PIX_FMT_0RGB     : 4,
    AV_PIX_FMT_BGR0     : 4,
    AV_PIX_FMT_ARGB     : 4,
    AV_PIX_FMT_BGRA     : 4,
    AV_PIX_FMT_GBRP     : 1,
    AV_PIX_FMT_GBRP9LE  : 2,
    }


cdef inline int roundup(int n, int m):
    return (n + m - 1) & ~(m - 1)


cdef class SWSFlags:
    cdef int flags
    cdef object flags_strs
    def __init__(self, int flags, flags_strs):
        self.flags = flags
        self.flags_strs = flags_strs

    def get_flags(self):
        return self.flags

    def __repr__(self):
        try:
            return "|".join(self.flags_strs)
        except:
            return str(self.flags_strs)


FLAG_NAMES = {
    SWS_BICUBIC         : "BICUBIC",
    SWS_BICUBLIN        : "BICUBLIN",
    SWS_FAST_BILINEAR   : "FAST_BILINEAR",
    SWS_ACCURATE_RND    : "ACCURATE_RND",
    }

#keeping this array in scope ensures the strings don't go away!
FLAGS_OPTIONS = (
            (30, (SWS_BICUBIC, ),       ("BICUBIC", )),
            (40, (SWS_BICUBLIN, ),      ("BICUBLIN", )),
            (60, (SWS_BILINEAR, ),      ("BILINEAR", )),
            (80, (SWS_FAST_BILINEAR, ), ("FAST_BILINEAR", )),
        )
FLAGS = []
for speed, flags, flag_strs in FLAGS_OPTIONS:
    flag_value = 0
    for flag in flags:
        flag_value |= flag
    swsf = SWSFlags(flag_value, flag_strs)
    FLAGS.append((speed, swsf))
    log("speed=%s %s=%s", speed, swsf, flag_value)
log("swscale flags: %s", FLAGS)


cdef int get_swscale_flags(int speed, int scaling, int subsampling, dst_format):
    if not scaling and not subsampling:
        speed = 100
    cdef int flags = 0
    for s, swsflags in FLAGS:
        if s>=speed:
            flags = swsflags.get_flags()
            break
    #not found? use the highest one:
    if flags==0:
        _, swsflags = FLAGS[-1]
        flags = swsflags.get_flags()
    #look away now: we get an acceleration warning with XRGB
    #when we don't add SWS_ACCURATE_RND...
    #but we don't want the flag otherwise, unless we are scaling or downsampling:
    if ((scaling or subsampling) and speed<100) or dst_format=="XRGB":
        flags |= SWS_ACCURATE_RND
    if dst_format=="GBRP":
        flags |= SWS_FULL_CHR_H_INT
    return flags


def get_swscale_flags_strs(int flags):
    return [flag_name for flag_value, flag_name in FLAG_NAMES.items()
            if (flag_value & flags)>0]


def init_module():
    #nothing to do!
    log("csc_swscale.init_module()")
    override_logger()

def cleanup_module():
    log("csc_swscale.cleanup_module()")
    restore_logger()

def get_type():
    return "swscale"

def get_version():
    return (LIBSWSCALE_VERSION_MAJOR, LIBSWSCALE_VERSION_MINOR, LIBSWSCALE_VERSION_MICRO)

def get_info():
    global COLORSPACES, MAX_WIDTH, MAX_HEIGHT
    return {
            "version"   : get_version(),
            "formats"   : COLORSPACES,
            "max-size"  : (MAX_WIDTH, MAX_HEIGHT),
            }

def get_input_colorspaces():
    return COLORSPACES

def get_output_colorspaces(input_colorspace):
    #exclude input colorspace:
    exclude = [input_colorspace]
    if input_colorspace in ("YUV420P", "YUV422P"):
        #these would cause a warning:
        #"No accelerated colorspace conversion found from yuv420p to gbrp."
        exclude.append("GBRP")
    return [x for x in COLORSPACES if x not in exclude]


#a safe guess, which we probe later on:
MAX_WIDTH = 16384
MAX_HEIGHT = 16384
def get_spec(in_colorspace, out_colorspace):
    assert in_colorspace in COLORSPACES, "invalid input colorspace: %s (must be one of %s)" % (in_colorspace, COLORSPACES)
    assert out_colorspace in COLORSPACES, "invalid output colorspace: %s (must be one of %s)" % (out_colorspace, COLORSPACES)
    #setup cost is very low (usually less than 1ms!)
    #there are restrictions on dimensions (8x2 minimum!)
    #swscale can be used to scale (obviously)
    return csc_spec(in_colorspace, out_colorspace,
                    ColorspaceConverter, codec_type=get_type(),
                    quality=100, speed=60,
                    setup_cost=20, min_w=8, min_h=2, can_scale=True,
                    max_w=MAX_WIDTH, max_h=MAX_HEIGHT)

assert (LIBSWSCALE_VERSION_MAJOR, LIBSWSCALE_VERSION_MINOR, LIBSWSCALE_VERSION_MICRO)>(2, 1, 1)


cdef class ColorspaceConverter:
    cdef int src_width
    cdef int src_height
    cdef AVPixelFormat src_format_enum
    cdef object src_format
    cdef int dst_width
    cdef int dst_height
    cdef unsigned char dst_bytes_per_pixel
    cdef AVPixelFormat dst_format_enum
    cdef object dst_format

    cdef unsigned long frames
    cdef double time
    cdef SwsContext *context
    cdef int flags

    cdef int out_height[4]
    cdef int out_stride[4]
    cdef unsigned long out_size[4]

    cdef object __weakref__

    def init_context(self, int src_width, int src_height, src_format,
                           int dst_width, int dst_height, dst_format, options:typedict=None):
        log("swscale.ColorspaceConverter.init_context%s", (
            src_width, src_height, src_format, dst_width, dst_height, dst_format, options))
        #src:
        cdef CSCPixelFormat src = FORMATS.get(src_format)
        log("source format=%s", src)
        assert src, "invalid source format: %s" % src_format
        self.src_format = src_format
        self.src_format_enum = src.av_enum
        #dst:
        cdef CSCPixelFormat dst = FORMATS.get(dst_format)
        log("destination format=%s", dst)
        assert dst, "invalid destination format: %s" % dst_format
        self.dst_format = dst_format
        self.dst_format_enum = dst.av_enum
        self.dst_bytes_per_pixel = BYTES_PER_PIXEL.get(dst.av_enum, 1)
        #pre-calculate plane heights:
        cdef int subsampling = False
        for i in range(4):
            self.out_height[i] = (int) (dst_height * dst.height_mult[i])
            self.out_stride[i] = roundup((int) (dst_width * dst.width_mult[i]), 16)
            if i!=3 and (dst.height_mult[i]!=1.0 or dst.width_mult[i]!=1.0):
                subsampling = True
            self.out_size[i] = self.out_stride[i] * self.out_height[i]

        self.src_width = src_width
        self.src_height = src_height
        self.dst_width = dst_width
        self.dst_height = dst_height

        cdef int scaling = (src_width!=dst_width) or (src_height!=dst_height)
        cdef int speed = typedict(options or {}).intget("speed", 100)
        self.flags = get_swscale_flags(speed, scaling, subsampling, dst_format)
        #log("sws get_swscale_flags(%s, %s, %s)=%s", speed, scaling, subsampling, get_swscale_flags_strs(self.flags))
        self.time = 0
        self.frames = 0

        self.context = sws_getContext(self.src_width, self.src_height, self.src_format_enum,
                                      self.dst_width, self.dst_height, self.dst_format_enum,
                                      self.flags, NULL, NULL, NULL)
        log("sws context=%#x", <uintptr_t> self.context)
        self.enable_fullrange()
        assert self.context!=NULL, "sws_getContext returned NULL"

    def enable_fullrange(self):
        cdef int* inv_table
        cdef int srcRange
        cdef int* table
        cdef int dstRange
        cdef int brightness
        cdef int contrast
        cdef int saturation
        if sws_getColorspaceDetails(self.context, &inv_table,
                                 &srcRange, &table, &dstRange,
                                 &brightness, &contrast, &saturation)==-1:
            log.warn("Warning: cannot enable fullrange")
            return
        log("brightness=%#x, contrast=%#x, saturation=%#x",
                 brightness, contrast, saturation)
        srcRange = 1
        dstRange = 1
        if sws_setColorspaceDetails(self.context, inv_table,
                             srcRange, table, dstRange,
                             brightness, contrast, saturation)==-1:
            log.warn("Warning: cannot enable fullrange")

    def get_info(self) -> Dict[str,Any]:
        info = get_info()
        info.update({
                "flags"     : get_swscale_flags_strs(self.flags),
                "frames"    : int(self.frames),
                "src_width" : self.src_width,
                "src_height": self.src_height,
                "dst_width" : self.dst_width,
                "dst_height": self.dst_height,
                "dst_bytes_per_pixel"   : self.dst_bytes_per_pixel,
                })
        if self.src_format:
            info["src_format"] = self.src_format
        if self.dst_format:
            info["dst_format"] = self.dst_format
        if self.frames>0 and self.time>0:
            pps = self.src_width * self.src_height * self.frames / self.time
            info["total_time_ms"] = int(self.time*1000.0)
            info["pixels_per_second"] = int(pps)
        return info

    def __repr__(self):
        if not self.src_format or not self.dst_format:
            return "swscale(uninitialized)"
        return "swscale(%s %sx%s - %s %sx%s)" % (self.src_format, self.src_width, self.src_height,
                                                 self.dst_format, self.dst_width, self.dst_height)

    def __dealloc__(self):
        self.clean()

    def get_src_width(self) -> int:
        return self.src_width

    def get_src_height(self) -> int:
        return self.src_height

    def get_src_format(self):
        return self.src_format

    def get_dst_width(self) -> int:
        return self.dst_width

    def get_dst_height(self) -> int:
        return self.dst_height

    def get_dst_format(self):
        return self.dst_format

    def get_type(self) -> str:
        return "swscale"


    def clean(self):
        #overzealous clean is cheap!
        cdef int i
        if self.context!=NULL:
            log("swscale.ColorspaceConverter.clean() sws context=%#x", <uintptr_t> self.context)
            sws_freeContext(self.context)
            self.context = NULL
        self.src_width = 0
        self.src_height = 0
        self.src_format_enum = AV_PIX_FMT_NONE
        self.src_format = ""
        self.dst_width = 0
        self.dst_height = 0
        self.dst_format_enum = AV_PIX_FMT_NONE
        self.dst_format = ""
        self.frames = 0
        self.time = 0
        self.flags = 0
        for i in range(4):
            self.out_height[i] = 0
            self.out_stride[i] = 0
            self.out_size[i] = 0

    def is_closed(self) -> bool:
        return self.context==NULL


    def convert_image(self, image):
        assert self.context!=NULL, "no context"
        cdef const uint8_t *input_image[4]
        cdef uint8_t *output_image[4]
        cdef int input_stride[4]
        cdef int i
        cdef size_t pad
        cdef double start = monotonic()
        cdef int iplanes = image.get_planes()
        pixels = image.get_pixels()
        strides = image.get_rowstride()
        assert iplanes in ImageWrapper.PLANE_OPTIONS, "invalid number of planes: %s" % iplanes
        if iplanes==ImageWrapper.PACKED:
            #magic: repack raw pixels/rowstride:
            planes = [pixels]
            strides = [strides]
            iplanes = 1
        else:
            planes = pixels
        if self.dst_format.endswith("P") or self.dst_format=="NV12":
            pad = self.dst_width
        else:
            pad = self.dst_width * 4
        #print("convert_image(%s) input=%s, strides=%s" % (image, len(input), strides))
        assert pixels, "failed to get pixels from %s" % image
        assert image.get_width()>=(self.src_width & 0xFFFE), "invalid image width: %s (minimum is %s)" % (image.get_width(), self.src_width)
        assert image.get_height()>=(self.src_height & 0xFFFE), "invalid image height: %s (minimum is %s)" % (image.get_height(), self.src_height)
        assert len(planes)==iplanes, "expected %s planes but found %s" % (iplanes, len(pixels))
        assert len(strides)==iplanes, "expected %s rowstrides but found %s" % (iplanes, len(strides))

        #allocate the output buffer(s):
        output_buf = []
        cdef MemBuf mb
        for i in range(4):
            if self.out_size[i]>0:
                mb = padbuf(self.out_size[i], pad)
                output_buf.append(mb)
                output_image[i] = <uint8_t *> mb.get_mem()
            else:
                #the buffer may not be used, but is not allowed to be NULL:
                output_image[i] = output_image[0]

        cdef Py_buffer py_buf[4]
        for i in range(4):
            memset(&py_buf[i], 0, sizeof(Py_buffer))
        cdef int result
        try:
            for i in range(4):
                #set input pointers
                if i<iplanes:
                    input_stride[i] = strides[i]
                    if PyObject_GetBuffer(planes[i], &py_buf[i], PyBUF_ANY_CONTIGUOUS):
                        raise ValueError("failed to read pixel data from %s" % type(pixels[i]))
                    input_image[i] = <const uint8_t*> py_buf[i].buf
                else:
                    #some versions of swscale check all 4 planes
                    #even when we only pass 1! see "check_image_pointers"
                    #(so we just copy the last valid plane in the remaining slots - ugly!)
                    input_stride[i] = input_stride[iplanes-1]
                    input_image[i] = input_image[iplanes-1]
            with nogil:
                result = sws_scale(self.context, input_image, input_stride, 0, self.src_height, output_image, self.out_stride)
            assert result!=0, "sws_scale failed!"
            assert result==self.dst_height, "invalid output height: %s, expected %s" % (result, self.dst_height)
        finally:
            for i in range(4):
                if py_buf[i].buf:
                    PyBuffer_Release(&py_buf[i])
        #now parse the output:
        cdef int oplanes
        if self.dst_format.endswith("P"):
            #planar mode, assume 3 planes:
            oplanes = ImageWrapper.PLANAR_3
            out = [memoryview(output_buf[i]) for i in range(3)]
            strides = [self.out_stride[i] for i in range(3)]
        elif self.dst_format=="NV12":
            oplanes = ImageWrapper.PLANAR_2
            out = [memoryview(output_buf[i]) for i in range(2)]
            strides = [self.out_stride[i] for i in range(2)]
        else:
            #assume no planes, plain RGB packed pixels:
            oplanes = ImageWrapper.PACKED
            strides = self.out_stride[0]
            out = memoryview(output_buf[0])
        cdef double elapsed = monotonic()-start
        log("%s took %.1fms", self, 1000.0*elapsed)
        self.time += elapsed
        self.frames += 1
        return ImageWrapper(0, 0, self.dst_width, self.dst_height, out, self.dst_format, 24, strides, self.dst_bytes_per_pixel, oplanes)


def selftest(full=False):
    global MAX_WIDTH, MAX_HEIGHT
    from xpra.codecs.codec_checks import testcsc, get_csc_max_size
    from xpra.codecs.ffmpeg import colorspace_converter
    override_logger()
    with SilenceAVWarningsContext():
        #test a limited set, not all combinations:
        if full:
            planar_tests = [x for x in get_input_colorspaces() if x.endswith("P")]
            packed_tests = [x for x in get_input_colorspaces() if ((x.find("BGR")>=0 or x.find("RGB")>=0) and not x not in planar_tests)]
        else:
            planar_tests = [x for x in ("YUV420P", "YUV422P", "YUV444P", "GBRP", "NV12") if x in get_input_colorspaces()]
            packed_tests = ["BGRX"]   #only test BGRX
        maxw, maxh = 2**24, 2**24
        for planar in planar_tests:
            for packed in packed_tests:
                #test planar to packed:
                if packed not in get_output_colorspaces(planar):
                    continue
                testcsc(colorspace_converter, full, [planar], [packed])
                if full:
                    mw, mh = get_csc_max_size(colorspace_converter, [planar], [packed])
                    maxw = min(maxw, mw)
                    maxh = min(maxh, mh)
                #test BGRX to planar:
                if packed not in get_input_colorspaces():
                    continue
                if planar not in get_output_colorspaces(packed):
                    continue
                testcsc(colorspace_converter, full, [packed], [planar])
                if full:
                    mw, mh = get_csc_max_size(colorspace_converter, [packed], [planar])
                    maxw = min(maxw, mw)
                    maxh = min(maxh, mh)
        if full and maxw<65536 and maxh<65536:
            MAX_WIDTH = maxw
            MAX_HEIGHT = maxh
            log("%s max dimensions: %ix%i", colorspace_converter, MAX_WIDTH, MAX_HEIGHT)
