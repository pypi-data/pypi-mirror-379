/*
 * This file is part of Xpra.
 * Copyright (C) 2013-2021 Antoine Martin <antoine@xpra.org>
 * Xpra is released under the terms of the GNU GPL v2, or, at your option, any
 * later version. See the file COPYING for details.
 */

#include <stdint.h>

extern "C" __global__ void XRGB_to_YUV444(uint8_t *srcImage, int src_w, int src_h, int srcPitch,
                             uint8_t *dstImage, int dst_w, int dst_h, int dstPitch,
                             int w, int h)
{
    const uint32_t gx = blockIdx.x * blockDim.x + threadIdx.x;
    const uint32_t gy = blockIdx.y * blockDim.y + threadIdx.y;
    const uint32_t src_y = gy * src_h / dst_h;
    const uint32_t src_x = gx * src_w / dst_w;

    if ((src_x < w) & (src_y < h)) {
        uint8_t R;
        uint8_t G;
        uint8_t B;
        //one 32-bit RGB pixel at a time:
        uint32_t si = (src_y * srcPitch) + src_x * 4;
        R = srcImage[si+1];
        G = srcImage[si+2];
        B = srcImage[si+3];

        uint32_t di;
        di = (gy * dstPitch) + gx;
        dstImage[di] = __float2int_rn(0.299 * R + 0.587 * G + 0.114 * B);
        di += dstPitch*dst_h;
        dstImage[di] = __float2int_rn(-0.169 * R - 0.331 * G + 0.500 * B + 128);
        di += dstPitch*dst_h;
        dstImage[di] = __float2int_rn(0.500 * R - 0.419 * G - 0.081 * B + 128);
    }
}
