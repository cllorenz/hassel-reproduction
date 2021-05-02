#!/usr/bin/env bash

BENCH=$1

LOG=stdout.log
echo "" > $LOG
HASSEL_DIR=.

export PYTHONPATH=$HASSEL_DIR

TF_GENERATOR=$HASSEL_DIR/hsa-python/examples/$BENCH/generate_$BENCH"_"backbone_tf.py
JSON_GENERATOR=$HASSEL_DIR/hsa-python/examples/$BENCH/generate_rules_json_file.py

if [ "$BENCH" == "i2" ]; then
    TF_GENERATOR=$HASSEL_DIR/hsa-python/examples/$BENCH/generate_internet2_backbone_tf.py
    JSON_GENERATOR=$HASSEL_DIR/hsa-python/examples/$BENCH/generate_i2_json_tfs.py
fi

ORIG_DIR=benchmarks/$BENCH"_orig"

TF_DIR=benchmarks/$BENCH"_tfs"

VANILLA_DIR=benchmarks/$BENCH"_json_vanilla"
mkdir -p $VANILLA_DIR

TF_LOG=$BENCH"_gen_tfs.log"
JSON_LOG=$BENCH"_gen_json.log"

VANILLA_LOG=$BENCH"_vanilla.log"

HDR_LEN=`grep "length" $VANILLA_DIR/config.json | tr -d ' ,' | cut -d: -f2`

echo "generate tfs"
mkdir -p $TF_DIR
PYTHONPATH=$HASSEL_DIR/hsa-python \
python2 $TF_GENERATOR $ORIG_DIR $TF_DIR > $TF_LOG
cat $TF_LOG >> $LOG

GEN_TFS=`grep "completed in" $TF_LOG | cut -d' ' -f3`
echo "run time: $GEN_TFS s"

echo "transform tfs to json"
PYTHONPATH=$HASSEL_DIR/hsa-python \
python2 $JSON_GENERATOR \
    $TF_DIR \
    $VANILLA_DIR > $JSON_LOG
cat $JSON_LOG >> $LOG

echo "generate policy"
python2 create_policy.py $VANILLA_DIR >> $LOG

echo "run vanilla benchmark"
$HASSEL_DIR/net_plumber/Ubuntu-NetPlumber-Release/net_plumber \
    --hdr-len $HDR_LEN \
    --load $VANILLA_DIR \
    --policy $VANILLA_DIR/policy.json > $VANILLA_LOG
cat $VANILLA_LOG >> $LOG

LOAD_VANILLA=`grep "total run time" $VANILLA_LOG | cut -d' ' -f 5`
POLICY_VANILLA=`grep "Loaded policy" $VANILLA_LOG | cut -d' ' -f5`

echo "init: "$(echo $LOAD_VANILLA | awk '{ print $1 / 1000000.0; }')" s"
echo "reach: $POLICY_VANILLA s"
