#ifndef _RES_H_
#define _RES_H_

#include "hs.h"

struct res {
  struct res *next, *parent;
  int refs;

  struct hs hs;
  uint32_t port;
  struct {
    int n, cur;
    const struct rule *arr[0];
  } rules;
};

struct res *res_create   (int);
void        res_free     (struct res *);
void        res_print    (const struct res *);

struct res *res_extend   (const struct res *, const struct hs *, int,
                          const struct rule *, bool);
void        res_rule_add (struct res *res, const struct rule *rule);

LIST (res);
void list_res_free  (struct list_res *);
void list_res_print (const struct list_res *);

#endif

