#ifndef TYPE_H
#define TYPE_H

#include "def.h"
#include "spec.h"
#include "config.h"
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

typedef int       (*qsort_f)(void const *,void const *);

typedef struct ircmsg{
  char             *pre_name;
  char             *pre_user;
  char             *pre_host;
  char             *cmd;
  size_t            argc;
  char             *argv[IRCD_ARG_MAX];
  char             *trail;
}ircmsg_t;

typedef void      (*tcpev_f)  (unsigned);
typedef void      (*ircev_f)  (unsigned,ircmsg_t const *);
typedef void      (*pestev_f) (unsigned,char const *,char const *);
typedef void      (*log_f)    (char const *,...);

typedef char        handle_t      [HANDLE_BUF];
typedef uint16_t    peerid_t;

typedef uint8_t     hash_t[SHA256_SIZE];

typedef struct addr{
  uint32_t          ip;
  uint16_t          port;
}addr_t;

typedef struct mess{
  char              path[PATH_BUF];
  size_t            idx_cnt;  //# of idx files
  size_t            msg_cnt;  //# of msg files
  size_t            idx_ecnt; //# of entries in last idx file
  size_t            msg_ecnt; //# of entries in last msg file
}mess_t;

typedef struct chain{
  char              path[PATH_BUF];
  size_t            cha_cnt;  //# of cha files
  size_t            cha_ecnt; //# of entries in last cha file
}chain_t;

//TODO: vtf call this
typedef struct ht{
  char              path[PATH_BUF];
  hash_t            hash[HEADTAIL_MAX]; 
  size_t            cnt;
  size_t            last;
}ht_t;

typedef struct rekey{
  unsigned          state;
  bool              log;
  uint64_t          time;
  size_t            pak_cnt;
  uint8_t           offer_self  [SHA512_SIZE];
  uint8_t           offer_peer  [SHA512_SIZE];
  uint8_t           slice_self  [KEY_SIZE];
  uint8_t           slice_peer  [KEY_SIZE];
  uint8_t           key_old     [KEY_SIZE];
  uint8_t           key_new     [KEY_SIZE];
}rekey_t;

typedef struct pkey{
  union{
    uint8_t         full          [KEY_SIZE];
    struct{
      uint8_t       sign          [KEY_SIGN_SIZE];
      uint8_t       ciph          [KEY_CIPH_SIZE];
    }sub;
  }key;
  uint8_t           ciph_serp     [SERPENT_SKEYSIZE];
  uint64_t          time;
}pkey_t;

typedef struct peer{
  peerid_t          id;
  handle_t          handle        [HANDLE_MAX];
  size_t            handle_cnt;
  pkey_t            key           [KEY_MAX];
  size_t            key_cnt;
  addr_t            addr;
  uint64_t          stamp;        //last validated paket recevid from pear indep. of key
  uint64_t          pak_stamp;    //last any paket recevid from pear indep. of key
  uint64_t          con_stamp;    //stamp of last message displayed in console
  bool              active;
  bool              paused;
  char              banner        [BANNER_BUF];
  mess_t            mess;         //peer <-> operator
  chain_t           dchain;       //peer  -> operator
  chain_t           bchain;       //peer  -> net
  ht_t              dhead;        //peer  -> operator
  ht_t              dtail;        //peer  -> operator
  ht_t              bhead;        //peer  -> net
  ht_t              btail;        //peer  -> net
  hash_t            self;         //peer <-  operator
  rekey_t           rekey;
}peer_t;

typedef struct getdata{
  hash_t            hash;
  peerid_t          peer_id;
  peerid_t          chan_id;
  uint64_t          ntime;
  size_t            attempt;
}getdata_t;

typedef struct hearsay{
  hash_t            hash;
  uint8_t           red           [RED_SIZE];
  peerid_t          peer          [PEER_MAX]; //this is fuckd but how fix?
  size_t            peer_cnt;
  peerid_t          speaker;
  uint64_t          ntime;
  uint8_t           bounces;
}hearsay_t;

typedef struct pending{
  uint8_t           m             [MESSAGE_SIZE];
  char              speaker       [HANDLE_EXT_BUF]; //this is so gay
  hash_t            hash;
  peerid_t          peer_id;
  peerid_t          chan_id;
  uint64_t          ntime;
  bool              tail;
}pending_t;

typedef struct knob{
  void             *data;
  char const       *name;
  char const       *desc;
  unsigned          type;
  union{
    bool            b;
    int64_t         i;
    char const     *s;
  }def;
  int64_t           min;
  int64_t           max;
}knob_t;

typedef void      (*strval_f)   (char *,size_t,void const *);
typedef unsigned  (*setval_f)   (knob_t const *,char const *);
typedef bool      (*storeval_f) (knob_t const *,char const *);
typedef unsigned  (*loadval_f)  (knob_t const *,char const *);

#endif

