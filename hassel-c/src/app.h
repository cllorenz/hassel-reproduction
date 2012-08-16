#ifndef _APP_H_
#define _APP_H_

#include "res.h"

void app_init (void);
void app_fini (void);

struct list_res reachability (const struct hs *, uint32_t, const uint32_t *, int);

#endif

