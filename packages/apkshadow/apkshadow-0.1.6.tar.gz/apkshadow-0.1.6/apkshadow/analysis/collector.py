from apkshadow.actions import decompile as decompile_action
from apkshadow.actions import pull as pull_action
from apkshadow.analysis.finding import Finding
from apkshadow.parser import Parser
import apkshadow.globals as GLOBALS
import apkshadow.filters as filters
import apkshadow.utils as utils
from tqdm import tqdm
import tempfile
import os


def filterNonClaimedPermissions(source_directory, findings):
    """Filter which custom permissions are not declared in any manifest in source_directory.

    Args:
        source_directory (str): Path to a directory containing APKs.
        findings (list[Finding]): List of Finding objects with 'custom' permissions.

    Returns:
        list[Finding]: Findings with un-declared custom permissions and upgraded to critical risk.
    """
    pkg_dirs = filters.getFilteredDirectories(None, source_directory, False)
    declared_perms = {}

    for pkg_path, _ in tqdm(pkg_dirs, desc="Scanning APKs for claimed permissions", unit="apk"):
        apk_files = utils.getApksInFolder(pkg_path)
        if not apk_files:
            print(
                f"{GLOBALS.WARNING}[!] No APKs in {pkg_path}, skipping.{GLOBALS.RESET}"
            )
            continue

        parser = Parser()
        for apk in apk_files:
            apk_path = os.path.join(pkg_path, apk)

            cached = parser.checkAndGetCached(apk_path)
            if cached:
                parsed = cached
            else:
                with tempfile.TemporaryDirectory(prefix="apkshadow_Decompiled_") as temp_dir:
                    decompile_action.handleDecompileAction(None, False, apk_path, temp_dir, "apktool")
                    parsed = parser.checkAndGetCached(apk_path)

            if not parsed:
                continue

            for perm in parsed.get("permissions", []):
                name = perm.name
                prot = perm.protectionLevel
                declared_perms[name] = prot

    nonClaimed = []
    for finding in findings:
        perm_name = finding.component.permission

        if not perm_name or perm_name.lower() == "none":
            continue

        if perm_name not in declared_perms:
            # not claimed anywhere -> escalate
            finding.perm_type = "custom-unclaimed"
            finding.risk_tier = "critical"
            finding.build_summary("Not claimed by another app!")
            nonClaimed.append(finding)
        else:
            # declared somewhere — inspect protection levels
            prot_levels = declared_perms[perm_name]

            if "dangerous" in prot_levels or "runtime" in prot_levels:
                finding.perm_type = "custom-declared-dangerous"
                finding.risk_tier = "medium"
            elif "signature" in prot_levels or "knownSigner" in prot_levels:
                finding.perm_type = "custom-declared-signature"
                finding.risk_tier = "low"
            else:
                finding.perm_type = "custom-declared"
                finding.risk_tier = "low"
    return nonClaimed


def analyzePackages(pkg_dirs):
    """Analyze APK manifests for exported components and classify risks.
    Args:
        pkg_dirs (list[tuple[str, str]]): List of (path, pkg_name) tuples for APKs to analyze.
        device (str): Target device identifier, passed to the decompiler.

    Returns:
        list[Finding]: List of all analyzed findings.
    """
    if not GLOBALS.PERMISSIONS:
        GLOBALS.PERMISSIONS = utils.loadJsonFile(GLOBALS.PERMISSIONS_FILE_PATH)

    findings = []
    custom_perm_findings = []

    # First pass: analyze given packages
    for pkg_path, _ in tqdm(pkg_dirs, desc="Analyzing manifests", unit="apk"):
        manifest_path = utils.find_manifest(pkg_path)

        if GLOBALS.VERBOSE and manifest_path:
            utils.debug(f"Found AndroidManifest.xml at {manifest_path}")

        parser = Parser()
        parsed = parser.parseManifest(manifest_path)
        if not parsed:
            continue

        for comp in parsed["components"]:
            if not comp.exported:
                continue

            finding = Finding(comp)

            if finding.perm_type == "custom":
                custom_perm_findings.append(finding)
            else:
                findings.append(finding)

    # Second pass: check if custom permissions are claimed elsewhere
    if custom_perm_findings:
        print(
            f"{GLOBALS.WARNING}[+] Custom permissions found, scanning other APKs...{GLOBALS.RESET}"
        )

        with tempfile.TemporaryDirectory(prefix="apkshadow_Apks_") as temp_dir:
            pull_action.handlePullAction(None, False, temp_dir)
            findings.extend(filterNonClaimedPermissions(temp_dir, custom_perm_findings))
    return findings
