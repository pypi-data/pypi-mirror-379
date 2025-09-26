import os
import subprocess
import requests
import sys

# ==============================
# CONFIG (better from env vars)
# ==============================
GITLAB_URL = "https://gitlab.com" #os.getenv("GITLAB_URL")
GITLAB_TOKEN = "glpat-hg7epYFgilXsXsvB8WQPyW86MQp1Omd4cmVkCw.01.121252fpx" #os.getenv("GITLAB_TOKEN")  # ⚠️ Set via environment variable
DEFAULT_GROUP_ID ="115815064"  #int(os.getenv("GITLAB_GROUP_ID", "115815064"))

def run(cmd):
    """Run a shell command and return output"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"⚠️ Command failed: {cmd}\n{result.stderr}")
    return result.stdout.strip()

def main():
    if not GITLAB_TOKEN:
        print("❌ Missing GitLab token. Set GITLAB_TOKEN environment variable.")
        sys.exit(1)

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

    if not os.path.isdir(source_path):
        print(f"❌ The path '{source_path}' is not valid.")
        sys.exit(1)

    os.chdir(source_path)
    print(f"📂 Using source folder: {source_path}")

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
