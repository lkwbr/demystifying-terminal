# GitHub Setup

## Step 1: Generate an SSH Key

1. **Open your terminal** and generate an SSH key pair:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   - Replace `your_email@example.com` with your GitHub email.
   - If `ed25519` is unsupported, use:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
     ```

2. **Save the key**:
   - When prompted, press `Enter` to accept the default location (`~/.ssh/id_ed25519`).
   - If you want added security, enter a passphrase when asked.

---

## Step 2: Add the SSH Key to the SSH Agent

1. **Start the SSH agent**:
   ```bash
   eval "$(ssh-agent -s)"
   ```

2. **Add your private key to the agent**:
   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

---

## Step 3: Add the SSH Key to Your GitHub Account

1. **Copy the public key** to your clipboard:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
   Or, use these commands for convenience:
   - **Linux**: `xclip -sel clip < ~/.ssh/id_ed25519.pub`
   - **macOS**: `pbcopy < ~/.ssh/id_ed25519.pub`

2. **Log in to GitHub** and navigate to:
   - **Settings → SSH and GPG Keys → New SSH Key**.

3. **Paste the public key** and give it a name (e.g., "My Laptop Key").

4. **Save the key** by clicking **Add SSH Key**.

---

## Step 4: Test the SSH Connection

1. Run this command to test your connection:
   ```bash
   ssh -T git@github.com
   ```
2. You should see a message like:
   ```
   Hi username! You've successfully authenticated, but GitHub does not provide shell access.
   ```

---

## Step 5: Set Up Git with Demystifying Terminal

1. **Set Git's global username and email**:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your_email@example.com"
   ```

2. **Clone the Demystifying Terminal repository**:
   ```bash
   git clone git@github.com:lkwbr/demystifying-terminal.git
   cd demystifying-terminal
   ```

3. **If you already cloned with HTTPS, switch to SSH**:
   ```bash
   git remote set-url origin git@github.com:lkwbr/demystifying-terminal.git
   ```

4. **Verify your remote URL**:
   ```bash
   git remote -v
   ```
   Should show:
   ```
   origin  git@github.com:lkwbr/demystifying-terminal.git (fetch)
   origin  git@github.com:lkwbr/demystifying-terminal.git (push)
   ```