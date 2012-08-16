#ifndef _TF_H_
#define _TF_H_

#include "res.h"

struct PACKED port_map {
  uint32_t n/*, padding*/;
  struct PACKED port_map_elem {
    uint32_t port;
    uint32_t start;
  } elems[0];
};

struct PACKED deps {
  uint32_t n;
  struct PACKED dep {
    uint32_t rule;
    uint32_t match;
    int32_t port;
  } deps[0];
};

struct PACKED ports {
  uint32_t n;
  uint32_t arr[0];
};

struct PACKED rule {
  uint32_t idx;
  int32_t in, out;
  uint32_t match, mask, rewrite;
  uint32_t deps, desc;
};

struct PACKED tf {
  uint32_t prefix;
  uint32_t nrules;
  uint32_t map_ofs;
  uint32_t ports_ofs, deps_ofs;
  struct rule rules[0];
};

struct list_res tf_apply (const struct tf *, const struct res *, bool);
struct tf      *tf_get   (int);
void            tf_print (const struct tf *);

#endif

