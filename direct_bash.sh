
# This code is used for the manual insertion
# to make this code work follow steps:
# 1.Execute: sudo nano ~/.bashrc 
# 2.Copy code bellow

function auto_activate_venv() {
    # Only activate if not already inside a virtualenv
    if [[ -z "$VIRTUAL_ENV" && -f "venv/bin/activate" ]]; then
        source venv/bin/activate
    fi
}
# Trigger auto_activate_venv function on directory change
PROMPT_COMMAND="auto_activate_venv; $PROMPT_COMMAND"

# Used for copying current working directory into buffer
alias pwdwlc="pwd | wl-copy"

# 3. To apply changes dont forget to write the file and execute following command afterwards: sudo source ~/.bashrc
