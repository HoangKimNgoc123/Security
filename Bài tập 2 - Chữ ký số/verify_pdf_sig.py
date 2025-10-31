#!/usr/bin/env python3
"""
verify_pdf_sig.py (final stable version)
Verify digital signatures inside PDF.
- Handles malformed /Contents with extra leading or trailing bytes
- Automatically trims ASN.1 DER length
- Fixes shifted ASN.1 (asn1_shifted > 0)
Usage:
  python verify_pdf_sig.py "signed.pdf" > verify_log.json
"""

import sys, json, binascii, hashlib, re
from pathlib import Path
from asn1crypto import cms
from cryptography import x509 as cryptox509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# ------------- helper functions -------------

def read_file_bytes(path: Path) -> bytes:
    with open(path, "rb") as f:
        return f.read()

def find_byteranges(raw: bytes):
    results = []
    idx = 0
    while True:
        i = raw.find(b"/ByteRange", idx)
        if i == -1:
            break
        lb = raw.find(b"[", i)
        rb = raw.find(b"]", lb)
        if lb == -1 or rb == -1:
            idx = i + 1
            continue
        br_text = raw[lb+1:rb]
        nums = re.findall(rb"\d+", br_text)
        if len(nums) == 4:
            results.append((i, [int(n) for n in nums]))
        idx = rb + 1
    return results

def find_contents_near(raw: bytes, bytepos: int, window: int = 20000):
    """Find /Contents near ByteRange"""
    start = max(0, bytepos - window)
    end = min(len(raw), bytepos + window)
    region = raw[start:end]
    cpos = region.find(b"/Contents")
    global_offset = None
    if cpos != -1:
        global_offset = start + cpos
    else:
        cpos = raw.find(b"/Contents")
        if cpos != -1:
            global_offset = cpos
    if global_offset is None:
        return None, None, None
    area = raw[global_offset: global_offset + 200000]
    lt = area.find(b"<")
    gt = area.rfind(b">")
    if lt != -1 and gt != -1 and gt > lt:
        contents_hex = area[lt+1:gt]
        return contents_hex, None, global_offset
    sidx = area.find(b"stream")
    if sidx != -1:
        eidx = area.find(b"endstream", sidx + 6)
        if eidx != -1:
            contents_stream = area[sidx+6:eidx].strip(b"\r\n")
            return None, contents_stream, global_offset
    return None, None, global_offset

def hex_to_bytes_safe(hexbytes: bytes) -> bytes:
    """Convert hex-like bytes (with whitespace/newlines) to binary."""
    cleaned = re.sub(rb'[^0-9A-Fa-f]', b'', hexbytes)
    if len(cleaned) % 2 == 1:
        cleaned += b'0'
    raw = binascii.unhexlify(cleaned)
    return raw.rstrip(b'\x00')  # strip padding nulls

def find_first_asn1_start(sig: bytes):
    """Find first 0x30 (ASN.1 SEQUENCE) near the beginning."""
    if len(sig) >= 2 and sig[0] == 0x30:
        return 0
    for i in range(0, min(1024, len(sig)-1)):
        if sig[i] == 0x30:
            return i
    return 0

def asn1_total_length(buf: bytes, offset: int = 0):
    """Parse ASN.1 length (short/long form)."""
    if offset + 2 > len(buf):
        raise ValueError("not enough bytes for header")
    if buf[offset] != 0x30:
        raise ValueError("not a SEQUENCE at offset")
    lb = buf[offset+1]
    if lb & 0x80 == 0:
        header_len = 2
        content_len = lb & 0x7F
    else:
        n = lb & 0x7F
        if n == 0 or offset + 2 + n > len(buf):
            raise ValueError("invalid length bytes")
        content_len = int.from_bytes(buf[offset+2:offset+2+n], "big")
        header_len = 2 + n
    return header_len + content_len

# ------------- core verifier -------------

def parse_and_verify(pdf_path: str):
    raw = read_file_bytes(Path(pdf_path))
    brs = find_byteranges(raw)
    summary = {"file": str(pdf_path), "candidates": []}
    if not brs:
        summary["error"] = "No /ByteRange found"
        return summary

    for idx, (pos, br) in enumerate(brs):
        entry = {"index": idx, "byterange": br, "checks": {}}
        contents_hex, contents_stream, cpos = find_contents_near(raw, pos)

        # Extract signature bytes
        try:
            if contents_stream is not None:
                sig_bytes = contents_stream
                entry["checks"]["contents_type"] = "stream"
            elif contents_hex is not None:
                sig_bytes = hex_to_bytes_safe(contents_hex)
                entry["checks"]["contents_type"] = "hex"
            else:
                raise ValueError("No /Contents found")
            entry["checks"]["contents_extracted"] = True
            entry["checks"]["contents_len"] = len(sig_bytes)
        except Exception as e:
            entry["checks"]["contents_extracted"] = False
            entry["checks"]["error"] = f"extract error: {e}"
            summary["candidates"].append(entry)
            continue

        # Detect ASN.1 start and shift
        start = find_first_asn1_start(sig_bytes)
        if start != 0:
            entry["checks"]["asn1_shifted"] = start
            sig_bytes = sig_bytes[start:]
            entry["checks"]["asn1_trimmed"] = True

        # Trim to declared DER length
        try:
            total_len = asn1_total_length(sig_bytes, 0)
            if 0 < total_len < len(sig_bytes):
                sig_bytes = sig_bytes[:total_len]
        except Exception as e:
            entry["checks"]["asn1_error"] = str(e)
            with open("sig_extracted.der", "wb") as fw:
                fw.write(sig_bytes)
            entry["checks"]["extract_dump"] = "sig_extracted.der"
            summary["candidates"].append(entry)
            continue

        # Save extracted DER for debug
        try:
            with open("sig_extracted.der", "wb") as fw:
                fw.write(sig_bytes)
            entry["checks"]["extracted_der_written"] = "sig_extracted.der"
        except Exception:
            pass

        # Parse CMS (PKCS#7)
        try:
            ci = cms.ContentInfo.load(sig_bytes)
            if ci['content_type'].native != 'signed_data':
                raise ValueError("Not a signed_data object")
            sd = ci['content']
            entry["checks"]["cms_parsed"] = True
        except Exception as e:
            entry["checks"]["cms_parsed"] = False
            entry["checks"]["error"] = f"CMS parse error: {e}"
            summary["candidates"].append(entry)
            continue

        signer_infos = sd['signer_infos']
        certs = sd['certificates']
        entry["cert_count"] = len(certs) if certs else 0
        if not signer_infos:
            entry["checks"]["signerinfo_present"] = False
            summary["candidates"].append(entry)
            continue

        si = signer_infos[0]
        entry["checks"]["signerinfo_present"] = True
        digest_algo = si['digest_algorithm']['algorithm'].native
        entry["digest_algorithm"] = digest_algo

        # Extract signed attributes
        sattrs = si['signed_attrs'] if 'signed_attrs' in si else None
        if sattrs is None:
            entry["checks"]["signed_attrs"] = False
            summary["candidates"].append(entry)
            continue

        entry["checks"]["signed_attrs"] = True
        md = None
        for a in sattrs:
            if a['type'].native == 'message_digest':
                md = bytes(a['values'][0].native)
                entry["messageDigest"] = md.hex()
            if a['type'].native == 'signing_time':
                entry["signing_time"] = str(a['values'][0].native)

        # Compute hash
        s1, l1, s2, l2 = br
        concat = raw[s1:s1+l1] + raw[s2:s2+l2]
        if digest_algo.startswith('sha512'):
            h = hashlib.sha512(concat).digest(); used = 'sha512'
        else:
            h = hashlib.sha256(concat).digest(); used = 'sha256'
        entry["computed_hash"] = h.hex()
        entry["checks"]["messageDigest_match"] = (md == h)

        # Verify signature
        try:
            sig = si['signature'].native
            sattrs_der = sattrs.dump()
            signer_cert = None
            sid = si['sid']
            if sid.name == 'issuer_and_serial_number':
                serial = sid.chosen['serial_number'].native
                for c in certs:
                    cert = c.chosen
                    if cert.serial_number == serial:
                        signer_cert = cert; break
            if signer_cert is None and certs:
                signer_cert = certs[0].chosen
            if signer_cert is None:
                entry["checks"]["signer_cert_found"] = False
                summary["candidates"].append(entry)
                continue
            entry["checks"]["signer_cert_found"] = True
            cert_obj = cryptox509.load_der_x509_certificate(signer_cert.dump())
            pub = cert_obj.public_key()
            hash_alg = hashes.SHA512() if used == 'sha512' else hashes.SHA256()
            pub.verify(sig, sattrs_der, padding.PKCS1v15(), hash_alg)
            entry["checks"]["signature_verified"] = True
        except Exception as e:
            entry["checks"]["signature_verified"] = False
            entry["checks"]["signature_error"] = str(e)

        # Unsigned attributes (timestamp)
        uattrs = si['unsigned_attrs'] if 'unsigned_attrs' in si else None
        ts_present = False
        if uattrs:
            for a in uattrs:
                if a['type'].dotted == '1.2.840.113549.1.9.16.2.14':
                    ts_present = True
        entry["checks"]["timestamp_present"] = ts_present

        # Detect incremental update
        total_covered = (br[0]+br[1]) + (br[2]+br[3])
        entry["file_len"] = len(raw)
        entry["incremental_update"] = len(raw) > total_covered

        summary["candidates"].append(entry)

    return summary

# ------------- main -------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: verify_pdf_sig.py signed.pdf")
        sys.exit(1)
    pdfp = sys.argv[1]
    res = parse_and_verify(pdfp)
    print(json.dumps(res, indent=2))
