/*
 * Cryptographic API.
 *
 * Serpent Cipher Algorithm.
 *
 * Copyright (C) 2002 Dag Arne Osvik <osvik@ii.uib.no>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * ********************MODIFIED FOR USE IN SMALPEST********************
 *
 */

#ifndef OTHERPPL_SERPENT_H
#define OTHERPPL_SERPENT_H

#include <stdint.h>
#include <stddef.h>

#define SERPENT_BLOCK_SIZE                   16
#define SERPENT_EXPKEY_WORDS                132

int                 serpent_setkey    (uint32_t *k,uint8_t const *key,size_t keylen);
void                serpent_block_enc (uint32_t const *k,uint8_t *dst,uint8_t const *src);
void                serpent_block_dec (uint32_t const *k,uint8_t *dst,uint8_t const *src);

#endif
