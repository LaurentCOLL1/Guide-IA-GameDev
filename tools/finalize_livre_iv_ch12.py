#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
payload_root = ROOT / ".chapter12"


def read_verified(path: str, expected: str) -> bytes:
    data = (payload_root / path).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected:
        raise SystemExit(f"Invalid {path} SHA: {actual}")
    return data


def join_verified(name: str, pieces: list[bytes], expected: str) -> bytes:
    rebuilt = b"".join(pieces)
    actual = hashlib.sha256(rebuilt).hexdigest()
    if actual != expected:
        raise SystemExit(f"Invalid rebuilt {name} SHA: {actual}")
    return rebuilt


def write_verified(name: str, pieces: list[bytes], expected: str) -> None:
    (payload_root / name).write_bytes(join_verified(name, pieces, expected))


def rebuild_b64_from_zlib(number: int, sha_a: str, sha_b: str, raw_sha: str, file_sha: str) -> None:
    raw = join_verified(
        f"ch12.{number:02d}.zlib",
        [
            read_verified(f"ch12.{number:02d}a.zlib", sha_a),
            read_verified(f"ch12.{number:02d}b.zlib", sha_b),
        ],
        raw_sha,
    )
    encoded = base64.b64encode(raw) + b"\n"
    actual = hashlib.sha256(encoded).hexdigest()
    if actual != file_sha:
        raise SystemExit(f"Invalid rebuilt ch12.{number:02d}.b64 SHA: {actual}")
    (payload_root / f"ch12.{number:02d}.b64").write_bytes(encoded)


write_verified(
    "ch12.02.b64",
    [
        read_verified("ch12.02a.part", "7c52b06aa85c0c6d27df8f952607eba6fb0df47b7d87bf30539f24aae9594e7e"),
        read_verified("ch12.02b.part", "20e323e178fa73878ab3342e68b02e674f9dee9d3b70345d6ec8546f996daa54"),
    ],
    "b862e7677f3473db558d55a5d1525743908d7cfd5f31dadb745f634168d0724f",
)
part_05b2 = join_verified(
    "ch12.05b2.part",
    [
        read_verified("ch12.05b2a.part", "e93e18d710edd28f39837552894661d1b39f6d019926bde58727a2ca38d9c7bc"),
        read_verified("ch12.05b2b.part", "1d3e12a4b7cb2865792bf7741d59275aa96ab763e93d9361a3b0b12e5aaed633"),
    ],
    "8e91300553112c785b4164bb863caba7485e08306159ef3622142d90ee0d8350",
)
part_05b = join_verified(
    "ch12.05b.part",
    [
        read_verified("ch12.05b1.part", "3a6f2af217f681cfcc8e3093cae37278280c501b6e3cebe05e96dd687952cc70"),
        part_05b2,
    ],
    "b6cd26f972c695151c3e6f9cb4534bf8219eb9b8f05e6c2d503020ab7816c7fe",
)
write_verified(
    "ch12.05.b64",
    [
        read_verified("ch12.05a.part", "9b556fee380d448b1d8b02f9cf1f0ae988d252a12bc1b4d6e9b8488d12949f3e"),
        part_05b,
    ],
    "6feb990c0a886287e5e950773274a7fc913c2a5712865b31be062723304d2e7a",
)

binary_payloads = {
    6: ("fa89c32e743665770ecdeba07ffee4299469fb30c6853d74e1a2cb418830b2b3", "31848a931ee9e32801bf917948bdffcc7d73cdcfbc271d61802af4fe8b8e27ee", "b4e923ce1f70f25f9bf644934e68806ea1656800101ad3ec46cb6ceedc324e2d", "b553cb14d497219d9ac5d061a536be9b84bdda9f8fed304e907e86b424a791ea"),
    7: ("844a6092bd8e8be2df49efe4d277c3a4d85b791750fc80826bc1cef5882f1d6f", "689d6566d029676c0f6017049803752561eccee2e81b87714709ed71d41a0d37", "cc19ecaf0e1c9c93f0a4f0df8b8103f49dcc60854556f9b5741d75836bd8a01b", "a2aa82dd05dd767b4cab0373ffb52a5fee5787268067e3871a5ba5cd8118133f"),
    8: ("8ba6ae2dbc607276543d29dfd73d8db2ce36ca8c2ec062a92ea4619bb4f32db2", "c20955964df0aa5a7cf9d163c02f7620de9948442b41c955327a791f728a577c", "feca927fb25caf797a60b10f874dd1a1a223501402a5b4c56ea67d63a50f8449", "04f744a9fdb2f5d74a30ee289f00411ef51fe8e9de5c5fb83e132cd964d521c7"),
    9: ("0a077bc2be8a9bd1dc134fcd4cba1d7cecc34765cc7f94e44c8af29f865f8a45", "73ad6c1f8af5a4734c5e7856b57701759f80089234dc3dc5827550de5fa14c6b", "94e09afc7b3aff08d41e7084f101f3f11ade192989e2805ab1d3f2f8b0f8d3c0", "0303a258b447792297ba02a91fb09975b25fdbfa32e16feb772fef80710547fe"),
    10: ("854d2b5096f485dfcba278f4f132a19a95d26f3386e7484a1e2f4dd185b917e0", "7ce500b3538315f9ee49c39abf9a36f7f690be48b3fdda8fb956ad35dea00247", "3dc6e98d621b331da27c465a46afd9d609335c0cea3b0951c5e4a4733accdcb3", "cbb5414e2a9f5f2864d5f1c11e0d83cb957e21ce6f851608e1035fdcb2a0d1ce"),
    11: ("6e6c50a7968beb8209d03b3391f6944698bb4bbcc0d4538dfa33bb345f8dba9c", "7a706aee0f313c90b61b7516ec90121316dd81e192a9fe7cf3d7ff0ba2c7b058", "a8fa38fc615c0757ab3e8ef8135cb1b5cf4c0dc28730c1d0fc8984f51750c1fb", "3ad0b2829db2d7707224272e2ccc22c374cee318dcb8698541dee460014fb588"),
    12: ("8a6ea1e82451a416c91732de768d198c5129b3767068cb19cfd4555b3d97b28c", "844da7600113571a770349da129b3ab00cd9e5480965e78da12acd25fe1422e8", "dbadaeb98ad803337164ea061267b63b74f40ca5ec25041d35051cb814e573f8", "a2aadacb4322db38efbbd7b681414b8436c1fab6b02d510cd5f5f19b252c1e01"),
}
for number, values in binary_payloads.items():
    rebuild_b64_from_zlib(number, *values)

parts: list[bytes] = []
for path in sorted(payload_root.glob("finalizer.*.b64")):
    parts.append(zlib.decompress(base64.b64decode(path.read_bytes())))
source = b"".join(parts)
expected = "d42a4b126d44bb60821fa9eb9d4ec30d0f33319ff37a6bc70b149b46a8d7944b"
actual = hashlib.sha256(source).hexdigest()
if actual != expected:
    raise SystemExit(f"Finalizer SHA mismatch: {actual}")
exec(
    compile(source, str(Path(__file__)), "exec"),
    {"__name__": "__main__", "__file__": str(Path(__file__))},
)
