# **Demystify the Terminal: Deploying and Testing an AWS Lambda Function**

This guide walks you through using the terminal for basic and advanced tasks, improving workflows, and deploying an AWS Lambda function.

---

## **Getting Started with the Terminal**

### **Basic Commands**
Start by running these commands to understand how the terminal interacts with your system:

1. **View Current Directory**:
   ```bash
   pwd
   ```
   Prints the current directory path (your location in the filesystem).

2. **List Files and Folders**:
   ```bash
   ls
   ```
   Lists the files and directories in your current location. Use `ls -lh` for detailed file information.

3. **Create a Directory**:
   ```bash
   mkdir my_folder
   ```
   Creates a new folder named `my_folder`.

4. **Navigate into a Directory**:
   ```bash
   cd my_folder
   ```
   Moves into the `my_folder` directory.

5. **Create a File**:
   ```bash
   touch my_file.txt
   ```
   Creates an empty file named `my_file.txt`.

6. **Remove a File**:
   ```bash
   rm my_file.txt
   ```
   Deletes the specified file.

---

### **Advanced Commands**

These commands showcase how the terminal can streamline workflows:

1. **Automate Tasks with `cron`**:
   Schedule a task to run every day at midnight:
   ```bash
   crontab -e
   ```
   Add this line:
   ```bash
   0 0 * * * echo "Hello from cron!" >> ~/cron_log.txt
   ```

2. **Search for Files or Text**:
   - Find all `.txt` files:
     ```bash
     find . -name "*.txt"
     ```
   - Search for "ERROR" in logs:
     ```bash
     grep "ERROR" file.log
     ```

3. **Command Aliases**:
   Speed up commands by creating an alias:
   ```bash
   alias ll="ls -lh"
   ```
   Make it permanent by adding it to `~/.zshrc` or `~/.bashrc`.

4. **Monitor System Resources**:
   ```bash
   htop
   ```
   A process manager to monitor CPU and memory usage (install with `brew install htop`).

5. **Compress and Extract Files**:
   - Compress a folder:
     ```bash
     tar -czvf archive.tar.gz my_folder
     ```
   - Extract the archive:
     ```bash
     tar -xzvf archive.tar.gz
     ```

6. **Redirect Output**:
   Save command output to a file:
   ```bash
   ls -lh > output.txt
   ```

7. **Run Jobs in the Background**:
   Run a command in the background:
   ```bash
   long_running_command &
   jobs
   ```

---

## **Overview of Terminals**

### Terminal Options: Pros and Cons

| Terminal      | Pros                                   | Cons                                    |
|---------------|---------------------------------------|-----------------------------------------|
| **Default macOS Terminal** | Reliable, pre-installed, minimal setup. | Limited features and customization.    |
| **iTerm2**    | Highly customizable, supports plugins, splits panes. | Can be overwhelming for beginners.     |
| **Alacritty** | Lightweight, GPU-accelerated, very fast. | Lacks a built-in terminal multiplexer. |
| **Kitty**     | Fast, modern features, good theming.  | Slightly steeper learning curve.        |
| **Warp**      | Autocomplete, collaboration features. | A newer tool, may not suit purists.     |

---

## **AWS Lambda Deployment**

### **Step 1: Prerequisites**

1. **Install Git**:
   ```bash
   brew install git
   ```

2. **Install AWS CLI**:
   ```bash
   brew install awscli
   ```

3. **Configure AWS CLI**:
   Set up your AWS credentials:
   ```bash
   aws configure
   ```

4. **Create an IAM Role**:
   - Go to the AWS Console.
   - Create an IAM role with the `AWSLambdaBasicExecutionRole` policy.
   - Note down the **Role ARN**.

---

### **Step 2: Clone the GitHub Repo**
Clone the repository containing the Lambda function:
```bash
git clone https://github.com/lkwbr/demystifying-terminal.git
cd demystifying-terminal
```

---

### **Step 3: Package and Deploy the Lambda Function**

1. **Package the Function**:
   ```bash
   zip -r lambda_function.zip lambda_function.py
   ```

2. **Create the Lambda Function**:
   ```bash
   aws lambda create-function \
       --function-name calculateSquare \
       --runtime python3.9 \
       --role <Your-Role-ARN> \
       --handler lambda_function.lambda_handler \
       --zip-file fileb://lambda_function.zip
   ```

3. **Verify Deployment**:
   ```bash
   aws lambda list-functions
   ```

---

### **Step 4: Test the Lambda Function**

1. **Use the Test Script**:
   ```bash
   chmod +x test_lambda.sh
   ./test_lambda.sh
   ```

2. **Invoke Manually**:
   ```bash
   aws lambda invoke \
       --function-name calculateSquare \
       --payload '{"number": 7}' \
       output.json
   cat output.json
   ```

3. **Expected Output**:
   ```json
   {"number": 7, "squared": 49}
   ```

---

### **Step 5: Cleanup**

Delete the Lambda function:
```bash
aws lambda delete-function --function-name calculateSquare
```

---

## **Troubleshooting**

1. **Role Permission Errors**:
   Ensure your IAM role has the `AWSLambdaBasicExecutionRole` policy.

2. **Syntax Errors**:
   Verify the `--function-name` and `--payload` syntax.

3. **Debugging Logs**:
   Check logs for errors:
   ```bash
   aws logs tail /aws/lambda/calculateSquare
   ```

---

## **Additional Resources**

- **Terminal Basics**:
  [Scripting OSX – First Steps in Terminal](https://scriptingosx.com/2017/07/first-steps-in-terminal/)
  [ExplainShell](https://explainshell.com)

- **Challenges for Practice**:
  [OverTheWire Wargames (Bandit)](https://overthewire.org/wargames/bandit/)

- **Bash Guide**:
  [GitHub: Bash Guide for Beginners](https://github.com/Idnan/bash-guide)