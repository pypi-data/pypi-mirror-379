import click
import requests
import subprocess
from importlib.metadata import version

from scp.app.sdk.cli.utils import confirm_with_help

package_name = "scp-app-sdk"

def get_version():
    return version('scp.app.sdk')

def get_latest_version():
    url = f"https://pypi.org/pypi/{package_name}/json"
    return requests.get(url).json()["info"]["version"]

def comp_versions(current_version, latest_version):
    if current_version >= latest_version:
        return True
    return False

def convert_version(version):
    major, minor, patch = map(int, version.split('.'))
    return (major << 16) | (minor << 8) | patch

def upgrade_version(current_version, latest_version):
    click.echo(f"🔄 Upgrading SCP APP CLI from version {current_version} to {latest_version}...")
    if not check_pipx_installed():
        click.echo("❌ pipx is not installed. Please install pipx to manage SCP APP CLI.")
        click.echo("   You can find installation instructions at: https://pipxproject.github.io/pipx/installation/")
        return

    try:
        if is_package_installed(package_name):
            click.echo(f"⚡ Package {package_name} is installed. Upgrading...")
            subprocess.run(["pipx", "upgrade", package_name], check=True)
            click.echo("✅ Upgrade completed successfully.")
        else:
            click.echo(f"⚠️ Package {package_name} is not installed. Installing...")
            subprocess.run(["pipx", "install", package_name], check=True)
            click.echo("✅ Installation completed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Operation failed: {e}")

def check_pipx_installed():
    import shutil
    return shutil.which("pipx") is not None

def is_package_installed(package_name: str) -> bool:
    try:
        result = subprocess.run(
            ["pipx", "list"], capture_output=True, text=True, check=True
        )
        return package_name in result.stdout
    except subprocess.CalledProcessError:
        return False

def version_check_hook():
    click.echo(f"🔄 Running version check hook...")
    latest_version = get_latest_version()
    current_version = get_version()
    upgrade = None

    if "dev" in  current_version:
        click.echo("⚠️ You are using a development version of SCP APP CLI.")
        upgrade = False

    if upgrade is None:
        version_check = comp_versions(convert_version(current_version), convert_version(latest_version))
        if not version_check:
            click.echo(f"⚠️ You are using an outdated version of SCP APP CLI.")
            if ask_for_upgrade(current_version, latest_version):
                upgrade = True
    
    if upgrade:
        upgrade_version(current_version, latest_version)
        
    click.echo("\n")

def ask_for_upgrade(current_version, latest_version, default=True):
    help_text = (
        "🗒️ Information:\n"
        "   • This application requires the latest version to work.\n"
        "   • By pressing yes, you'll ugrade to latest stable version\n"
        f"      • From: {current_version}\n"
        f"      • To: {latest_version}\n"
        "   • By pressing no, you'll stay on your current version\n"

    )

    return confirm_with_help(
        f"👉 Would you like to upgrade to the latest version?",
        help_text=help_text,
        default=default
    )


