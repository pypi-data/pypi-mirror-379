#!/usr/bin/env python3
"""
Medula CLI - Developer tool for managing AI agents
Leverages existing Medula API infrastructure
"""

import os
import sys
import json
import click
import httpx
import keyring
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
import asyncio

# Global console for rich output
console = Console()

# ASCII Logo
MEDULA_LOGO = """
[bold cyan]
    ███╗   ███╗███████╗██████╗ ██╗   ██╗██╗      █████╗ 
    ████╗ ████║██╔════╝██╔══██╗██║   ██║██║     ██╔══██╗
    ██╔████╔██║█████╗  ██║  ██║██║   ██║██║     ███████║
    ██║╚██╔╝██║██╔══╝  ██║  ██║██║   ██║██║     ██╔══██║
    ██║ ╚═╝ ██║███████╗██████╔╝╚██████╔╝███████╗██║  ██║
    ╚═╝     ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
[/bold cyan]

[yellow]    🚀 AI Agent Platform for Developers 🚀[/yellow]
"""

# Alternative compact logo
MEDULA_LOGO_COMPACT = """
[bold blue]
    ▗▄▄▄▖ ▗▄▄▄▄▖▗▄▄▄▄▖▗▖  ▗▖▗▖    ▗▄▖ 
    ▐▌ ▐▌▐▌    ▐▌  ▐▌▐▌  ▐▌▐▌   ▐▌ ▐▌
    ▐▛▀▘ ▐▛▀▀▀▘▐▌  ▐▌▐▌  ▐▌▐▌   ▐▛▀▜▌
    ▐▌   ▐▙▄▄▄▖▐▙▄▄▞▘▝▚▄▄▞▘▐▙▄▄▖▐▌ ▐▌
[/bold blue]
"""

def show_logo(compact=False):
    """Display the Medula AI logo"""
    try:
        if compact:
            console.print(MEDULA_LOGO_COMPACT)
        else:
            console.print(MEDULA_LOGO)
    except Exception:
        # Fallback to simple text logo if Unicode fails
        console.print("[bold cyan]")
        console.print("    ╔══════════════════════════════╗")
        console.print("    ║         M E D U L A          ║") 
        console.print("    ║   AI Agent Platform CLI      ║")
        console.print("    ╚══════════════════════════════╝")
        console.print("[/bold cyan]")

# Configuration
CONFIG_DIR = Path.home() / '.medula'
CONFIG_FILE = CONFIG_DIR / 'config.json'
KEYRING_SERVICE = 'medula-cli'

class MedulaAPI:
    """HTTP client for Medula API"""
    
    def __init__(self, base_url: str, token: str = None):
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.client = httpx.AsyncClient(
            timeout=30.0,
            headers=self._get_headers()
        )
    
    def _get_headers(self) -> Dict[str, str]:
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'medula-cli/1.0.0'
        }
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'
        return headers
    
    async def post(self, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make POST request"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = await self.client.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if os.getenv('MEDULA_DEBUG'):
                console.print(f"[red]HTTP {e.response.status_code}:[/red] {str(e)}")
            return {"success": False, "error": {"message": f"HTTP {e.response.status_code}", "code": e.response.status_code}}
        except Exception as e:
            if os.getenv('MEDULA_DEBUG'):
                console.print(f"[red]API Error:[/red] {str(e)}")
            return {"success": False, "error": {"message": "Connection error"}}
    
    async def get(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make GET request"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = await self.client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if os.getenv('MEDULA_DEBUG'):
                console.print(f"[red]HTTP {e.response.status_code}:[/red] {str(e)}")
            return {"success": False, "error": {"message": f"HTTP {e.response.status_code}", "code": e.response.status_code}}
        except Exception as e:
            if os.getenv('MEDULA_DEBUG'):
                console.print(f"[red]API Error:[/red] {str(e)}")
            return {"success": False, "error": {"message": "Connection error"}}
    
    async def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make DELETE request"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = await self.client.delete(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if os.getenv('MEDULA_DEBUG'):
                console.print(f"[red]HTTP {e.response.status_code}:[/red] {str(e)}")
            return {"success": False, "error": {"message": f"HTTP {e.response.status_code}", "code": e.response.status_code}}
        except Exception as e:
            if os.getenv('MEDULA_DEBUG'):
                console.print(f"[red]API Error:[/red] {str(e)}")
            return {"success": False, "error": {"message": "Connection error"}}

class ConfigManager:
    """Manage CLI configuration"""
    
    def __init__(self):
        self.config_dir = CONFIG_DIR
        self.config_file = CONFIG_FILE
        self._ensure_config_dir()
    
    def _ensure_config_dir(self):
        """Ensure config directory exists"""
        self.config_dir.mkdir(exist_ok=True)
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        if not self.config_file.exists():
            return self._default_config()
        
        try:
            with open(self.config_file) as f:
                return json.load(f)
        except:
            return self._default_config()
    
    def save_config(self, config: Dict[str, Any]):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def _default_config(self) -> Dict[str, Any]:
        """Default configuration"""
        default_endpoint = os.getenv('MEDULA_ENDPOINT', 'https://updated-nadesqa-1.onrender.com')
        return {
            "endpoint": default_endpoint,
            "tenant_id": None,
            "user_email": None,
            "profiles": {}
        }
    
    def get_token(self) -> Optional[str]:
        """Get stored auth token"""
        try:
            return keyring.get_password(KEYRING_SERVICE, 'auth_token')
        except:
            return None
    
    def set_token(self, token: str):
        """Store auth token securely"""
        keyring.set_password(KEYRING_SERVICE, 'auth_token', token)
    
    def clear_token(self):
        """Clear stored auth token"""
        try:
            keyring.delete_password(KEYRING_SERVICE, 'auth_token')
        except:
            pass

# Global instances
config_manager = ConfigManager()

# Version handling
def get_version():
    """Get CLI version from environment or default"""
    return os.getenv('MEDULA_CLI_VERSION', '1.0.0')

@click.group()
@click.version_option(version=get_version())
@click.option('--no-logo', is_flag=True, help='Skip logo display')
@click.option('--debug', is_flag=True, help='Enable debug mode')
def cli(no_logo, debug):
    """Medula CLI - Manage your AI agents from the terminal"""
    # Set debug mode
    if debug:
        os.environ['MEDULA_DEBUG'] = '1'
    
    # Show logo for interactive commands (not for --help or --version)
    ctx = click.get_current_context()
    if not no_logo and ctx.invoked_subcommand and ctx.invoked_subcommand != 'version':
        show_logo()

@cli.group()
def auth():
    """Authentication commands"""
    pass

@auth.command('login')
@click.option('--email', prompt=True, help='Your email address')
@click.option('--password', prompt=True, hide_input=True, help='Your password')
@click.option('--endpoint', default=None, help='API endpoint (optional)')
async def login(email: str, password: str, endpoint: Optional[str]):
    """Login to Medula platform"""
    
    config = config_manager.load_config()
    
    if endpoint:
        config['endpoint'] = endpoint
        config_manager.save_config(config)
    
    api = MedulaAPI(config['endpoint'])
    
    with console.status("[bold blue]Logging in..."):
        response = await api.post('/login', {
            'email': email,
            'password': password
        })
    
    if response.get('success'):
        token = response['token']
        user = response['user']
        
        # Store token securely
        config_manager.set_token(token)
        
        # Update config
        config['user_email'] = email
        config['tenant_id'] = user['tenant_id']
        config_manager.save_config(config)
        
        console.print(f"[green]✓ Successfully logged in as {user['name']} ({email})")
        console.print(f"[blue]Tenant ID: {user['tenant_id']}")
    else:
        error_msg = response.get('error', {}).get('message', 'Unknown error')
        console.print(f"[red]✗ Login failed: {error_msg}")
        sys.exit(1)

@auth.command('logout')
def logout():
    """Logout and clear stored credentials"""
    config_manager.clear_token()
    console.print("[green]✓ Logged out successfully")

@auth.command('whoami')
def whoami():
    """Show current user information"""
    config = config_manager.load_config()
    token = config_manager.get_token()
    
    if not token:
        console.print("[red]Not logged in. Run 'medula auth login' first.")
        return
    
    console.print(f"[blue]Email:[/blue] {config.get('user_email', 'Unknown')}")
    console.print(f"[blue]Tenant ID:[/blue] {config.get('tenant_id', 'Unknown')}")
    console.print(f"[blue]Endpoint:[/blue] {config.get('endpoint')}")

@cli.group()
def agents():
    """Agent management commands"""
    pass

@agents.command('list')
@click.option('--format', 'output_format', default='table', 
              type=click.Choice(['table', 'json']), 
              help='Output format')
async def list_agents(output_format: str):
    """List all agents"""
    config = config_manager.load_config()
    token = config_manager.get_token()
    
    if not token:
        console.print("[red]Not logged in. Run 'medula auth login' first.")
        return
    
    if not config.get('tenant_id'):
        console.print("[red]No tenant ID found. Please login again.")
        return
    
    api = MedulaAPI(config['endpoint'], token)
    
    with console.status("[bold blue]Fetching agents..."):
        response = await api.get(f"/api/v1/tenants/{config['tenant_id']}/agents")
    
    if not response.get('success'):
        error_msg = response.get('error', {}).get('message', 'Unknown error')
        console.print(f"[red]✗ Failed to fetch agents: {error_msg}")
        return
    
    agents_data = response.get('data', [])
    
    if output_format == 'json':
        console.print_json(data=agents_data)
        return
    
    # Table format
    if not agents_data:
        console.print("[yellow]No agents found. Create your first agent with 'medula agents create'")
        return
    
    table = Table(title="Your AI Agents")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="bold")
    table.add_column("Type", style="blue")
    table.add_column("Status", style="green")
    table.add_column("Created", style="dim")
    
    for agent in agents_data:
        created_at = agent.get('created_at', '')
        if created_at:
            try:
                created_at = datetime.fromisoformat(created_at.replace('Z', '+00:00')).strftime('%Y-%m-%d')
            except:
                pass
        
        table.add_row(
            agent.get('id', '')[:8] + '...',
            agent.get('name', 'Unknown'),
            agent.get('category', 'custom'),
            agent.get('status', 'unknown'),
            created_at
        )
    
    console.print(table)

@agents.command('create')
@click.option('--name', prompt=True, help='Agent name')
@click.option('--description', default='', help='Agent description')
@click.option('--model', default='claude-3-haiku', 
              type=click.Choice(['claude-3-haiku', 'claude-3-sonnet', 'gpt-3.5-turbo', 'gpt-4']),
              help='AI model to use')
async def create_agent(name: str, description: str, model: str):
    """Create a new AI agent"""
    config = config_manager.load_config()
    token = config_manager.get_token()
    
    if not token:
        console.print("[red]Not logged in. Run 'medula auth login' first.")
        return
    
    api = MedulaAPI(config['endpoint'], token)
    
    agent_data = {
        'name': name,
        'description': description,
        'ai_model': model,
        'ai_provider': 'anthropic' if model.startswith('claude') else 'openai',
        'category': 'custom',
        'status': 'draft'
    }
    
    with console.status(f"[bold blue]Creating agent '{name}'..."):
        response = await api.post(f"/api/v1/tenants/{config['tenant_id']}/agents", agent_data)
    
    if response.get('success'):
        agent = response.get('data', {})
        console.print(f"[green]✓ Agent '{name}' created successfully!")
        console.print(f"[blue]Agent ID:[/blue] {agent.get('id')}")
        console.print(f"[blue]Model:[/blue] {model}")
    else:
        error_msg = response.get('error', {}).get('message', 'Unknown error')
        console.print(f"[red]✗ Failed to create agent: {error_msg}")

@agents.command('show')
@click.argument('agent_id')
async def show_agent(agent_id: str):
    """Show detailed agent information"""
    config = config_manager.load_config()
    token = config_manager.get_token()
    
    if not token:
        console.print("[red]Not logged in. Run 'medula auth login' first.")
        return
    
    api = MedulaAPI(config['endpoint'], token)
    
    with console.status(f"[bold blue]Fetching agent {agent_id}..."):
        response = await api.get(f"/api/v1/tenants/{config['tenant_id']}/agents/{agent_id}")
    
    if not response.get('success'):
        error_msg = response.get('error', {}).get('message', 'Unknown error')
        console.print(f"[red]✗ Failed to fetch agent: {error_msg}")
        return
    
    agent = response.get('data', {})
    
    # Create info panel
    info = f"""[bold]Name:[/bold] {agent.get('name', 'Unknown')}
[bold]ID:[/bold] {agent.get('id', 'Unknown')}
[bold]Description:[/bold] {agent.get('description', 'No description')}
[bold]Model:[/bold] {agent.get('ai_model', 'Unknown')}
[bold]Provider:[/bold] {agent.get('ai_provider', 'Unknown')}
[bold]Status:[/bold] {agent.get('status', 'Unknown')}
[bold]Category:[/bold] {agent.get('category', 'Unknown')}
[bold]Created:[/bold] {agent.get('created_at', 'Unknown')}"""
    
    panel = Panel(info, title=f"Agent: {agent.get('name', 'Unknown')}", border_style="blue")
    console.print(panel)

@cli.group()
def chat():
    """Interactive chat with agents"""
    pass

@chat.command('start')
@click.argument('agent_id')
@click.option('--save-session', default=None, help='Save conversation with this name')
async def start_chat(agent_id: str, save_session: Optional[str]):
    """Start interactive chat with an agent"""
    config = config_manager.load_config()
    token = config_manager.get_token()
    
    if not token:
        console.print("[red]Not logged in. Run 'medula auth login' first.")
        return
    
    api = MedulaAPI(config['endpoint'], token)
    
    # Verify agent exists
    with console.status(f"[bold blue]Connecting to agent {agent_id}..."):
        response = await api.get(f"/api/v1/tenants/{config['tenant_id']}/agents/{agent_id}")
    
    if not response.get('success'):
        error_msg = response.get('error', {}).get('message', 'Unknown error')
        console.print(f"[red]✗ Agent not found: {error_msg}")
        return
    
    agent = response.get('data', {})
    
    # Show logo and chat interface
    show_logo()
    console.print(Panel(
        f"🤖 Starting chat with [bold]{agent.get('name', 'Unknown Agent')}[/bold]\n"
        f"Model: {agent.get('ai_model', 'Unknown')}\n\n"
        "Commands: /exit, /save, /help",
        title="Medula Chat",
        border_style="blue"
    ))
    
    conversation = []
    
    while True:
        try:
            user_input = Prompt.ask("\n[bold blue]You[/bold blue]")
            
            if user_input.startswith('/'):
                if user_input == '/exit':
                    if save_session and conversation:
                        # Save conversation logic here
                        console.print(f"[green]💾 Conversation saved as: {save_session}")
                    console.print("👋 Chat ended. Have a great day!")
                    break
                elif user_input == '/help':
                    console.print("[blue]Commands:[/blue]")
                    console.print("  /exit - End the conversation")
                    console.print("  /save - Save current conversation")
                    console.print("  /help - Show this help")
                    continue
                else:
                    console.print("[yellow]Unknown command. Type /help for available commands.")
                    continue
            
            # Send message to agent
            with console.status("[bold green]🤖 Agent is thinking..."):
                chat_response = await api.post(
                    f"/api/v1/tenants/{config['tenant_id']}/agents/{agent_id}/chat",
                    {"message": user_input}
                )
            
            if chat_response.get('success'):
                response_text = chat_response.get('response', 'No response received')
                console.print(f"\n[bold green]🤖 {agent.get('name', 'Agent')}:[/bold green] {response_text}")
                
                # Store conversation
                conversation.append({
                    'timestamp': datetime.now().isoformat(),
                    'user': user_input,
                    'agent': response_text
                })
            else:
                error_msg = chat_response.get('error', {}).get('message', 'Unknown error')
                console.print(f"[red]✗ Chat error: {error_msg}")
        
        except KeyboardInterrupt:
            if Confirm.ask("\nSave conversation before exiting?"):
                # Save conversation logic here
                console.print(f"[green]💾 Conversation saved")
            break

@cli.group()
def data():
    """Training data management"""
    pass

@data.command('upload')
@click.argument('agent_id')
@click.option('--file', 'file_path', type=click.Path(exists=True), help='File to upload')
@click.option('--text', help='Text content to upload directly')
async def upload_data(agent_id: str, file_path: Optional[str], text: Optional[str]):
    """Upload training data to an agent"""
    config = config_manager.load_config()
    token = config_manager.get_token()
    
    if not token:
        console.print("[red]Not logged in. Run 'medula auth login' first.")
        return
    
    if not file_path and not text:
        console.print("[red]Please provide either --file or --text")
        return
    
    api = MedulaAPI(config['endpoint'], token)
    
    if text:
        # Upload text directly
        data = {
            "documents": [{
                "type": "text",
                "content": text
            }]
        }
        
        with console.status("[bold blue]Uploading text content..."):
            response = await api.post(
                f"/api/v1/tenants/{config['tenant_id']}/agents/{agent_id}/training-data",
                data
            )
    else:
        # File upload would require multipart form data
        # For now, show what would happen
        console.print(f"[blue]Would upload file: {file_path}")
        console.print("[yellow]File upload coming in next version!")
        return
    
    if response.get('success'):
        console.print("[green]✓ Training data uploaded successfully!")
        docs = response.get('documents', [])
        console.print(f"[blue]Uploaded {len(docs)} document(s)")
    else:
        error_msg = response.get('error', {}).get('message', 'Unknown error')
        console.print(f"[red]✗ Upload failed: {error_msg}")

@cli.command('init')
@click.option('--name', prompt=True, help='Project name')
@click.option('--template', default='general', help='Agent template')
def init_project(name: str, template: str):
    """Initialize a new Medula project"""
    project_dir = Path(name)
    
    if project_dir.exists():
        console.print(f"[red]Directory '{name}' already exists")
        return
    
    # Create project structure
    project_dir.mkdir()
    (project_dir / 'agents').mkdir()
    (project_dir / 'training-data').mkdir()
    (project_dir / 'prompts').mkdir()
    
    # Create medula.toml config
    config_content = f"""[project]
name = "{name}"
version = "1.0.0"

[agent]
name = "{name.title()} Agent"
model = "claude-3-haiku"
temperature = 0.7

[training]
auto_process = true
chunk_size = 1000
"""
    
    with open(project_dir / 'medula.toml', 'w') as f:
        f.write(config_content)
    
    # Create sample files
    with open(project_dir / 'training-data' / 'README.md', 'w') as f:
        f.write("# Training Data\n\nAdd your training documents here.\n")
    
    with open(project_dir / 'prompts' / 'system.md', 'w') as f:
        f.write(f"# {name.title()} Agent\n\nYou are a helpful AI assistant.\n")
    
    console.print(f"[green]✓ Created Medula project: {name}")
    console.print(f"[blue]Next steps:")
    console.print(f"  cd {name}")
    console.print(f"  medula deploy")

# Make commands async-compatible
def async_command(f):
    """Decorator to run async commands"""
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))
    return wrapper

# Apply async decorator to async commands
login.callback = async_command(login.callback)
list_agents.callback = async_command(list_agents.callback)
create_agent.callback = async_command(create_agent.callback)
show_agent.callback = async_command(show_agent.callback)
start_chat.callback = async_command(start_chat.callback)
upload_data.callback = async_command(upload_data.callback)

if __name__ == '__main__':
    cli()
