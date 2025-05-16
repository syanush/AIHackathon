# Chainlit configuration file
# See https://docs.chainlit.io/api-reference/chainlit-config for more details

# App configuration
app_title: "AIHackathon"
app_description: "AI Hackathon conversational interface powered by Chainlit"
# App favicon relative to the static directory
favicon: "/favicon.ico"

# UI customization
theme:
  primary_color: "#4f46e5"
  background_color: "#f9fafb"
  
# Chat settings
chat:
  # Number of messages to show in history
  message_history_limit: 50
  # Allow users to upload files
  allow_file_uploads: true
  # Maximum upload file size in MB
  max_upload_file_size: 10

# Features to enable/disable
features:
  # Enable dark mode toggle
  dark_mode_toggle: true
  # Show settings button
  settings: true

# GitHub link in the header
github:
  # URL to the repository
  url: ""
  # Text to show on hover
  label: "Star us on GitHub"
