# ⚠️ GPU Preference Registry Editor (Experimental)

This tool attempts to modify the Windows Registry to force applications to run using the **dedicated GPU** instead of the integrated GPU (iGPU).  
The purpose of this project is **experimental** and still **under development** — especially because the behavior may vary between different laptops, GPU vendors, and Windows versions.

> **⚠️ IMPORTANT DISCLAIMER  
> USE THIS TOOL AT YOUR OWN RISK.**  
> Editing the registry can cause system issues if not done correctly.  
> I DO NOT take responsibility for any damage, errors, or irreversible changes caused by using this tool.

---

## ❗ Project Status

🚧 **This project is still in development.**  
I cannot fully test it on my desktop PC, and will only be able to test it properly using a laptop environment later.  
Behavior on different systems is **not guaranteed**.

---

## 📝 What This Tool Does

The script edits the following registry path:

```
HKEY_CURRENT_USER\Software\Microsoft\DirectX\UserGpuPreferences
```

It attempts to assign:

- `GpuPreference=2` → High-performance (Dedicated GPU)

This forces Windows to *prefer* the dedicated GPU when launching the selected `.exe`.

---

## 🧪 Example Usage (Work in Progress)

```python
import winreg

REG_PATH = r"Software\Microsoft\DirectX\UserGpuPreferences"

def force_high_gpu(exe_path):
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
    winreg.SetValueEx(key, exe_path, 0, winreg.REG_SZ, "GpuPreference=2;")
```

This is the core logic, but **not final**.  
More checks, error handling, system detection, and safety features will be added.

---

## ⚠️ Warnings & Limitations

- **Modifying the registry carries risk.**
- Windows or GPU drivers may ignore the setting depending on:
  - Vendor (NVIDIA / AMD / Intel)
  - Laptop power mode
  - Windows version
  - Admin restrictions
- Some apps *always* choose their GPU regardless of settings.
- Reverting changes may require advanced registry cleanup.
- You should **back up your registry before using this tool**.

---

## 🔄 Reverting Changes

The tool will include a future option to revert registry entries.  
For now, users must manually remove entries via:

```
regedit → HKEY_CURRENT_USER\Software\Microsoft\DirectX\UserGpuPreferences
```

Again, **do this carefully**.

---

## 🧰 Requirements

- Windows 10 / 11
- Python 3.8+
- Administrator or elevated permissions recommended

---

## 🛡️ Safety Notes

- Always create a **System Restore Point** before using tools involving the registry.
- Test on non-critical machines when possible.
- Do not run scripts from unknown sources.
- The author is **not responsible** for data loss, Windows corruption, or hardware misbehavior.

---

## 🤝 Contributing

Contributions are welcome — especially from users with:
- Laptops containing hybrid GPU setups (iGPU + dGPU)
- Experience with Windows GPU selection
- Knowledge of registry safety practices

Feel free to open an issue or pull request.

---

## 📜 License

MIT License — use freely, but **no warranty** of any kind.

---

## 📢 Final Note

This project is intended **for educational and testing purposes only**, not as a guaranteed GPU management tool.  
Proceed carefully and responsibly.
