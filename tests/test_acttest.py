#!/usr/bin/python3
import pytest


def test_doc_hashes(scenario):
    s = scenario

    # Register a security generator
    s.contract_acttest.registerSecurityGenerator(s.acc_security_generator1, {"from": s.acc_admin})

    # Add a document
    doc_hash1 = b'!\x07\xb1~\x93BZ\x03*\x12\x0f\xf9\x1f\x8a\x10\xc0\x10\xbd\x96\x13L\x9a\x81J\xa4=\x0e/\n\xa3\xf9e';
    s.contract_acttest.addDocHash(doc_hash1, {"from": s.acc_security_generator1})
    s.contract_acttest.removeDocHash(doc_hash1, {"from": s.acc_security_generator1})

    with pytest.raises(Exception):
        s.contract_acttest.addDocHash(doc_hash1, {"from": s.acc_security_owner1})

    with pytest.raises(Exception):
        s.contract_acttest.removeDocHash(doc_hash1, {"from": s.acc_security_owner1})
