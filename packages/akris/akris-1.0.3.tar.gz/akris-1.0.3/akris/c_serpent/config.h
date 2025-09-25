#ifndef CONFIG_H
#define CONFIG_H

#define RNG_PATH              "/dev/urandom" //entropy source file
#define STACK_WIPE_SIZE       (4*MEGABYTE)  //amount of stack to zeroize/randomize
//#define BIG_ENDIAN            //system endianess

#define NET_SILENT_SLEEP     10 //milliseconds to sleep when no tcp/udp
#define NET_RETRY_SLEEP    1000 //milliseconds to sleep when cant listen tcp/udp
#define IRCD_RECV_MAX         4 //max number of recvs before yield to udp
#define PEST_RECV_MAX        32 //max number of recvs before yield to tcp
#define PEST_WAIT_IRC        10 //number of seconds to wait for irc connection before fire up pest

#define PEER_MAX             64 //max number of peers
#define KILLFILE_MAX         64 //max number of entries in killfile
#define DEDUP_POW2           18 //dedup buffer size (2^x)
#define HEARSAY_MAX          64 //hearsay buffer size
#define PENDING_MAX         512 //pending message buffer size (msg where selfchain doenst link)
#define GETDATA_MAX          64 //max parallel getdata requests
#define HEADTAIL_MAX         16 //max number of heads/tails kept track of for each chain

#define CHAIN_CHA_POW2       17 //chain table alloc. entries (2^x, filesize = 2^x*64)
#define CHAIN_CHA_LOAD      700 //chain table load factor (x/1000)
#define CHAIN_CHA_ZEROS       5 //chain table cha* files number of zeros
#define MESS_IDX_POW2        18 //message index table alloc. entries in (2^x, filesize = 2^x*40)
#define MESS_IDX_LOAD       700 //message index table load factor (x/1000)
#define MESS_IDX_ZEROS        5 //message index idx* files number of zeros
#define MESS_MSG_POW2        15 //message files max entries in (2^x, filesize = 2^x*428)
#define MESS_MSG_ZEROS        5 //message files number of zeros in

#define NOTICE_CHAN             //send NOTICE messages to #pest channel (chain warn. always sent)
#define CONSOLE_STAMP_FMT     "%F %T"   //stamp format for console output
#define GETDATA_STAMP_FMT     "[%T]"    //stamp format for old messages
#define GETDATA_OLDSTAMP_FMT  "[%F %T]" //stamp format for >24h old messages

#define LOG_STAMP_FMT         "%F %T"   //stamp format for log output
#define LOG_HASH_BYTES        4 //number of least significant bytes of sha256 to display in log
#define LOG_ANSI_COLORS         //use ansi colors for packet log output
#define LOG_COLLAPSE            //collapse broadcast messages into one log entry
//#define LOG_MARTIAN           //log martian packets
//#define LOG_STALE             //log stale (invalid timestamp) packets
//#define LOG_DUPLICATE         //log duplicate packets
//#define LOG_IGNORE            //log incoming and outgoing ignore packets
//#define LOG_CUTOFF            //log messages discarded due to bounce cutoff
//#define LOG_IOSPAM            //log io operations
//#define LOG_MESS              //log message storage operations
//#define LOG_CHAIN             //log chain operations

#endif

