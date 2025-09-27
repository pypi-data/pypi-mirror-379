import json
import os
from datetime import datetime, timedelta, timezone

import pytest

from biscuit_auth import Algorithm, KeyPair, Authorizer, AuthorizerBuilder, Biscuit, BiscuitBuilder, BlockBuilder, Check, Fact, KeyPair, Policy, PrivateKey, PublicKey, Rule, UnverifiedBiscuit

def test_fact():
    fact = Fact('fact(1, true, "", "Test", hex:aabbcc, 2023-04-29T01:00:00Z)')
    assert fact.name == "fact"
    assert fact.terms == [1, True, "", "Test", b'\xaa\xbb\xcc', datetime(2023, 4, 29, 1, 0, 0, tzinfo = timezone.utc)]

def test_biscuit_builder():
    kp = KeyPair()
    pubkey = PublicKey("ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189")

    builder = BiscuitBuilder(
      """
        string({str});
        int({int});
        bool({bool});
        bytes({bytes});
        datetime({datetime});
        set({set});
        array({array});
        map({map});
        check if true trusting {pubkey};
      """,
      { 'str': "1234",
        'int': 1,
        'bool': True,
        'bytes': b'\xaa\xbb',
        'datetime': datetime(2023, 4, 3, 10, 0, 0, tzinfo = timezone.utc),
        'set': {2, True, "Test", datetime(2023, 4, 29, 1, 0, 0, tzinfo = timezone.utc) },
        'array': [2, True, "Test", ["inner"]],
        'map': { 'key': [{12: "value"}]}
      },
      { 'pubkey': pubkey }
    )

    builder.add_fact(Fact("fact(false)"));
    builder.add_fact(Fact("fact({f})", { 'f': True }));
    builder.add_rule(Rule("head($var) <- fact($var, {f})", { 'f': True }));
    builder.add_rule(Rule(
        "head($var) <- fact($var, {f}) trusting {pubkey}",
        { 'f': True },
        { 'pubkey': pubkey }
    ));
    builder.add_check(Check("check if fact($var, {f})", { 'f': True }));
    builder.add_check(Check("check if fact($var, {f}) trusting {pubkey}", { 'f': True }, { 'pubkey': pubkey }));
    builder.merge(BlockBuilder('builder(true);'))

    builder.add_code("add_code(true);")
    builder.add_code("add_code(true, {f});", { 'f': True})
    builder.add_code("check if add_code(true, {f}) trusting {pubkey};", { 'f': True}, { 'pubkey': pubkey })

    assert repr(builder) == """// no root key id set
string("1234");
int(1);
bool(true);
bytes(hex:aabb);
datetime(2023-04-03T10:00:00Z);
set({2, "Test", 2023-04-29T01:00:00Z, true});
array([2, true, "Test", ["inner"]]);
map({"key": [{12: "value"}]});
fact(false);
fact(true);
builder(true);
add_code(true);
add_code(true, true);
head($var) <- fact($var, true);
head($var) <- fact($var, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
check if true trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
check if fact($var, true);
check if fact($var, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
check if add_code(true, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
"""

    builder.build(kp.private_key)
    assert True

def test_block_builder():
    pubkey = PublicKey("ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189")
    builder = BlockBuilder(
      """
        string({str});
        int({int});
        bool({bool});
        bytes({bytes});
        datetime({datetime});
        check if true trusting {pubkey};
      """,
      { 'str': "1234",
        'int': 1,
        'bool': True,
        'bytes': b'\xaa\xbb',
        'datetime': datetime(2023, 4, 3, 10, 0, 0, tzinfo = timezone.utc),
      },
      { 'pubkey': pubkey }
    )

    builder.add_fact(Fact("fact(false)"));
    builder.add_fact(Fact("fact({f})", { 'f': True }));
    builder.add_rule(Rule("head($var) <- fact($var, {f})", { 'f': True }));
    builder.add_rule(Rule(
        "head($var) <- fact($var, {f}) trusting {pubkey}",
        { 'f': True },
        { 'pubkey': pubkey }
    ));
    builder.add_check(Check("check if fact($var, {f})", { 'f': True }));
    builder.add_check(Check("check if fact($var, {f}) trusting {pubkey}", { 'f': True }, { 'pubkey': pubkey }));
    builder.merge(BlockBuilder('builder(true);'))
    builder.add_code("add_code(true);")
    builder.add_code("add_code(true, {f});", { 'f': True})
    builder.add_code("check if add_code(true, {f}) trusting {pubkey};", { 'f': True}, { 'pubkey': pubkey })

    assert repr(builder) == """string("1234");
int(1);
bool(true);
bytes(hex:aabb);
datetime(2023-04-03T10:00:00Z);
fact(false);
fact(true);
builder(true);
add_code(true);
add_code(true, true);
head($var) <- fact($var, true);
head($var) <- fact($var, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
check if true trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
check if fact($var, true);
check if fact($var, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
check if add_code(true, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
"""

def test_authorizer_builder():
    pubkey = PublicKey("ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189")
    builder = AuthorizerBuilder(
      """
        string({str});
        int({int});
        bool({bool});
        bytes({bytes});
        datetime({datetime});
        check if true trusting {pubkey};
        allow if true;
        allow if true trusting {pubkey};
      """,
      { 'str': "1234",
        'int': 1,
        'bool': True,
        'bytes': b'\xaa\xbb',
        'datetime': datetime(2023, 4, 3, 10, 0, 0, tzinfo = timezone.utc),
      },
      { 'pubkey': pubkey }
    )

    builder.add_fact(Fact("fact(false)"));
    builder.add_fact(Fact("fact({f})", { 'f': True }));
    builder.add_rule(Rule("head($var) <- fact($var, {f})", { 'f': True }));
    builder.add_rule(Rule(
        "head($var) <- fact($var, {f}) trusting {pubkey}",
        { 'f': True },
        { 'pubkey': pubkey }
    ));
    builder.add_check(Check("check if fact($var, {f})", { 'f': True }));
    builder.add_check(Check("check if fact($var, {f}) trusting {pubkey}", { 'f': True }, { 'pubkey': pubkey }));
    builder.add_policy(Policy("allow if fact($var, {f})", { 'f': True}))
    builder.add_policy(Policy("allow if fact($var, {f}) trusting {pubkey}", { 'f': True}, { 'pubkey': pubkey }))
    builder.merge_block(BlockBuilder('builder(true);'))
    builder.merge(AuthorizerBuilder('builder(false);'))
    builder.add_code("add_code(true);")
    builder.add_code("add_code(true, {f});", { 'f': True})
    builder.add_code("check if add_code(true, {f}) trusting {pubkey};", { 'f': True}, { 'pubkey': pubkey })

    assert repr(builder) == """string("1234");
int(1);
bool(true);
bytes(hex:aabb);
datetime(2023-04-03T10:00:00Z);
fact(false);
fact(true);
builder(true);
builder(false);
add_code(true);
add_code(true, true);
head($var) <- fact($var, true);
head($var) <- fact($var, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
check if true trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
check if fact($var, true);
check if fact($var, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
check if add_code(true, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
allow if true;
allow if true trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
allow if fact($var, true);
allow if fact($var, true) trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;
"""


def test_authorizer_limits():
    auth = AuthorizerBuilder()
    limits = auth.limits()
    limits.max_time = timedelta(microseconds=2000)
    auth.set_limits(limits)
    limits = auth.limits()
    assert limits.max_time.microseconds == 2000


def test_key_selection():
    private_key = PrivateKey("ed25519-private/473b5189232f3f597b5c2f3f9b0d5e28b1ee4e7cce67ec6b7fbf5984157a6b97")
    root = KeyPair.from_private_key(private_key)
    other_root = KeyPair()

    def choose_key(kid):
        if kid is None:
            return other_root.public_key
        elif kid == 1:
            return root.public_key
        else:
            raise Exception("Unknown key identifier")

    biscuit_builder0 = BiscuitBuilder("user({id})", { 'id': "1234" })
    token0 = biscuit_builder0.build(other_root.private_key).to_base64()
    biscuit_builder1 = BiscuitBuilder("user({id})", { 'id': "1234" })
    biscuit_builder1.set_root_key_id(1)
    token1 = biscuit_builder1.build(private_key).to_base64()
    biscuit_builder2 = BiscuitBuilder("user({id})", { 'id': "1234" })
    biscuit_builder2.set_root_key_id(2)
    token2 = biscuit_builder2.build(private_key).to_base64()


    Biscuit.from_base64(token0, choose_key)
    Biscuit.from_base64(token0, other_root.public_key)
    Biscuit.from_base64(token1, choose_key)
    try:
      Biscuit.from_base64(token2, choose_key)
    except:
      pass

def test_complete_lifecycle():
    private_key = PrivateKey("ed25519-private/473b5189232f3f597b5c2f3f9b0d5e28b1ee4e7cce67ec6b7fbf5984157a6b97")
    root = KeyPair.from_private_key(private_key)

    biscuit_builder = BiscuitBuilder("user({id})", { 'id': "1234" })

    for right in ["read", "write"]:
        biscuit_builder.add_fact(Fact("fact({right})", { 'right': right}))

    token = biscuit_builder.build(private_key).append(BlockBuilder('check if user($u)')).to_base64()

    parsedToken = Biscuit.from_base64(token, root.public_key)

    authorizer = AuthorizerBuilder("allow if user({id})", { 'id': "1234" })

    print(authorizer)
    authorizer = authorizer.build(parsedToken)

    policy = authorizer.authorize()

    assert policy == 0

    rule = Rule("u($id) <- user($id), $id == {id}", { 'id': "1234"})
    facts = authorizer.query(rule)

    assert len(facts) == 1
    assert facts[0].name == "u"
    assert facts[0].terms == ["1234"]

def test_snapshot():
    private_key = PrivateKey("ed25519-private/473b5189232f3f597b5c2f3f9b0d5e28b1ee4e7cce67ec6b7fbf5984157a6b97")
    root = KeyPair.from_private_key(private_key)

    biscuit_builder = BiscuitBuilder("user({id})", { 'id': "1234" })

    for right in ["read", "write"]:
        biscuit_builder.add_fact(Fact("fact({right})", { 'right': right}))

    token = biscuit_builder.build(private_key).append(BlockBuilder('check if user($u)')).to_base64()

    parsedToken = Biscuit.from_base64(token, root.public_key)

    authorizer = AuthorizerBuilder("allow if user({id})", { 'id': "1234" })

    print(authorizer)
    authorizer = authorizer.build(parsedToken)

    snapshot = authorizer.base64_snapshot()
    parsed = Authorizer.from_base64_snapshot(snapshot)
    assert repr(authorizer) == repr(parsed)

    policy = parsed.authorize()

    assert policy == 0

    rule = Rule("u($id) <- user($id), $id == {id}", { 'id': "1234"})
    facts = parsed.query(rule)

    assert len(facts) == 1
    assert facts[0].name == "u"
    assert facts[0].terms == ["1234"]

    raw_snapshot = authorizer.raw_snapshot()
    parsed_from_raw = Authorizer.from_raw_snapshot(raw_snapshot)
    assert repr(authorizer) == repr(parsed_from_raw)

    raw_policy = parsed_from_raw.authorize()

    assert raw_policy == 0

    rule = Rule("u($id) <- user($id), $id == {id}", { 'id': "1234"})
    raw_facts = parsed_from_raw.query(rule)

    assert len(raw_facts) == 1
    assert raw_facts[0].name == "u"
    assert raw_facts[0].terms == ["1234"]

def test_builder_snapshot():
    authorizer = AuthorizerBuilder("allow if user({id})", { 'id': "1234" })

    print(authorizer)

    snapshot = authorizer.base64_snapshot()
    parsed = AuthorizerBuilder.from_base64_snapshot(snapshot)
    assert repr(authorizer) == repr(parsed)

    raw_snapshot = authorizer.raw_snapshot()
    parsed_from_raw = AuthorizerBuilder.from_raw_snapshot(raw_snapshot)
    assert repr(authorizer) == repr(parsed_from_raw)

def test_public_keys():
    # Happy path (hex to bytes and back)
    public_key_from_hex = PublicKey("ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189")
    public_key_bytes = bytes(public_key_from_hex.to_bytes())
    public_key_from_bytes = PublicKey.from_bytes(public_key_bytes, Algorithm.Ed25519)
    assert repr(public_key_from_bytes) == "ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189"

    # Not valid hex
    with pytest.raises(ValueError):
        PublicKey("notarealkey")

    # Valid hex, but too short
    with pytest.raises(ValueError):
        PublicKey("ed25519/deadbeef1234")

    # Not enough bytes
    with pytest.raises(ValueError):
        PublicKey.from_bytes(b"1230fw9ia3", Algorithm.Ed25519)

def test_private_keys():
    # Happy path (hex to bytes and back)
    private_key_from_hex = PrivateKey("ed25519-private/12aca40167fbdd1a11037e9fd440e3d510d9d9dea70a6646aa4aaf84d718d75a")
    private_key_bytes = bytes(private_key_from_hex.to_bytes())
    private_key_from_bytes = PrivateKey.from_bytes(private_key_bytes, Algorithm.Ed25519)
    assert repr(private_key_from_bytes) == "ed25519-private/12aca40167fbdd1a11037e9fd440e3d510d9d9dea70a6646aa4aaf84d718d75a"

    # Not valid hex
    with pytest.raises(ValueError):
        PrivateKey("notarealkey")

    # Valid hex, but too short
    with pytest.raises(ValueError):
        PrivateKey("ed25519-private/deadbeef1234")

    # Not enough bytes
    with pytest.raises(ValueError):
        PrivateKey.from_bytes(b"1230fw9ia3", Algorithm.Ed25519)


def test_biscuit_inspection():
    kp = KeyPair()
    pubkey = PublicKey("ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189")

    builder = BiscuitBuilder(
      """
        test({bool});
        check if true trusting {pubkey};
      """,
      { 'bool': True },
      { 'pubkey': pubkey }
    )

    print(builder)
    token1 = builder.build(kp.private_key)
    print(token1.to_base64())

    builder.set_root_key_id(42)
    token2 = builder.build(kp.private_key).append(BlockBuilder('test(false);'))
    print(token2.to_base64())

    utoken1 = UnverifiedBiscuit.from_base64(token1.to_base64())
    utoken2 = UnverifiedBiscuit.from_base64(token2.to_base64())

    assert utoken1.root_key_id() is None
    assert utoken2.root_key_id() == 42

    assert utoken1.block_count() == 1
    assert utoken2.block_count() == 2

    assert utoken1.block_source(0) == "test(true);\ncheck if true trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;\n"

    assert utoken2.block_source(0) == "test(true);\ncheck if true trusting ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189;\n"
    assert utoken2.block_source(1) == "test(false);\n"

def test_biscuit_revocation_ids():
    public_key = PublicKey("ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189")

    token = Biscuit.from_base64("Ep8BCjUKB3VzZXJfaWQKBWFsaWNlCgVmaWxlMRgDIgoKCAiACBIDGIEIIg4KDAgHEgMYgQgSAxiCCBIkCAASINFHns5iUW6aZiXA0GoqXyrpvFXrquiRGBZjPy3VJPoHGkAC0oew5bIngBkvg1FThYPBf30CAOBksyofzweJnmT_sQ5N4yT1xevHLImmPkJDFyJs9VXrQtroGy_UY5z3WREIGsgBCl4KATAKATEYAyouCgsIBBIDCIMIEgIYABIHCAISAwiDCBIICIAIEgMIhAgSDAgHEgMIhAgSAwiDCDIkCiIKAggbEgcIAhIDCIMIEgYIAxICGAASCwgEEgMIgwgSAhgAEiQIABIg2QCord1Cw30xC2Oea3AuAOPZ2Mvm9-EQmV3zN7zXwQEaQCLnXqIAz3srYrOJKY_g3slzt_nH5U52w8QYEdcuqCxoInvJB5t9BZht4X75MBzM3Aj1AjRVOGmH0ebuQ5GxnwYagwEKGQoFZmlsZTIYAyIOCgwIBxIDGIEIEgMYhQgSJAgAEiAMOoeV68xL1RTh_y4VeK3DUDBP_gnlPSsckzo87Pf7ihpAFAo2Mf7K5VC1HlC5uCK5R_tIXIAHCzRIL6EWzepWAUAWSh0KlZtA_tinJ-L2LAtXY1dgxIjIvw7agO5ZFVjECSIiCiBuSznFYC0NJn8VmDlZmiq1GpBSOERAwHjLZoQJG_24NA==", public_key)
    utoken = UnverifiedBiscuit.from_base64("Ep8BCjUKB3VzZXJfaWQKBWFsaWNlCgVmaWxlMRgDIgoKCAiACBIDGIEIIg4KDAgHEgMYgQgSAxiCCBIkCAASINFHns5iUW6aZiXA0GoqXyrpvFXrquiRGBZjPy3VJPoHGkAC0oew5bIngBkvg1FThYPBf30CAOBksyofzweJnmT_sQ5N4yT1xevHLImmPkJDFyJs9VXrQtroGy_UY5z3WREIGsgBCl4KATAKATEYAyouCgsIBBIDCIMIEgIYABIHCAISAwiDCBIICIAIEgMIhAgSDAgHEgMIhAgSAwiDCDIkCiIKAggbEgcIAhIDCIMIEgYIAxICGAASCwgEEgMIgwgSAhgAEiQIABIg2QCord1Cw30xC2Oea3AuAOPZ2Mvm9-EQmV3zN7zXwQEaQCLnXqIAz3srYrOJKY_g3slzt_nH5U52w8QYEdcuqCxoInvJB5t9BZht4X75MBzM3Aj1AjRVOGmH0ebuQ5GxnwYagwEKGQoFZmlsZTIYAyIOCgwIBxIDGIEIEgMYhQgSJAgAEiAMOoeV68xL1RTh_y4VeK3DUDBP_gnlPSsckzo87Pf7ihpAFAo2Mf7K5VC1HlC5uCK5R_tIXIAHCzRIL6EWzepWAUAWSh0KlZtA_tinJ-L2LAtXY1dgxIjIvw7agO5ZFVjECSIiCiBuSznFYC0NJn8VmDlZmiq1GpBSOERAwHjLZoQJG_24NA==")

    assert token.revocation_ids == [
        "02d287b0e5b22780192f8351538583c17f7d0200e064b32a1fcf07899e64ffb10e4de324f5c5ebc72c89a63e424317226cf555eb42dae81b2fd4639cf7591108",
        "22e75ea200cf7b2b62b389298fe0dec973b7f9c7e54e76c3c41811d72ea82c68227bc9079b7d05986de17ef9301cccdc08f5023455386987d1e6ee4391b19f06",
        "140a3631fecae550b51e50b9b822b947fb485c80070b34482fa116cdea560140164a1d0a959b40fed8a727e2f62c0b57635760c488c8bf0eda80ee591558c409"
    ]
    assert utoken.revocation_ids == [
        "02d287b0e5b22780192f8351538583c17f7d0200e064b32a1fcf07899e64ffb10e4de324f5c5ebc72c89a63e424317226cf555eb42dae81b2fd4639cf7591108",
        "22e75ea200cf7b2b62b389298fe0dec973b7f9c7e54e76c3c41811d72ea82c68227bc9079b7d05986de17ef9301cccdc08f5023455386987d1e6ee4391b19f06",
        "140a3631fecae550b51e50b9b822b947fb485c80070b34482fa116cdea560140164a1d0a959b40fed8a727e2f62c0b57635760c488c8bf0eda80ee591558c409"
    ]

def test_unverified_biscuit_signature_check():
    public_key = PublicKey("ed25519/acdd6d5b53bfee478bf689f8e012fe7988bf755e3d7c5152947abc149bc20189")

    utoken = UnverifiedBiscuit.from_base64("Ep8BCjUKB3VzZXJfaWQKBWFsaWNlCgVmaWxlMRgDIgoKCAiACBIDGIEIIg4KDAgHEgMYgQgSAxiCCBIkCAASINFHns5iUW6aZiXA0GoqXyrpvFXrquiRGBZjPy3VJPoHGkAC0oew5bIngBkvg1FThYPBf30CAOBksyofzweJnmT_sQ5N4yT1xevHLImmPkJDFyJs9VXrQtroGy_UY5z3WREIGsgBCl4KATAKATEYAyouCgsIBBIDCIMIEgIYABIHCAISAwiDCBIICIAIEgMIhAgSDAgHEgMIhAgSAwiDCDIkCiIKAggbEgcIAhIDCIMIEgYIAxICGAASCwgEEgMIgwgSAhgAEiQIABIg2QCord1Cw30xC2Oea3AuAOPZ2Mvm9-EQmV3zN7zXwQEaQCLnXqIAz3srYrOJKY_g3slzt_nH5U52w8QYEdcuqCxoInvJB5t9BZht4X75MBzM3Aj1AjRVOGmH0ebuQ5GxnwYagwEKGQoFZmlsZTIYAyIOCgwIBxIDGIEIEgMYhQgSJAgAEiAMOoeV68xL1RTh_y4VeK3DUDBP_gnlPSsckzo87Pf7ihpAFAo2Mf7K5VC1HlC5uCK5R_tIXIAHCzRIL6EWzepWAUAWSh0KlZtA_tinJ-L2LAtXY1dgxIjIvw7agO5ZFVjECSIiCiBuSznFYC0NJn8VmDlZmiq1GpBSOERAwHjLZoQJG_24NA==")

    utoken.verify(public_key)

def test_append_on_unverified():
    utoken = UnverifiedBiscuit.from_base64("Ep8BCjUKB3VzZXJfaWQKBWFsaWNlCgVmaWxlMRgDIgoKCAiACBIDGIEIIg4KDAgHEgMYgQgSAxiCCBIkCAASINFHns5iUW6aZiXA0GoqXyrpvFXrquiRGBZjPy3VJPoHGkAC0oew5bIngBkvg1FThYPBf30CAOBksyofzweJnmT_sQ5N4yT1xevHLImmPkJDFyJs9VXrQtroGy_UY5z3WREIGsgBCl4KATAKATEYAyouCgsIBBIDCIMIEgIYABIHCAISAwiDCBIICIAIEgMIhAgSDAgHEgMIhAgSAwiDCDIkCiIKAggbEgcIAhIDCIMIEgYIAxICGAASCwgEEgMIgwgSAhgAEiQIABIg2QCord1Cw30xC2Oea3AuAOPZ2Mvm9-EQmV3zN7zXwQEaQCLnXqIAz3srYrOJKY_g3slzt_nH5U52w8QYEdcuqCxoInvJB5t9BZht4X75MBzM3Aj1AjRVOGmH0ebuQ5GxnwYagwEKGQoFZmlsZTIYAyIOCgwIBxIDGIEIEgMYhQgSJAgAEiAMOoeV68xL1RTh_y4VeK3DUDBP_gnlPSsckzo87Pf7ihpAFAo2Mf7K5VC1HlC5uCK5R_tIXIAHCzRIL6EWzepWAUAWSh0KlZtA_tinJ-L2LAtXY1dgxIjIvw7agO5ZFVjECSIiCiBuSznFYC0NJn8VmDlZmiq1GpBSOERAwHjLZoQJG_24NA==")

    utoken2 = utoken.append(BlockBuilder("check if true"))
    assert utoken2.block_source(3) == "check if true;\n"


def test_keypair_from_private_key_der():
    private_key_der = bytes.fromhex("302e020100300506032b6570042204200499694d0da05dcac40052663e71d50c1539465f8926dfe92033cf7aaad53d65")
    private_key_hex = "ed25519-private/0499694d0da05dcac40052663e71d50c1539465f8926dfe92033cf7aaad53d65"
    kp = KeyPair.from_private_key(PrivateKey.from_der(der=private_key_der))
    assert repr(kp.private_key) == private_key_hex


def test_keypair_from_private_key_pem():
    private_key_pem = "-----BEGIN PRIVATE KEY-----\nMC4CAQAwBQYDK2VwBCIEIASZaU0NoF3KxABSZj5x1QwVOUZfiSbf6SAzz3qq1T1l\n-----END PRIVATE KEY-----"
    private_key_hex = "ed25519-private/0499694d0da05dcac40052663e71d50c1539465f8926dfe92033cf7aaad53d65"
    kp = KeyPair.from_private_key(PrivateKey.from_pem(pem=private_key_pem))
    assert repr(kp.private_key) == private_key_hex

def test_extern_func():
    def test(left, right):
        if left == right:
            return True
        else:
            return False

    authorizer = AuthorizerBuilder("""
    check if 2.extern::other();
    allow if 1.extern::test(1);
    """)
    authorizer.register_extern_funcs({
      'test': test,
      'other': lambda x : x == 2,
    })
    policy = authorizer.build_unauthenticated().authorize()
    assert policy == 0

def test_append_third_party():
    root_kp = KeyPair()
    biscuit_builder = BiscuitBuilder("user({id})", { 'id': "1234" })
    biscuit = biscuit_builder.build(root_kp.private_key)

    third_party_kp = KeyPair()
    new_block = BlockBuilder("external_fact({fact})", { 'fact': "56" })
    third_party_request = biscuit.third_party_request()
    third_party_block = third_party_request.create_block(third_party_kp.private_key, new_block)
    biscuit_with_third_party_block = biscuit.append_third_party(third_party_kp.public_key, third_party_block)

    assert repr(biscuit_with_third_party_block.block_external_key(1)) == repr(third_party_kp.public_key)

def test_read_third_party_facts():
    root_kp = KeyPair()
    biscuit_builder = BiscuitBuilder("user({id})", { 'id': "1234" })
    biscuit = biscuit_builder.build(root_kp.private_key)

    third_party_kp = KeyPair()
    new_block = BlockBuilder("external_fact({fact})", { 'fact': "56" })
    third_party_request = biscuit.third_party_request()
    third_party_block = third_party_request.create_block(third_party_kp.private_key, new_block)
    biscuit_with_third_party_block = biscuit.append_third_party(third_party_kp.public_key, third_party_block)


    authorizer  = AuthorizerBuilder("allow if true").build(biscuit_with_third_party_block)
    rule = Rule(f"ext_fact($fact) <- external_fact($fact) trusting {third_party_kp.public_key}")
    facts = authorizer.query(rule)

    assert facts[0].terms[0] == "56"
