/*
 * Python-based AES-GCM testbench for testing OpenSSL's AES-GCM
 * implementation (and serve as a reference implementation to test
 * your own AES-GCM implementation)
 *
 * Copyright (C) 2018 Rajesh Vaidheeswarrana
 * 
 * This program is free software: you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see
 * <https://www.gnu.org/licenses/>.
 */

#include <Python.h>
#include <stdio.h>
#include <openssl/bio.h>
#include <openssl/evp.h>
#include <string.h>

// Compatibility with 1.0.x
#ifndef EVP_CTRL_AEAD_SET_IVLEN
#define EVP_CTRL_AEAD_SET_IVLEN EVP_CTRL_GCM_SET_IVLEN
#endif

#ifndef EVP_CTRL_AEAD_SET_TAG
#define EVP_CTRL_AEAD_SET_TAG EVP_CTRL_GCM_SET_TAG
#endif

#ifndef EVP_CTRL_AEAD_GET_TAG
#define EVP_CTRL_AEAD_GET_TAG EVP_CTRL_GCM_GET_TAG
#endif

static PyObject *AesgcmpyError;
static int Debug = 0;

static PyObject *
aes_debug(PyObject *self, PyObject *args)
{
    Debug++;
    return Py_BuildValue("i", Debug);
}

static PyObject *
aes_gcm_encrypt(PyObject *self, PyObject *args)
{
    EVP_CIPHER_CTX *ctx;
    int outlen, rv, olen;
    unsigned char tag[16];
    const unsigned char *key, *pt, *aad, *iv;
    const int keylen, ptlen, aadlen, ivlen;
    if (Debug) printf("AES GCM Encrypt:\n");
    if (!PyArg_ParseTuple(args,
#if PY_MAJOR_VERSION < 3
			  "s#s#s#s#:encrypt",
#else
			  "y#y#y#y#:encrypt",
#endif
			  &key, &keylen, &pt, &ptlen,
			  &iv, &ivlen, &aad, &aadlen)) {
	PyErr_SetString(AesgcmpyError, "Usage: encrypt <key> <data> <iv> <aad>");
	return NULL;
    }
    if (Debug > 1) {
	printf("KEY:\n");
	BIO_dump_fp(stdout, (const char *)key, keylen);
	printf("IV:\n");
	BIO_dump_fp(stdout, (const char *)iv, ivlen);
	printf("AAD:\n");
	BIO_dump_fp(stdout, (const char *)aad, aadlen);
	printf("Plaintext:\n");
	BIO_dump_fp(stdout, (const char *)pt, ptlen);
    }
    unsigned char *outbuf = (unsigned char *)PyMem_Malloc(ptlen+16);
    if(!outbuf) {
      return PyErr_NoMemory();
    }
    ctx = EVP_CIPHER_CTX_new();
    /* Set cipher type and mode */
    switch (keylen) {
    case 16:
	EVP_EncryptInit_ex(ctx, EVP_aes_128_gcm(), NULL, NULL, NULL);
	break;
    case 24:
	EVP_EncryptInit_ex(ctx, EVP_aes_192_gcm(), NULL, NULL, NULL);
	break;
    case 32:
	EVP_EncryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, NULL, NULL);
	break;
    }
    /* Set IV length if default 96 bits is not appropriate */
    EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_SET_IVLEN, ivlen, NULL);
    /* Initialise key and IV */
    EVP_EncryptInit_ex(ctx, NULL, NULL, key, iv);
    /* Zero or more calls to specify any AAD */
    if (aadlen) EVP_EncryptUpdate(ctx, NULL, &outlen, aad, aadlen);
    /* Encrypt plaintext */
    EVP_EncryptUpdate(ctx, outbuf, &outlen, pt, ptlen);
    if (Debug > 1) {
	printf("Ciphertext (%d):\n", outlen);
	BIO_dump_fp(stdout, (const char *)outbuf, outlen);
    }
    /* Finalise: note get no output for GCM */
    EVP_EncryptFinal_ex(ctx, outbuf, &olen);

    /* Get tag */
    rv = EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_GET_TAG, 16, tag);
    if (Debug > 1) {
	printf("Tag (%d):\n", 16);
	BIO_dump_fp(stdout, (const char *)tag, 16);
    }
    EVP_CIPHER_CTX_free(ctx);
    PyObject *ret = Py_BuildValue(
#if PY_MAJOR_VERSION < 3
				  "{s:s#,s:s#, s:i}",
#else
				  "{s:y#,s:y#, s:i}",
#endif
				  "ciphertext", outbuf, outlen, "tag", tag, 16, "status", rv);
    PyMem_Free(outbuf);
    return ret;
}

static PyObject *
aes_gcm_decrypt(PyObject *self, PyObject *args)
{
    EVP_CIPHER_CTX *ctx;
    int outlen, rv, olen;
    unsigned char *key, *ct, *aad, *iv, *tag;
    int keylen, ctlen, aadlen, ivlen, taglen;
    if (!PyArg_ParseTuple(args,
#if PY_MAJOR_VERSION < 3
			  "s#s#s#s#s#:decrypt",
#else
			  "y#y#y#y#y#:decrypt",
#endif
			  &key, &keylen, &ct, &ctlen,
			  &iv, &ivlen, &aad, &aadlen, &tag, &taglen)) {
	PyErr_SetString(AesgcmpyError, "Usage: decrypt <key> <data> <iv> <aad> <tag>");
	return NULL;
    }

    if (Debug) printf("AES GCM Decrypt:\n");
    if (Debug > 1) {
	printf("Ciphertext:\n");
	BIO_dump_fp(stdout, (const char *)ct, ctlen);
    }
    unsigned char *outbuf = (unsigned char *)PyMem_Malloc(ctlen);
    if(!outbuf) {
      return PyErr_NoMemory();
    }
    ctx = EVP_CIPHER_CTX_new();
    /* Select cipher */
    switch (keylen) {
    case 16:
	EVP_DecryptInit_ex(ctx, EVP_aes_128_gcm(), NULL, NULL, NULL);
	break;
    case 24:
	EVP_DecryptInit_ex(ctx, EVP_aes_192_gcm(), NULL, NULL, NULL);
	break;
    case 32:
	EVP_DecryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, NULL, NULL);
	break;
    }
    /* Set IV length, omit for 96 bits */
    EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_SET_IVLEN, ivlen, NULL);
    /* Specify key and IV */
    EVP_DecryptInit_ex(ctx, NULL, NULL, key, iv);
    /* Zero or more calls to specify any AAD */
    if (aadlen) EVP_DecryptUpdate(ctx, NULL, &outlen, aad, aadlen);
    /* Decrypt plaintext */
    EVP_DecryptUpdate(ctx, outbuf, &outlen, ct, ctlen);
    /* Set expected tag value. */
    EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_SET_TAG, taglen, (void *)tag);
    /* Finalise: note get no output for GCM */
    rv = EVP_DecryptFinal_ex(ctx, outbuf, &olen);
    /*
     * Print out return value. If this is not successful authentication
     * failed and plaintext is not trustworthy.
     */
    if (Debug > 1) printf("Tag Verify %s\n", rv > 0 ? "Successful!" : "Failed!");
    PyObject *ret =  Py_BuildValue(
#if PY_MAJOR_VERSION < 3
				   "{s:s#, s:i}",
#else
				   "{s:y#, s:i}",
#endif
				   "plaintext", outbuf, outlen, "status", rv);
    PyMem_Free(outbuf);
    EVP_CIPHER_CTX_free(ctx);
    return ret;
}

int
set_buf_to_testcase(PyObject *testcase, const char *key, const unsigned char *buffer, const int len)
{
    char error[256];
    if (PyObject_SetAttrString(testcase, key, Py_BuildValue(
#if PY_MAJOR_VERSION < 3
							    "s#",
#else
							    "y#",
#endif
							    buffer, len)) == -1) {
	sprintf(error, "cannot set %s in testcase", key);
	PyErr_SetString(AesgcmpyError, error);
	return -1;
    }
    return 1;
}

int
set_int_to_testcase(PyObject *testcase, const char *key, const int val)
{
    char error[256];
    if (PyObject_SetAttrString(testcase, key, PyLong_FromLong(val)) == -1) {
	sprintf(error, "cannot set %s in testcase", key);
	PyErr_SetString(AesgcmpyError, error);
	return -1;
    }
    return 1;
}

int
get_from_testcase(PyObject *testcase, const char *key, Py_buffer *buf, int *len)
{
    char error[256];
    PyObject *obj = PyObject_GetAttrString(testcase, key);
    if (obj == NULL) {
	sprintf(error, "testcase does not have member '%s'", key);
	PyErr_SetString(AesgcmpyError, error);
	return 0;
    }
    if (!PyObject_CheckBuffer(obj)) {
	sprintf(error, "%s does not have a buffer interface", key);
	PyErr_SetString(AesgcmpyError, error);
	return 0;
    }
    if (PyObject_GetBuffer(obj, buf, PyBUF_SIMPLE) == 0) {
	*len  = buf->len;
	return 1;
    }
    //sprintf(error, "unable to get buffer for member %s ", key);
    //PyErr_SetString(AesgcmpyError, error);
    return 0;
}

static PyObject *
aes_gcm_testcase_encrypt(PyObject *self, PyObject *args)
{
    EVP_CIPHER_CTX *ctx;
    int outlen, rv, olen;
    unsigned char tag[16];
    PyObject *testcase;
    Py_buffer key, pt, aad, iv;
    int keylen, ptlen, aadlen, ivlen;
    if (!PyArg_ParseTuple(args, "O:tc_encrypt", &testcase)) {
	PyErr_SetString(AesgcmpyError, "Usage: tc_encrypt <testcase>");
	return NULL;
    }
    if (! (
	   get_from_testcase(testcase, "plaintext", &pt, &ptlen) &&
	   get_from_testcase(testcase, "key", &key, &keylen) &&
	   get_from_testcase(testcase, "nonce", &iv, &ivlen) &&
	   get_from_testcase(testcase, "aad", &aad, &aadlen))) {
	return NULL;
    }

    if (Debug) printf("AES GCM Testcase Encrypt:\n");
    if (Debug > 1) {
	printf("KEY (%d):\n", keylen);
	BIO_dump_fp(stdout, key.buf, keylen);
	printf("IV (%d):\n", ivlen);
	BIO_dump_fp(stdout, iv.buf, ivlen);
	printf("AAD (%d):\n", aadlen);
	BIO_dump_fp(stdout, aad.buf, aadlen);
	printf("Plaintext (%d):\n", ptlen);
	BIO_dump_fp(stdout, pt.buf, ptlen);
    }
    unsigned char *outbuf = (unsigned char *)PyMem_Malloc(ptlen+16);
    if(!outbuf) {
      return PyErr_NoMemory();
    }
    ctx = EVP_CIPHER_CTX_new();
    /* Set cipher type and mode */
    switch (keylen) {
    case 16:
	EVP_EncryptInit_ex(ctx, EVP_aes_128_gcm(), NULL, NULL, NULL);
	break;
    case 24:
	EVP_EncryptInit_ex(ctx, EVP_aes_192_gcm(), NULL, NULL, NULL);
	break;
    case 32:
	EVP_EncryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, NULL, NULL);
	break;
    }
    /* Set IV length if default 96 bits is not appropriate */
    EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_SET_IVLEN, ivlen, NULL);
    /* Initialise key and IV */
    EVP_EncryptInit_ex(ctx, NULL, NULL, key.buf, iv.buf);
    /* Zero or more calls to specify any AAD */
    if (aadlen) EVP_EncryptUpdate(ctx, NULL, &outlen, aad.buf, aadlen);
    /* Encrypt plaintext */
    EVP_EncryptUpdate(ctx, outbuf, &outlen, pt.buf, ptlen);
    if (Debug > 1) {
	printf("Ciphertext (%d):\n", outlen);
	BIO_dump_fp(stdout, (const char *)outbuf, outlen);
    }
    /* Finalise: note get no output for GCM */
    EVP_EncryptFinal_ex(ctx, outbuf, &olen);

    /* Get tag */
    rv = EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_GET_TAG, 16, tag);
    if (Debug > 1) {
	printf("Tag (%d):\n", 16);
	BIO_dump_fp(stdout, (const char *)tag, 16);
    }
    EVP_CIPHER_CTX_free(ctx);
    set_buf_to_testcase(testcase, "enc_ciphertext", outbuf, outlen);
    set_buf_to_testcase(testcase, "enc_tag", tag, 16);
    set_int_to_testcase(testcase, "enc_status", rv);
    PyMem_Free(outbuf);
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject *
aes_gcm_testcase_decrypt(PyObject *self, PyObject *args)
{
    EVP_CIPHER_CTX *ctx;
    int outlen, rv, olen;
    PyObject *testcase;
    Py_buffer key, ct, aad, iv;
    int keylen, ctlen, aadlen, ivlen;
    if (!PyArg_ParseTuple(args, "O:tc_decrypt", &testcase)) {
	PyErr_SetString(AesgcmpyError, "Usage: tc_encrypt <testcase>");
	return NULL;
    }
    if (! (get_from_testcase(testcase, "key", &key, &keylen) &&
	   get_from_testcase(testcase, "ctext_tag", &ct, &ctlen) &&
	   get_from_testcase(testcase, "nonce", &iv, &ivlen) &&
	   get_from_testcase(testcase, "aad", &aad, &aadlen))) {
	return NULL;
    }

    if (Debug) printf("AES GCM Decrypt:\n");
    if (Debug > 1) {
	printf("Ciphertext (%d):\n", ctlen-16);
	BIO_dump_fp(stdout, ct.buf, ctlen-16);
	printf("TAG (16):\n");
	BIO_dump_fp(stdout, ct.buf+ctlen-16, 16);
    }
    unsigned char *outbuf = (unsigned char *)PyMem_Malloc(ctlen);
    if(!outbuf) {
      return PyErr_NoMemory();
    }
    ctx = EVP_CIPHER_CTX_new();
    /* Select cipher */
    switch (keylen) {
    case 16:
	EVP_DecryptInit_ex(ctx, EVP_aes_128_gcm(), NULL, NULL, NULL);
	break;
    case 24:
	EVP_DecryptInit_ex(ctx, EVP_aes_192_gcm(), NULL, NULL, NULL);
	break;
    case 32:
	EVP_DecryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, NULL, NULL);
	break;
    }
    /* Set IV length, omit for 96 bits */
    EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_SET_IVLEN, ivlen, NULL);
    /* Specify key and IV */
    EVP_DecryptInit_ex(ctx, NULL, NULL, key.buf, iv.buf);
    /* Zero or more calls to specify any AAD */
    if (aadlen) EVP_DecryptUpdate(ctx, NULL, &outlen, aad.buf, aadlen);
    /* Decrypt plaintext */
    EVP_DecryptUpdate(ctx, outbuf, &outlen, ct.buf, ctlen-16);
    if (Debug > 1) {
	printf("Plaintext (%d):\n", outlen);
	BIO_dump_fp(stdout, (const char *)outbuf, outlen);
    }
    /* Set expected tag value. */
    EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_SET_TAG, 16, ct.buf+ctlen-16);
    /* Finalise: note get no output for GCM */
    rv = EVP_DecryptFinal_ex(ctx, outbuf, &olen);
    /*
     * Print out return value. If this is not successful authentication
     * failed and plaintext is not trustworthy.
     */
    if (Debug > 1) printf("Tag Verify %s\n", rv > 0 ? "Successful!" : "Failed!");
    EVP_CIPHER_CTX_free(ctx);
    set_buf_to_testcase(testcase, "dec_plaintext", outbuf, outlen);
    set_int_to_testcase(testcase, "dec_status", rv);
    PyMem_Free(outbuf);
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef AesGcmMethods[] = {
    {"encrypt",  aes_gcm_encrypt, METH_VARARGS, "Encrypt with AES-GCM."},
    {"decrypt",  aes_gcm_decrypt, METH_VARARGS, "Decrypt with AES-GCM."},
    {"tc_encrypt",  aes_gcm_testcase_encrypt, METH_VARARGS, "Encrypt testcase with AES-GCM."},
    {"tc_decrypt",  aes_gcm_testcase_decrypt, METH_VARARGS, "Decrypt testcase with AES-GCM."},
    {"debug",    aes_debug,       METH_VARARGS, "Debug."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC
initaesgcmpy(void)
{
    PyObject *m;
    m = Py_InitModule("aesgcmpy", AesGcmMethods);
    if (m == NULL) return;
    AesgcmpyError = PyErr_NewException("AesgcmpyError.error", NULL, NULL);
    Py_INCREF(AesgcmpyError);
    PyModule_AddObject(m, "error", AesgcmpyError);
}

int
main(int argc, char *argv[])
{
    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(argv[0]);

    /* Initialize the Python interpreter.  Required. */
    Py_Initialize();

    /* Add a static module */
    initaesgcmpy();
    return 0;
}

#else

static struct PyModuleDef aesgcmpy = {
  PyModuleDef_HEAD_INIT,
  "aesgcmpy",   /* name of module */
  NULL, /* module documentation, may be NULL */
  -1,       /* size of per-interpreter state of the module,
	       or -1 if the module keeps state in global variables. */
  AesGcmMethods
};

PyMODINIT_FUNC
PyInit_aesgcmpy(void)
{
  return PyModule_Create(&aesgcmpy);
}

int
main(int argc, char *argv[])
{
  wchar_t *program = Py_DecodeLocale(argv[0], NULL);
  if (program == NULL) {
    fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
    exit(1);
  }

  /* Add a built-in module, before Py_Initialize */
  PyImport_AppendInittab("aesgcmpy", PyInit_aesgcmpy);

  /* Pass argv[0] to the Python interpreter */
  Py_SetProgramName(program);

  /* Initialize the Python interpreter.  Required. */
  Py_Initialize();

  /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
  //PyImport_ImportModule("spam");

    PyMem_RawFree(program);
    return 0;
}

#endif
