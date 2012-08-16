#include "res.h"
#include "tf.h"

struct res *
res_create (int nrules)
{
  struct res *res = xcalloc (1, sizeof *res + nrules * sizeof *res->rules.arr);
  res->rules.n = nrules;
  return res;
}

void
res_free (struct res *res)
{
  if (res->refs) { res->next = NULL; return; }

  hs_destroy (&res->hs);
  struct res *parent = res->parent;
  free (res);
  if (parent) { parent->refs--; res_free (parent); }
}

void
res_print (const struct res *res)
{
  if (res->parent) res_print (res->parent);
  printf ("-> Port: %d, HS: ", res->port);
  //hs_print (&res->hs);
  if (res->rules.cur) {
    printf ("   Rules: ");
    for (int i = 0; i < res->rules.cur; i++) {
      if (i) printf (", ");
      printf ("%" PRIu32, res->rules.arr[i]->idx);
    }
  }
  printf ("\n");
}


struct res *
res_extend (const struct res *src, const struct hs *hs, int port,
            const struct rule *rule, bool append)
{
  struct res *res = res_create (src->rules.n);
  if (hs) hs_copy (&res->hs, hs);
  res->port = port;
  if (append) {
    res->rules.cur = src->rules.cur;
    memcpy (res->rules.arr, src->rules.arr, res->rules.cur * sizeof *res->rules.arr);
  }
  res_rule_add (res, rule);
  return res;
}

void
res_rule_add (struct res *res, const struct rule *rule)
{
  assert (res->rules.cur < res->rules.n);
  res->rules.arr[res->rules.cur++] = rule;
}


/* Won't free structs with refs, but next pointers will be NULLed. */
void
list_res_free (struct list_res *l)
{ list_destroy (l, res_free); }

void
list_res_print (const struct list_res *l)
{
  int count = 0;
  for (const struct res *res = l->head; res; res = res->next, count++) {
    res_print (res);
    printf ("-----\n");
  }
  printf ("Count: %d\n", count);
}

