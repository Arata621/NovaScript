## Setting Up Novascript

#### 🗂️ Folder Structure
Ensure that both `novascript.py` (the interpreter) and your `.nsc` script file are in the same directory.
```
Novascript/
├── novascript.py   # Interpreter
├── my_script.nsc   # Your Novascript program
```

#### 📌 Navigating to the Correct Directory
1. Open **Command Prompt (CMD)**
2. Use `cd` to move to the folder where `novascript.py` is located. Example:
   ```sh
   cd C:\Users\YourUsername\Downloads\Novascript
   ```

3. Confirm you are in the right directory by running:
   ```sh
   dir
   ```
   You should see `novascript.py` and your `.nsc` file listed.

---

## Running a Novascript Program
Once in the correct directory, execute your script using:
```sh
python novascript.py my_script.nsc
```
Example output:
```
 _  _  _____  _  _  __    ___   ___    __    ____  ____
( \( )(  _  )( \/ )/__\  / __) / __)  /__\  (  _ \( ___)
 )  (  )(_)(  \  //(__)\ \__ \( (__  /(__)\  )___/ )__)
(_)_)(_____)  \/(__)(__)(___/ \___)(__)(__)(__)  (____)

Starting Novascript...

Hello, World!
```
