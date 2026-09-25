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
        formatted_users += f'      status: "{u.get("status", "active")}",\n'
        formatted_users += f'      passwordHash: "{u.get("passwordHash", "")}",\n'
        formatted_users += f'      registeredAt: "{u.get("registeredAt", datetime.now().strftime("%Y-%m-%d"))}"\n'
        formatted_users += "    }" + (",\n" if i < len(users) - 1 else "\n")
    formatted_users += "  ];"

    new_content = re.sub(r'const\s+USER_REGISTRY\s*=\s*\[\s*\{.*?\}\s*\];', formatted_users, original_content, flags=re.DOTALL)
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✓ Registry successfully updated: {REGISTRY_PATH}")

def git_commit_and_push(commit_msg):
    portal_dir = os.path.dirname(REGISTRY_PATH) or '.'
    try:
        print("  ➔ Staging and pushing update to GitHub...")
        subprocess.run(['git', 'add', os.path.basename(REGISTRY_PATH)], cwd=portal_dir, check=True)
        subprocess.run(['git', 'commit', '-m', commit_msg], cwd=portal_dir, check=True)
        res = subprocess.run(['git', 'push', 'origin', 'main'], cwd=portal_dir, check=True)
        print("✓ Successfully pushed to remote repository. User changes are now live on GitHub Pages!")
    except Exception as e:
        print(f"Notice: Git push failed or skipped ({e}). Run git push manually when connected.")

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
                "status": "active",
                "passwordHash": pw_hash,
                "registeredAt": datetime.now().strftime("%Y-%m-%d")
            }
            users.append(new_u)
            print(f"Registered new approved user: {username} ({new_u['name']})")

        write_registry(users, content)
        if not args.no_push:
            git_commit_and_push(f"Approve and activate user '{username}' in portal registry")

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
