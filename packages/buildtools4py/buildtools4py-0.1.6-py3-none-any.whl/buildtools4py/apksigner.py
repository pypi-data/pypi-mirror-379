# SPDX-FileCopyrightText: 2025 Michael Pöhn <michael@poehn.at>
# SPDX-License-Identifier: Apache-2.0


"""Wrapper for apksinger from Android build-tools."""


import re
import pathlib
import subprocess
import dataclasses
from typing import Dict, List, Optional, Union

import buildtools4py


@dataclasses.dataclass
class SignerData:
    """Fingerprints of signatures, public keys, etc."""

    public_key_sha256: Optional[str] = None
    certificate_sha256: Optional[str] = None


@dataclasses.dataclass
class ApkSignerData:
    """Verification data of an APK."""

    verifies: Optional[bool] = None
    v1_verified: Optional[bool] = None
    v2_verified: Optional[bool] = None
    v3_verified: Optional[bool] = None
    v31_verified: Optional[bool] = None
    v4_verified: Optional[bool] = None
    source_stamp_verified: Optional[bool] = None
    number_of_signers: Optional[int] = None
    error: Optional[str] = None
    signers: List[SignerData] = dataclasses.field(default_factory=list)


_REGEXCACHE: Dict[str, re.Pattern] = {}


def _re_parse(regex, string):
    r = _REGEXCACHE.get(regex)
    if not r:
        r = re.compile(regex)
        _REGEXCACHE[regex] = r
    m = r.match(string)
    if m:
        return m.group(1)
    return None


def _specific_bin_lookup(
    bin_name: str, specific_path: Optional[Union[str, pathlib.Path]] = None
) -> pathlib.Path:
    bin_path = (
        buildtools4py.lookup_buildtools_bin(bin_name)
        if specific_path is None
        else pathlib.Path(specific_path)
    )
    if bin_path is None or not bin_path.is_file():
        raise FileNotFoundError(
            f"Could not find '{bin_name}' please make sure it's installed (e.g. sdkmanager 'build-tools;36.0.0')"
        )
    return bin_path


REQUIRED_APKSIGNER_VERSION = "0.9"


def apksigner_version_outdated(
    apksigner_path: Optional[Union[str, pathlib.Path]] = None,
) -> bool:
    """Check if apksigner is older than REQUIRED_APKSIGNER_VERSION (>= {})."""
    apksigner = _specific_bin_lookup("apksigner", specific_path=apksigner_path)
    cmd = [str(apksigner), "--version"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 0:
        v = buildtools4py.Ver(r.stdout.strip())
        if v >= buildtools4py.Ver(REQUIRED_APKSIGNER_VERSION):
            return False
    return True


apksigner_version_outdated.__doc__ = apksigner_version_outdated.__doc__.format(  # type: ignore[union-attr]
    REQUIRED_APKSIGNER_VERSION
)


def apksigner_verify(
    apk_path: Union[str, pathlib.Path],
    apksigner_path: Optional[Union[str, pathlib.Path]] = None,
    min_sdk: Optional[int] = None,
    max_sdk: Optional[int] = None,
) -> ApkSignerData:
    """Get output from apksigner verify call."""
    apksigner = _specific_bin_lookup("apksigner", specific_path=apksigner_path)
    if not pathlib.Path(apk_path).is_file():
        raise FileNotFoundError(f"Could not find '{apk_path}'.")

    cmd = [str(apksigner), "verify", "--verbose", "--print-certs"]
    if min_sdk is not None:
        cmd += ["--min-sdk-version", str(min_sdk)]
    if max_sdk is not None:
        cmd += ["--max-sdk-version", str(max_sdk)]
    cmd.append(str(apk_path))

    r = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    if r.returncode == 0:
        return parse_apksigner_output(r.stdout, stderr=r.stderr)
    else:
        return ApkSignerData(error=r.stderr)


def parse_apksigner_output(
    apksigner_output: str, stderr: Optional[str] = None
) -> ApkSignerData:
    """Parse apksigner verify output into python data class."""
    result = ApkSignerData()
    signer_data = None  # SignerData()

    lines = apksigner_output.split("\n")
    result.verifies = len(lines) > 0 and lines[0] == "Verifies"

    for line in [line.lower() for line in lines[1:]]:
        verified_v1 = _re_parse(
            r"^verified using v1 scheme \(jar signing\): (true|false)$", line
        )
        if verified_v1:
            result.v1_verified = verified_v1 == "true"

        verified_v2 = _re_parse(
            r"^verified using v2 scheme \(apk signature scheme v2\): (true|false)$",
            line,
        )
        if verified_v2:
            result.v2_verified = verified_v2 == "true"

        verified_v3 = _re_parse(
            r"^verified using v3 scheme \(apk signature scheme v3\): (true|false)$",
            line,
        )
        if verified_v3:
            result.v3_verified = verified_v3 == "true"

        verified_v31 = _re_parse(
            r"^verified using v3.1 scheme \(apk signature scheme v3.1\): (true|false)$",
            line,
        )
        if verified_v31:
            result.v31_verified = verified_v31 == "true"

        verified_v4 = _re_parse(
            r"^verified using v4 scheme \(apk signature scheme v4\): (true|false)$",
            line,
        )
        if verified_v4:
            result.v4_verified = verified_v4 == "true"

        source_stamp_verified = _re_parse(
            r"^verified for sourcestamp: (false|true)$", line
        )
        if source_stamp_verified:
            result.source_stamp_verified = source_stamp_verified == "true"

        number_of_signer = _re_parse(r"^number of signers: ([0-9]+)$", line)
        if number_of_signer:
            result.number_of_signers = int(number_of_signer)

        if line.startswith("signer "):
            cert_sha256 = _re_parse(
                r"signer .* certificate sha-256 digest: ([a-f0-9]{64})",
                line,
            )
            if cert_sha256:
                if signer_data is None or signer_data.certificate_sha256:
                    signer_data = SignerData()
                    result.signers.append(signer_data)
                signer_data.certificate_sha256 = cert_sha256

            pubkey_sha256 = _re_parse(
                r"signer .* public key sha-256 digest: ([a-f0-9]{64})", line
            )
            if pubkey_sha256:
                if signer_data is None or signer_data.public_key_sha256:
                    signer_data = SignerData()
                    result.signers.append(signer_data)
                signer_data.public_key_sha256 = pubkey_sha256

    # if signer_data.public_key_sha256:
    #     result.signers.append(signer_data)

    if stderr:
        result.error = stderr

    return result
