# Stack Buffer Overflow in a Linux Kernel Module

## Project Goal

The objective of this project is to create a vulnerable Linux kernel module that demonstrates a stack buffer overflow. It also walks through the process of identifying and fixing the vulnerability. This project uses user-space input to simulate the overflow scenario and includes best practices to avoid common setup issues.

---

## Tools Required

- Linux system (Ubuntu recommended)
- Terminal with `sudo` privileges
- Required packages: `build-essential`, `linux-headers`

---

## Setup and Execution

### Step 1: Install Required Packages

```bash
sudo apt update
```

```bash
sudo apt install build-essential linux-headers-$(uname -r)
```

---

### Step 2: Create Project Directory

```bash
mkdir -p ~/stack-overflow-lab/vuln_module
```

```bash
cd ~/stack-overflow-lab/vuln_module
```

---

### Step 3: Create Kernel Module Source File

```bash
nano stack_overflow.c
```

Paste the following code:

```c
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/uaccess.h>

#define DEVICE_NAME "vuln"
#define BUF_LEN 32

static int major;
static char kernel_buffer[BUF_LEN];

ssize_t device_write(struct file *file, const char __user *buf, size_t len, loff_t *offset) {
    printk(KERN_INFO "[vuln] Writing %zu bytes (max: %d) to kernel buffer.\n", len, BUF_LEN);
    copy_from_user(kernel_buffer, buf, len);  // Vulnerability: no bounds checking
    return len;
}

static struct file_operations fops = {
    .write = device_write,
};

static int __init vuln_init(void) {
    major = register_chrdev(0, DEVICE_NAME, &fops);
    printk(KERN_INFO "[vuln] Module loaded. Major number: %d\n", major);
    return 0;
}

static void __exit vuln_exit(void) {
    unregister_chrdev(major, DEVICE_NAME);
    printk(KERN_INFO "[vuln] Module unloaded.\n");
}

module_init(vuln_init);
module_exit(vuln_exit);
MODULE_LICENSE("GPL");
```

---

### Step 4: Create Makefile

```bash
nano Makefile
```

Paste the following content:

```make
obj-m += stack_overflow.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

---

### Step 5: Compile the Kernel Module

```bash
make
```

---

### Step 6: Load the Kernel Module

```bash
sudo insmod stack_overflow.ko
```

Verify module is loaded:

```bash
sudo dmesg | grep vuln
```

Example output:

```
[vuln] Module loaded. Major number: 236
```

---

### Step 7: Create the Character Device Node

Remove any existing device:

```bash
sudo rm -f /dev/vuln
```

Create the device using the correct major number:

```bash
sudo mknod /dev/vuln c 236 0
```

Set appropriate permissions:

```bash
sudo chmod 666 /dev/vuln
```

Verify the device:

```bash
ls -l /dev/vuln
```

Expected output:

```
crw-rw-rw- 1 root root 236, 0 ... /dev/vuln
```

---

### Step 8: Trigger the Buffer Overflow

Send a long string to the device:

```bash
echo "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" | sudo tee /dev/vuln
```

Check kernel logs:

```bash
sudo dmesg | grep vuln
```

Example output:

```
[vuln] Writing 58 bytes (max: 32) to kernel buffer.
```

---

### Step 9: Fix the Vulnerability

Open the source code:

```bash
nano stack_overflow.c
```

Replace the vulnerable line:

```c
copy_from_user(kernel_buffer, buf, len);
```

With a safer version:

```c
size_t safe_len = len > BUF_LEN ? BUF_LEN : len;
copy_from_user(kernel_buffer, buf, safe_len);
```

---

### Step 10: Rebuild and Reload the Module

```bash
make clean
```

```bash
make
```

```bash
sudo rmmod stack_overflow
```

```bash
sudo insmod stack_overflow.ko
```

---

### Step 11: Test After Fix

Send the long input again:

```bash
echo "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" | sudo tee /dev/vuln
```

Check logs:

```bash
sudo dmesg | grep vuln
```

Output will show safe handling of the input without overflow.

---

## Troubleshooting and Best Practices

| Issue | Solution |
|-------|----------|
| Created `/dev/vuln` as a regular file | Use `mknod` with correct major number |
| No output from `dmesg` | Use `sudo dmesg | grep vuln` |
| No effect when writing to `/dev/vuln` | Ensure module is loaded and device node exists |
| Changes to code have no effect | Run `make clean && make` before reloading |

---

## Conclusion

This project demonstrated:

- How to write and compile a Linux kernel module
- How to simulate a stack buffer overflow
- How to safely handle user-space input to prevent kernel-space vulnerabilities
- Proper methods for creating character devices and debugging with `dmesg`

---

## Project Files

All project files can be downloaded or cloned from the following repository:

**GitHub**: [https://github.com/Arisudan](https://github.com/Arisudan)
