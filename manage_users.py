#!/usr/bin/env python3
"""
TelTech & Comclark — 5G FWA Portal User Administration Utility
Author: OLIVER TUNGOL (oliver.tungol@comclark.com.ph)

Usage:
  python3 manage_users.py list
  python3 manage_users.py approve <username> <password_or_hash> --name "Full Name" --email "user@company.com" [--org "Company"] [--role "Role"] [--no-push]
  python3 manage_users.py revoke <username> [--no-push]
  python3 manage_users.py delete <username> [--no-push]
"""

import sys, os, re, json, hashlib, argparse, subprocess
from datetime import datetime

REGISTRY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fwa_online_portal/auth_registry.js')
if not os.path.exists(REGISTRY_PATH):
    # Check if run from within fwa_online_portal
    if os.path.exists('auth_registry.js'):
        REGISTRY_PATH = 'auth_registry.js'

def compute_sha256(text):
    # If text is already a 64-char hex string, treat it as an existing hash
    if re.match(r'^[a-fA-F0-9]{64}$', text.strip()):
        return text.strip().lower()
    return hashlib.sha256(text.strip().encode('utf-8')).hexdigest()

def read_registry():
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract USER_REGISTRY array
    match = re.search(r'const\s+USER_REGISTRY\s*=\s*(\[\s*\{.*?\}\s*\]);', content, re.DOTALL)
    if not match:
        raise ValueError("Could not parse USER_REGISTRY array in auth_registry.js")
    
    raw_array = match.group(1)
    # Convert JS object keys to valid JSON format if needed
    cleaned_json = re.sub(r'(\w+):', r'"\1":', raw_array)
    # Remove trailing commas
    cleaned_json = re.sub(r',\s*([\]}])', r'\1', cleaned_json)
    
    try:
        users = json.loads(cleaned_json)
    except Exception:
        # Fallback manual regex extractor
        users = []
        user_blocks = re.findall(r'\{\s*(.*?)\s*\}', raw_array, re.DOTALL)
        for b in user_blocks:
            u = {}
            for line in b.split('\n'):
                line = line.strip().rstrip(',')
                m = re.match(r'(\w+)\s*:\s*["\']?(.*?)["\']?$', line)
                if m:
                    k, v = m.group(1), m.group(2)
                    if v.lower() == 'true': v = True
                    elif v.lower() == 'false': v = False
                    u[k] = v
            if 'username' in u:
                users.append(u)
    return users, content

def write_registry(users, original_content):
    formatted_users = "const USER_REGISTRY = [\n"
    for i, u in enumerate(users):
        formatted_users += "    {\n"
        formatted_users += f'      username: "{u.get("username", "")}",\n'
        formatted_users += f'      name: "{u.get("name", "")}",\n'
        formatted_users += f'      email: "{u.get("email", "")}",\n'
        formatted_users += f'      organization: "{u.get("organization", "TelTech / Comclark")}",\n'
        formatted_users += f'      role: "{u.get("role", "Presentation Viewer")}",\n'
        formatted_users += f'      isAdmin: {"true" if u.get("isAdmin") else "false"},\n'
        if u.get("isBidder"):
            formatted_users += f'      isBidder: true,\n'
        formatted_users += f'      status: "{u.get("status", "active")}",\n'
        formatted_users += f'      passwordHash: "{u.get("passwordHash", "")}",\n'
        formatted_users += f'      registeredAt: "{u.get("registeredAt", datetime.now().strftime("%Y-%m-%d"))}"\n'
        formatted_users += "    }" + (",\n" if i < len(users) - 1 else "\n")
    formatted_users += "  ];"

    new_content = re.sub(r'const\s+USER_REGISTRY\s*=\s*\[\s*\{.*?\}\s*\];', formatted_users, original_content, flags=re.DOTALL)
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✓ Registry successfully updated: {REGISTRY_PATH}")
    
    # Also sync to 03_Online_Portal if running from fwa_online_portal
    alt_path = os.path.abspath(os.path.join(os.path.dirname(REGISTRY_PATH), '../../../03_Online_Portal/auth_registry.js'))
    if os.path.exists(os.path.dirname(alt_path)):
        with open(alt_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Synced to: {alt_path}")

def send_approval_email(name, email, username, password, role="Bidder"):
    if not email:
        return
    
    # Check if password is raw or a 64-char hash
    is_hash = bool(re.match(r'^[a-fA-F0-9]{64}$', password.strip()))
    pw_instruction = f"• Initial Security Passcode: {password}" if not is_hash else "• Password / Security Passcode: The security passcode you created during your access request."
    
    subject = "[CLEARANCE APPROVED] TelTech 5G FWA E-Tender Portal Access Granted (RFP-TELTECH-FWA-2026-001)"
    body = f"""Dear {name or username.title()},

Your clearance request for the TelTech Nationwide 5G Standalone Fixed Wireless Access (FWA) E-Tender Portal has been formally approved by the Tender Secretariat.

Your credentials have been activated with full access to read tender specifications, fill out the interactive Technical Compliance Matrix, complete the commercial BoQ price book, and submit sealed bids.

PORTAL ACCESS CREDENTIALS:
--------------------------------------------------
• Dedicated E-Tender Sign-In: https://quizoli.github.io/fwa-5g-presentation/rfp_login.html
• Direct E-Tender Suite: https://quizoli.github.io/fwa-5g-presentation/rfp_portal.html
• Username: {username}
• Assigned Role: {role}
• Authorized Email: {email}
{pw_instruction}
--------------------------------------------------

OPERATIVE TENDER DELIVERABLES:
1. 00 RFP Tender Invitation & Transmittal Letter (PDF)
2. 01 Master Tender Document & Instructions to Bidders (PDF)
3. 02 Appendix A: Technical Specifications & Compliance Matrix (Interactive Form & Excel)
4. 03 Appendix B: Commercial Proposal BoQ Templates (PDF)
5. 04 Appendix C: SLAs, Network KPIs & Liquidated Damages (PDF)
6. 05 Appendix D: Siting, RF Planning, Civil & Power Engineering Guidelines (PDF)
7. 06 RFP Commercial Price Book & BoQ Template (10-Sheet Excel)
8. 07 Candidate Siting Schedule & Locations (5,000 Target Barangays Excel)

KEY BIDDING MILESTONES:
• Official RFP Issuance: October 14, 2026
• Bidder Confirmation & NDA Submission: October 21, 2026
• Deadline for Written Clarifications: November 4, 2026
• Consolidated Clarifications Response: November 11, 2026
• Final Bid Submission Deadline: December 2, 2026 (17:00 PHT)

Should you require any technical assistance with portal navigation or tender clarifications, please contact the undersigned.

Sincerely,

OLIVER TUNGOL
Corporate Tender Secretariat
Telecommunications Technology Solutions Incorporated (TelTech)
Email: oliver.tungol@comclark.com.ph"""

    # Escape quotes for AppleScript
    clean_body = body.replace('\\', '\\\\').replace('"', '\\"')
    clean_subj = subject.replace('"', '\\"')
    recipient_name = (name or username).replace('"', '\\"')
    
    applescript = f'''tell application "Mail"
        set msg to make new outgoing message with properties {{subject:"{clean_subj}", content:"{clean_body}", visible:false}}
        tell msg
            set sender to "Oliver Tungol <oliver.tungol@comclark.com.ph>"
            make new to recipient at end of to recipients with properties {{address:"{email}", name:"{recipient_name}"}}
        end tell
        send msg
    end tell'''
    
    try:
        res = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"✓ Official access approval email dispatched to: {email}")
        else:
            print(f"Notice: Mail.app notification: {res.stderr.strip()}")
    except Exception as e:
        print(f"Notice: Could not send automated email via Mail.app ({e})")

def main():
    parser = argparse.ArgumentParser(description="TelTech & Comclark 5G FWA Portal User Management")
    subparsers = parser.add_subparsers(dest="command", help="Action to perform")

    # List
    parser_list = subparsers.add_parser("list", help="List all registered users")

    # Approve / Add
    parser_add = subparsers.add_parser("approve", help="Approve and register a user")
    parser_add.add_argument("username", help="Username for the account")
    parser_add.add_argument("password", help="Password or SHA-256 hash")
    parser_add.add_argument("--name", default="", help="User's full name")
    parser_add.add_argument("--email", default="", help="Corporate email address")
    parser_add.add_argument("--org", default="TelTech / Comclark Partner", help="Organization / Department")
    parser_add.add_argument("--role", default="Presentation Reviewer", help="Assigned role")
    parser_add.add_argument("--admin", action="store_true", help="Grant administrator privileges")
    parser_add.add_argument("--bidder", action="store_true", help="Grant bidder portal access privileges")
    parser_add.add_argument("--no-push", action="store_true", help="Do not git push automatically")

    # Revoke / Suspend
    parser_revoke = subparsers.add_parser("revoke", help="Suspend a user's access")
    parser_revoke.add_argument("username", help="Username to suspend")
    parser_revoke.add_argument("--no-push", action="store_true", help="Do not git push automatically")

    # Delete
    parser_del = subparsers.add_parser("delete", help="Permanently delete a user from registry")
    parser_del.add_argument("username", help="Username to delete")
    parser_del.add_argument("--no-push", action="store_true", help="Do not git push automatically")

    args = parser.parse_args()

    if not args.command or args.command == "list":
        users, _ = read_registry()
        print("\n=== TELTECH & COMCLARK FWA PORTAL — REGISTERED USERS ===")
        print(f"{'USERNAME':<16} {'NAME':<24} {'EMAIL':<30} {'ROLE':<22} {'STATUS'}")
        print("-" * 105)
        for u in users:
            stat_icon = "🟢 ACTIVE" if u.get("status") == "active" else "🔴 SUSPENDED"
            print(f"{u.get('username',''):<16} {u.get('name',''):<24} {u.get('email',''):<30} {u.get('role',''):<22} {stat_icon}")
        print("-" * 105)
        print(f"Total Users: {len(users)}\n")
        return

    users, content = read_registry()

    if args.command == "approve":
        pw_hash = compute_sha256(args.password)
        username = args.username.strip().lower()

        # Check existing
        existing = next((u for u in users if u.get('username', '').lower() == username), None)
        if existing:
            existing['passwordHash'] = pw_hash
            if args.name: existing['name'] = args.name
            if args.email: existing['email'] = args.email
            if args.org: existing['organization'] = args.org
            if args.role: existing['role'] = args.role
            if args.bidder: existing['isBidder'] = True
            existing['status'] = 'active'
            print(f"Updated existing user: {username}")
        else:
            new_u = {
                "username": username,
                "name": args.name or username.title(),
                "email": args.email or f"{username}@comclark.com.ph",
                "organization": args.org,
                "role": args.role,
                "isAdmin": args.admin,
                "isBidder": args.bidder or ("bidder" in username or "Bidder" in args.role),
                "status": "active",
                "passwordHash": pw_hash,
                "registeredAt": datetime.now().strftime("%Y-%m-%d")
            }
            users.append(new_u)
            print(f"Registered new approved user: {username} ({new_u['name']})")

        write_registry(users, content)
        if not args.no_push:
            git_commit_and_push(f"Approve and activate user '{username}' in portal registry")

        # Dispatch official clearance approval email
        target_email = args.email or (existing.get('email') if existing else '')
        target_name = args.name or (existing.get('name') if existing else username.title())
        target_role = args.role or (existing.get('role') if existing else 'Bidder')
        send_approval_email(target_name, target_email, username, args.password, target_role)

    elif args.command == "revoke":
        username = args.username.strip().lower()
        target = next((u for u in users if u.get('username', '').lower() == username), None)
        if not target:
            print(f"Error: User '{username}' not found.")
            return
        target['status'] = 'suspended'
        write_registry(users, content)
        print(f"User '{username}' access has been SUSPENDED.")
        if not args.no_push:
            git_commit_and_push(f"Suspend access for user '{username}' in portal registry")

    elif args.command == "delete":
        username = args.username.strip().lower()
        if username == 'oliver.tungol':
            print("Error: Cannot delete primary master administrator account.")
            return
        new_users = [u for u in users if u.get('username', '').lower() != username]
        if len(new_users) == len(users):
            print(f"Error: User '{username}' not found.")
            return
        write_registry(new_users, content)
        print(f"User '{username}' permanently removed from registry.")
        if not args.no_push:
            git_commit_and_push(f"Delete user '{username}' from portal registry")

if __name__ == '__main__':
    main()
