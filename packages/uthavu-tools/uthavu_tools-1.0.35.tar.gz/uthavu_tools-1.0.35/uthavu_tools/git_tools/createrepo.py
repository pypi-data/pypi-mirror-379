import os
import subprocess
import requests
import sys
import shutil
import re

# ==============================
# CONFIG (better from env vars)
# ==============================
GITLAB_URL = "https://gitlab.com" #os.getenv("GITLAB_URL")
GITLAB_TOKEN = "glpat-hg7epYFgilXsXsvB8WQPyW86MQp1Omd4cmVkCw.01.121252fpx" #os.getenv("GITLAB_TOKEN")  # ⚠️ Set via environment variable
DEFAULT_GROUP_ID ="115815064"  #int(os.getenv("GITLAB_GROUP_ID", "115815064"))

TEMPLATE_ROOT = os.path.join(os.path.dirname(__file__), "template_files")

def run(cmd):
    """Run a shell command and return output"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"⚠️ Command failed: {cmd}\n{result.stderr}")
    return result.stdout.strip()

def copy_template(stack, target_path):
    """Copy template files (including dotfiles) into the project directory"""
    source = os.path.join(TEMPLATE_ROOT, stack)
    if not os.path.isdir(source):
        print(f"⚠️ No template found for '{stack}', skipping...")
        print(f"⚠️ source '{source}', skipping...")
        return

    for root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        dest_dir = os.path.join(target_path, rel_path) if rel_path != "." else target_path
        os.makedirs(dest_dir, exist_ok=True)

        for file in files:
            s = os.path.join(root, file)
            d = os.path.join(dest_dir, file)
            shutil.copy2(s, d)

    print(f"📂 Template '{stack}' files copied into project (including dotfiles).")

def update_gitlab_ci(target_path, app_name, port):
    """Update .gitlab-ci.yml with provided app_name and port"""
    ci_file = os.path.join(target_path, ".gitlab-ci.yml")
    if not os.path.exists(ci_file):
        print("⚠️ No .gitlab-ci.yml found to update.")
        return

    with open(ci_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace lines safely
    content = re.sub(r"(APP_NAME:\s*).*", lambda m: f"{m.group(1)}{app_name}", content)
    content = re.sub(r"(APP_PORT:\s*).*", lambda m: f"{m.group(1)}{port}", content)

    with open(ci_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Updated .gitlab-ci.yml with APP_NAME={app_name}, APP_PORT={port}")
 
    
def main():
    if not GITLAB_TOKEN:
        print("❌ Missing GitLab token. Set GITLAB_TOKEN environment variable.")
        sys.exit(1)
    stacks = {
        "1": "php",
        "2": "plain_html",
        "3": "fastapi",
        "4": "nextjs"
    }
    print("👉 Select Tech Stack:")
    for k, v in stacks.items():
        print(f"  {k}. {v}")
    choice = input("Enter choice [default=plain_html]: ").strip() or "2"
    stack = stacks.get(choice, "plain_html")
    
    # ==============================
    # Ask for project details
    # ==============================
    project_name = input("👉 Enter GitLab project name: ").strip()
    project_desc = input("👉 Enter project description [default = same as name]: ").strip() or project_name
    visibility = input("👉 Enter visibility (private/internal/public) [default=private]: ").strip() or "private"

    group_id_input = input(f"👉 Enter GitLab group ID [default = {DEFAULT_GROUP_ID}]: ").strip()
    group_id = int(group_id_input) if group_id_input else DEFAULT_GROUP_ID

    # ==============================
    # Ask for source folder
    # ==============================
    source_path = input(f"👉 Enter full path to your source code folder [default = current folder]: ").strip()
    if not source_path:
        source_path = os.getcwd()  # default to current directory

    app_name = input("👉 Enter App Name (for container): ").strip() or "uthavu-site"
    port = input("👉 Enter App Port: ").strip() or "8081"

    if not os.path.isdir(source_path):
        print(f"❌ The path '{source_path}' is not valid.")
        sys.exit(1)

    os.chdir(source_path)
    print(f"📂 Using source folder: {source_path}")
    
     # Copy template files
    copy_template(stack, source_path)
    update_gitlab_ci(source_path, app_name, port)

    # ==============================
    # Step 1: Create GitLab project
    # ==============================
    headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    data = {
        "name": project_name,
        "description": project_desc,
        "visibility": visibility,
        "namespace_id": group_id,
    }

    print(f"🔧 Creating GitLab project '{project_name}'...")

    response = requests.post(f"{GITLAB_URL}/api/v4/projects", headers=headers, data=data)

    if response.status_code == 201:
        project = response.json()
        project_id = project["id"]
        repo_url = project["http_url_to_repo"]
        print(f"✅ Project created: {project['web_url']}")
        print(f"📂 Repo URL: {repo_url}")
    else:
        print("❌ Failed to create project:", response.status_code, response.json())
        sys.exit(1)

    # ==============================
    # Step 2: Git operations
    # ==============================
    if not os.path.exists(".git"):
        run("git init")

    run("git add .")
    status = run("git diff --cached --quiet || echo 'changes'")
    if "changes" in status:
        run('git commit -m "Initial commit"')
    else:
        print("ℹ️ Nothing to commit, skipping...")

    run("git branch -M main")

    # Add GitLab remote with token
    remote_url = repo_url.replace("https://", f"https://oauth2:{GITLAB_TOKEN}@")
    run("git remote remove origin || true")
    run(f"git remote add origin {remote_url}")

    run("git push -u origin main")
    print("✅ Code pushed to main branch.")

    # ==============================
    # Step 3: Create dev branch and set default
    # ==============================
    print("🔧 Creating 'dev' branch from 'main'...")
    run("git checkout -b dev")
    run("git push -u origin dev")

    print("🔧 Setting 'dev' as default branch in GitLab...")
    set_branch_resp = requests.put(
        f"{GITLAB_URL}/api/v4/projects/{project_id}",
        headers=headers,
        data={"default_branch": "dev"}
    )

    if set_branch_resp.status_code == 200:
        print("✅ 'dev' set as default branch.")
    else:
        print("❌ Failed to set default branch:", set_branch_resp.json())

    print(f"🚀 Project '{project_name}' ready with 'dev' as default branch.")

if __name__ == "__main__":
    main()
