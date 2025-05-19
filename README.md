
# Virtual Environment Auto-Activation 

Run the following commands to set up automatic activation of your virtual environment:

```sh
chmod +x auto_venv_activate.sh
./auto_venv_activate.sh.sh
```
## For direct insertion into the bashrc follow these steps
```sh
nvim ~/.bashrc
```
## after the file is open insert following at the bottom of the file

```bash
function auto_activate_venv() {
    # Only activate if not already inside a virtualenv
    if [[ -z "$VIRTUAL_ENV" && -f "venv/bin/activate" ]]; then
        source venv/bin/activate
    fi
}
# Trigger auto_activate_venv function on directory change
PROMPT_COMMAND="auto_activate_venv; $PROMPT_COMMAND"

```

