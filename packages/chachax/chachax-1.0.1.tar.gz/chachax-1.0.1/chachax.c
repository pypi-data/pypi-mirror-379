/*
 * Copyright (c) 2014-2025, Wood
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright notice,
 *       this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright notice,
 *       this list of conditions and the following disclaimer in the documentation
 *       and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */
#include <Python.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef uint8_t  byte;
typedef uint32_t uint;
typedef uint64_t uint64;
#define BLOCKLEN 64

static void QuarterRound(uint *x, uint a, uint b, uint c, uint d) {
    x[a] += x[b];
    x[d] ^= x[a];
    x[d] = (x[d] << 16) | (x[d] >> 16);
    x[c] += x[d];
    x[b] ^= x[c];
    x[b] = (x[b] << 12) | (x[b] >> 20);
    x[a] += x[b];
    x[d] ^= x[a];
    x[d] = (x[d] << 8) | (x[d] >> 24);
    x[c] += x[d];
    x[b] ^= x[c];
    x[b] = (x[b] << 7) | (x[b] >> 25);
}

static void DoRound(byte *output, int rounds, uint *state) {
    uint x[16];
    int i;

    for (i = 0; i < 16; i++) {
        x[i] = state[i];
    }

    for (i = rounds; i > 0; i -= 2) {
        QuarterRound(x, 0, 4, 8, 12);
        QuarterRound(x, 1, 5, 9, 13);
        QuarterRound(x, 2, 6, 10, 14);
        QuarterRound(x, 3, 7, 11, 15);
        QuarterRound(x, 0, 5, 10, 15);
        QuarterRound(x, 1, 6, 11, 12);
        QuarterRound(x, 2, 7, 8, 13);
        QuarterRound(x, 3, 4, 9, 14);
    }

    for (i = 0; i < 16; i++) {
        uint sum = x[i] + state[i];
        output[i * 4] = (byte)sum;
        output[i * 4 + 1] = (byte)(sum >> 8);
        output[i * 4 + 2] = (byte)(sum >> 16);
        output[i * 4 + 3] = (byte)(sum >> 24);
    }

    state[12] += 1;
    if (state[12] == 0) {
        state[13] += 1;
    }
}

static void generate_key(byte *context, uint *key, uint *nonce, int counter, int round) {
    uint state[16];
    int i;

    state[0] = 1634760805;
    state[1] = 857760878;
    state[2] = 2036477234;
    state[3] = 1797285236;
    for (i = 0; i < 8; i++) {
        state[4 + i] = key[i];
    }
    state[12] = counter;
    for (i = 0; i < 3; i++) {
        state[13 + i] = nonce[i];
    }
    DoRound(context, round, state);
}

static void decrypt(byte *data, int dataLen, byte *keyBytes, byte *nonceBytes, int rounds, int counter) {
    int count, count2, dataIndex, i, j;
    uint key[8], nonce[3];
    byte array[BLOCKLEN];
    for(int i = 0;i < 8; i++){
        key[i] = ((uint)keyBytes[i*4]) | ((uint)keyBytes[i*4+1]<<8) | ((uint)keyBytes[i*4+2]<<16) | ((uint)keyBytes[i*4+3]<<24);
    }
    for(int i = 0;i < 3; i++){
        nonce[i] = ((uint)nonceBytes[i*4]) | ((uint)nonceBytes[i*4+1]<<8) | ((uint)nonceBytes[i*4+2]<<16) | ((uint)nonceBytes[i*4+3]<<24);
    }
    count = dataLen / BLOCKLEN;
    count2 = dataLen % BLOCKLEN;
    dataIndex = 0;

    if (count > 0) {
        for (i = 0; i < count; i++) {
            generate_key(array, key, nonce, counter++, rounds);
            for (j = 0; j < BLOCKLEN; j++) {
                data[dataIndex++] ^= array[j];
            }
        }
    }
    if (count2 > 0) {
        generate_key(array, key, nonce, counter++, rounds);
        for (i = 0; i < count2; i++) {
            data[dataIndex++] ^= array[i];
        }
    }
}

static PyObject* py_decrypt(PyObject* self, PyObject* args) {
    Py_buffer data;
    Py_buffer keyBytes;
    Py_buffer nonceBytes;
    PyObject *result;
    byte *buffer;
    int rounds = 8;
    int counter = 0;

    if (!PyArg_ParseTuple(args, "y*y*y*|ii", &data, &keyBytes, &nonceBytes, &rounds, &counter)) {
        return NULL;
    }

    buffer = (byte*)malloc(data.len);
    if (!buffer) {
        PyBuffer_Release(&data);
        PyBuffer_Release(&keyBytes);
        PyBuffer_Release(&nonceBytes);
        PyErr_SetString(PyExc_MemoryError, "Unable to allocate memory for decryption");
        return NULL;
    }

    memcpy(buffer, data.buf, data.len);
    decrypt(buffer, (int)data.len, (byte*)keyBytes.buf, (byte*)nonceBytes.buf, rounds, counter);
    result = PyBytes_FromStringAndSize((const char *)buffer, data.len);
    free(buffer);
    PyBuffer_Release(&data);
    PyBuffer_Release(&keyBytes);
    PyBuffer_Release(&nonceBytes);

    return result;
}

static PyMethodDef ChaChaXMethods[] = {
    {"decrypt", (PyCFunction)py_decrypt, METH_VARARGS, "Decrypt data"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef chachaxmodule = {
    PyModuleDef_HEAD_INIT,
    "chachax",
    NULL,
    -1,
    ChaChaXMethods
};

PyMODINIT_FUNC PyInit_chachax(void) {
    return PyModule_Create(&chachaxmodule);
}

