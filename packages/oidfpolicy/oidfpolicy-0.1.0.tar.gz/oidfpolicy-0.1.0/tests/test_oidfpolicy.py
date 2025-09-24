import json
import os
from pprint import pprint
from unittest import TestCase

from oidfpolicy import *

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

def test_merging_policies():
    self = TestCase()
    self.maxDiff = None
    with open(os.path.join(data_dir, "tapolicy0.json")) as fobj:
        tapolicy = fobj.read()

    with open(os.path.join(data_dir, "iapolicy0.json")) as fobj:
        iapolicy_full = json.load(fobj)

    # Now for mering policies we need to find only the policy part from the
    # whole iapolicy document
    iapolicy = json.dumps(iapolicy_full["metadata_policy"])

    merged = merge_policies(tapolicy, iapolicy)
    data = json.loads(merged)
    with open(os.path.join(data_dir, "policymerge0.json")) as fobj:
        real_merged = json.load(fobj)


    self.assertEqual(real_merged, data)


def test_merging_policies_with_other_types():
    self = TestCase()
    self.maxDiff = None
    with open(os.path.join(data_dir, "tapolicy1.json")) as fobj:
        tapolicy = fobj.read()

    with open(os.path.join(data_dir, "iapolicy1.json")) as fobj:
        iapolicy_full = json.load(fobj)

    iapolicy = json.dumps(iapolicy_full["metadata_policy"])
    merged = merge_policies(tapolicy, iapolicy)
    data = json.loads(merged)
    with open(os.path.join(data_dir, "policymerge1.json")) as fobj:
        real_merged = json.load(fobj)


    self.assertEqual(real_merged, data)


def test_apply_policy():
    self = TestCase()
    self.maxDiff = None

    with open(os.path.join(data_dir, "mergedpolicy0.json")) as fobj:
        merged_policy = fobj.read()

    with open(os.path.join(data_dir, "metadata0.json")) as fobj:
        metadata = fobj.read()


    applied = json.loads(apply_policy(merged_policy, metadata))

    with open(os.path.join(data_dir, "appliedmetadata0.json")) as fobj:
        metadata_from_spec = json.load(fobj)
    self.assertEqual(metadata_from_spec, applied)


