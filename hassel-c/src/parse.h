#ifndef _PARSE_H_
#define _PARSE_H_

#include "array.h"
#include "map.h"

struct parse_dep {
  struct parse_dep *next;
  int rule;
  array_t *match;
  int nports;
  uint32_t ports[0];
};

struct parse_rule {
  struct parse_rule *next;
  int idx;
  ARR_PTR(uint32_t, uint32_t) in, out;
  array_t *match;
  array_t *mask, *rewrite;
  LIST (parse_dep) deps;
  //char *file, *lines;
};

struct parse_tf {
  int len, nrules;
  char *prefix;
  LIST (parse_rule) rules;

  struct map in_map;
};

struct parse_ntf {
  int ntfs;
  int stages;
  struct parse_tf *tfs[0];
};

void parse_dir (const char *, const char *, const char *);

#endif

