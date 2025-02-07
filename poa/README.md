# Padding Oracle Attack Lab

## Overview
In this lab, we will practice executing a **Padding Oracle Attack** by writing a script that performs it.

## Step 1: Setup
- Use **Python 3** and the `pycryptodome` library.
- Ensure that the library is installed and working correctly (`pip install pycryptodome`).
- Use the following imports:

```python
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad
```

- The first import allows us to perform encryption using the **DES block cipher**.
- The second import helps us **add and remove padding**.

## Step 2: Padding the String
Pad the string `"Hello World"` to be **16 bytes long**.
The padded string should look like this when printed:

```python
b'Hello World\x05\x05\x05\x05\x05'
```

## Step 3: Encrypt the Padded String
- Encrypt the padded string using **DES in CBC mode**.
- Use the key `poaisfun` and an **IV of all zeros**.
- (Reminder: DES block size is **8 bytes**).
- After encryption, the **ciphertext** should be:

```
0x33 0xaa 0xa3 0x1 0x7e 0x45 0x33 0x7b
0xd3 0x63 0x42 0xb3 0x92 0x0b 0xe6 0x56
```

## Step 4: Decrypt and Remove Padding
Ensure that you can **decrypt** the ciphertext and correctly **remove the padding** to retrieve the original plaintext.

## Step 5: Implement XOR Function
Write a function `xor` that takes **three parameters** and returns their XOR result.

Example usage:

```python
print(xor(0,0,0))
print(xor(0,0,1))
print(xor(0,1,0))
print(xor(0,1,1))
print(xor(1,0,0))
print(xor(1,0,1))
print(xor(1,1,0))
print(xor(1,1,1))
```

Expected output:

```
b'\x00'
b'\x01'
b'\x01'
b'\x00'
b'\x01'
b'\x00'
b'\x00'
b'\x01'
```

## Step 6: Implement the Oracle Function
Write a function `oracle` that:
- Takes a ciphertext.
- Decrypts it and removes padding.
- Returns `True` if successful, otherwise `False`.

Example:
- If you input your generated ciphertext, it should return `True`.
- If you modify the ciphertext in any way, it should return `False`.

## Step 7: Construct Variable `c`
Create a variable `c` that consists of **an all-zero block concatenated with the second block of the ciphertext**.

The bytes of `c` should be:

```
0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00
0xd3 0x63 0x42 0xb3 0x92 0x0b 0xe6 0x56
```

## Step 8: Oracle Query Loop
Send `c` to the oracle in a loop, increasing the **eighth byte** by `1` each time, until the oracle returns `True`.

## Step 9: Extract Last Byte of Second Block
Use the equation from the presentation and the `xor` function to extract the last byte of the second block.
(This byte should be `0x00`).

## Step 10: Modify `c` to Reveal Next Byte
Use the equation and `xor` function to modify `c` so that the last decrypted byte is `0x02`.

## Step 11: Automate Byte Extraction
Turn **steps 8-10 into a loop** that reveals **one byte at a time** until the entire block is exposed.

## Step 12: Automate Full Decryption
Turn **step 11 into a loop** that can **decrypt the entire ciphertext**, block by block.

---

### Completion
Once all steps are successfully implemented, your script should be able to **fully decrypt any ciphertext encrypted with DES-CBC using a padding oracle attack.**

