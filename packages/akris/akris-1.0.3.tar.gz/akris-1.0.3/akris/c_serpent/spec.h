#ifndef SPEC_H
#define SPEC_H

#define PEST_VERSION                 0xFC

#define CUTOFF_MIN                      0
#define CUTOFF_MAX                    255
#define BOUNCES_MAX                   255

#define TIMESTAMP_MAXDIFF               (60*15) //15min
#define DEDUP_TIMEOUT                   (60*60) //60min

#define HEARSAY_PARENS_MAX              3

#define REKEY_PACKET_CNT                3

#define KEY_SIGN_SIZE                  32
#define KEY_CIPH_SIZE                  32
#define KEY_SIZE                        (KEY_SIGN_SIZE+KEY_CIPH_SIZE)
#define BANNER_LEN                      TEXT_SIZE

#define CMD_BROADCAST                0x00
#define CMD_DIRECT                   0x01
#define CMD_BANNER                   0x02
#define CMD_GETDATA                  0x03
#define CMD_KEYOFFER                 0x04
#define CMD_KEYSLICE                 0x05
#define CMD_ADDRESSCAST              0xFE
#define CMD_IGNORE                   0xFF

#define CMD_UNDEF_MIN                0x06
#define CMD_UNDEF_MAX                0xFD

//--- red address cast ----------------------------------------------------
#define AC_CMD_SIZE                     sizeof(uint32_t)
#define AC_PORT_SIZE                    sizeof(uint16_t)
#define AC_IP_SIZE                      sizeof(uint32_t)
#define AC_RPAD_SIZE                  262

#define AC_CMD_OFF                      ( 0                               )
#define AC_PORT_OFF                     ( AC_CMD_OFF     + AC_CMD_SIZE    )
#define AC_IP_OFF                       ( AC_PORT_OFF    + AC_PORT_SIZE   )
#define AC_RPAD_OFF                     ( AC_IP_OFF      + AC_IP_SIZE     )

#define AC_RED_SIZE                     ( AC_RPAD_OFF    + AC_RPAD_SIZE   )

//--- black address cast --------------------------------------------------
#define AC_SIGN_SIZE                    HMAC384_SIZE
#define AC_BPAD_SIZE                    4

#define AC_RED_OFF                      ( 0                               )
#define AC_SIGN_OFF                     ( AC_RED_OFF    + AC_RED_SIZE     )
#define AC_BPAD_OFF                     ( AC_SIGN_OFF   + AC_SIGN_SIZE    )

#define AC_BLACK_SIZE                   ( AC_BPAD_OFF   + AC_BPAD_SIZE    )

//--- message -------------------------------------------------------------
#define TIMESTAMP_SIZE                  sizeof(uint64_t)
#define SELFCHAIN_SIZE                  HASH_SIZE
#define NETCHAIN_SIZE                   HASH_SIZE
#define SPEAKER_SIZE                   32
#define TEXT_SIZE                     324

#define TIMESTAMP_OFF                   ( 0                               )
#define SELFCHAIN_OFF                   ( TIMESTAMP_OFF + TIMESTAMP_SIZE  )
#define NETCHAIN_OFF                    ( SELFCHAIN_OFF + SELFCHAIN_SIZE  )
#define SPEAKER_OFF                     ( NETCHAIN_OFF  + NETCHAIN_SIZE   )
#define TEXT_OFF                        ( SPEAKER_OFF   + SPEAKER_SIZE    )

#define MESSAGE_SIZE                    ( TEXT_OFF      + TEXT_SIZE       )

//--- red packet ----------------------------------------------------------
#define NONCE_SIZE                     16
#define BOUNCES_SIZE                    sizeof(uint8_t)
#define VERSION_SIZE                    sizeof(uint8_t)
#define RESERVED_SIZE                   sizeof(uint8_t)
#define COMMAND_SIZE                    sizeof(uint8_t)

#define NONCE_OFF                       ( 0                               )
#define BOUNCES_OFF                     ( NONCE_OFF     + NONCE_SIZE      )
#define VERSION_OFF                     ( BOUNCES_OFF   + BOUNCES_SIZE    )
#define RESERVED_OFF                    ( VERSION_OFF   + VERSION_SIZE    )
#define COMMAND_OFF                     ( RESERVED_OFF  + RESERVED_SIZE   )
#define MESSAGE_OFF                     ( COMMAND_OFF   + COMMAND_SIZE    )

#define RED_SIZE                        ( MESSAGE_OFF   + MESSAGE_SIZE    )

//--- black packet --------------------------------------------------------
#define SIGN_SIZE                       HMAC384_SIZE

#define RED_OFF                         ( 0                               )
#define SIGN_OFF                        ( RED_OFF       + RED_SIZE        )

#define BLACK_SIZE                      ( SIGN_OFF      + SIGN_SIZE       )

#endif

