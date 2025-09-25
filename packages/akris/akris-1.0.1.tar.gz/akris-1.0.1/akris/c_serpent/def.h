#ifndef DEF_H
#define DEF_H

#define PROG_NAME                       "smalpest"
#define PROG_VERSION                    "98K"
#define PROG_FULLNAME                   PROG_NAME "-" PROG_VERSION

#define INT64_LEN                      20 //18446744073709551616
#define KILOBYTE                        (1024)
#define MEGABYTE                        (1024*KILOBYTE)
#define GIGABYTE                        (1024*MEGABYTE)

#define PATH_LEN                      255
#define DATA_MODE                    0700
#define DATA_UMASK                      (~DATA_MODE)
#define DATA_PATH_DEF                   "./data"
#define LOG_PATH_DEF                    "./log"
#define DIR_PEER                        "peer"
#define DIR_MESS                        "mess"
#define DIR_CHAIN                       "chain"
#define DIR_BCHAIN                      "bchain"
#define DIR_DCHAIN                      "dchain"
#define FILE_IRC_USER                   "user"
#define FILE_IRC_PASS                   "pass"
#define FILE_IRC_PORT                   "iport"
#define FILE_PEST_PORT                  "pport"
#define FILE_SCRAM_PASS                 "scram"
#define FILE_KILLFILE                   "kill"
#define FILE_SETPORT                    "setport"
#define FILE_CUTOFF                     "cutoff"
#define FILE_HSTIME                     "hstime"
#define FILE_GDTIME                     "gdtime"
#define FILE_GDATT                      "gdatt"
#define FILE_GDINT                      "gdint"
#define FILE_RKRECV                     "rkrecv"
#define FILE_RKSEND                     "rksend"
#define FILE_RKTIME                     "rktime"
#define FILE_RKINT                      "rkint"
#define FILE_IGINT                      "igint"
#define FILE_BANNER                     "banner"
#define FILE_BAINT                      "baint"
#define FILE_ACADDR                     "acaddr"
#define FILE_ACINT                      "acint"
#define FILE_IRCTIME                    "irctime"
#define FILE_MASTER                     "master"
#define FILE_DEDUP                      "dedup"
#define FILE_ALIAS                      "alias"
#define FILE_KEY                        "key"
#define FILE_ADDR                       "addr"
#define FILE_STAMP                      "stamp"
#define FILE_PAUSE                      "pause"
#define FILE_SELF                       "self"
#define FILE_NET                        "net"
#define FILE_HEAD                       "head"
#define FILE_TAIL                       "tail"

#define WHITE_LEN                      32 //allocated for whitespace/extra newline/whatever in files

#define PORT_MIN                        0
#define PORT_MAX                    65535
#define IPV4_LEN                       15 //255.255.255.255
#define IPV4_CHARSET                    "0123456789."
#define PORT_LEN                        5 //55555
#define PORT_CHARSET                    "0123456789"
#define AT_LEN                          (IPV4_LEN+1+PORT_LEN) //IPV4:PORT
#define STAMP_LEN                      64

#define IRC_PORT_DEF                 6668
#define IRC_MSG_LEN                   512
#define IRC_USER_LEN                   63
#define IRC_HOST_LEN                   63
#define IRC_SERV_LEN                   63
#define IRC_CHAN_LEN                  128
#define IRCD_ARG_MAX                    8
#define IRCD_CMD_LEN                   31
#define IRC_SERV                        "pest"
#define IRC_MOTD                        "welcome, operator"
#define IRC_PEERHOST                    "pest.net"

#define PEST_PORT_DEF                7778
#define HANDLE_LEN                      SPEAKER_SIZE
#define HANDLE_MAX                      8
#define HANDLE_CHARSET                  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"
#define KEY_MAX                         8
#define DEDUP_MAX                       (1<<DEDUP_POW2)
#define PEER_ID_INVALID                 ((peerid_t)-1)
#define B64_KEY_LEN                     BASE64_ENC_SIZE(KEY_SIZE,0)

#define KNOB_VAL_LEN                  511
#define KNOB_MIN                        INT64_MIN
#define KNOB_MAX                        INT64_MAX

#define SERPENT_SKEYSIZE                (132*sizeof(uint32_t))
#define SHA256_SIZE                     (256/8)
#define SHA384_SIZE                     (384/8)
#define SHA512_SIZE                     (512/8)
#define HMAC384_SIZE                    (384/8)
#define HASH_SIZE                       SHA256_SIZE
#define HASH_HEX_LEN                    (2*HASH_SIZE)
#define HASH_B64_LEN                    BASE64_ENC_SIZE(sizeof(hash_t),0)
#define PASS_SIZE                       SHA512_SIZE
#define B64_PASS_LEN                    BASE64_ENC_SIZE(PASS_SIZE,0)
#define BASE64_CHARSET                  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

#define SEC_MIN                         (60ULL            )
#define SEC_HOUR                        (60ULL  * SEC_MIN )
#define SEC_DAY                         (24ULL  * SEC_HOUR)
#define SEC_YEAR                        (365ULL * SEC_DAY )

#define MSEC_SEC                     1000ULL
#define NSEC_MSEC                 1000000ULL
#define NSEC_SEC               1000000000ULL

#define STAMPDIFF_BUF                  20 //+584942417355 years\0

#define INT64_BUF                       (1+INT64_LEN)
#define PATH_BUF                        (1+PATH_LEN)
#define IPV4_BUF                        (1+IPV4_LEN)
#define PORT_BUF                        (1+PORT_LEN)
#define AT_BUF                          (1+AT_LEN)
#define STAMP_BUF                       (1+STAMP_LEN)
#define IRC_MSG_BUF                     (1+IRC_MSG_LEN)
#define IRC_USER_BUF                    (1+IRC_USER_LEN)
#define IRC_HOST_BUF                    (1+IRC_HOST_LEN)
#define IRC_CHAN_BUF                    (1+IRC_CHAN_LEN)
#define IRCD_CMD_BUF                    (1+IRCD_CMD_LEN)
#define B64_KEY_BUF                     (1+B64_KEY_LEN)
#define B64_PASS_BUF                    (1+B64_PASS_LEN)
#define KNOB_VAL_BUF                    (1+KNOB_VAL_LEN)
#define HANDLE_BUF                      (1+HANDLE_LEN)
#define BANNER_BUF                      (1+BANNER_LEN)
#define TEXT_BUF                        (1+TEXT_SIZE)
#define HASH_HEX_BUF                    (1+HASH_HEX_LEN)
#define HASH_B64_BUF                    (1+HASH_B64_LEN)

#define HANDLE_EXT_BUF                  (SPEAKER_SIZE+1+(HANDLE_LEN+1)*HANDLE_MAX+1) //speaker[handle0,...,handleN]\0

#define _STR(X)                         #X
#define STR(X)                          _STR(X)

#define ARR_CNT(A)                      (sizeof(A)/sizeof(*(A)))
#define ARR_INDEXOF(A,P)                ((size_t)((P)-(A)))
#define ARR_DEL(A,N,P)                  memmove(P,(P)+1,((A+N)-((P)+1))*sizeof(*(A)))
#define ARR_DEL_IDX(A,N,I)              memmove(A+I,(A+I)+1,((A+N)-((A+I)+1))*sizeof(*(A)))

#define VAR_ZERO(V)                     memset_ffs      ((&(V)),0x00,sizeof(V))
#define BUF_ZERO(B)                     memset_ffs      ((  B ),0x00,sizeof(B))
#define VAR_RAND(V)                     rng_read_nolog  ((&(V)),     sizeof(V))
#define BUF_RAND(B)                     rng_read_nolog  ((  B ),     sizeof(B))

#define FMT_PATH(P,F,...)               snprintf(P,sizeof(P),"%s/"F,data_path,__VA_ARGS__)

#define BASE64_ENC_SIZE(S,NT)           (((S)+2)/3*4+(NT))

enum{
  LOOKUP_IO,
  LOOKUP_FOUND,
  LOOKUP_NOTFOUND,
};

enum{
  TCP_CONNECT,
  TCP_DISCONNECT,
};

enum{
  IRCD_CONNECT,
  IRCD_DISCONNECT,
  IRCD_MESSAGE,
};

enum{
  PEST_BROADCAST,
  PEST_DIRECT,
  PEST_ACTIVE,
  PEST_INACTIVE,
};

enum{
  KNOB_BOOL,
  KNOB_INT,
  KNOB_STR,
};

enum{
  KNOB_SUCCESS,
  KNOB_INVALID,
  KNOB_RANGE,
  KNOB_STORE,
  KNOB_LOAD,
};

#endif

