import os
import sys
from django.core.management import execute_from_command_line

# Set default DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_project.settings")  # <-- replace your_project_name

# Get the port from Railway, default to 8000
port = os.environ.get("PORT", 8000)

# Run the server
execute_from_command_line([sys.argv[0], "runserver", f"0.0.0.0:{port}"])