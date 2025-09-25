#include "crypto.h"
#include "lib/serpent.h"
#include <string.h>
#include <assert.h>
#include <stdio.h>

void serpent_init(uint8_t        *skey,
                  uint8_t const  *key,
                  size_t          key_size){

  int r = serpent_setkey((void *)skey,key,key_size);
  assert(r); (void)r;
}

static inline void xor_block(uint8_t       *r,
                             uint8_t const *a,
                             uint8_t const *b){

  for(size_t x = 0;x < SERPENT_BLOCK_SIZE;x++){
    r[x] = a[x]^b[x];
  }
}

void serpent_cbc_ciph(uint8_t const  *skey,
                      uint8_t        *dst,
                      uint8_t const  *src,
                      size_t          size){

  uint8_t tmp[SERPENT_BLOCK_SIZE];
  size_t  block_cnt;

  assert(size%SERPENT_BLOCK_SIZE == 0);
  block_cnt = size/SERPENT_BLOCK_SIZE;
  memset(tmp,0x00,SERPENT_BLOCK_SIZE);

  for(size_t x = 0;x < block_cnt;x++){
    size_t off = x*SERPENT_BLOCK_SIZE;
    xor_block(tmp,src+off,tmp); 
    serpent_block_enc((void const *)skey,dst+off,tmp);
    memcpy(tmp,dst+off,SERPENT_BLOCK_SIZE);
  }
}

void serpent_cbc_deciph(uint8_t const  *skey,
                        uint8_t        *dst,
                        uint8_t const  *src,
                        size_t          size){

  uint8_t  _tmp1[SERPENT_BLOCK_SIZE]; 
  uint8_t  _tmp2[SERPENT_BLOCK_SIZE]; 
  uint8_t  *tmp1 = _tmp1;
  uint8_t  *tmp2 = _tmp2;
  uint8_t  *tmp3;
  size_t    block_cnt;

  assert(size%SERPENT_BLOCK_SIZE == 0);
  block_cnt = size/SERPENT_BLOCK_SIZE;
  memset(tmp2,0x00,SERPENT_BLOCK_SIZE);

  for(size_t x = 0;x < block_cnt;x++){
    size_t off = x*SERPENT_BLOCK_SIZE;

    memcpy(tmp1,src+off,SERPENT_BLOCK_SIZE);
    serpent_block_dec((void const *)skey,dst+off,src+off);
    xor_block(dst+off,dst+off,tmp2);

    tmp3 = tmp1;
    tmp1 = tmp2;
    tmp2 = tmp3;
  }
}

