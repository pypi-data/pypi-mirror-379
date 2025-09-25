#ifndef CRYPTO_H
#define CRYPTO_H

#include "type.h"
#include "def.h"
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <string.h>

void                serpent_init      (uint8_t *skey,uint8_t const *key,size_t key_size);
void                serpent_cbc_ciph  (uint8_t const *skey,uint8_t *dst,uint8_t const *src,size_t size);
void                serpent_cbc_deciph(uint8_t const *skey,uint8_t *dst,uint8_t const *src,size_t size);

void                sha256            (uint8_t *sha,uint8_t const *data,size_t data_len);
void                sha384            (uint8_t *sha,uint8_t const *data,size_t data_len);
void                sha512            (uint8_t *sha,uint8_t const *data,size_t data_len);

void                hmac384           (uint8_t const *key,size_t key_size,uint8_t *mac,uint8_t const *msg,size_t msg_size);

size_t              base64_dec_size   (char const *in,bool nullterm);
size_t              base64_dec        (char const *in,uint8_t *out,size_t out_size,bool nullterm);
size_t              base64_enc        (uint8_t const *in,size_t in_size,char *out,size_t out_size);

bool                rng_open          (char const *path);
void                rng_close         (void);
bool                rng_read          (void *data,size_t size);
bool                rng_read_nolog    (void *data,size_t size);

inline void         hash_data         (hash_t h,void const *data,size_t size);
inline void         hash_zero         (hash_t h);
inline void         hash_copy         (hash_t dst,hash_t const src);
inline bool         hash_equal        (hash_t const a,hash_t const b);
inline bool         hash_null         (hash_t const h);

void                hash_str          (char *buf,size_t buf_size,hash_t const hash);
void                hash_str_log      (char *buf,size_t buf_size,hash_t const hash);

void                key_zero          (uint8_t *key);
void                key_copy          (uint8_t *dst,uint8_t const *src);
void                key_xor           (uint8_t *dst,uint8_t const *a,uint8_t const *b);
bool                key_equal         (uint8_t const *a,uint8_t const *b);

bool                key_gen           (uint8_t *key);
void                b64_from_key      (char *buf,size_t buf_size,uint8_t const *key);
bool                key_from_b64      (uint8_t *key,char const *b64_key);

void               *memset_ffs        (void *dst,int c,size_t size);
bool                entropy_missing   (uint8_t const *data,size_t size);

inline void hash_data(hash_t h,void const *data,size_t size){
  sha256(h,data,size);
}

inline void hash_zero(hash_t h){
  memset(h,0x00,sizeof(hash_t));
}

inline void hash_copy(hash_t dst,hash_t const src){
  memcpy(dst,src,sizeof(hash_t));
}

inline bool hash_equal(hash_t const a,hash_t const b){
  return memcmp(a,b,sizeof(hash_t)) == 0;
}

inline bool hash_null(hash_t const h){
  for(size_t x = 0;x < HASH_SIZE;x++){
    if(h[x] != 0x00) return 0;
  }
  return 1;
}

#endif

