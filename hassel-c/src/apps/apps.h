#include "app.h"
#include "data.h"
#include <libgen.h>
#include <limits.h>
#include <valgrind/callgrind.h>

#ifndef NTF_STAGES
#define NTF_STAGES 1
#endif

static void
unload (void)
{ data_unload (); }

static void
load (char *argv0)
{
  fflush (stdout);

  char name[PATH_MAX + 1];
  snprintf (name, sizeof name, "data/%s.dat", basename (argv0));
  data_load (name);
  if (atexit (unload)) errx (1, "Failed to set exit handler.");
}

int
main (int argc, char **argv)
{
  CALLGRIND_TOGGLE_COLLECT;
  if (argc < 2) {
    fprintf (stderr, "Usage: %s <in_port> [<out_ports>...]\n", argv[0]);
    exit (1);
  }

  load (argv[0]);
  app_init ();

  struct hs hs;
  memset (&hs, 0, sizeof hs);
  hs.len = data_arrs_len;
  hs_add (&hs, array_create (hs.len, BIT_X));

  int nout = argc - 2;
  uint32_t out[nout];
  for (int i = 0; i < nout; i++) out[i] = atoi (argv[i + 2]);

  CALLGRIND_TOGGLE_COLLECT;
  struct list_res res = reachability (&hs, atoi (argv[1]), nout ? out : NULL, nout);
  CALLGRIND_TOGGLE_COLLECT;

  list_res_print (&res);
  list_res_free (&res);
  hs_destroy (&hs);
  app_fini ();
  return 0;
}

