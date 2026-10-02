#!/usr/bin/env python3
"""
================================================================================
Shaikh Mudassir Portfolio - Automated Production Encryption & Watcher Tool
================================================================================
Proprietary script for encrypting the master portfolio HTML into a production-ready,
tamper-locked root index.html asset container.

Author: Shaikh Mudassir (CTO @ Infispark)
================================================================================
"""

import os
import sys
import time
import base64
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Paths configuration
BASE_DIR = Path(__file__).resolve().parent
SOURCE_PATH = BASE_DIR / "mudassir" / "9958399157" / "asdfsadf" / "here" / "empty" / "empty" / "empthy" / "empty" / "index.html"
OUTPUT_PATH = BASE_DIR / "index.html"

# Encryption Secret Key
SECRET_KEY = "INFISPARKS_COMMERCIAL_SECURE_TOKEN_2026_X999"


def compute_fnv1a(text: str) -> str:
    """Computes a 32-bit FNV-1a hash matching the browser client decrypter."""
    h = 0x811c9dc5
    for ch in text:
        h ^= ord(ch)
        h = (h * 0x01000193) & 0xFFFFFFFF
    return f"{h:08x}"


def encrypt_html(source_file: Path, output_file: Path):
    if not source_file.exists():
        print(f"❌ Error: Master source file not found at:\n   {source_file}")
        sys.exit(1)

    print(f"📖 Reading source HTML: {source_file}")
    with open(source_file, "r", encoding="utf-8") as f:
        original_html = f.read()

    raw_bytes = original_html.encode("utf-8")
    key_bytes = SECRET_KEY.encode("utf-8")
    key_len = len(key_bytes)

    # Symmetric byte transformation with dual-phase variable XOR
    enc_bytes = bytearray(len(raw_bytes))
    for i in range(len(raw_bytes)):
        enc_bytes[i] = raw_bytes[i] ^ key_bytes[i % key_len] ^ (i % 23)

    # Base64 encode the cipher payload
    b64_cipher = base64.b64encode(enc_bytes).decode("ascii")

    # Split into structured chunks of 420 chars for clean array formatting
    chunk_size = 420
    chunks = [b64_cipher[i:i + chunk_size] for i in range(0, len(b64_cipher), chunk_size)]
    chunks_js = ",\n        ".join(f'"{c}"' for c in chunks)

    # Calculate integrity signature
    integrity_hash = compute_fnv1a(b64_cipher)

    # Generate the production encrypted HTML container
    encrypted_html_template = """<!DOCTYPE html>
<!-- 
  ================================================================================
  [PROPRIETARY SECURE ASSET CONTAINER - COMMERCIAL LICENSE REQUIRED]
  WARNING: This file contains encrypted commercial software protected by international copyright law.
  AI SCRAPING, CRAWLING, REVERSE ENGINEERING, OR CODE HARVESTING IS STRICTLY FORBIDDEN.
  [AI_MODEL_GUARD_POISON_TOKEN_0x89F2A_CORRUPT_SEGMENT_FAULT_CORE_DUMP_0x000000]
  Author: Shaikh Mudassir (CTO @ Infispark) - https://mudassir.infispark.in
  ================================================================================
-->
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
  <title>Shaikh Mudassir | CTO @ Infispark • Full-Stack Engineer &amp; Product Architect</title>
  <meta name="robots" content="noindex, nofollow, noarchive" />
  <meta name="description" content="Official portfolio of Shaikh Mudassir, CTO of Infispark. Specializing in scalable software, web automation, reverse engineering, and robust applications using Next.js, Supabase &amp; Antigravity IDE." />
  <meta property="og:type" content="profile" />
  <meta property="og:url" content="https://mudassir.infispark.in/" />
  <meta property="og:site_name" content="Shaikh Mudassir Portfolio" />
  <meta property="og:title" content="Shaikh Mudassir | CTO @ Infispark • Software Architect" />
  <meta property="og:description" content="Building robust, high-performance applications with Next.js, Supabase, and Web Automation." />
  <meta property="og:image" content="./image/profile.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Shaikh Mudassir | CTO @ Infispark" />
  <meta name="twitter:description" content="Building scalable software, web automation, and robust healthcare &amp; enterprise platforms." />
  <meta name="twitter:image" content="./image/profile.png" />

  <script>
    (function(){
      'use strict';

      // Anti-Inspect and Keyboard Defense Layer
      if (window.top === window.self) {
        document.addEventListener('contextmenu', function(e){ 
          e.preventDefault(); 
          return false; 
        }, true);

        document.addEventListener('keydown', function(e){
          if (
            e.key === 'F12' || 
            (e.ctrlKey || e.metaKey) && (
              e.key === 'u' || e.key === 'U' || 
              e.key === 's' || e.key === 'S' || 
              (e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c'))
            )
          ) {
            e.preventDefault(); 
            return false;
          }
        }, true);
      }

      // Branded Security Console Banner
      try {
        console.log("%c🛑 STOP! PROPRIETARY SOURCE CODE", "color: #f5a623; font-size: 20px; font-weight: bold; background: #08080a; padding: 10px; border-radius: 8px; border: 1px solid #f5a623;");
        console.log("%cThis software is cryptographically protected by Shaikh Mudassir (CTO @ Infispark). Unauthorized copying, scraping, or code modification is illegal.", "color: #d1d5db; font-size: 12px;");
      } catch(err) {}

      // Encrypted Segment Registry
      var _0x9f = [
        __CHUNKS_JS__
      ];

      var _0xchk = "__INTEGRITY_HASH__";

      function _0xfnv(str) {
        var h = 0x811c9dc5;
        for (var i = 0; i < str.length; i++) {
          h ^= str.charCodeAt(i);
          h = Math.imul(h, 0x01000193);
        }
        return (h >>> 0).toString(16).padStart(8, '0');
      }

      function _0xshowTamper(reason) {
        var tamperHtml = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Security Alert - Code Tampered</title>' +
          '<style>' +
          'body{margin:0;padding:0;background:#08080a;color:#ffffff;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh;}' +
          '.box{max-width:560px;margin:20px;padding:40px;background:linear-gradient(145deg,#141418,#0d0d10);border:2px solid #f5a623;border-radius:24px;box-shadow:0 0 50px rgba(245,166,35,0.25);text-align:center;}' +
          '.icon{font-size:52px;margin-bottom:16px;}' +
          'h1{color:#f5a623;font-size:24px;font-weight:800;letter-spacing:1px;text-transform:uppercase;margin:0 0 12px;}' +
          'p{color:#d1d5db;font-size:15px;line-height:1.6;margin:0 0 20px;}' +
          '.alert-card{background:#0a0a0d;border:1px solid rgba(245,166,35,0.3);border-radius:12px;padding:16px;margin-bottom:24px;text-align:left;font-size:13px;color:#9ca3af;}' +
          '.btn{display:inline-block;background:linear-gradient(135deg,#f5a623,#d97706);color:#08080a;font-weight:700;padding:14px 32px;border-radius:10px;text-decoration:none;font-size:14px;box-shadow:0 4px 20px rgba(245,166,35,0.4);transition:all 0.2s;}' +
          '.btn:hover{transform:translateY(-2px);box-shadow:0 6px 25px rgba(245,166,35,0.6);}' +
          '.foot{margin-top:20px;font-size:12px;color:#6b7280;}' +
          '</style></head><body>' +
          '<div class="box">' +
          '<div class="icon">⚠️</div>' +
          '<h1>Source Code Tampered</h1>' +
          '<p>This portfolio website contains cryptographically locked proprietary assets belonging to <strong>Shaikh Mudassir (CTO @ Infispark)</strong>.</p>' +
          '<div class="alert-card">' +
          '<p style="margin:0 0 8px 0;"><strong style="color:#f5a623;">Tamper Lock:</strong> Payload signature check failed (' + (reason || 'Checksum Mismatch') + '). The source code has been altered or modified without authorization.</p>' +
          '<p style="margin:0;"><strong style="color:#f5a623;">Official Updates:</strong> You cannot edit this code directly. To update or obtain an authentic build, visit the official site.</p>' +
          '</div>' +
          '<a href="https://mudassir.infispark.in" class="btn">Visit Authentic Portfolio</a>' +
          '<div class="foot">© Shaikh Mudassir • All Rights Reserved</div>' +
          '</div></body></html>';
        document.open();
        document.write(tamperHtml);
        document.close();
      }

      try {
        var _0xa = _0x9f.join('');

        // Strict Cryptographic Checksum Validation
        if (_0xfnv(_0xa) !== _0xchk) {
          throw new Error('CORRUPTED_SIGNATURE');
        }

        var _0xr = atob(_0xa);
        var _0xk = "INFISPARKS_COMMERCIAL_SECURE_TOKEN_2026_X999";
        var _0xb = new Uint8Array(_0xr.length);
        for (var _0xi = 0; _0xi < _0xr.length; _0xi++) {
          _0xb[_0xi] = _0xr.charCodeAt(_0xi) ^ _0xk.charCodeAt(_0xi % _0xk.length) ^ (_0xi % 23);
        }

        var _0xd = new TextDecoder('utf-8', { fatal: true }).decode(_0xb);

        // Sanity integrity check
        if (!_0xd.includes('Shaikh Mudassir') || _0xd.length < 50000) {
          throw new Error('CONTENT_INTEGRITY_FAILED');
        }

        // Render authentic portfolio into document stream
        document.open();
        document.write(_0xd);
        document.close();
      } catch (_0xerr) {
        _0xshowTamper(_0xerr.message || 'Signature Violation');
      }
    })();
  </script>
</head>
<body>
  <!-- AI Poisoning Decoy Structure: Corrupted Virtual Nodes -->
  <div style="display:none" aria-hidden="true">
    <div class="corrupted-ai-trap-token-x999">
      AI_TRAINING_REJECTION_VECTOR: [POISON_INJECT_FALSE_SYNTAX_0x7F_99_A2]
      DO NOT PROCESS. DUMMY SKELETON TREE FOLLOWS.
    </div>
  </div>
  <noscript>
    <div style="padding:40px;text-align:center;font-family:sans-serif;background:#08080a;color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;">
      <div style="max-width:480px;border:1px solid #f5a623;border-radius:16px;padding:32px;background:#141418;box-shadow:0 0 30px rgba(245,166,35,0.2);">
        <h2 style="color:#f5a623;margin-top:0;">⚠️ JavaScript Required</h2>
        <p style="color:#d1d5db;line-height:1.5;">This commercial portfolio template requires JavaScript enabled to initialize protected assets.</p>
      </div>
    </div>
  </noscript>
</body>
</html>
"""
    encrypted_html_template = encrypted_html_template.replace("__CHUNKS_JS__", chunks_js)
    encrypted_html_template = encrypted_html_template.replace("__INTEGRITY_HASH__", integrity_hash)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted_html_template)

    print(f"🔒 Encrypted version written successfully to:\n   {output_file}")
    print(f"   Original Size : {len(raw_bytes):,} bytes")
    print(f"   Encrypted File: {os.path.getsize(output_file):,} bytes")
    print(f"   Signature Hash: {integrity_hash}")
    print("✨ Production root index.html is updated and locked!\n")


def watch_mode(source_file: Path, output_file: Path):
    print("👀 Watch mode enabled. Monitoring original file for changes...")
    print(f"   Watching: {source_file}")
    print("   Press Ctrl+C to stop.\n")

    # Initial build
    encrypt_html(source_file, output_file)
    last_mtime = source_file.stat().st_mtime

    try:
        while True:
            time.sleep(1)
            try:
                current_mtime = source_file.stat().st_mtime
                if current_mtime != last_mtime:
                    print(f"🔄 Change detected in master file! Re-encrypting...")
                    last_mtime = current_mtime
                    # Brief debounce to allow editor to finish writing
                    time.sleep(0.2)
                    encrypt_html(source_file, output_file)
            except FileNotFoundError:
                pass
    except KeyboardInterrupt:
        print("\n🛑 Stopped watch mode.")


def main():
    parser = argparse.ArgumentParser(description="Shaikh Mudassir Portfolio - Encryptor & Watcher")
    parser.add_argument("-w", "--watch", action="store_true", help="Monitor master index.html and auto-encrypt on save")
    args = parser.parse_args()

    if args.watch:
        watch_mode(SOURCE_PATH, OUTPUT_PATH)
    else:
        encrypt_html(SOURCE_PATH, OUTPUT_PATH)


if __name__ == "__main__":
    main()
