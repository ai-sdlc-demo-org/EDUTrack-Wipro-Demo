#!/usr/bin/env python3
"""
Script to create GitHub issues using GitHub REST API.
This version uses the git credential helper to obtain authentication.
"""

import os
import re
import json
import subprocess
import sys
from typing import Dict, List, Optional

# Add the scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from create_github_issues import BacklogItem, collect_backlog_items, DEFAULT_REPO

def get_github_token() -> Optional[str]:
    """Get GitHub token from git credential helper or environment"""
    # Try environment variable first
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if token:
        return token
    
    # Try to get from git credential helper
    try:
        # Get the remote URL
        result = subprocess.run(
            ['git', 'config', '--get', 'remote.origin.url'],
            capture_output=True, text=True, check=True, cwd='/home/runner/work/EDUTrack-Demo/EDUTrack-Demo'
        )
        remote_url = result.stdout.strip()
        
        # Extract host
        if 'github.com' in remote_url:
            # Try git credential fill
            credential_input = f"protocol=https\nhost=github.com\n\n"
            result = subprocess.run(
                ['git', 'credential', 'fill'],
                input=credential_input,
                capture_output=True, text=True, cwd='/home/runner/work/EDUTrack-Demo/EDUTrack-Demo'
            )
            
            # Parse credential output
            for line in result.stdout.split('\n'):
                if line.startswith('password='):
                    return line.split('=', 1)[1].strip()
    except Exception as e:
        print(f"Could not get token from git credential helper: {e}")
    
    return None


def create_issue_via_api(repo: str, title: str, body: str, labels: List[str], token: str) -> Optional[int]:
    """Create a GitHub issue using the REST API"""
    import urllib.request
    import urllib.error
    
    url = f"https://api.github.com/repos/{repo}/issues"
    
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'EDUTrack-Issue-Creator'
    }
    
    try:
        request = urllib.request.Request(
            url,
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
            issue_number = result.get('number')
            print(f"✅ Created issue #{issue_number}: {title}")
            return issue_number
            
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"❌ Failed to create issue '{title}': HTTP {e.code}")
        print(f"   Error: {error_body}")
        return None
    except Exception as e:
        print(f"❌ Failed to create issue '{title}': {e}")
        return None


def main():
    """Main entry point"""
    print("🔍 GitHub Issue Creation via REST API")
    print("=" * 60)
    
    # Get GitHub token
    print("\n📋 Checking for GitHub authentication...")
    token = get_github_token()
    
    if not token:
        print("❌ Error: No GitHub authentication available")
        print("\nThis script needs GitHub authentication to create issues.")
        print("Since we're running in a GitHub Actions environment,")
        print("the authentication should be available automatically.")
        print("\nPlease check that:")
        print("  1. The workflow has 'write' permissions for issues")
        print("  2. GITHUB_TOKEN is available in the environment")
        return 1
    
    print("✅ GitHub authentication found")
    
    # Get repository
    repo = os.environ.get('GITHUB_REPOSITORY', DEFAULT_REPO)
    print(f"📦 Repository: {repo}")
    
    # Collect backlog items
    print("\n🔍 Collecting backlog items...")
    backlog_dir = '/home/runner/work/EDUTrack-Demo/EDUTrack-Demo/backlog'
    items = collect_backlog_items(backlog_dir)
    
    total = sum(len(items[cat]) for cat in items)
    print(f"📊 Found {total} backlog items:")
    for category, item_list in items.items():
        print(f"   - {len(item_list)} {category}")
    
    # Create issues in hierarchy order
    print(f"\n📝 Creating GitHub issues...")
    issue_map = {}  # item_id -> issue_number
    
    for category in ['epics', 'features', 'stories', 'tasks']:
        if not items[category]:
            continue
            
        print(f"\n📌 Creating {category}...")
        for item in items[category]:
            # Find parent issue number if exists
            parent_issue = None
            if item.parent_id and item.parent_id in issue_map:
                parent_issue = issue_map[item.parent_id]
            
            # Create issue
            title = f"[{item.item_id}] {item.title}"
            body = item.create_issue_body(parent_issue)
            
            issue_number = create_issue_via_api(
                repo=repo,
                title=title,
                body=body,
                labels=item.labels,
                token=token
            )
            
            if issue_number:
                issue_map[item.item_id] = issue_number
                item.issue_number = issue_number
    
    # Save mapping
    print(f"\n✨ Summary:")
    print(f"   Created {len(issue_map)} GitHub issues")
    print(f"\n🔗 Issue Mapping:")
    for item_id, issue_num in sorted(issue_map.items()):
        print(f"   {item_id} -> Issue #{issue_num}")
    
    # Save to file
    mapping_file = os.path.join(backlog_dir, 'issue-mapping.json')
    try:
        with open(mapping_file, 'w') as f:
            json.dump(issue_map, f, indent=2)
        print(f"\n💾 Saved issue mapping to: {mapping_file}")
    except Exception as e:
        print(f"⚠️  Warning: Could not save mapping: {e}")
    
    print("\n✅ Done!")
    return 0


if __name__ == '__main__':
    sys.exit(main())
